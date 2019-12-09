# Download an image from the Web

import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + "indirilen.jpg"
    urllib.request.urlretrieve(url,full_name) #download this / save as a name

url_to_download = "https://www.mercedes-amg.com/dam/hq/model-pages/Vehicles/E-class/Coup%C3%A9/E53/C238-53-ext-SSPIP84735-hd.jpg/_jcr_content/renditions/cq5dam.web.1280.1280.jpeg.image_file.716.403.file/cq5dam.web.1280.1280.jpg"
download_web_image(url_to_download)






