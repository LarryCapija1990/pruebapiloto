precision highp float;
uniform vec2 uSize;
uniform float uP;
uniform float uReduced;
uniform sampler2D uThunder;
uniform sampler2D uSpace;
uniform sampler2D uStars;
uniform sampler2D uSymbol;
uniform sampler2D uField;
uniform sampler2D uRay;
uniform sampler2D uOriginalAtlas;
uniform sampler2D uLineTexture;
varying vec2 vUv;
float ramp(float a,float b,float p){return smoothstep(a,b,p);}
float box(vec2 p,vec2 lo,vec2 hi){return step(lo.x,p.x)*step(lo.y,p.y)*step(p.x,hi.x)*step(p.y,hi.y);}
vec4 at(sampler2D tex,vec2 p){return texture2D(tex,p/vec2(1066.,600.));}
vec3 over(vec3 bg,vec4 fg,float a){return mix(bg,fg.rgb,clamp(fg.a*a,0.,1.));}
void main(){
 float p=uP;
 float opening=ramp(0.,.10,p),closing=ramp(.90,1.,p);
 float docH=mix(593.,594.,closing);
 float fit=min((uSize.x-40.)/600.,max(100.,uSize.y-(uSize.y<500.?120.:220.))/docH);
 float fill=max(uSize.x/1066.,uSize.y/600.);
 float reducedFit=min((uSize.x-24.)/1066.,max(100.,uSize.y-220.)/600.);
 float scale=mix(mix(fit,fill,opening),fit,closing);
 scale=mix(scale,reducedFit,uReduced);
 // A common, uniformly scaled camera registers both documentary originals.
 vec2 center=vec2(uSize.x*.5,uSize.y*.5-(uSize.y<500.?0.:12.));
 vec2 q=(vUv*uSize-center)/scale+vec2(533.,300.);
 vec3 dark=vec3(8.,10.,15.)/255.;
 float shift=280.*ramp(.30,.80,p)*(1.-uReduced);
 vec2 terrain=q-vec2(0.,shift);
 float terrainInside=box(terrain,vec2(0.),vec2(1066.,600.));
 vec3 space=at(uSpace,q).rgb;
 vec2 fields=at(uField,terrain).rg;
 // CP05 masks after undoing their terrain displacement give threshold ≈ p−.115.
 float threshold=p-.115;
 float reveal=ramp(fields.r-.13,fields.r+.13,threshold);
 // Never clamp the exposed top to a row of cloud pixels.
 vec3 sky=space;
 vec3 ground=at(uThunder,terrain).rgb;
 vec3 color=mix(sky,mix(ground,space,reveal),terrainInside);
 vec4 ray=at(uRay,terrain);
 // A slight scroll-bound charge keeps the retained photographic bolt alive.
 // No flicker or time-based pulsing; reduced motion keeps CP01 pixel-identical.
 float charge=1.+.30*clamp((p-.10)/.18,0.,1.)*(1.-uReduced);
 ray.rgb*=charge;ray.a*=charge;
 float rayAlpha=mix(1.-ramp(.28,.46,p),1.-ramp(.10,.22,p),uReduced)*terrainInside;
 color=over(color,ray,rayAlpha);
 float earlySky=mix(fields.g,1.,ramp(.25,.55,p));
 float starVisibility=ramp(.12,.65,p)*mix(1.,reveal*earlySky,terrainInside);
 color=over(color,at(uStars,q),starVisibility);
 float lineAlpha=ramp(.25,.43,p)*(1.-ramp(.82,.90,p))*(1.-uReduced);
 color=over(color,at(uLineTexture,q),lineAlpha);
 // The master is never warped. Reveal axis and arc separately.
 float axis=1.-smoothstep(11.,25.,abs(q.x-524.));
 float arcProgress=ramp(.54,.84,p);
 float arcReveal=ramp(440.-170.*arcProgress-18.,440.-170.*arcProgress+18.,q.y)*arcProgress;
 float axisReveal=mix(ramp(.82,.90,p),ramp(.65,.84,p),uReduced);
 // The arc's lower crossing is not part of the delayed vertical-axis mask.
 float junction=ramp(390.,405.,q.y)*(1.-ramp(425.,440.,q.y))*(1.-uReduced);
 float symbolReveal=mix(arcReveal,axisReveal,axis*(1.-junction));
 color=over(color,at(uSymbol,q),symbolReveal);
 float sceneInside=box(q,vec2(0.),vec2(1066.,600.));
 color=mix(dark,color,sceneInside);
 // Local documentary restoration in the original's registered footprint.
 vec2 docUV=(q-vec2(233.,3.))/vec2(600.,docH);
 float insideDoc=box(docUV,vec2(0.),vec2(1.));
 vec2 atlasUV=vec2((docUV.x+step(.5,p))*.5,docUV.y*docH/594.);
 vec3 documentary=texture2D(uOriginalAtlas,atlasUV).rgb;
 float docAmount=(1.-opening)+closing;
 color=mix(dark,color,1.-docAmount*(1.-insideDoc));
 // Delay restoration of scanned perimeter marks until the extensions withdraw.
 vec2 edge=min(docUV,1.-docUV)*vec2(600.,docH);
 float interior=smoothstep(0.,5.,min(edge.x,edge.y));
 float perimeter=mix(interior,1.,ramp(.9,1.,docAmount));
 color=mix(color,documentary,insideDoc*docAmount*perimeter);
 gl_FragColor=vec4(color,1.);
}
