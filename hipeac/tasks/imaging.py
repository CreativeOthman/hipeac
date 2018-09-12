import os

from celery.decorators import task
from PIL import Image

from hipeac.tools.imaging import contain, generate_square_thumbnail, resize, trim_transparency


@task()
def generate_banner_variants(path: str):
    parts = os.path.splitext(path)
    img = Image.open(path)

    variants = {
        'sm': contain(img.copy(), width=100, height=25),
        'md': contain(img.copy(), width=400, height=100),
        'lg': contain(img.copy(), width=1200, height=300),
        'th': contain(img.copy(), width=200, height=200),
    }

    for size, image in variants.items():
        image.save(''.join([parts[0], '_', size, '.jpg']), 'JPEG')

    return True


@task()
def generate_logo_variants(path: str):
    parts = os.path.splitext(path)
    trimmed_img = trim_transparency(Image.open(path))

    variants = {
        'sm': resize(trimmed_img.copy(), max_width=100, max_height=50),
        'md': resize(trimmed_img.copy(), max_width=150, max_height=75),
        'lg': resize(trimmed_img.copy(), max_width=200, max_height=100),
        'th': generate_square_thumbnail(trimmed_img.copy(), side=200, padding=20),
    }

    for size, image in variants.items():
        image.save(''.join([parts[0], '_', size, '.png']), 'PNG')

    return True
