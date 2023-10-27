from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import qrcode
import os
from PIL import Image
from io import BytesIO

def qrview(request):
    image_url = None

    if request.method == "POST":
        url = request.POST.get('link')
        qr = qrcode.QRCode(
            version=1,  # QR code version (1 to 40)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each "box" in the QR code
            border=4,  # Border size (in boxes)
        )

        # Add data to the QR code (in this case, a URL)
        data = url
        qr.add_data(data)
        qr.make(fit=True)

        # Create a QR code image
        img = qr.make_image(fill_color="black", back_color="white")

        # Create a BytesIO buffer to temporarily store the image
        image_buffer = BytesIO()
        img.save(image_buffer, format='PNG')
        
        # Get the image as bytes and rewind the buffer
        image_data = image_buffer.getvalue()
        image_buffer.seek(0)

        # Save the QR code image to the media folder
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filename = fs.save("my_qr_code.png", image_buffer)

        # Get the URL of the saved image
        image_url = fs.url(filename)

    return render(request, 'index.html', {'image_url': image_url})


# Create your views here.
