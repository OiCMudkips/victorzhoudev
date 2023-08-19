import os
import datetime

from feedgen.feed import FeedGenerator
import pytz

TIMEZONE = pytz.timezone("America/Vancouver")

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

    generate_jp_entries(fg)

    if os.environ.get("RSS_OUTPUT_PATH"):
        fg.rss_file(os.environ["RSS_OUTPUT_PATH"])
    
    if os.environ.get("ATOM_OUTPUT_PATH"):
        fg.atom_file(os.environ["ATOM_OUTPUT_PATH"])

def generate_jp_entries(fg: FeedGenerator):
    fe1 = fg.add_entry()
    fe1.id("https://www.victorzhou.dev/jp_language_stuff/glad_youre_evil.html")
    fe1.title("PinocchioP - I'm glad you're evil too")
    fe1.link(href="https://www.victorzhou.dev/jp_language_stuff/glad_youre_evil.html")
    fe1.published(datetime.datetime(year=2019, month=12, day=28, tzinfo=TIMEZONE))

    fe2 = fg.add_entry()
    fe2.id("https://www.victorzhou.dev/jp_language_stuff/code_geass_episode_25.html")
    fe2.title("Ruining a line in translation: Code Geass R2 episode 25")
    fe2.link(href="https://www.victorzhou.dev/jp_language_stuff/code_geass_episode_25.html")
    fe2.published(datetime.datetime(year=2020, month=9, day=3, tzinfo=TIMEZONE))

if __name__ == "__main__":
    generate_feed()