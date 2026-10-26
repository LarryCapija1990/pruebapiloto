/* CP11: isolated T45 module. No edits to embedded F4. Absolute progress only. */
const $=id=>document.getElementById(id), C=$('t45'),ctx=C.getContext('2d',{alpha:false}),frame=$('base');
const clamp=x=>Math.max(0,Math.min(1,x)),mix=(a,b,t)=>a+(b-a)*t;
const S=(a,b,x)=>{const t=clamp((x-a)/(b-a));return t*t*(3-2*t)};
const media=matchMedia('(prefers-reduced-motion: reduce)');let reduced=media.matches,override=false,ready=false,queued=false,syncing=false,w=0,h=0,q=0,p=0,lastY=0,snap;
const stats={renders:0,frameMs:[],errors:[],assets:0};const images={};
const photoLayer=document.createElement('canvas'),photoContext=photoLayer.getContext('2d');
const milestones=[0,.12,.28,.36,.40,.42,.44,.48,.52,.56,.60,.64,.70,.80,.94,1];
// Real source contour traced manually on original 600×593 JPG. Not an exact segmentation.
const edge=[[296,278],[300,284],[308,289],[307,294],[307,300],[306,305],[302,307],[298,305],[295,306],[290,308],[285,307],[282,303],[282,298],[284,292],[288,287],[292,282]];
const target=edge.map(([x,y])=>[524+(x-295)*8,350+(y-297)*8]);
function cubic(a,b,c,d,n=24){return Array.from({length:n},(_,i)=>{const t=i/(n-1),u=1-t;return [u*u*u*a[0]+3*u*u*t*b[0]+3*u*t*t*c[0]+t*t*t*d[0],u*u*u*a[1]+3*u*u*t*b[1]+3*u*t*t*c[1]+t*t*t*d[1]]})}
function resample(points,n){const ds=[0];for(let i=1;i<points.length;i++)ds.push(ds[i-1]+Math.hypot(points[i][0]-points[i-1][0],points[i][1]-points[i-1][1]));return Array.from({length:n},(_,j)=>{const d=ds.at(-1)*j/(n-1);let i=1;while(i<ds.length-1&&ds[i]<d)i++;const t=(d-ds[i-1])/(ds[i]-ds[i-1]||1);return points[i].map((v,k)=>mix(points[i-1][k],v,t))})}
// Traverse left open tip → lower crossing → right open tip; both tips converge on same real tip.
const source=resample([...cubic([459,318],[375,329],[344,385],[435,412]),...cubic([435,412],[504,441],[638,424],[662,379]),...cubic([662,379],[691,347],[614,320],[579,318])],96);
const targetOrdered=resample([...target.slice(8).reverse(),...target.slice(0,9).reverse()],96);
// Correct orientation: tip, left perimeter, lower notch, right perimeter, tip.
const ordered=resample([target[0],...target.slice(8).reverse(),...target.slice(1,9).reverse(),target[0]],96);
function geometry(v){
 const t=S(.18,.42,v),out=source.map((a,i)=>a.map((x,k)=>mix(x,ordered[i][k],t)));
 // Both endpoints exactly coincide from .42 onward: closure never reopens or overshoots.
 return {points:out,closed:v>=.42,top:mix(100,198,S(.12,.42,v)),bottom:mix(540,490,S(.18,.52,v)),stem:S(.36,.52,v),ink:S(.43,.59,v),paper:S(.40,.60,v)};
}
function dims(){return {cy:h/2-(h<500?0:12),fit:Math.min((w-40)/600,Math.max(100,h-(h<500?120:220))/594)}}
function camera(v){
 const {cy,fit}=dims(),zoom=Math.min((w-48)/350,Math.max(110,h-(h<500?130:230))*.70/350);
 const scale=mix(fit,zoom,S(.04,.18,v));
 // A long, nearly stationary geometric phase, then smooth monotone withdrawal.
 const start=zoom*8,finish=Math.min((w-40)/600,Math.max(100,h-(h<500?120:220))/593);
 const u=S(.54,.94,v)**3,photoScale=Math.exp(mix(Math.log(start),Math.log(finish),u));
 const center=[mix(295,300,S(.72,.94,v)),mix(297,296.5,S(.72,.94,v))];
 return {scale:v<.54?scale:photoScale/8,photoScale,center,cy};
}
function path(points,close){ctx.beginPath();ctx.moveTo(...points[0]);for(const a of points.slice(1))ctx.lineTo(...a);if(close)ctx.closePath()}
function transformed(v,fn){const a=camera(v);ctx.save();ctx.translate(w/2,a.cy);ctx.scale(a.scale,a.scale);ctx.translate(-524,-350);fn(a);ctx.restore()}
function drawPhoto(v,dc=ctx){const a=camera(v);dc.save();dc.translate(w/2,a.cy);dc.scale(a.photoScale,a.photoScale);dc.translate(-a.center[0],-a.center[1]);dc.drawImage(images.salute,0,0);dc.restore()}
function draw(v){
 const begin=performance.now();ctx.setTransform(C.width/w,0,0,C.height/h,0,0);ctx.fillStyle='#080a0f';ctx.fillRect(0,0,w,h);
 if(v<=.04||(reduced&&v<.52)){ctx.drawImage(snap,0,0,w,h);finish(begin);return}
 if(reduced){const {fit,cy}=dims();const im=v<.52?images.innervision:images.salute;const s=Math.min((w-40)/600,Math.max(100,h-(h<500?120:220))/im.height);ctx.drawImage(im,w/2-300*s,cy-im.height*s/2,600*s,im.height*s);finish(begin);return}
 const g=geometry(v),a=camera(v);
 if(v>=.70){drawPhoto(v);finish(begin);return}
 // Snapshot zoom preserves the exact F4 endpoint before any shape substitution.
 if(v<.18){const {fit,cy}=dims(),z=a.scale/fit;ctx.save();ctx.translate(w/2,a.cy);ctx.scale(z,z);ctx.translate(-w/2+9*fit,-cy-50*fit*S(.04,.18,v));ctx.drawImage(snap,0,0,w,h);ctx.restore()}
 // Original expanded field, no rectangular Salute layer on stars.
 ctx.globalAlpha=S(.12,.18,v);if(v>=.18)ctx.globalAlpha=1;
 transformed(v,()=>{ctx.drawImage(images.space,0,0);ctx.drawImage(images.stars,0,0)});ctx.globalAlpha=1;
 // Whole-field material, fixed matte grain. Never a rectangular photographic insert.
 if(g.paper>0){const t=g.paper;ctx.fillStyle=`rgba(${Math.round(mix(70,181,t))},${Math.round(mix(65,174,t))},${Math.round(mix(66,186,t))},${t})`;ctx.fillRect(0,0,w,h);ctx.globalAlpha=.075*t;ctx.fillStyle='#504851';for(let i=0;i<620;i++){const x=((i*109.37)%997)/997*w,y=((i*67.19)%991)/991*h;ctx.fillRect(x,y,1.4,1.4)}ctx.globalAlpha=1}
 if(v<.22){ctx.globalAlpha=S(.12,.18,v)*(1-S(.18,.22,v));transformed(v,()=>ctx.drawImage(images.symbol,0,0));ctx.globalAlpha=1}
 const layer=S(.18,.22,v);ctx.globalAlpha=layer;
 transformed(v,()=>{
  const col=g.ink,orange=[255,137,31],ink=[48,48,37],color=orange.map((c,i)=>Math.round(mix(c,ink[i],col)));const str=`rgb(${color})`;
  // Only the CLOSED silhouette receives fill. An inset clipped stroke brings ink inward.
  path(g.points,g.closed);
  if(g.closed){ctx.save();ctx.clip();ctx.fillStyle=`rgba(48,48,37,${S(.47,.59,v)})`;ctx.fillRect(300,150,450,400);ctx.strokeStyle='#34372c';ctx.lineWidth=140*S(.43,.58,v);path(g.points,true);ctx.stroke();ctx.restore()}
  ctx.strokeStyle=str;ctx.lineJoin='round';ctx.lineCap='round';ctx.lineWidth=mix(6,1.4,col);ctx.shadowColor='rgb(255,112,17)';ctx.shadowBlur=12*(1-col);path(g.points,g.closed);ctx.stroke();ctx.shadowBlur=0;
  // Axis retracts geometrically from above, compresses below and widens into original stem.
  const axisTop=mix(g.top,350,S(.42,.52,v)),axisBottom=mix(g.bottom,390,S(.42,.52,v));
  ctx.beginPath();ctx.moveTo(mix(524,532,S(.18,.42,v)),axisTop);ctx.lineTo(524,axisBottom);ctx.strokeStyle=str;ctx.lineWidth=mix(6,8,g.stem);ctx.stroke();
  const stem=[[(296-295)*8+524,(305-297)*8+350],[(295-295)*8+524,(310-297)*8+350],[(292-295)*8+524,(315-297)*8+350],[(301-295)*8+524,(314-297)*8+350],[(299-295)*8+524,(309-297)*8+350],[(299-295)*8+524,(305-297)*8+350]];
  if(g.stem>0){ctx.save();ctx.translate(524,414);ctx.scale(g.stem,g.stem);ctx.translate(-524,-414);path(stem,true);ctx.fillStyle=str;ctx.fill();ctx.restore()}
 });ctx.globalAlpha=1;
 // Ornament transfer uses the same source-to-plane matrix as the traced contour.
 if(v>.56){
  ctx.save();transformed(v,()=>{path(g.points,true);const foot=[[296,305],[295,310],[292,315],[301,314],[299,309],[299,305]].map(([x,y])=>[524+(x-295)*8,350+(y-297)*8]);ctx.moveTo(...foot[0]);for(const p of foot.slice(1))ctx.lineTo(...p);ctx.closePath()});ctx.clip();
  ctx.globalAlpha=S(.56,.64,v);drawPhoto(v);ctx.restore();
  // Full support reveals by a continuous radial material boundary, not full-cover opacity.
  // There are no stars at this point. Fixed per-pixel front is tied solely to q.
  if(v>.64){
   const t=S(.64,.70,v),r=t*Math.hypot(w,h),cx=w/2,cy=a.cy;
   if(photoLayer.width!==C.width||photoLayer.height!==C.height){photoLayer.width=C.width;photoLayer.height=C.height}
   const pc=photoContext;pc.setTransform(1,0,0,1,0,0);pc.globalCompositeOperation='source-over';pc.clearRect(0,0,photoLayer.width,photoLayer.height);pc.setTransform(C.width/w,0,0,C.height/h,0,0);drawPhoto(v,pc);pc.setTransform(1,0,0,1,0,0);
   pc.globalCompositeOperation='destination-in';const factor=C.width/w;const grad=pc.createRadialGradient(cx*factor,cy*factor,Math.max(0,r-w*.20)*factor,cx*factor,cy*factor,Math.max(1,r)*factor);grad.addColorStop(0,'#fff');grad.addColorStop(1,'#fff0');pc.fillStyle=grad;pc.fillRect(0,0,photoLayer.width,photoLayer.height);ctx.drawImage(photoLayer,0,0,w,h);
  }
 }

 finish(begin);
}
function finish(start){stats.renders++;stats.frameMs.push(performance.now()-start);if(stats.frameMs.length>2000)stats.frameMs.shift();C.dataset.q=q.toFixed(6)}
function lengths(){return {first:5.5*h,hold:.2*h,second:5.5*h}}
function go(v){const a=lengths();scrollTo({top:a.first+a.hold+clamp(v)*a.second,behavior:'instant'});schedule()}
function goT34(v){scrollTo({top:clamp(v)*lengths().first,behavior:'instant'});schedule()}
function schedule(){if(!queued){queued=true;requestAnimationFrame(update)}}
function update(){queued=false;if(!ready)return;const a=lengths(),y=scrollY;p=clamp(y/a.first);q=clamp((y-a.first-a.hold)/a.second);
 const ext=y>a.first+a.hold+.01;
 if(!ext){syncing=true;frame.contentWindow.__F4.go(p);syncing=false}
 frame.inert=ext;frame.setAttribute('aria-hidden',String(ext));C.hidden=!ext;$('head').hidden=!ext;$('foot').hidden=!ext;$('continue').hidden=ext||p<.999;
 if(ext){draw(q);$('scrub').value=Math.round(q*1000);$('percent').textContent=Math.round(q*100)+' %';const text=q<.18?'Innervision · acercamiento':q<.42?'El arco asciende y se cierra':q<.60?'Luz → tinta · soporte':q<.80?'Pica original · retirada':'Salute · cubierta original';$('phase').textContent=text;$('live').textContent=text;$('scrub').setAttribute('aria-valuetext',Math.round(q*100)+' por ciento — '+text)}
 lastY=y;
}
function resize(){const oldh=h||innerHeight,oldY=scrollY;w=innerWidth;h=innerHeight;const d=Math.min(devicePixelRatio||1,1.5,Math.sqrt(2500000/(w*h)));C.width=Math.round(w*d);C.height=Math.round(h*d);if(ready){refreshSnap();scrollTo({top:oldY/oldh*h,behavior:'instant'})}schedule()}
function refreshSnap(){const f=frame.contentWindow;f.dispatchEvent(new f.Event('resize'));f.__F4.go(1);f.__F4.benchmark();capture();f.__F4.go(p);f.__F4.benchmark()}
function capture(){const src=frame.contentDocument.getElementById('scene');snap=document.createElement('canvas');snap.width=src.width;snap.height=src.height;snap.getContext('2d').drawImage(src,0,0)}
function mode(){if(frame.contentWindow.__F4&&frame.contentWindow.__F4.state.reduced!==reduced)frame.contentDocument.getElementById('motion').click();$('motion').textContent=reduced?'Movimiento reducido ✓':'Reducir movimiento';$('motion').setAttribute('aria-pressed',reduced);if(ready)requestAnimationFrame(()=>{refreshSnap();schedule()});schedule()}
async function init(){for(const [name,data]of Object.entries(PACKAGE.images)){const im=new Image();im.src=data;await im.decode();images[name]=im;stats.assets++}
 frame.srcdoc=PACKAGE.f4;
 await new Promise((resolve,reject)=>{let tries=0;const id=setInterval(()=>{if(frame.contentWindow.__F4?.state.ready){clearInterval(id);resolve()}else if(++tries>400){clearInterval(id);reject(Error('WebGL no disponible o F4 no pudo cargar'))}},50)});
 w=innerWidth;h=innerHeight;frame.contentWindow.__F4.go(1);await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));refreshSnap();ready=true;resize();mode();$('status').hidden=true;
 const doc=frame.contentDocument;
 doc.addEventListener('keydown',e=>{if(e.target.matches('input,button,a'))return;const delta={ArrowDown:40,ArrowUp:-40,PageDown:h*.85,PageUp:-h*.85,' ':h*.85}[e.key];if(delta){e.preventDefault();scrollBy(0,delta)}});
 doc.addEventListener('wheel',e=>{e.preventDefault();scrollBy({top:e.deltaY,behavior:'instant'})},{passive:false});
 let touchY;doc.addEventListener('touchstart',e=>touchY=e.touches[0].clientY,{passive:true});doc.addEventListener('touchmove',e=>{if(e.target.closest('input,button,a'))return;e.preventDefault();const y=e.touches[0].clientY;scrollBy(0,touchY-y);touchY=y},{passive:false});
 // Existing F4 control gestures map to its unchanged 550vh domain.
 for(const id of ['scrub','begin','end'])doc.getElementById(id).addEventListener(id==='scrub'?'input':'click',()=>requestAnimationFrame(()=>{goT34(frame.contentWindow.__F4.state.progress)}));
 doc.getElementById('motion').addEventListener('click',()=>{reduced=frame.contentWindow.__F4.state.reduced;override=true;mode()});
 window.__T45={go,goT34,geometry,camera,stats,get state(){return {q,p,reduced,ready,width:w,height:h,scrollY,firstLength:5.5*h,secondLength:5.5*h}},render(v){q=clamp(v);draw(q)},benchmark(v){const t=performance.now();draw(v);ctx.getImageData(0,0,1,1);return performance.now()-t}};schedule()
}
$('scrub').oninput=e=>go(e.target.value/1000);$('back').onclick=()=>go(0);$('end').onclick=()=>go(1);$('next').onclick=()=>go(milestones.find(v=>v>q+.002)??1);$('continue').onclick=()=>go(.0005);$('motion').onclick=()=>{override=true;reduced=!reduced;mode()};media.onchange=e=>{if(!override){reduced=e.matches;mode()}};
addEventListener('scroll',schedule,{passive:true});addEventListener('resize',resize);addEventListener('keydown',e=>{if(e.target.matches('input,button'))return;if(e.key==='Home'){e.preventDefault();goT34(0)}if(e.key==='End'){e.preventDefault();go(1)}});
init().catch(e=>{stats.errors.push(e.message);$('status').textContent='No pudo iniciarse la composición: '+e.message+'. Puedes consultar las portadas originales y reintentar en un navegador con WebGL.';const img=new Image();img.id='fallback';img.src=PACKAGE.images.innervision;$('status').append(img);const a=document.createElement('a');a.href=PACKAGE.images.salute;a.textContent='Abrir Salute original';$('status').append(a)});
