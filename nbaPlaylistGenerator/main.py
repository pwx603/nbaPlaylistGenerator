import logging
from pathlib import Path

from selenium import webdriver
from scrapers import RNbaStreamsScraper
from writer import M3U8Writer, S3Writer

import os


def main():
    logging.basicConfig(level=logging.INFO)
    selenium_host = os.getenv("SELENIUM_HOST", default="localhost")
    options = webdriver.ChromeOptions()
    logging.info("Connecting to Selenium")
    driver = webdriver.Remote(f'http://{selenium_host}:4444/wd/hub', options=options)
    logging.info("Connected to Selenium")
    try:
        r_nba_scraper = RNbaStreamsScraper(driver=driver)
        game_streams = r_nba_scraper.get_game_stream_list()

        logging.info(game_streams)

        file_path = Path("/tmp/nba-stream.m3u")
        play_list_writer = M3U8Writer(file_path)
        play_list_writer.write_games_to_m3_u8(game_streams)

        s3_writer = S3Writer(bucket_name="nba-reddit-stream")
        if s3_writer.write_to_s3(str(file_path.resolve()), file_path.name):
            logging.info("Successfully uploaded M3U playlist.")
        else:
            logging.info("Failed to upload M3U playlist.")
    finally:
        driver.close()


if __name__ == '__main__':
    main()
