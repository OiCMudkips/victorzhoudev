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
    generate_rants_entries(fg)
    generate_transit_entries(fg)
    generate_se_entries(fg)
    generate_travel_entries(fg)

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


def generate_rants_entries(fg: FeedGenerator):
    fe1 = fg.add_entry()
    fe1.id("https://www.victorzhou.dev/rants/doordash_shitty_receipts.html")
    fe1.title("Difficulty with DoorDash Receipts and Reimbursement")
    fe1.link(href="https://www.victorzhou.dev/rants/doordash_shitty_receipts.html")
    fe1.published(datetime.datetime(year=2022, month=5, day=24, tzinfo=TIMEZONE))

    fe2 = fg.add_entry()
    fe2.id("https://www.victorzhou.dev/rants/form5444.html")
    fe2.title("My experience with FS Form 5444")
    fe2.link(href="https://www.victorzhou.dev/rants/form5444.html")
    fe2.published(datetime.datetime(year=2022, month=8, day=17, tzinfo=TIMEZONE))

    fe3 = fg.add_entry()
    fe3.id("https://www.victorzhou.dev/rants/n_good_musicals.html")
    fe3.title("n good musicals")
    fe3.link(href="https://www.victorzhou.dev/rants/n_good_musicals.html")
    fe3.published(datetime.datetime(year=2022, month=11, day=1, tzinfo=TIMEZONE))


def generate_transit_entries(fg: FeedGenerator):
    fe1 = fg.add_entry()
    fe1.id("https://www.victorzhou.dev/transit/saturdays.html")
    fe1.title("Saturdays")
    fe1.link(href="https://www.victorzhou.dev/transit/saturdays.html")
    fe1.published(datetime.datetime(year=2020, month=7, day=20, tzinfo=TIMEZONE))

def generate_se_entries(fg: FeedGenerator):
    fe1 = fg.add_entry()
    fe1.id("https://www.victorzhou.dev/se/argparse_and_cmd.html")
    fe1.title("Using argparse and cmd together")
    fe1.link([
        {
            "href": "https://www.victorzhou.dev/se/argparse_and_cmd.html",
            "rel": "self",
        },
        {
            "href": "https://www.victorzhou.dev/se/argparse_and_cmd_non_gist.html",
            "rel": "alternate",
        },
    ])
    fe1.published(datetime.datetime(year=2020, month=5, day=24, tzinfo=TIMEZONE))

    fe2 = fg.add_entry()
    fe2.id("https://www.victorzhou.dev/se/updates_2023.html")
    fe2.title("victorzhou.dev Updates April 2023")
    fe2.link(href="https://www.victorzhou.dev/se/updates_2023.html")
    fe2.published(datetime.datetime(year=2023, month=4, day=22, tzinfo=TIMEZONE))

def generate_travel_entries(fg: FeedGenerator):
    fe1 = fg.add_entry()
    fe1.id("https://www.victorzhou.dev/travels/a_photo_a_trip_2019.html")
    fe1.title("A Photo a Trip (2019 edition) - An Abandoned Article")
    fe1.link(href="https://www.victorzhou.dev/travels/a_photo_a_trip_2019.html")
    fe1.published(datetime.datetime(year=2022, month=5, day=16, tzinfo=TIMEZONE))

if __name__ == "__main__":
    generate_feed()