
from flask import Flask, request, send_file, render_template
from PIL import Image
import segno
import os

app = Flask(__name__)

# Path to store generated QR codes
QR_CODE_FOLDER = 'qrcodes'
if not os.path.exists(QR_CODE_FOLDER):
    os.makedirs(QR_CODE_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['qr_input']
        # Generate QR code with the user input
        output_file = generate_qr_code(user_input)
        return send_file(output_file, as_attachment=True)
    return render_template('index.html')

def generate_qr_code(input_text):
    LOGO = 'apkudo_logo_new.jpg'
    OUTPUT = os.path.join(QR_CODE_FOLDER, f"{input_text}.png")

    # Create the QR code
    qr = segno.make_qr(input_text, error='H')
    qr.save(OUTPUT, finder_dark='#14C374', finder_light="#FFFFFF", scale=100)

    # Open the generated QR code image
    img = Image.open(OUTPUT).convert("RGBA")
    width, height = img.size

    # Define logo size and open logo image
    logo_size = 900
    logo = Image.open(LOGO).convert("RGBA")
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))

    # Resize and paste the logo into the QR code
    logo = logo.resize((xmax - xmin, ymax - ymin))
    img.paste(logo, (xmin, ymin, xmax, ymax), logo)
    img.save(OUTPUT)

    return OUTPUT

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

