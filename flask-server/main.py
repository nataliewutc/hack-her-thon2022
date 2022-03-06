from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask("__main__")

def get_youtube_videos(title):
    link = "https://www.youtube.com/watch?v=rfscVS0vtbw"
    response = requests.get(link, headers=HEADER)
    soup = BeautifulSoup(response.text, "html.parser")
    titleSoupMeta = soup.find("meta", property = "og:title")
    videoTitle = titleSoupMeta["content"] if titleSoupMeta else "Notfound"
    thumbSoupMeta = soup.find("meta", property="og:image")
    videoImage = thumbSoupMeta["content"] if thumbSoupMeta else "Notfound"
    return(videoTitle, "Thumbnail", videoImage) # ttps://i.ytimg.com/vi/rfscVS0vtbw/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG\u0026rs=AOn4CLBcbOHe1sGObiBHwNSA32uZ25dPgg

@app.route("/")
def my_index():
    return render_template("index.html")

@app.route('/api/get_youtube', methods=["POST"])
def get_playlist():
    get_youtube_videos(sentence)
    return jsonify({"playlist_id": playlist_id})

app.run(debug=True)