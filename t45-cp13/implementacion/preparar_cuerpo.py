from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw,ImageFilter
from scipy.ndimage import distance_transform_edt,binary_fill_holes,binary_closing,label,gaussian_filter
R=Path(__file__).resolve().parents[1];S=R/'NV_SCOTT_T45_M2_CP10_v1.0'
a=np.array(Image.open(S/'recursos_F4/symbol.png').convert('RGBA'));source=(a[:,:,3]>60)&(a[:,:,:3].max(2)>145)
# Segment the actual ink perimeter in a small ROI. Manual ROI excludes adjacent card art,
# not the authentic wavy edge. Keep the largest connected component and fill ornament holes.
im=np.array(Image.open(S/'originales/salute.jpg').convert('RGB'));roi=Image.new('L',(600,593));dr=ImageDraw.Draw(roi)
dr.polygon([(296,276),(301,282),(310,288),(309,298),(309,307),(302,310),(301,311),(304,317),(289,318),(292,310),(283,310),(279,303),(280,294),(287,284)],fill=255)
mask=(im.mean(2)<135)&(np.array(roi)>0);mask=binary_closing(mask,iterations=1);labs,n=label(mask);sizes=np.bincount(labs.ravel());sizes[0]=0;mask=binary_fill_holes(labs==sizes.argmax())
Image.fromarray((mask*255).astype('uint8')).save(R/'assets/pica-mascara-original.png')
# Bicubic interpolation rounds scan-pixel stair steps; no polygonal guide becomes the final edge.
tiny=Image.fromarray((mask*255).astype('uint8')).crop((270,265,320,325)).resize((400,480),Image.Resampling.BICUBIC).filter(ImageFilter.GaussianBlur(5))
target=Image.new('L',(1066,600));target.paste(tiny,(524+(270-295)*8,350+(265-297)*8));target=np.array(target)>127
fields=[]
for index,m in enumerate([source,target]):
 d=distance_transform_edt(m)-distance_transform_edt(~m);d=gaussian_filter(d,10 if index==0 else .7);u=np.round((np.clip(d,-512,512)+512)/1024*65535).astype('uint16');fields.extend([(u>>8).astype('uint8'),(u&255).astype('uint8')])
opaque=np.full_like(fields[0],255);zero=np.zeros_like(fields[0]);packed=np.concatenate([np.stack([fields[0],fields[1],zero,opaque],2),np.stack([fields[2],fields[3],zero,opaque],2)],0);Image.fromarray(packed,'RGBA').save(R/'assets/campos-cuerpo.png')
print('SDF and source-ink mask generated')
