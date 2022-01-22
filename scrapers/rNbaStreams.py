import json
import requests

from bs4 import BeautifulSoup

class RNbaStreamsScraper:

    def get_game_stream_list(self):
        gameList = []
        currentGames = self._get_all_current_games()
        for game in currentGames:
            streamLink = self._get_stream_link_for_game(game)
            if streamLink:
                gameList.append({"name": game["name"], "url": streamLink, "logo": game["homeTeam"]["logo"]})
        return gameList

    def _get_all_current_games(self):
        r = requests.get('https://reddit.rnbastreams.com/')
        soup = BeautifulSoup(r.text, 'html.parser')
        data = json.loads(soup.find(id='__NEXT_DATA__').text)
        events = data['props']['pageProps']['initialState']['sport']['leagues'][0]["events"]
        filteredEvent = [event for event in events if event["statusDescription"] != "Ended"]
        return filteredEvent

    def _get_stream_link_for_game(self, game):
        stream_table_url = f'https://sportscentral.io/streams-table/{game["id"]}/basketball'
        print(stream_table_url)
        r = requests.get(stream_table_url)
        soup = BeautifulSoup(r.text, 'html.parser')

        streamItems = soup.findAll(class_="stream-item")

        return next((item.find('a', class_="watch")['href'] for item in streamItems if
                    "1stream" in item.find('a', class_="watch")['href']), None)
