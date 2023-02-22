import qrcode as qr

img = qr.make("https://www.youtube.com/channel/UC-Z_fXgbVEBreXA9sJghIlQ")
img.save("@coding_world.png")