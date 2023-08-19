import os

from feedgen.feed import FeedGenerator

def generate_feed():
    fg = FeedGenerator()
    fg.id("https://www.victorzhou.dev/")
    fg.title("Victor Zhou")
    fg.author(name="Victor Zhou", uri="https://www.victorzhou.dev/")
    fg.link(href="https://www.victorzhou.dev/", rel="self")
    fg.logo("https://cdn.victorzhou.dev/img/Icon+-+300x300.jpg")
    fg.subtitle("Victor Zhou's homepages")
    fg.language("en")

    fg.docs("https://www.rssboard.org/rss-specification")

    if os.environ["RSS_OUTPUT_PATH"]:
        fg.rss_file(os.environ["RSS_OUTPUT_PATH"])
    
    if os.environ["ATOM_OUTPUT_PATH"]:
        fg.atom_file(os.environ["ATOM_OUTPUT_PATH"])

if __name__ == "__main__":
    generate_feed()