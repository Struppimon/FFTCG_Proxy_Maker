import os
import os.path
from PIL import Image

def Create_PDF(image_list, output_path="gen/output.pdf"):
    #Size of a card at 300 DPI: 63mm x 88mm ≈ 248 x 346 pixels
    card_width, card_height = 248, 346

    #Page will divide into a 3x3 grid
    padding = 10
    cols, rows = 3, 3
    page_width = cols * card_width + (cols + 1) * padding
    page_height = rows * card_height + (rows + 1) * padding

    pages = []
    for i in range(0, len(image_list), 9):
        page = Image.new('RGB', (page_width, page_height), color='white')

        for j, card in enumerate(image_list[i:i+9]):
            with Image.open(card) as img:
                img = img.convert("RGB")
                img = img.resize((card_width, card_height))

                col = j % cols
                row = j // cols

                x = padding + col * (card_width + padding)
                y = padding + row * (card_height + padding)

                page.paste(img, (x, y))
        pages.append(page)

    #Delete existing pdf file
    if os.path.exists(output_path):
        os.remove(output_path)

    pages[0].save(output_path, save_all=True, append_images=pages[1:])
    print(f"PDF saved to: {output_path}")
