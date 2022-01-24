import json
import re

import requests

from bs4 import BeautifulSoup
from . import OneStreamScraper


class RNbaStreamsScraper:
    def __init__(self, driver):
        self.oneStreamScraper = OneStreamScraper(driver=driver)

    def get_game_stream_list(self):
        game_streams = []
        current_games = self._get_all_current_games()
        for game in current_games:
            stream_link = self._get_stream_link_for_game(game)
            if stream_link:

                # The rNbaStream website has the home team and away team swapped.
                home_team = _get_shorten_team_name(game["awayTeam"]["name"])
                away_team = _get_shorten_team_name(game["homeTeam"]["name"])
                game_stream_data = {"home": home_team, "away": away_team, "streams": []}

                # 1stream
                game_stream_data["streams"].append(self.oneStreamScraper.get_stream_source_link(stream_link))

                # givemenbastream
                game_stream_data["streams"].append(
                    f'https://d10nbk66ckd93y.cloudfront.net/hls/{home_team.lower()}/playlist.m3u8')

                game_streams.append(game_stream_data)
        return game_streams

    @staticmethod
    def _get_all_current_games():
        r = requests.get('https://reddit.rnbastreams.com/')
        soup = BeautifulSoup(r.text, 'html.parser')
        data = json.loads(soup.find(id='__NEXT_DATA__').text)
        events = data['props']['pageProps']['initialState']['sport']['leagues'][0]["events"]
        filtered_event = [event for event in events if
                          event["statusDescription"] != "Ended" or event["status"]["code"] != 0]
        return filtered_event

    @staticmethod
    def _get_stream_link_for_game(game):
        stream_table_url = f'https://sportscentral.io/streams-table/{game["id"]}/basketball'
        r = requests.get(stream_table_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        stream_items = soup.findAll(class_="stream-item")
        return next((item.find('a', class_="watch")['href'] for item in stream_items if
                     "1stream" in item.find('a', class_="watch")['href']), None)


def _get_shorten_team_name(team_name):
    return re.sub(r'.* (\w+)$', r'\1', team_name)
