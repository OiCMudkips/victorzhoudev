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
    fg.subtitle("Victor Zhou's homepage")
    fg.language("en")
    fg.docs("https://www.rssboard.org/rss-specification")
    fg.copyright("© Copyright Victor Zhou")
    fg.rights("© Copyright Victor Zhou")

    generate_jp_entries(fg)
    generate_rants_entries(fg)
    generate_transit_entries(fg)
    generate_se_entries(fg)
    generate_travel_entries(fg)
    generate_translation_of_fr_reasons(fg)

    fg.rss_file(os.environ.get("RSS_OUTPUT_PATH", "rss.xml"))
    fg.atom_file(os.environ.get("ATOM_OUTPUT_PATH", "atom.xml"))


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


def generate_translation_of_fr_reasons(fg: FeedGenerator):
    fe1 = fg.add_entry()
    fe1.id("https://www.victorzhou.dev/rants/sinclair.html")
    fe1.title("English translation of reasons for judgment in Sinclair-Desgagné c. Procureur général du Canada, 2025 QCCS 3859")
    fe1.link(href="https://www.victorzhou.dev/rants/sinclair.html")
    fe1.published(datetime.datetime(year=2026, month=3, day=3, tzinfo=TIMEZONE))
    fe1.updated(datetime.datetime(year=2026, month=3, day=4, tzinfo=TIMEZONE))

    fe2 = fg.add_entry()
    fe2.id("https://www.victorzhou.dev/rants/sinclair2.html")
    fe2.title("English translation of reasons for judgment in Sinclair-Desgagné c. Procureur général du Canada, 2025 QCCS 2551")
    fe2.link(href="https://www.victorzhou.dev/rants/sinclair2.html")
    fe2.published(datetime.datetime(year=2026, month=3, day=4, tzinfo=TIMEZONE))

    fe3 = fg.add_entry()
    fe3.id("https://www.victorzhou.dev/rants/sinclair3.html")
    fe3.title("English translation of reasons for judgment in Sinclair-Desgagné c. Procureur général du Canada, 2025 QCCS 2556")
    fe3.link(href="https://www.victorzhou.dev/rants/sinclair3.html")
    fe3.published(datetime.datetime(year=2026, month=3, day=6, tzinfo=TIMEZONE))

    fe4 = fg.add_entry()
    fe4.id("https://www.victorzhou.dev/rants/paiement.html")
    fe4.title("English translation of reasons for judgment in Sa Majesté la Reine c. Paiement, 2011 BCSC 415")
    fe4.link(href="https://www.victorzhou.dev/rants/paiement.html")
    fe4.published(datetime.datetime(year=2026, month=3, day=9, tzinfo=TIMEZONE))
    fe4.updated(datetime.datetime(year=2026, month=3, day=10, tzinfo=TIMEZONE))

    fe5 = fg.add_entry()
    fe5.id("https://www.victorzhou.dev/rants/bandaogo.html")
    fe5.title("English translation of reasons for judgment in R. c. Bandaogo, 2023 BCSC 2514")
    fe5.link(href="https://www.victorzhou.dev/rants/bandaogo.html")
    fe5.published(datetime.datetime(year=2026, month=3, day=10, tzinfo=TIMEZONE))

    fe6 = fg.add_entry()
    fe6.id("https://www.victorzhou.dev/rants/2024-bcsc-2600.html")
    fe6.title("English translation of reasons for judgment in R. c. Grenier, 2024 BCSC 2600")
    fe6.link(href="https://www.victorzhou.dev/rants/2024-bcsc-2600.html")
    fe6.published(datetime.datetime(year=2026, month=3, day=11, tzinfo=TIMEZONE))

    fe7 = fg.add_entry()
    fe7.id("https://www.victorzhou.dev/translation_of_fr_reasons/2025-fc-114199-canlii.html")
    fe7.title("English translation of reasons for judgment in Droits collectifs Québec c. Canada (Cour suprême), 2025 CanLII 114199 (CF)")
    fe7.link(href="https://www.victorzhou.dev/translation_of_fr_reasons/2025-fc-114199-canlii.html")
    fe7.published(datetime.datetime(year=2026, month=3, day=16, tzinfo=TIMEZONE))

    fe8 = fg.add_entry()
    fe8.id("https://www.victorzhou.dev/translation_of_fr_reasons/T-2936-24-court-file.html")
    fe8.title("English translation of Federal Court file T-2936-24 document summary")
    fe8.link(href="https://www.victorzhou.dev/translation_of_fr_reasons/T-2936-24-court-file.html")
    fe8.published(datetime.datetime(year=2026, month=3, day=24, tzinfo=TIMEZONE))

    fe9 = fg.add_entry()
    fe9.id("https://www.victorzhou.dev/translation_of_fr_reasons/2024-bcsc-277.html")
    fe9.title("English translation of reasons for judgment in R. c. Abdullah, 2024 BCSC 277")
    fe9.link(href="https://www.victorzhou.dev/translation_of_fr_reasons/2024-bcsc-277.html")
    fe9.published(datetime.datetime(year=2026, month=3, day=26, tzinfo=TIMEZONE))




def generate_transit_entries(fg: FeedGenerator):
    fe1 = fg.add_entry()
    fe1.id("https://www.victorzhou.dev/transit/saturdays.html")
    fe1.title("Saturdays")
    fe1.link(href="https://www.victorzhou.dev/transit/saturdays.html")
    fe1.published(datetime.datetime(year=2020, month=7, day=20, tzinfo=TIMEZONE))

    fe2 = fg.add_entry()
    fe2.id("https://www.victorzhou.dev/transit/victoria_clipper.html")
    fe2.title("The Victoria Clipper during Thanksgiving 2022")
    fe2.link(href="https://www.victorzhou.dev/transit/victoria_clipper.html")
    fe2.enclosure(url="https://cdn.victorzhou.dev/img/victoria_clipper/img1.jpg", type="image/jpeg")
    fe2.published(datetime.datetime(year=2026, month=3, day=24, tzinfo=TIMEZONE))


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

    fe3 = fg.add_entry()
    fe3.id("https://www.victorzhou.dev/se/gha_nfs.html")
    fe3.title("Automating victorzhou.dev deployments using Github Actions")
    fe3.link(href="https://www.victorzhou.dev/se/gha_nfs.html")
    fe3.published(datetime.datetime(year=2024, month=4, day=19, tzinfo=TIMEZONE))


def generate_travel_entries(fg: FeedGenerator):
    fe1 = fg.add_entry()
    fe1.id("https://www.victorzhou.dev/travels/a_photo_a_trip_2019.html")
    fe1.title("A Photo a Trip (2019 edition) - An Abandoned Article")
    fe1.link(href="https://www.victorzhou.dev/travels/a_photo_a_trip_2019.html")
    fe1.published(datetime.datetime(year=2022, month=5, day=16, tzinfo=TIMEZONE))

    fe2 = fg.add_entry()
    fe2.id("https://www.victorzhou.dev/travels/buntzen.html")
    fe2.title("Some photos from Buntzen Lake")
    fe2.link(href="https://www.victorzhou.dev/travels/buntzen.html")
    fe2.published(datetime.datetime(year=2024, month=4, day=15, tzinfo=TIMEZONE))


if __name__ == "__main__":
    generate_feed()