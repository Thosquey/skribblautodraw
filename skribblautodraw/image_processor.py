import re
import typing
import urllib.error
from urllib.request import urlopen

import PIL
from PIL import Image


def get_image(url: str) -> typing.Optional["PIL.Image"]:
    url_validator = """(http)?s?:?(\/\/[^"']*\.(?:png|jpg|jpeg|gif|png|svg))"""
    correct = re.match(url_validator, url)

    if correct:
        try:
            return Image.open(urlopen(url))
        except urllib.error.URLError:
            print("Unexpected error while retrieving the image. Please verify provided URL.")
    else:
        print("Please provide a correct URL to image.")


def create_representation(image: PIL.Image, quality: int = 2) -> typing.Optional[list]:
    pass

