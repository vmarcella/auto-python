import logging

import xmltodict
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS

from gps_conversion import exif_to_decimal, rdf_to_decimal


def main():
    image1 = Image.open("photo-dublin-a1.jpg")
    logging.info(f"Obtaining the images height: {image1.height}")
    logging.info(f"Obtaining the images width: {image1.width}")

    logging.info(f"Obtaining the images format: {image1.format}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    main()
