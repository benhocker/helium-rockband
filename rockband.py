#!/usr/bin/python

# Std Python Libs
import logging
import sys

# 3rd Party Libs
from helium import *
import yaml

def load_work(config_file = './config.yaml'):
    song_list = []

    logging.info(f"Loading {config_file}")
    with open(config_file, 'r') as f:
        return yaml.load(f)['songs']

def submit_request(song, artist, url='www.harmonixmusic.com/games/rock-band/request'):
    logging.info(f"Logging into {url}")
    start_chrome(url)
    write(song, into='Song Title')
    write(artist, into='Artist')
    logging.info(f"Submitting request for '{song}' by '{artist}'")
    click('Submit')
    kill_browser()

def main():
    # Set up logging
    logging.basicConfig(
        format="%(asctime)-15s %(levelname)s %(message)s", level='INFO'
    )

    logging.info('Entering main')
    song_list = load_work()
    for song_info in song_list:
        logging.debug(f"Song: {song_info['song']}, Artist: {song_info['artist']}")
        submit_request(
            song_info['song'],
            song_info['artist']
        )

    # Stop logging and clean up
    logging.shutdown()

if __name__ == "__main__":
    sys.exit(main())