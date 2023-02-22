import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,error_correction= qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data("https://www.youtube.com/channel/UC-Z_fXgbVEBreXA9sJghIlQ")
qr.make(fit=True)
img = qr.make_image(fill_color = "Black", back_color = "Grey")
img.save("@coding_world2.png")
