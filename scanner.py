#Importing library
import qrcode

#Data to encode

data="Hello World"

#creating an instance of QRCode class

qr=qrcode.QRCode(version=1,box_size=12,border=5)

#Adding data to the instance 'qr'

qr.add_data(data)

qr.make(fit=True)
img=qr.make_image(fill_color='orange',back_color='white')

img.save('sunitha.png')
