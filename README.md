# spotify_api_client

A python library for easily incorporating Spotify's Web API in your Python projects. For further info checkout the [Official Docs](https://developer.spotify.com/documentation/web-api/reference/)

#### Requirements

- Python 3.x
- pip => `python-dotenv`, `requests`

# Usage

To use this library in your own projects, simply follow the following steps:

1. Clone this repo into your the root of your project folder

```bash
git clone https://github.com/QMIND-Team/spotify_api_client.git
```

2. Install the required pip packages

```bash
pip install requests python-dotenv
```

3. Obtain a `CLIENT ID` and `CLIENT SECRET` from [Spotify](https://developer.spotify.com/dashboard/applications) and create a `.env` file in the root of your folder as follows (replacing with actual values):

```
CLIENT_ID=ABC123
CLIENT_SECRET=DEF456
```

After following these steps you should be good to go! See below for some examples of using this library in your programs.

# Examples

Here are some examples of how you can use this library to easily make requests to the Spotify API:

```python
from spotify_api_client import get

# Gets a list of greatest hits albums
response = get('v1/search', {'q':'greatest hits', 'type':'album'})
print(response)

# The following will also return the same result
response = get('/v1/search?q='greatest hits'&type=album')
print(response)
```

Or alternatively you could do

```python
from spotify_api_client import search, search_all

# Gets the id of the first greatest hits album from the search results
response = search('greatest hits', 'album')
print(response)

# Gets the ids of all the greatest hits album from the search results (limit 20)
response = search_all('greatest hits', 'album')
print(response)
```

```python
import spotify_api_client as client

# Gets track with id 1UjyF6okUHhnVxaLV8ojsA (Am I Wrong by Anderson .Paak)
response = client.get('api.spotify.com/v1/tracks/1UjyF6okUHhnVxaLV8ojsA')
print(response)
```

```python
import spotify_api_client

# Gets album with id 7xJ7jHNu3JNfdnao9xwMho (Donuts by J Dilla)
spotify_api_client.get('https://api.spotify.com/v1/albums/7xJ7jHNu3JNfdnao9xwMho')
```
