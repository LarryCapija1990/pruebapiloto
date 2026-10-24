const $ = id => document.getElementById(id);
const canvas = $('scene');
const media = matchMedia('(prefers-reduced-motion: reduce)');
const metrics = { renders: 0, frameMs: [], loadErrors: [], contextLosses: 0, assets: 0 };
let reduced = media.matches, override = false, gl, locations, program, p = 0, queued = false, ready = false;
let width = 0, height = 0, lastPhase = -1;
let geometry = [];
let lineContext, lineTexture;
const clamp = x => Math.max(0, Math.min(1, x));
const smooth = (a, b, x) => { const t = clamp((x-a)/(b-a)); return t*t*(3-2*t); };
// Correspondences start at the bottom of Thunder's discharge and end in the cloud.
const irregular = [[460,245],[458,234],[460,225],[462,214],[464,201],[464,191],[476,180],[482,176],[485,165],[497,160],[510,150],[516,144],[539,139],[554,133],[574,126],[596,112]];
const assetNames = ['thunder-scene.png','space.png','stars.png','symbol.png','reveal-field.png','lightning.png','thunder-original.jpg','innervision-original.jpg'];
const uniforms = ['uThunder','uSpace','uStars','uSymbol','uField','uRay','uOriginalAtlas','uLineTexture'];

function linePoints(progress) {
  const x=clamp((progress-.1)/.7)*(geometry.length-1),i=Math.min(geometry.length-2,Math.floor(x)),t=x-i;
  const a=geometry[Math.max(0,i-1)],b=geometry[i],c=geometry[i+1],d=geometry[Math.min(geometry.length-1,i+2)];
  // Catmull–Rom interpolates point correspondences, never rendered frames.
  return b.flatMap((point,j)=>point.map((v,k)=>.5*(2*v+(-a[j][k]+c[j][k])*t+(2*a[j][k]-5*v+4*c[j][k]-d[j][k])*t*t+(-a[j][k]+3*v-3*c[j][k]+d[j][k])*t*t*t)));
}
function updateLine(progress) {
  const ctx=lineContext, points=linePoints(progress),t=smooth(.22,.65,progress);
  ctx.clearRect(0,0,1066,600);
  if (!reduced && progress>.10 && progress<.90) {
    ctx.strokeStyle=`rgb(${255*(.66+.34*t)},${255*(.79-.12*t)},${255*(1-.72*t)})`;
    ctx.lineWidth=1+1.5*smooth(.26,.68,progress);ctx.lineCap='round';ctx.lineJoin='round';
    ctx.beginPath();ctx.moveTo(points[0],points[1]);
    for(let i=2;i<points.length;i+=2)ctx.lineTo(points[i],points[i+1]);
    ctx.stroke();
  }
  gl.activeTexture(gl.TEXTURE7);gl.bindTexture(gl.TEXTURE_2D,lineTexture);
  gl.texSubImage2D(gl.TEXTURE_2D,0,0,0,gl.RGBA,gl.UNSIGNED_BYTE,ctx.canvas);
}

