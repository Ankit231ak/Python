import qrcode

data = input("Enter text or URL to generate QR code: ")
img = qrcode.make(data)
img.save("qrcode.png")
print("QR code saved as qrcode.png!") 