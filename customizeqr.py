import qrcode as qr
from PIL import Image

q=qr.QRCode(version=1,
            error_correction=qr.constants.ERROR_CORRECT_H,
            box_size=34,
            border = 4)

q.add_data("https://youtube.com/@raonegamingbeastmode1352?si=63aJlXsNnCUpLU-T")
q.make(fit=True)
img = q.make_image(fill_color="pink",back_color="black")
img.save("Ghost.png")
