import re
import sys
import typing
import urllib.error
from urllib.request import urlopen

import PIL
import pyautogui
from PIL import Image


def get_image(url: str) -> typing.Optional["PIL.Image"]:
    url_validator = """(http)?s?:?(\/\/[^"']*\.(?:png|jpg|jpeg|gif|png|svg))"""
    correct = re.match(url_validator, url)

    if correct:
        try:
            return Image.open(urlopen(url))
        except urllib.error.URLError:
            sys.exit("Unexpected error while retrieving the image. Please verify provided URL.")
    else:
        sys.exit("Please provide a correct URL to image.")


def get_board_position() -> typing.Optional[list]:
    if (position := pyautogui.locateOnScreen("assets/board.png", confidence=0.9)) is not None:
        return position
    else:
        sys.exit("Drawing board has not been found on the screen. Please make sure than the entire board is visible.")


def create_representation(image: PIL.Image, quality: int = 2, drawing_method: int = 0) -> typing.Optional[list]:
    pass
