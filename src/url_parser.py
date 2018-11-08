import re


def parse(url):
    """ Parse a given URL so that it is a valid Spotify API endpoint """
    valid_url_regex = re.compile(r'^https?://api\.spotify\.com/v1/.+')
    if(re.match(valid_url_regex, url)):
        return url

    missing_https_regex = re.compile(r'^api\.spotify\.com/v1/.+')
    if(re.match(missing_https_regex, url)):
        return f'https://{url}'

    starts_with_v1_regex = re.compile(r'^/?v1/.+')
    if(re.match(starts_with_v1_regex, url)):
        return f'https://api.spotify.com{url}' if url.startswith('/') else f'https://api.spotify.com/{url}'

    raise Exception('Invalid URL provided')
