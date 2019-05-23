import logging

import xmltodict
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS

from gps_conversion import exif_to_decimal, rdf_to_decimal


def get_exif(image: Image.Image) -> dict:
    exif_data = {}
    for tag, value in image._getexif().items():
        exif_data[TAGS.get(tag, tag)] = value
    return exif_data


def main():
    image1 = Image.open("photo-dublin-a1.jpg")
    logging.info("---BASIC IMAGE STATS OF DUBLIN JPG---")
    logging.info(f"Obtaining the images height: {image1.height}")
    logging.info(f"Obtaining the images width: {image1.width}")
    logging.info(f"Obtaining the images format: {image1.format}")

    logging.info("---GETTING EXIF DATA FROM IMAGE 1---")
    exif_data = get_exif(image1)
    logging.info(f"Phone model: {exif_data['Model']}")
    logging.info(f"Lens model: {exif_data['LensModel']}")
    logging.info(f"Time created: {exif_data['DateTimeOriginal']}")

    image2 = Image.open("photo-dublin-a2.png")
    logging.info("---BASIC IMAGE STATS OF DUBLIN PNG---")
    logging.info(f"Obtaining the images height: {image2.height}")
    logging.info(f"Obtaining the images width: {image2.width}")
    logging.info(f"Obtaining the images format: {image2.format}")
    logging.info(image2.info)
    logging.info("PIL won't read the XMP data on the file, can't move on for now :(")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    main()
