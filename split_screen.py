import re
from flask import Flask, request, make_response, render_template
from werkzeug.routing import Rule, Map, BaseConverter, ValidationError
app = Flask(__name__)

class RegexConverter(BaseConverter):
    #Using a converter so we can use a regex to parse the follower link url
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/splitscreen')
def splitscreen():
   return render_template('splitscreen.html')

@app.route('/<regex("[0-9]{3}[-][0-9]{3}[-][0-9]{3}"):session_id>/')
#the regex checks whether the url contains the session id
def index_session_id(session_id):
   return render_template('follower_side.html')

@app.route('/start_page')
def first_frame():
   return render_template('start_page.html')

@app.route('/popup_link')
def popup_link():
   return render_template('popup_link.html')


