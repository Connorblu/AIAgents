import os
import csv



with open('all_playlists.csv', 'x') as all_playlists:
    all_playlists.write("Track ID,Track Name,Album Name,Artist Name(s),Release Date,Duration (ms),Popularity,Added By,Added At,Genres,Record Label,Danceability,Energy,Key,Loudness,Mode,Speechiness,Acousticness,Instrumentalness,Liveness,Valence,Tempo,Time Signature\n")
    # Get the directory containing the CSV files
    directory = './spotify_playlists'

    # Write the header row first (assuming all files have the same structure)
    header_written = False

    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            
            with open(file_path, 'r') as playlist_file:
                try:
                    print("reading from " + file_path)
                    playlist_file.readline()
                    lines = playlist_file.readlines()
                    for line in lines:
                        all_playlists.write(line)
                except UnicodeDecodeError:
                    print("Unable to read " + file_path + " due to unicode error. Skipping")
                '''try:
                    # Write header from the first file only
                    header = next(csv_reader)
                    if not header_written:
                        all_playlists.write(','.join(header) + '\n')
                        header_written = True


                    
                    # Copy all data rows to the combined file
                    for row in csv_reader:
                        all_playlists.write(','.join(row) + '\n')
                except UnicodeDecodeError as e:
                    print("cannot read file " + file_path + "due to unicode decode error. Skipping this file.")
                    continue'''