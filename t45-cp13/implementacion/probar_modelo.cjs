const fs=require('fs'),vm=require('vm'),path=require('path');
const root=path.resolve(__dirname,'..');const r=vm.runInNewContext(fs.readFileSync(path.join(__dirname,'ritmo.js'),'utf8')+';rhythm');
const checks=[];function check(name,pass,details){checks.push({name,passed:!!pass,details});if(!pass)process.exitCode=1}
for(const id of ['T34','T45']){
 const [a,b]=r.ranges[id];check(id+' abstracto exactamente mitad',Math.abs((r.distance(b,id)-r.distance(a,id))/(b-a)-.5)<1e-12);
 check(id+' acercamiento conserva distancia',Math.abs(r.distance(a,id)-a)<1e-12);
 check(id+' revelación conserva distancia',Math.abs((r.distance(1,id)-r.distance(b,id))-(1-b))<1e-12);
 let monotone=true,maxInverse=0,maxSpeed=0;
 for(let i=0;i<=10000;i++){const p=i/10000,d=r.distance(p,id);maxInverse=Math.max(maxInverse,Math.abs(r.progress(d,id)-p));if(i&&d<=r.distance((i-1)/10000,id))monotone=false;if(i)maxSpeed=Math.max(maxSpeed,1e-4/(d-r.distance((i-1)/10000,id)))}
 check(id+' monótono, sin pausas insertadas',monotone);check(id+' ida/vuelta analítica',maxInverse<1e-10,maxInverse);check(id+' velocidad acotada',maxSpeed<=2.250001,maxSpeed);
 for(const p of [a,b]){const e=1e-6,left=(r.distance(p,id)-r.distance(p-e,id))/e,right=(r.distance(p+e,id)-r.distance(p,id))/e;check(id+' empalme suave '+p,Math.abs(left-right)<1e-6&&Math.abs(left-1)<1e-6,{left,right})}
}
const total=5.5*(r.distance(1,'T34')+r.distance(1,'T45'))+.2;
check('Total reducido sin añadir pausas',Math.abs(total-7.57)<1e-12,{before:11.2,after:total,reduction:1-total/11.2,hold:.2});
fs.writeFileSync(path.join(root,'evidencias/MODELO.json'),JSON.stringify({checks,passed:checks.filter(c=>c.passed).length,failed:checks.filter(c=>!c.passed).length},null,2));console.log(checks.filter(c=>c.passed).length,'PASS',checks.filter(c=>!c.passed).length,'FAIL');
