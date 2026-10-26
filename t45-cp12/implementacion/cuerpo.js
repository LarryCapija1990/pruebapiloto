// Local-body SDF morph: no screen-sized flash and no independent axis/outline layer.
let bodyCanvas,bodyGL,bodyUniforms;
function initBody(){
 bodyCanvas=document.createElement('canvas');bodyCanvas.width=1066;bodyCanvas.height=600;
 const gl=bodyGL=bodyCanvas.getContext('webgl',{alpha:true,premultipliedAlpha:false,preserveDrawingBuffer:true,antialias:false});if(!gl)throw Error('WebGL del cuerpo M2 no disponible');
 function sh(type,src){const s=gl.createShader(type);gl.shaderSource(s,src);gl.compileShader(s);if(!gl.getShaderParameter(s,gl.COMPILE_STATUS))throw Error(gl.getShaderInfoLog(s));return s}
 const vs='attribute vec2 pos;varying vec2 uv;void main(){uv=vec2((pos.x+1.)*.5,(1.-pos.y)*.5);gl_Position=vec4(pos,0.,1.);}';
 const fs=`precision highp float;varying vec2 uv;uniform sampler2D field,original;uniform float q;
 float ramp(float a,float b,float x){float t=clamp((x-a)/(b-a),0.,1.);return t*t*(3.-2.*t);}
 void main(){vec4 f=texture2D(field,vec2(uv.x,uv.y*.5));vec4 ft=texture2D(field,vec2(uv.x,uv.y*.5+.5));float ds=(f.r*65280.+f.g*255.)/65535.*1024.-512.;float dt=(ft.r*65280.+ft.g*255.)/65535.*1024.-512.;
 float m=ramp(.325,.365,q),ink=ramp(.350,.390,q);float d=mix(ds,dt,m)+10.*sin(3.14159265*m);
 float body=smoothstep(-.85,.85,d);float pulse=ramp(.320,.335,q)*(1.-ramp(.335,.390,q));
 float halo=exp(-max(0.,-d)*max(0.,-d)/45.)*.30*(1.-ink);float a=max(body,halo);
 vec3 orange=mix(vec3(1.,.40,.06),vec3(1.,.74,.22),pulse*.7);vec3 color=mix(orange,vec3(.19,.20,.15),ink);
 vec4 orig=texture2D(original,uv);orig.rgb=1.-(1.-orig.rgb)*(1.-orig.rgb*.45*pulse);float enter=ramp(.325,.338,q);vec4 fresh=vec4(color,a);gl_FragColor=mix(orig,fresh,enter);
 }`;
 const pr=gl.createProgram();gl.attachShader(pr,sh(gl.VERTEX_SHADER,vs));gl.attachShader(pr,sh(gl.FRAGMENT_SHADER,fs));gl.linkProgram(pr);if(!gl.getProgramParameter(pr,gl.LINK_STATUS))throw Error(gl.getProgramInfoLog(pr));gl.useProgram(pr);
 const buf=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buf);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);const loc=gl.getAttribLocation(pr,'pos');gl.enableVertexAttribArray(loc);gl.vertexAttribPointer(loc,2,gl.FLOAT,false,0,0);
 [images.field,images.symbol].forEach((im,i)=>{gl.activeTexture(gl.TEXTURE0+i);const t=gl.createTexture();gl.bindTexture(gl.TEXTURE_2D,t);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MIN_FILTER,gl.LINEAR);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MAG_FILTER,gl.LINEAR);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_S,gl.CLAMP_TO_EDGE);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_T,gl.CLAMP_TO_EDGE);gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA,gl.RGBA,gl.UNSIGNED_BYTE,im);gl.uniform1i(gl.getUniformLocation(pr,i?'original':'field'),i)});
 bodyUniforms={q:gl.getUniformLocation(pr,'q')};gl.viewport(0,0,1066,600);
}
function renderBody(v){bodyGL.uniform1f(bodyUniforms.q,v);bodyGL.drawArrays(bodyGL.TRIANGLE_STRIP,0,4)}
