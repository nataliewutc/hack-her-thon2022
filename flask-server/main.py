from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import csv
import time

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

def get_reddit_posts(title):
    url = "https://www.reddit.com/search/?q=how%20to%20make%20a%20web%20app%20with%20python"
    hdr = { 'User-Agent' : 'Nomads shower crawler'}
    req = urllib2.Request(url, headers=hdr)
    htmlpage = urlib2.urlopen(req).read()
    BeautifulSoupFormat = Beautifulsoup(htmlpage, 'lxml')
    name_box = BeautifulSoupFormat.find_all('a')
    return(data.text)

@app.route("/")
def my_index():
    return render_template("index.html")

@app.route('/api/get_resources', methods=["POST"])
def get_lists():
    keys = get_youtube_videos(sentence) + get_reddit-posts(sentence)
    list_of_resources = dict(zip(keys, values))
    return jsonify({"list_id": list_id})

app.run(debug=True)