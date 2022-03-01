!pip install little_mallet_wrapper
!pip install seaborn

import little_mallet_wrapper
import seaborn
import glob
from pathlib import Path
import os

os.environ['MALLET_HOME'] = 'path to mallet folder'

directory = "folder where text files are stored" 

files = glob.glob(f"{directory}/*.txt")

training_data = []
for file in files:
    # For some reason utf-8 encoding was resulting in an error message
    text = open(file, encoding='latin-1').read()
    processed_text = little_mallet_wrapper.process_string(text, numbers='remove')
    training_data.append(processed_text)

# Summary of training data
little_mallet_wrapper.print_dataset_stats(training_data)

# Define number of topics to model
num_topics = 8

#Output directory path
output_directory_path = 'C:/Users/...'

Path(f"{output_directory_path}").mkdir(parents=True, exist_ok=True)

path_to_training_data           = f"{output_directory_path}/training.txt"
path_to_formatted_training_data = f"{output_directory_path}/mallet.training"
path_to_model                   = f"{output_directory_path}/mallet.model.{str(num_topics)}"
path_to_topic_keys              = f"{output_directory_path}/mallet.topic_keys.{str(num_topics)}"
path_to_topic_distributions     = f"{output_directory_path}/mallet.topic_distributions.{str(num_topics)}"

path_to_mallet = 'C:/Users/...'

# Train model
little_mallet_wrapper.quick_train_topic_model(path_to_mallet,
                                             output_directory_path,
                                             num_topics,
                                             training_data)

# Print topics
topics = little_mallet_wrapper.load_topic_keys(path_to_topic_keys)

for topic_number, topic in enumerate(topics):
    print(f"🤠Topic {topic_number}🤠\n\n{topic}\n")
    
# Define song titles by their text file path stem
song_titles = [Path(file).stem for file in files]
song_titles

# Create random group of song titles or ceate a curate your own
import random
#target_labels = random.sample(song_titles, 10)
target_labels = ['Alan_Jackson_Its_Five_OClock_Somewhere','Alabama_If_Youre_Gonna_Play_In_Texas_You_Gotta_Have_A_Fiddle_In_The_Band','Billy_Currington_Pretty_Good_At_Drinkin_Beer','Billy_Ray_Cyrus_Achy_Breaky_Heart','Billy_Ray_Cyrus_I_Want_My_Mullet_Back','Brooks__Dunn_Neon_Moon','Carrie_Underwood_Before_He_Cheats','Charley_Pride_Kiss_An_Angel_Good_Mornin','Chris_Stapleton_Tennessee_Whiskey','Conway_Twitty_Tight_Fittin_Jeans','David_Allan_Coe_You_Never_Even_Called_Me_By_My_Name','David_Lee_Murphy_Dust_on_the_Bottle']

# Distribution of correspondence to a particular category
topic_distributions = little_mallet_wrapper.load_topic_distributions(path_to_topic_distributions)

# Create box plot of distributions
little_mallet_wrapper.plot_categories_by_topics_heatmap(song_titles,
                                      topic_distributions,
                                      topics, 
                                      output_directory_path + '/categories_by_topics.pdf',
                                      target_labels=target_labels,
                                      dim= (13, 9)
                                     )

# Check the distribution of a particular song
song_to_check = "Billy_Ray_Cyrus_Achy_Breaky_Heart"

song_number = song_titles.index(song_to_check)

print(f"Topic Distributions for {song_titles[song_number]}\n")
for topic_number, (topic, topic_distribution) in enumerate(zip(topics, topic_distributions[song_number])):
    print(f"✨Topic {topic_number} {topic[:6]} ✨\nProbability: {round(topic_distribution, 3)}\n")
    
# Show top songs for each category
original_texts = []
for file in files:
    text = open(file, encoding='latin-1').read()
    original_texts.append(text)

training_data_song_titles = dict(zip(training_data, song_titles))
training_data_original_text = dict(zip(training_data, original_texts))

def display_top_titles_per_topic(topic_number=0, number_of_documents=5):
    
    print(f"🤠Topic {topic_number}🤠\n\n{topics[topic_number]}\n")

    for probability, document in little_mallet_wrapper.get_top_docs(training_data, topic_distributions, topic_number, n=number_of_documents):
        print(round(probability, 4), training_data_song_titles[document] + "\n")
    return

display_top_titles_per_topic(topic_number=2, number_of_documents=10)