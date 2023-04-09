from PIL import Image, ImageDraw, ImageFilter, ImageFont
from rich.prompt import Prompt
from rich.traceback import install
install(show_locals = True)

# path to the main picture
main_pic_path = Prompt.ask("Input the Main Picture Path")

# text to be inserted
text = Prompt.ask("Text to be inserted over the picture")

# font size and font file path
font_size = 150
font_path = "C:\\Users\\hadir\\Documents\\Mulish\\Muli-Bold.ttf"

# open the main picture
main_pic = Image.open(main_pic_path)

# create a new blank image with the same size as the main picture
new_image = Image.new(mode='RGB', size=main_pic.size, color=(0, 0, 0, 0))

# paste the main picture onto the new image
new_image.paste(main_pic, (0, 0))

# get the dimensions of the new image
width, height = new_image.size

# create a new image for the text with the same size as the new image
text_image = Image.new(mode='RGBA', size=(width, font_size+20), color=(0, 0, 0, 0))

# get a drawing context for the text image
draw = ImageDraw.Draw(text_image)

# load the font file and set the font size
font = ImageFont.truetype(font_path, font_size)

# get the size of the text and calculate the position
text_width, text_height = draw.textsize(text, font=font)
text_x = int((width - text_width) / 2)
text_y = height - font_size - 150

# draw the text onto the text image
draw.text((text_x, 10), text, font=font, fill=(255, 255, 255, 255))

# apply a background blur to the lower side of the new image
blur_radius = 20
blur_box = (0, text_y, width, height)
blur_region = new_image.crop(blur_box)
blur_region = blur_region.filter(ImageFilter.GaussianBlur(radius=blur_radius))
new_image.paste(blur_region, blur_box)

# paste the text image onto the new image
new_image.paste(text_image, (0, text_y))

# save the new image
saving_path = Prompt.ask("Path to the saved image")
new_image.save(saving_path)

