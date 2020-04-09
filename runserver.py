from os import environ
from flask import Flask, render_template, url_for
from file_loader import *

pic_max_num = 4

app = Flask(__name__)

#index
@app.route('/')
def index():
	pics = pic_list()[:pic_max_num]
	songs = song_list()[:pic_max_num]
	texts = text_list()[:pic_max_num]
	return render_template('index.html', len = len(pics), pics = pics, songs = songs, texts = texts)

#gallery
@app.route('/gallery')
def gallery():
	pics = pic_list()
	songs = song_list()
	texts = text_list()
	return render_template('gallery.html', len = len(pics), pics = pics, songs = songs, texts = texts)

if __name__ == '__main__':
    # HOST = environ.get('SERVER_HOST', 'localhost')
    # try:
    #     PORT = int(environ.get('SERVER_PORT', '5555'))
    # except ValueError:
    #     PORT = 5555
    app.run(host='0.0.0.0', port=1234)
