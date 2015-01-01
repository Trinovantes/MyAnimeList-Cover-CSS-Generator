from datetime import datetime
import logging

from models.media import Media
import helpers

class MediaScraper():
    def __init__(self, rel_url):
        self.rel_url = rel_url

    def run(self):
        soup = helpers.request_soup('http://myanimelist.net/' + self.rel_url)
        img = soup.find('div', id='content').select('img[src^=http://cdn.myanimelist.net/images/anime/]')

        media = Media.all().filter('rel_url =', self.rel_url).get()
        media.cover_path = img['src']
        media.last_scraped = datetime.now()
        media.put()

        logging.info('Updated media: ' + rel_url)
