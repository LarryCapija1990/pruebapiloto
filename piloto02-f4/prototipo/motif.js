// CP02: only the central discharge changes. Every value depends on absolute scroll.
const clamp = x => Math.max(0, Math.min(1, x));
export function smooth(a, b, x) { const t=clamp((x-a)/(b-a)); return t*t*(3-2*t); }
const mix = (a,b,t) => a+(b-a)*t;
const jag = [0,.55,-.7,.3,-.25,.85,-.5,.15,-.8,.45,-.1,.65];

export function createMotif(source) {
  const start=source[0],end=source[source.length-1];
  const dx=end[0]-start[0],dy=end[1]-start[1],chord=Math.hypot(dx,dy);
  const normal=[-dy/chord,dx/chord],lengths=[0];
  for(let i=1;i<source.length;i++) lengths.push(lengths[i-1]+Math.hypot(source[i][0]-source[i-1][0],source[i][1]-source[i-1][1]));
  // Resample the original irregular contour by arc length, preserving its bends.
  const profile=Array.from({length:48},(_,i)=>{
    const u=i/47,d=u*lengths[lengths.length-1];
    let k=0;while(k<source.length-2&&lengths[k+1]<d)k++;
    const t=(d-lengths[k])/(lengths[k+1]-lengths[k]);
    const pt=[mix(source[k][0],source[k+1][0],t),mix(source[k][1],source[k+1][1],t)];
    return {u,lateral:(pt[0]-mix(start[0],end[0],u))*normal[0]+(pt[1]-mix(start[1],end[1],u))*normal[1]};
  });
  return function shape(progress,tracking,terrainShift) {
    const align=smooth(.28,.52,progress),straightening=smooth(.62,.90,progress);
    const bottom=[mix(start[0],tracking[0],align),mix(start[1]+terrainShift,tracking[1],align)];
    const top=[mix(end[0],tracking[tracking.length-2],align),mix(end[1]+terrainShift,tracking[tracking.length-1],align)];
    const vx=top[0]-bottom[0],vy=top[1]-bottom[1],len=Math.hypot(vx,vy);
    const nx=-vy/len,ny=vx/len,scale=Math.sqrt(len/chord),retain=1-straightening;
    const points=profile.map(({u,lateral},i)=>{
      // Fixed spatial irregularity, no animated noise or temporal flicker.
      const detail=jag[i%jag.length]*4*smooth(.28,.48,progress)*Math.sin(Math.PI*u);
      const offset=(lateral*scale+detail)*retain;
      const y=mix(bottom[1],top[1],u)+ny*offset;
      const x=mix(mix(bottom[0],top[0],u),524,smooth(.82,.90,progress))+nx*offset;
      // Join the existing arc locally while the rest of the bolt remains bent.
      const join=smooth(.62,.82,progress)*Math.exp(-Math.pow((y-418)/38,2));
      return [mix(x,524,join),y];
    });
    return {points,straightening,colorProgress:smooth(.35,.82,progress),
      bodyWidth:3.4+1.8*smooth(.30,.78,progress),coreWidth:1.35+.8*smooth(.30,.78,progress)};
  };
}
