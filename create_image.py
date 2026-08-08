from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

WIDTH = 1080
HEIGHT = 1920

BACKGROUND = "assets/bg.png"
FONT = "assets/sanva_font.ttf"
OUTPUT = "output/quote.png"


def create_image(quote):

    image = Image.open(BACKGROUND).convert("RGB")
    image = image.resize((WIDTH, HEIGHT))

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(FONT, 60)

    # Keep large margins so YouTube buttons never overlap
    max_text_width = 700

    wrapped = []

    for paragraph in quote.split("\n"):

        words = paragraph.split()

        line = ""

        for word in words:

            test = line + word + " "

            bbox = draw.textbbox((0, 0), test, font=font)

            if bbox[2] <= max_text_width:
                line = test
            else:
                wrapped.append(line.strip())
                line = word + " "

        if line:
            wrapped.append(line.strip())

    line_spacing = 20

    heights = []

    for line in wrapped:
        bbox = draw.textbbox((0, 0), line, font=font)
        heights.append(bbox[3] - bbox[1])

    total_height = sum(heights) + line_spacing * (len(wrapped) - 1)

    y = (HEIGHT - total_height) / 2

    for i, line in enumerate(wrapped):

        bbox = draw.textbbox((0, 0), line, font=font)

        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = (WIDTH - text_width) / 2

        draw.text(
            (x, y),
            line,
            fill="white",
            font=font
        )

        y += text_height + line_spacing

    os.makedirs("output", exist_ok=True)

    image.save(OUTPUT)

    return OUTPUT