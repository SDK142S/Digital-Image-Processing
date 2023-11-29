from PIL import Image
import numpy as np
image=Image.open('img1.jpeg')
image_array=255-np.array(image)
negative_image=Image.fromarray(image_array)
negative_image.show()
negative_image.save('negative_image.jpeg')


