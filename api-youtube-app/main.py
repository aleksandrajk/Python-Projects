from flask import Flask, jsonify, render_template
from numerize.numerize import numerize
import requests

app = Flask(__name__)

CHANNELS = {
  'LeagueOfLegends' : 'UC2t5bjwHdUX4vM2g8TRDq5g',
  'Fireship' : 'UCsBjURrPoezykLs9EqgamOA',
  'Lex' : 'UCSHZKyawb77ixDdsGog4iWA',
}

@app.route('/')
def index():
  url = "https://youtube138.p.rapidapi.com/channel/videos/"
  querystring = {"id": CHANNELS['LeagueOfLegends'], 
                 "filter":"uploads_latest", 
                 "hl":"en", "gl":"US"}
  headers = {
  	"X-RapidAPI-Key": "d72c98894cmsh28b3af34c5863e1p19f360jsne4b9c3aa39ec",
  	"X-RapidAPI-Host": "youtube138.p.rapidapi.com"
  }
  
  response = requests.get(url, headers=headers, params=querystring)
  data = response.json()
  contents = data['contents']
  
  videos = [video['video'] for video in contents if video['video']['publishedTimeText']]
  
  print(videos[0])
  
  return render_template('index.html', videos=videos)

@app.template_filter()
def numberize(views):
  return numerize(views, 1)

@app.template_filter()
def highest_quality_image(images):
  return images[3]['url'] if len(images) >= 4 else images[0]['url']
  
app.run(host='0.0.0.0', port=81)
