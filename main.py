from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapers import OneStreamScraper, RNbaStreamsScraper
from writer import M3U8Writer

def main():
    try:
        chrome_options = Options()
        chrome_options.add_extension('./asset/uBlock-Origin.crx')
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

        oneStreamScraper = OneStreamScraper(driver=driver)
        rNbaScraper = RNbaStreamsScraper()

        game_list = rNbaScraper.get_game_stream_list()

        for game in game_list:
            sourceLink = oneStreamScraper.get_stream_source_link(game["url"])
            game["source"] = sourceLink

        playListWriter = M3U8Writer("./nba-stream.m3u")
        playListWriter.write_games_to_m3_u8(game_list)
    finally:
        driver.quit()


if __name__ == '__main__':
    main()