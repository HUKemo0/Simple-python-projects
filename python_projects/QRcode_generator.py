import qrcode


def qr_generator(link, file_name):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(link)
    image = qr.make_image(fill_color='black', back_color='white')
    image.save(file_name)
    print(f'QR code saved as {file_name}')


link = input('Please enter your link: ').strip()
file_name = input('Enter the file name: ').strip()
file_name += '.png'
qr_generator(link, file_name)
