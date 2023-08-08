# Python-Song-Script

This Python script allows you to download the music videos of songs from a specified Spotify playlist using the YouTube Data API and convert them to MP3 format using the pytube and ffmpeg libraries.

## Prerequisites

Before running the script, you need to have the following:

- Spotify Developer Account: Get your Spotify API client ID and client secret.
- Google Cloud Project: Create a new project in the Google Cloud Console and enable the YouTube Data API.
- YouTube Data API Key: Obtain an API key for the YouTube Data API.

## Installation

1. Clone the repository: `git clone https://github.com/yourusername/spotify-youtube-music-downloader.git`
2. Install the required Python libraries: `pip install spotipy google-api-python-client pytube ffmpeg-python`
3. Replace the placeholders in the script with your Spotify client ID, client secret, and YouTube API key.
4. Run the script: `python main.py`

## Usage

1. Replace the `spotify_playlist_id` variable with the ID of the Spotify playlist you want to download the songs from.
2. The script will search for the official music videos of each song in the playlist on YouTube using the song name and artist name. 
3. If a music video is found, it will be downloaded from YouTube and converted to MP3 format using the pytube and ffmpeg libraries.
4. The downloaded MP3 files will be saved in the same directory as the script.
5. The script will print a message for each successful download, indicating the song name, artist name, and the name of the MP3 file.

Please note that the script will only download the music videos for the first result found on YouTube. If you want to download a specific music video, you can modify the search query in the `seach_yt_musicvideos()` function to include any/more specific keywords.

## Things to do

1. Create a helper function `upload_files_to_itunes()` which helps us to upload the downloaded mp3 files to my Itunes account

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request on the project's GitHub repository.

## Author

[Sahil Dayal](https://github.com/sahildayal)

## Resources

- [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
- [Google Cloud Console](https://console.cloud.google.com/)
- [YouTube Data API](https://developers.google.com/youtube/v3)
- [pytube Documentation](https://python-pytube.readthedocs.io/en/latest/)
- [ffmpeg-python Documentation](https://github.com/kkroening/ffmpeg-python)
