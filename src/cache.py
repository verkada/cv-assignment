import os
import requests

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
CACHE_DIR = os.path.join(SCRIPT_PATH, '..', 'cache')
INDEX_FILE = 'index.txt'
INDEX_URL = '...'
TS_URL = '...'

def get_cache_dir():
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    return CACHE_DIR


def get_index_file():
    cache = get_cache_dir()
    filename = os.path.join(cache, INDEX_FILE)

    if not os.path.exists(filename):
        download_file(INDEX_URL, filename)

    return [line.strip() for line in open(filename)]


def get_image(timestamp):
    '''
    downloads a ts file and writes the first frame to the cache as a jpeg.

    timestamp is an integer (seconds since unix epoch)
    '''
    pass


def download_file(url, filename):
    '''
    downloads a the contents of the provided url to a local file
    '''
    contents = requests.get(url).content
    with open(filename, 'wb') as f:
        f.write(contents)
