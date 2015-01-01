import logging
from google.appengine.api import urlfetch

import sys
sys.path.insert(0, 'libs') # Add /libs/ folder to $PATH
from bs4 import BeautifulSoup

import settings
import private

#------------------------------------------------------------------------------

def request_soup(url):
    logging.debug('Requesting: ' + url)

    result = urlfetch.fetch(
        url,
        headers = {'User-Agent': private.USER_AGENT }
    )

    logging.debug('Received response from: ' + url)

    if result.status_code == 200:
        return BeautifulSoup(result.content)
    else:
        logging.error('Received ' +  str(result.status_code) + ' error from ' + url)
        return None
