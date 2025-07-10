import json
import requests
import os
import TextConverter
import PDF_Creator


def main():
    download_list = []
    pdf_list = []

    databank = json.load(open('utils/CardDatabank.json'))
    cardlist = TextConverter.TextToListConverter('cardlist.txt')

    # Prepare list for cards to download
    print("Preparing card list...")
    for card in cardlist:
        for data in databank["cards"]:
            if data["serial"] == card[2]:
                download_list.append([card[0], card[1], card[2], data["imageUrl"]])
                break

    # Download cards from list
    print("Start downloads...")
    for cards in download_list:
        img_data = requests.get(cards[3]).content
        filename = "gen/downloads/" + cards[1] + "_" + cards[2] + ".jpg"
        for i in range(cards[0]):
            pdf_list.append(filename)
        with open(filename, 'wb') as handler:
            handler.write(img_data)

    # Create PDF with a list of cards
    print("Create PDF...")
    PDF_Creator.Create_PDF(pdf_list)

    # Deleting temp downloads maybe use like a databank for later like 2 or 3 downloads {update later}?
    for f in os.listdir("gen/downloads"):
        os.remove(os.path.join("gen/downloads", f))

if __name__ == '__main__':
    main()