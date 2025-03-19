import pandas as pd
import random
import json

all_playlists = pd.read_csv('all_playlists.csv', on_bad_lines='warn')
print("total songs:", all_playlists.shape[0])
print(all_playlists[:3])


dataset = pd.DataFrame(columns=['prompt', 'completion', 'label'])

possible_prompts = [
    "I am looking for a song in the style of ",
    "Recommend me a song that is a genre like ",
    "Based on the following criteria, recommend me a song. It should be ",
    " ",
    "I am in the mood for",
    "Give me a suggestion for a song to listen to. This song should be ",
    "What is a song that has the following vibes:"
]

"""
Chat template:

<|start_header_id|>user<|end_header_id|>

What is the weather in SF and Seattle?<|eot_id|><|start_header_id|>assistant<|end_header_id|>
[get_weather(city='San Francisco', metric='celsius'), get_weather(city='Seattle', metric='celsius')]<|eot_id|>
"""

#I should save all this in JSON format

data_list = []

for index, row in all_playlists.iterrows():
    if pd.isna(row['Genres']) or pd.isna(row['Danceability']) or pd.isna(row['Acousticness']) or pd.isna(row['Tempo']) or pd.isna(row['Track Name']) or pd.isna(row['Artist Name(s)']):
        continue
    prompt = possible_prompts[random.randint(0, len(possible_prompts) - 1)] + row["Genres"] + ", "
    if row["Danceability"] > 0.66 and row["Energy"] > 0.66:
        prompt += "it should be high energy, "
    if row["Acousticness"] > 0.66:
        prompt += "it should have little to no vocals, "
    if row["Tempo"] < 85:
        prompt+= "it should be chill and slow, "
    if row["Tempo"] > 125:
        prompt += "it should be fast and hype,"
    
    completion = "I recommend you listen to " + row["Track Name"] + " by " + row["Artist Name(s)"] + "!"

    data = [{
        "from": "human",
        "value": prompt
    }, {
        "from": "assistant",
        "value": completion
    }]

    data_list.append({
        "id": index,
        "conversations": data
    })

    with open('song_recommendations.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=2)

