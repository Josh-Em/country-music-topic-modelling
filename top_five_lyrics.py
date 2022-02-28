#!/usr/bin/env python
# coding: utf-8

# I was unable to download the API wrapper to my jupyter notebook directly from github so I first cloned it then installed it from my local diretory,
# i.e. !pip install 'C:/Users/...'

!pip install git+https://github.com/johnwmillr/LyricsGenius.git
     
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import lyricsgenius
import requests
from pathlib import Path

# Wikipedia url that lists country performers by era.    
my_url = 'https://en.wikipedia.org/wiki/List_of_country_performers_by_era'

# Parse web page. 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

# Artist names are listed under the 'a' tag.
artists_tags = page_soup.find_all('a')

# Append all 'a' tag texts to list.
artist_names = [name.text for name in artists_tags]

# Begin slicing list to isolate artist names and to not include other non-artist name tags.
first_slice = artist_names.index('List of country rock musicians')

artist_names = artist_names[first_slice+1:-1]

second_slice = artist_names.index('edit')

artist_names = artist_names[second_slice+1:-1]

artist_names = [i for i in artist_names if i != 'edit']

artist_names.remove('Zac Brown Band')

third_slice = artist_names.index('Zac Brown Band')

artist_names = artist_names[0:third_slice+1]

# For some reason this partiular artist caused the API call to crash. Thus, 'Exile' was exiled. 
artist_names.remove('Exile')

# Remove any duplicate entries in the artist_names list. 
name_list = []
for name in artist_names:
    if name not in name_list:
        name_list.append(name)
    else:
        continue

# API access token.
client_access_token = '[Enter your API key here]'

# Function to download the lyrics for the top five most popular songs of a given artist on Genius.com
def download_lyrics(artist_list):  
    
    LyricsGenius = lyricsgenius.Genius(client_access_token)
    LyricsGenius.remove_section_headers = True

    j = 1

    k = len(artist_list)


    for name in artist_list:

        print(j,'of ',k,' artists')
        artist = LyricsGenius.search_artist(name, max_songs=5)

        if artist != None:

            for i in range(len(artist.songs)):

                song_title = artist.songs[i].title
                song_title = song_title.replace(' ','_')
                artist_name = name.replace(' ','_')

                #Save the lyrics for the song as a text file
                artist.songs[i].save_lyrics(f"{artist_name}_{song_title}", extension='txt')
        else:
            continue
        j = j + 1

# Call function on the list of artists scraped from Wikipedia.

# The code may timeout if run long enough, in which case note the index of the last searched artist and run the function
# again as download_lyrics(name_list[index:-1]) where index = name_list.index('name of last searched artist').

download_lyrics(name_list)

# We have now obtained a text files containg the lyrics of the top five songs of each artist in name_list.