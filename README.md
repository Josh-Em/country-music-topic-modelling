## 🍻 country-music-topic-modelling

### Intro 

#### 

### Hypothesis

#### Let us surmise that the majority of country and western music songs can be characterized by a combination of the following eight categories.
1. Songs about drinking. E.g. Tom T. Hall - I Like Beer, Gary Stewart - Whiskey Trip, Jimmy Buffet - Margaritaville
2. Songs about heart break. E.g. Billy Ray Cyrus - Achy Breaky Heart, Dolly Parton - I Will Always Love You 
3. Songs about falling in love/being in love. E.g. Dolly Parton - Here You Come Again, Randy Travis - Forever and Ever Amen, Conway Twitty - Hello Darlin'
4. Songs about rural life and/or urban withdrawal. E.g. John Denver - Take Me Home, Country Roads, Merle Haggard - Okie From Muskogee
5. Songs about family. E.g. Alan Jackson - Drive (For Daddy Gene), CW McCall - Roses For Mama
6. Songs about country music itself. E.g. George Jones- Who's Gonna Fill Their Shoes, Waylon Jennings - Luckenbach Texas
7. Songs about tragedy. E.g. Townes Van Zandt - Tecumseh Valley, George Jones - Grand Tour
8. Songs about religion. E.g. Willie Nelson - Seven Spanish Angels, Kitty Wells - It Wasn't God Who Made Honky Tonk Angels
#### For example, In George Strait's hit All My Ex's Live in Texas, he reminisces on his childhood in Texas, tells us the towns in which his various exes live and explains that that is why he resides in Tennessee. Broadly speaking, the themes of the track are summarised by categories 2,4, and 6. I.e. Heartbreak (although the song's sound is rather jovial it is nonetheless about ex-partners), a longing for a simpler time in rural life (learning to swim in the Frio river), and an ode to the state of Texas, carrying with it a recognition of Texas' contribution to the development and evolution of the country and western genre. 

### Code
#### top_five_lyrics.py
This program first scrapes a Wikipedia page to create a list of the names of popular country music artists. Next a function is created using the LyricsGenius API wrapper that takes as its input an artists name and has as its output the text files of the lyrics to the artists top five songs on Genius.com. The list of artists from Wikipedia is sent to this function to download the top five songs of each artist in the list.
#### topic_model.py
Now that we have a large collection of text files we can use them to train the machine learning tool MALLET[cite]. More specifically we'll use a MALLET wrapper to be able to use the tool with Python. Once trained, MALLET is used to display the words contained in each topic. We can further find which topics a song is most likely to relate to and can visualize our results as a heat map.

### Results
```
🤠Topic 0🤠

['love', 'know', 'never', 'heart', 'one', 'like', 'time', 'say', 'could', 'see', 'baby', 'let', 'way', 'still', 'ever', 'life', 'every', 'would', 'away', 'tell']

🤠Topic 1🤠

['gone', 'like', 'every', 'rain', 'time', 'long', 'night', 'miss', 'dance', 'song', 'hear', 'home', 'play', 'christmas', 'nobody', 'sweet', 'moon', 'sky', 'wind', 'santa']

🤠Topic 2🤠

['man', 'god', 'good', 'made', 'life', 'love', 'world', 'stand', 'sometimes', 'believe', 'people', 'woman', 'way', 'know', 'kind', 'make', 'cause', 'hard', 'rise', 'jesus']

🤠Topic 3🤠

['got', 'ain', 'yeah', 'gonna', 'good', 'girl', 'like', 'one', 'get', 'know', 'cause', 'right', 'time', 'back', 'baby', 'night', 'take', 'think', 'lyrics', 'call']

🤠Topic 4🤠

['back', 'country', 'got', 'like', 'get', 'road', 'old', 'little', 'ride', 'town', 'yeah', 'ain', 'truck', 'girls', 'night', 'way', 'roll', 'real', 'boys', 'red']

🤠Topic 5🤠

['wanna', 'like', 'baby', 'yeah', 'little', 'ooh', 'let', 'love', 'make', 'get', 'want', 'whoa', 'feel', 'take', 'come', 'hey', 'gotta', 'kiss', 'way', 'night']

🤠Topic 6🤠

['said', 'well', 'daddy', 'got', 'old', 'back', 'man', 'mama', 'like', 'boy', 'took', 'never', 'went', 'could', 'made', 'told', 'name', 'house', 'years', 'home']

🤠Topic 7🤠

['come', 'heaven', 'lord', 'one', 'day', 'home', 'need', 'away', 'well', 'take', 'land', 'texas', 'devil', 'river', 'angel', 'train', 'wind', 'soul', 'blue', 'water']
```

![country_music_heatmap](https://user-images.githubusercontent.com/98699929/156208876-1854e7ff-01ed-46a8-8268-252370e1ab01.JPG)

### Discussion

