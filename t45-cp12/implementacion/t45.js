/* CP12: isolated T45 module. No edits to embedded F4. Absolute progress only. */
const $=id=>document.getElementById(id), C=$('t45'),ctx=C.getContext('2d',{alpha:false}),frame=$('base');
const clamp=x=>Math.max(0,Math.min(1,x)),mix=(a,b,t)=>a+(b-a)*t;
const S=(a,b,x)=>{const t=clamp((x-a)/(b-a));return t*t*(3-2*t)};
const media=matchMedia('(prefers-reduced-motion: reduce)');let reduced=media.matches,override=false,ready=false,queued=false,syncing=false,w=0,h=0,q=0,p=0,lastY=0,snap;
const stats={renders:0,frameMs:[],errors:[],assets:0};const images={};
const photoLayer=document.createElement('canvas'),photoContext=photoLayer.getContext('2d');
const milestones=[0,.18,.30,.32,.33,.34,.35,.36,.365,.375,.39,.42,.50,.60,.70,.80,1];
// CP12: seven percent for the complete local ignition/body morph/extinction.
function geometry(v){return {morph:S(.325,.365,v),ink:S(.350,.390,v),pulse:S(.320,.335,v)*(1-S(.335,.390,v)),paper:S(.335,.410,v),closed:v>=.365,axisLayer:false,hollowPhase:false}}
function dims(){return {cy:h/2-(h<500?0:12),fit:Math.min((w-40)/600,Math.max(100,h-(h<500?120:220))/594)}}
function camera(v){
 const {cy,fit}=dims(),zoom=Math.min((w-48)/350,Math.max(110,h-(h<500?130:230))*.70/350);
 const scale=mix(fit,zoom,S(.04,.18,v));
 // A long, nearly stationary geometric phase, then smooth monotone withdrawal.
 const start=zoom*8,finish=Math.min((w-40)/600,Math.max(100,h-(h<500?120:220))/593);
 const u=S(.350,.94,v)**.65,photoScale=Math.exp(mix(Math.log(start),Math.log(finish),u));
 const center=[mix(295,300,S(.72,.94,v)),mix(297,296.5,S(.72,.94,v))];
 return {scale:v<.350?scale:photoScale/8,photoScale,center,cy};
}
function path(points,close){ctx.beginPath();ctx.moveTo(...points[0]);for(const a of points.slice(1))ctx.lineTo(...a);if(close)ctx.closePath()}
function transformed(v,fn){const a=camera(v);ctx.save();ctx.translate(w/2+(295-a.center[0])*a.photoScale,a.cy+(297-a.center[1])*a.photoScale);ctx.scale(a.scale,a.scale);ctx.translate(-524,-350);fn(a);ctx.restore()}
function drawPhoto(v,dc=ctx){const a=camera(v);dc.save();dc.translate(w/2,a.cy);dc.scale(a.photoScale,a.photoScale);dc.translate(-a.center[0],-a.center[1]);dc.drawImage(images.salute,0,0);dc.restore()}
function draw(v){
 const begin=performance.now();ctx.setTransform(C.width/w,0,0,C.height/h,0,0);ctx.fillStyle='#080a0f';ctx.fillRect(0,0,w,h);
 if(v<=.04||(reduced&&v<.52)){ctx.drawImage(snap,0,0,w,h);finish(begin);return}
 if(reduced){const {cy}=dims(),im=images.salute,s=Math.min((w-40)/600,Math.max(100,h-(h<500?120:220))/im.height);ctx.drawImage(im,w/2-300*s,cy-im.height*s/2,600*s,im.height*s);finish(begin);return}
 const g=geometry(v),a=camera(v),texture=S(2.8,2.0,a.photoScale),context=S(2.25,1.85,a.photoScale);
 if(context>=1){drawPhoto(v);finish(begin);return}
 if(v<.18){const {fit,cy}=dims(),z=a.scale/fit;ctx.save();ctx.translate(w/2,a.cy);ctx.scale(z,z);ctx.translate(-w/2+9*fit,-cy-50*fit*S(.04,.18,v));ctx.drawImage(snap,0,0,w,h);ctx.restore()}
 ctx.globalAlpha=S(.12,.18,v);transformed(v,()=>{ctx.drawImage(images.space,0,0);ctx.drawImage(images.stars,0,0)});ctx.globalAlpha=1;
 if(g.paper>0){const t=g.paper;ctx.fillStyle=`rgba(${Math.round(mix(70,181,t))},${Math.round(mix(65,174,t))},${Math.round(mix(66,186,t))},${t})`;ctx.fillRect(0,0,w,h);ctx.globalAlpha=.075*t;ctx.fillStyle='#504851';for(let i=0;i<620;i++)ctx.fillRect(((i*109.37)%997)/997*w,((i*67.19)%991)/991*h,1.4,1.4);ctx.globalAlpha=1}
 // The authentic symbol remains intact until ignition. Gain is confined to its own pixels.
 if(v<.320){ctx.globalAlpha=S(.12,.18,v);transformed(v,()=>{ctx.drawImage(images.symbol,0,0);if(g.pulse>0){ctx.globalCompositeOperation='screen';ctx.globalAlpha=.45*g.pulse;ctx.drawImage(images.symbol,0,0)}});ctx.globalAlpha=1}
 else{renderBody(v);transformed(v,()=>ctx.drawImage(bodyCanvas,0,0))}
 // Original ornament is withheld until its source pixels are <=2.8 CSS px each.
 if(texture>0){
  if(photoLayer.width!==C.width||photoLayer.height!==C.height){photoLayer.width=C.width;photoLayer.height=C.height}
  const pc=photoContext;pc.setTransform(1,0,0,1,0,0);pc.globalCompositeOperation='source-over';pc.clearRect(0,0,photoLayer.width,photoLayer.height);pc.setTransform(C.width/w,0,0,C.height/h,0,0);drawPhoto(v,pc);pc.globalCompositeOperation='destination-in';pc.save();pc.translate(w/2+(295-a.center[0])*a.photoScale,a.cy+(297-a.center[1])*a.photoScale);pc.scale(a.scale,a.scale);pc.translate(-524,-350);pc.drawImage(bodyCanvas,0,0);pc.restore();ctx.globalAlpha=texture;ctx.drawImage(photoLayer,0,0,w,h);ctx.globalAlpha=1;
 }
 if(context>0){
  const pc=photoContext;pc.setTransform(1,0,0,1,0,0);pc.globalCompositeOperation='source-over';pc.clearRect(0,0,photoLayer.width,photoLayer.height);pc.setTransform(C.width/w,0,0,C.height/h,0,0);drawPhoto(v,pc);pc.setTransform(1,0,0,1,0,0);pc.globalCompositeOperation='destination-in';const factor=C.width/w,r=context*Math.hypot(w,h),grad=pc.createRadialGradient(w/2*factor,a.cy*factor,Math.max(0,r-w*.2)*factor,w/2*factor,a.cy*factor,Math.max(1,r)*factor);grad.addColorStop(0,'#fff');grad.addColorStop(1,'#fff0');pc.fillStyle=grad;pc.fillRect(0,0,photoLayer.width,photoLayer.height);ctx.drawImage(photoLayer,0,0,w,h);
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
 if(ext){draw(q);$('scrub').value=Math.round(q*1000);$('percent').textContent=Math.round(q*100)+' %';const text=q<.18?'Innervision · acercamiento':q<.32?'Símbolo original':q<.39?'Encendido · cuerpo → pica · tinta':q<.60?'Tinta · retirada':q<.80?'Pica original · retirada':'Salute · cubierta original';$('phase').textContent=text;$('live').textContent=text;$('scrub').setAttribute('aria-valuetext',Math.round(q*100)+' por ciento — '+text)}
 lastY=y;
}
function resize(){const oldh=h||innerHeight,oldY=scrollY;w=innerWidth;h=innerHeight;const d=Math.min(devicePixelRatio||1,1.5,Math.sqrt(2500000/(w*h)));C.width=Math.round(w*d);C.height=Math.round(h*d);if(ready){refreshSnap();scrollTo({top:oldY/oldh*h,behavior:'instant'})}schedule()}
function refreshSnap(){const f=frame.contentWindow;f.dispatchEvent(new f.Event('resize'));f.__F4.go(1);f.__F4.benchmark();capture();f.__F4.go(p);f.__F4.benchmark()}
function capture(){const src=frame.contentDocument.getElementById('scene');snap=document.createElement('canvas');snap.width=src.width;snap.height=src.height;snap.getContext('2d').drawImage(src,0,0)}
function mode(){if(frame.contentWindow.__F4&&frame.contentWindow.__F4.state.reduced!==reduced)frame.contentDocument.getElementById('motion').click();$('motion').textContent=reduced?'Movimiento reducido ✓':'Reducir movimiento';$('motion').setAttribute('aria-pressed',reduced);if(ready)requestAnimationFrame(()=>{refreshSnap();schedule()});schedule()}
async function init(){for(const [name,data]of Object.entries(PACKAGE.images)){const im=new Image();im.src=data;await im.decode();images[name]=im;stats.assets++}
 initBody();frame.srcdoc=PACKAGE.f4;
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
