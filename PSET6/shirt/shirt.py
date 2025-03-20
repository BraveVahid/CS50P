import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_image = sys.argv[1]
    output_image = sys.argv[2]

    if not input_image.lower().endswith((".jpg", ".jpeg", ".png")) or not output_image.lower().endswith(
        (".jpg", ".jpeg", ".png")
    ):
        sys.exit("Invalid file format")

    if not input_image.split(".")[-1].lower() == output_image.split(".")[-1].lower():
        sys.exit("Input and output file extensions must match")

    try:
        shirt = Image.open("shirt.png")
        with Image.open(input_image) as im:
            resized_im = ImageOps.fit(im, shirt.size)
            resized_im.paste(shirt, shirt)
            resized_im.save(output_image)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
