#!/usr/bin/python

"This script logs into the Rock Band website and requests new songs"

# Std Python Libs
import logging
import sys

# 3rd Party Libs
from helium import start_chrome, write, click, kill_browser
import yaml


def load_work(config_file='./config.yaml'):
    "Loads yaml config file"

    logging.info("Loading yaml file")
    with open(config_file, 'r') as file_reader:
        return yaml.load(file_reader)['songs']


def submit_request(
                    song,
                    artist,
                    url='www.harmonixmusic.com/games/rock-band/request'
                  ):
    "Uses helium framework to open chrome, open a website, and submit a song"

    logging.info("Logging into %s", url)
    start_chrome(url, headless=True)
    write(song, into='Song Title')
    write(artist, into='Artist')
    logging.info("Submitting request for '%s' by '%s'", song, artist)
    click('Submit')
    kill_browser()


def main():
    "This is the main method"

    # Set up logging
    logging.basicConfig(
        format="%(asctime)-15s %(levelname)s %(message)s", level='INFO'
    )

    logging.info('Entering main')
    song_list = load_work()
    for song_info in song_list:
        logging.debug("Song: %s, Artist: %s",
                      song_info['song'],
                      song_info['artist'])
        submit_request(
            song_info['song'],
            song_info['artist']
        )

    # Stop logging and clean up
    logging.shutdown()


if __name__ == "__main__":
    sys.exit(main())