function fail(error) {
  console.error(error);
  $('loading').hidden = true;
  const node = $('error'); node.hidden = false;
  node.replaceChildren(document.createTextNode(`No se ha podido iniciar la composición: ${error.message}. `));
  const retry = document.createElement('button'); retry.textContent = 'Reintentar'; retry.onclick = () => location.reload();
  node.append(retry, document.createElement('br'));
  for (const [label, src] of [['Ver Thunder','thunder-original.jpg'],['Ver Innervision','innervision-original.jpg']]) {
    const a = document.createElement('a'); a.href = `assets/${src}`; a.textContent = label; node.append(a, document.createTextNode(' · '));
  }
  $('scrub').disabled = true;
}
function shader(type, source) {
  const s = gl.createShader(type); gl.shaderSource(s, source); gl.compileShader(s);
  if (!gl.getShaderParameter(s,gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s));
  return s;
}
async function loadImage(name) {
  const img = new Image(); img.src = `assets/${name}`;
  try { await img.decode(); metrics.assets++; return img; }
  catch { metrics.loadErrors.push(name); throw new Error(`falló la carga de ${name}`); }
}
function mode() {
  $('motion').setAttribute('aria-pressed', String(reduced));
  $('motion').textContent = reduced ? 'Movimiento reducido ✓' : 'Reducir movimiento';
  $('hint').textContent = reduced ? 'Cámara fija · scroll o control de recorrido' : 'Desliza para transformar · vuelve para regresar';
  schedule();
}
function extent() { return Math.max(1,$('journey').offsetHeight-$('stage').clientHeight); }
function scrollProgress() { return clamp((scrollY-$('journey').offsetTop)/extent()); }
function go(value) { window.scrollTo({top:$('journey').offsetTop+clamp(value)*extent(),behavior:'instant'}); schedule(); }
function schedule() { if (!queued) { queued = true; requestAnimationFrame(draw); } }
function resize() {
  width = $('stage').clientWidth; height = $('stage').clientHeight;
  // Limit mobile memory and fill rate; source images do not support macro detail.
  const dpr = Math.min(devicePixelRatio || 1, 1.5, Math.sqrt(2500000/(width*height)));
  canvas.width = Math.round(width*dpr); canvas.height = Math.round(height*dpr);
  if (gl) gl.viewport(0,0,canvas.width,canvas.height);
  schedule();
}
function draw() {
  queued = false;
  if (!ready || gl.isContextLost()) return;
  const begin = performance.now(); p = scrollProgress();
  gl.uniform2f(locations.uSize,width,height);
  gl.uniform1f(locations.uP,p); gl.uniform1f(locations.uReduced,reduced ? 1 : 0);
  updateLine(p);
  gl.drawArrays(gl.TRIANGLE_STRIP,0,4);
  $('scrub').value = String(Math.round(p*1000));
  const percent = Math.round(p*100); $('percent').textContent = `${percent} %`;
  $('scrub').setAttribute('aria-valuetext',`${percent} por ciento`);
  const phase = p<.1?0:p<.4?1:p<.7?2:p<.9?3:4;
  if (phase !== lastPhase) {
    lastPhase = phase;
    const text = [
      ['01 / THUNDER AND LIGHTNING','Del trueno<br>al espacio.','Thin Lizzy → Phenomena','Portada original de Thunder and Lightning, Thin Lizzy.'],
      ['02 / EL CIELO SE ABRE','Dentro<br>del cielo.','Las primeras estrellas.','El cielo oscuro se convierte en espacio; aparecen estrellas.'],
      ['03 / ASCENSO','La luz<br>cambia de forma.','De la descarga al eje.','El terreno se retira y el rayo se alinea hacia el signo.'],
      ['04 / INNERVISION','Otro<br>universo.','Phenomena · Innervision','El símbolo original se revela sobre el campo estrellado.'],
      ['05 / PORTADA ORIGINAL','Innervision.','Phenomena','Reencuadre hacia la portada original completa de Innervision, Phenomena.']
    ][phase];
    $('phase').textContent=text[0]; $('title').innerHTML=text[1]; $('description').textContent=text[2]; $('accessible-state').textContent=text[3];
  }
  // Editorial captions step out of the artwork during the intermediate view.
  document.querySelector('.caption').style.opacity = (width>680 && width<1250 && p>.04&&p<.97) ? '0' : '1';
  metrics.renders++; metrics.frameMs.push(performance.now()-begin);
  if (metrics.frameMs.length>2000) metrics.frameMs.shift();
  canvas.dataset.progress=p.toFixed(6);
}

