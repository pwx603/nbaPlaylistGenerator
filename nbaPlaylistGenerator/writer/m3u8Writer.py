class M3U8Writer:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_games_to_m3_u8(self, game_streams):
        with self.file_path.open("w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            f.write(f'#EXTINF:-1, NBATV\n')
            f.write("https://d10nbk66ckd93y.cloudfront.net/hls/nbatv/playlist.m3u8\n")

            for game in game_streams:
                stream_title = f'{game["home"]} vs {game["away"]}'
                for index, streamLink in enumerate(game["streams"]):
                    f.write(f'#EXTINF:-1, {stream_title} - {index + 1}\n')
                    f.write(f'{streamLink}\n')


