from PIL import Image
import pandas as pd
import numpy as np

tmp = 'MOSUNGBI'
name = []

for i in tmp:
    name.append('img/realworld/img/'+i+'_changed.png')

name.append('img/realworld/img/N2_changed.png')

file_to_bit = []
for i in name:
    img = Image.open(i)
    bit = np.array(img)
    tmp = np.concatenate(bit).tolist()
    
    file_to_bit.append(tmp)

df = pd.DataFrame(file_to_bit)

myname = 'MOSUNGBIN'
label = []

for i in myname:
    label.append(i)

df.insert(loc=0, column='label', value=label)
df.to_csv('real_data.csv', index=False)