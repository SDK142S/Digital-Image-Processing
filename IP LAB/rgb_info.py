from PIL import Image
def print_image_info(image_path):
    img=Image.open(image_path)
    img.show()
    print("image size=",img.size)
    print("image format=",img.format)
    print("image mode=",img.mode)
    r_channel,g_channel,b_channel=img.split()
    pixel_data=list(img.getdata())
    first_pixel_color=pixel_data[50]
    print("color of first pixel",first_pixel_color)
image_path="img1.jpeg"
print_image_info(image_path)