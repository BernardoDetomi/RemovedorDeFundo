from rembg import remove
from PIL import Image



url = Image.open('imgfundo.jpg')
output = remove(url)
output.save('imgsemfundo.png')