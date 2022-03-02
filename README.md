## 🍻 country-music-topic-modelling

### Intro 

#### I spend most of my days applying for jobs and listening to Country Hayride on NTS radio so I thought, *why not make myself look more employable and study country music at the same time?* This project is heavily influenced by Melanie Walsh's course *Introduction to Cultural Analytics & Python* and much of the code was borrowed from the sections on Topic Modelling and Data Collection (API). Thank you Melanie for making your work publicly accessible!

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
Now that we have a large collection of text files we can use them to train the machine learning tool MALLET. More specifically we'll use a MALLET wrapper to be able to use the tool with Python. Once trained, MALLET is used to display the words contained in each topic. We can further find which topics a song is most likely to relate to and can visualize our results as a heat map.

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
![country_music_heatmap](https://user-images.githubusercontent.com/98699929/156213827-5799f965-9cf5-4932-8df9-bab389c5191d.JPG)

### Discussion

Each song in the heat map was chosen to represent a particular category as defined from the Hypothesis section. In the places of categories 1, 6, 7, and 8 we have respectievely Jonhy Lee's "Hey Bartender", Waylon Jennings' "Are You Sure Hank Would Have Done It This Way?", Tammy Wynette's "DIVORCE", and Phil Vassar's "This is God". 

At a first glance, it's not immediately clear which topic belongs to which type of category. Take for example Johny Lee's Hey Bartender, a song that is  explicitly about drinking. According to the model, this song is most likely to belong to Topic 3. We might then assign Topic 3 as the Drinking category, **except** the words in the Topic 3 list do not make any reference to alcohol. We would probably need at least a 'beer' or 'whiskey' entry to justifiably give Topic 3 the Drinking label.

All is not lost though. Topics 0, 2 and 5 all have 'love' as an entry, hinting that perhaps they correspond to one of the love categories. The heat map lends authority to this claim by showing Randy Travis' Forever and Ever Amen as most likely belonging to the category represented by Topic 0. Since Forever and Ever Amen was used as a placeholder for the *songs about falling in love* we can tentatively give Topic 0 this label. 

Topic 2 also mentions 'jesus', 'believe, 'god, and is most correlated to Phil Vassar's This is God, our decidely religious song. Here again, we can tentatively give this topic the *songs about religion* label.

Tammy Wynette's DIVORCE tells the tale of, you guessed it, a divorce. It could be argued that this song is a *song about heart break*, which is sort of true, but the story more so focuses on a mothers efforts to conceal an ugly divorce and custody battle from her young child. Now that's a sad country song! From the heat map we see that this song is most likely to fall under the Topic 1 umbrella. The list entries in Topic 1 include things like 'gone', 'miss', 'night', 'night', and 'christmas'. With this in mind, I think we can give this topic the *songs about tragedy* label. After all, everyone knows that a sad song is made even sadder if the events take place around the holidays.

So that leaves *songs about heart break, rural life, family, and country music itself*. 

Even though Alan Jackson's Drive is about remembering the fond memories his father gave him as a kid, I think this theme is overshadowed by the nature of the memories themselves, e.g. steering a boat, driving a truck, etc. Perhaps this was a less than ideal choice to represent the *songs about family* category. Nonetheless, Topic 6 contains both 'mamma' and 'daddy' as entries making it a strong candidate for *songs about family*. 

I feel like Topics 4 and 7 are almost two sides of the same coin but that Topic 7 is almost like the more mature, older, and wiser version of Topic 4. While Topic 4 concerns itself with 'country', 'trucks', and 'roads', Topic 7 thinks more about 'land', 'trains', and 'river'. The entries in both topics elicit images of nature and rural life. I'm tempted to label these categories as *modern rural nostalgia* and *oldies rural nostalgia*.

#### Thus we have,
```
🤠 Falling in Love 🤠

['love', 'know', 'never', 'heart', 'one', 'like', 'time', 'say', 'could', 'see', 'baby', 'let', 'way', 'still', 'ever', 'life', 'every', 'would', 'away', 'tell']

🤠 Tragedy 🤠

['gone', 'like', 'every', 'rain', 'time', 'long', 'night', 'miss', 'dance', 'song', 'hear', 'home', 'play', 'christmas', 'nobody', 'sweet', 'moon', 'sky', 'wind', 'santa']

🤠 Religion 🤠

['man', 'god', 'good', 'made', 'life', 'love', 'world', 'stand', 'sometimes', 'believe', 'people', 'woman', 'way', 'know', 'kind', 'make', 'cause', 'hard', 'rise', 'jesus']

🤠 Inconclusive 🤠

['got', 'ain', 'yeah', 'gonna', 'good', 'girl', 'like', 'one', 'get', 'know', 'cause', 'right', 'time', 'back', 'baby', 'night', 'take', 'think', 'lyrics', 'call']

🤠 Modern Rural Nostalgia 🤠

['back', 'country', 'got', 'like', 'get', 'road', 'old', 'little', 'ride', 'town', 'yeah', 'ain', 'truck', 'girls', 'night', 'way', 'roll', 'real', 'boys', 'red']

🤠 Inconclusive 🤠

['wanna', 'like', 'baby', 'yeah', 'little', 'ooh', 'let', 'love', 'make', 'get', 'want', 'whoa', 'feel', 'take', 'come', 'hey', 'gotta', 'kiss', 'way', 'night']

🤠 Family/Mom & Dad 🤠

['said', 'well', 'daddy', 'got', 'old', 'back', 'man', 'mama', 'like', 'boy', 'took', 'never', 'went', 'could', 'made', 'told', 'name', 'house', 'years', 'home']

🤠 Oldies Rural Nostalgia 🤠

['come', 'heaven', 'lord', 'one', 'day', 'home', 'need', 'away', 'well', 'take', 'land', 'texas', 'devil', 'river', 'angel', 'train', 'wind', 'soul', 'blue', 'water']
```
### Comments
 