async function init() {
  gl = canvas.getContext('webgl',{alpha:false,antialias:false,depth:false,stencil:false,preserveDrawingBuffer:true,powerPreference:'low-power'});
  if (!gl) throw new Error('WebGL no está disponible; abre este prototipo en un navegador con WebGL habilitado');
  const [response, geometryResponse, ...images] = await Promise.all([fetch('scene.frag'),fetch('assets/line-geometry.json'),...assetNames.map(loadImage)]);
  if (!response.ok) throw new Error(`shader HTTP ${response.status}`);
  if (!geometryResponse.ok) throw new Error(`geometría HTTP ${geometryResponse.status}`);
  geometry=[irregular,...(await geometryResponse.json()).map(s=>s.points)];
  const frag = await response.text();
  program = gl.createProgram();
  gl.attachShader(program,shader(gl.VERTEX_SHADER,'attribute vec2 aPos; varying vec2 vUv; void main(){vUv=vec2((aPos.x+1.)*.5,(1.-aPos.y)*.5);gl_Position=vec4(aPos,0.,1.);}'));
  gl.attachShader(program,shader(gl.FRAGMENT_SHADER,frag)); gl.linkProgram(program);
  if (!gl.getProgramParameter(program,gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(program));
  gl.useProgram(program);
  const buffer=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buffer);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
  const attribute=gl.getAttribLocation(program,'aPos');gl.enableVertexAttribArray(attribute);gl.vertexAttribPointer(attribute,2,gl.FLOAT,false,0,0);
  locations=Object.fromEntries(['uSize','uP','uReduced',...uniforms].map(n=>[n,gl.getUniformLocation(program,n)]));
  // Pack documentary originals at native size: 8 samplers suffice even on WebGL1.
  const atlas=document.createElement('canvas');atlas.width=1200;atlas.height=594;
  const atlasContext=atlas.getContext('2d');atlasContext.drawImage(images[6],0,0);atlasContext.drawImage(images[7],600,0);
  const lineCanvas=document.createElement('canvas');lineCanvas.width=1066;lineCanvas.height=600;
  lineContext=lineCanvas.getContext('2d');
  [...images.slice(0,6),atlas,lineCanvas].forEach((img,i)=>{
    gl.activeTexture(gl.TEXTURE0+i);const texture=gl.createTexture();gl.bindTexture(gl.TEXTURE_2D,texture);
    gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL,false);gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL,false);
    gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MIN_FILTER,gl.LINEAR);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MAG_FILTER,gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_S,gl.CLAMP_TO_EDGE);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_T,gl.CLAMP_TO_EDGE);
    gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA,gl.RGBA,gl.UNSIGNED_BYTE,img);gl.uniform1i(locations[uniforms[i]],i);
    if(i===7)lineTexture=texture;
  });
  const error=gl.getError();if(error!==gl.NO_ERROR)throw new Error(`WebGL error ${error}`);
  ready=true;resize();mode();draw();$('loading').hidden=true;
  window.__F4={
    go, metrics, get state(){return {progress:p,reduced,ready,width,height,buffer:[canvas.width,canvas.height],terrainShift:280*smooth(.3,.8,p)*(reduced?0:1)};},
    // Manual GPU timing for the validation script; no continuous animation loop.
    benchmark(){const start=performance.now();draw();gl.finish();return performance.now()-start;}
  };
}
$('scrub').addEventListener('input',e=>go(Number(e.target.value)/1000));
$('begin').addEventListener('click',()=>go(0));$('end').addEventListener('click',()=>go(1));
$('motion').addEventListener('click',()=>{override=true;reduced=!reduced;mode();});
media.addEventListener('change',e=>{if(!override){reduced=e.matches;mode();}});
window.addEventListener('scroll',schedule,{passive:true});window.addEventListener('resize',resize);
new ResizeObserver(resize).observe($('stage'));
canvas.addEventListener('webglcontextlost',e=>{e.preventDefault();metrics.contextLosses++;ready=false;fail(new Error('se perdió el contexto gráfico; recarga para continuar'));});
mode();init().catch(fail);
