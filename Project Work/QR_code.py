import qrcode
import PySimpleGUI as sg
import base64
import os
import sys

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def encode_image_to_base64(filename):
    with open(filename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string

def main():
    sg.theme('DarkBlue3')
    layout = [
        [sg.Text('Enter the data to encode as QR code',text_color='blue',background_color='black')],
        [sg.InputText()],
        [sg.Button('Generate'), sg.Button('Exit')],
        [sg.Image(key='-IMAGE-', size=(300, 300))],
    ]
    window = sg.Window('QR Code Generator', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Generate':
            data = values[0]
            filename = 'qrcode.png'
            generate_qr_code(data, filename)
            encoded_image = encode_image_to_base64(filename)
            os.remove(filename)
            window['-IMAGE-'].update(data=encoded_image)

    window.close()

if __name__ == '__main__':
    main()