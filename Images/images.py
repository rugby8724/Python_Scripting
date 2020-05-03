from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
# filtered_img = img.convert('L')
# filtered_img = img.filter(ImageFilter.SHARPEN)
# resize =filtered_img.resize((300, 300))
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save('region.png', 'png')

img = Image.open('./astro.jpg')
img.thumbnail((400,400))
img.save('thumbnail.jpg')
