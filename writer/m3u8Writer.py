class M3U8Writer:
    def __init__(self, fileLocation):
        self.file = fileLocation

    def write_games_to_m3_u8(self, gameList):
        with open(self.file, 'w') as f:
            f.write("#EXTM3U\n")

            for game in gameList:
                f.write(f'#EXTINF:-1, {game["name"]}\n')
                f.write(f'{game["source"]}\n')