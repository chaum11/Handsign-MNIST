from PIL import Image

tmp = 'MOSUNGBI'
name = []

for i in tmp:
    name.append('original_img/'+i+'.png')

name.append('original_img/N2.png')

print(name)


for i in name:
    img = Image.open(i)
    img_gray = img.convert('L')
    img_gray_resized = img_gray.resize((28, 28))

    img_gray_resized.save('img/' + i[13:-4] + '_changed.png')


