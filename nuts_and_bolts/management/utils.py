import os
import secrets
from PIL import Image
from flask import current_app


def save_image(form_image):
    _, ext = os.path.splitext(form_image.filename)
    image_filename = secrets.token_hex(8) + ext
    print(image_filename)
    image_path = os.path.join(
        current_app.root_path,
        'static/images/products',
        image_filename
    )
    open_image = Image.open(form_image)
    open_image.save(image_path)
    return image_filename
