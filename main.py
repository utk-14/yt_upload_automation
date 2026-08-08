from create_image import create_image
from create_video import create_video
from upload_youtube import upload_video

QUOTES_FILE = "quotes.txt"
INDEX_FILE = "current_index.txt"

def update_index(index):

    with open(INDEX_FILE, "w") as f:
        f.write(str(index + 1))

def get_next_quote():

    with open(QUOTES_FILE, "r", encoding="utf-8") as f:
        quotes = [line.strip() for line in f if line.strip()]

    try:
        with open(INDEX_FILE, "r") as f:
            index = int(f.read().strip())
    except FileNotFoundError:
        index = 0

    if index >= len(quotes):
        index = 0

    return quotes[index], index

def main():

    quote, index = get_next_quote()

    print(f"Today's Quote:\n{quote}\n")

    create_image(quote)

    create_video()

    upload_video(
        title=quote[:90] + " #shorts",
        description="""
🌟 Daily Motivation

#motivation
#quotes
#mindset
#shortvideo
#youtubeshorts
#shorts
"""
    )

    update_index(index)

    print("Done!")

if __name__ == "__main__":
    main()