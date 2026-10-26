// CP13: scroll distance only. Rendering always receives the accepted CP12 progress.
const rhythm = (()=>{
 const ranges={T34:[.10,.90],T45:[.18,.70]},edge=.10,floor=4/9;
 const clip=x=>Math.max(0,Math.min(1,x));
 const integral=t=>t*t*t-.5*t*t*t*t;
 // Integral of a positive C1 density: 1 at both ends, 4/9 at the center.
 // Its total is exactly .5. Inverse speed is bounded by 2.25, never infinite.
 function compressed(u){
  u=clip(u);if(u>1-edge)return .5-compressed(1-u);
  const ramp=edge*(1-(1-floor)*.5);
  if(u<edge)return u-(1-floor)*edge*integral(u/edge);
  return ramp+floor*(u-edge);
 }
 function distance(p,id){p=clip(p);const [a,b]=ranges[id];if(p<=a)return p;if(p>=b)return p-(b-a)/2;return a+(b-a)*compressed((p-a)/(b-a))}
 function progress(s,id){const end=distance(1,id);s=Math.max(0,Math.min(end,s));if(s===0)return 0;if(s===end)return 1;let a=0,b=1;for(let i=0;i<42;i++){const m=(a+b)/2;if(distance(m,id)<s)a=m;else b=m}return (a+b)/2}
 return {ranges,distance,progress,compressed,edge,floor};
})();
