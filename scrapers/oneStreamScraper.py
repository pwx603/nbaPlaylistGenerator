import re


class OneStreamScraper:
    def __init__(self, driver):
        self.driver = driver
        self.resolution = '1080p'

    def get_stream_source_link(self, webUrl):
        self.driver.get(webUrl)
        source = self.driver.execute_script('return player.options.source')
        return format_source_url(source, self.resolution)


def format_source_url(source, res):
    return re.sub(r'^(.*)/.*(.m3u8)$', f'\\1/{res}\\2', source)
