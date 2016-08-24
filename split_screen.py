import re
from flask import Flask, request, make_response, render_template
from werkzeug.routing import Rule, Map, BaseConverter, ValidationError
app = Flask(__name__)

class RegexConverter(BaseConverter):
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

@app.route('/splitscreen/<regex("[0-9]{3}[-][0-9]{3}[-][0-9]{3}"):string>/')
def index_session_id(string):
   return render_template('follower_side.html')

"""
@app.route('/splitscreen/<session_id>')
def original_session_id(session_id):
   return render_template('follower_side.html')
"""

@app.route('/<regex("[abcABC0-9]{4,6}"):uid>-<slug>/')
def example(uid, slug):
    return "uid: %s, slug: %s" % (uid, slug)

"""
http://localhost:5000/abc0-foo/
"""

@app.route('/start_page')
def first_frame():
   return render_template('start_page.html')

@app.route('/fourth_frame')
def fourth_frame():
   return render_template('/fourth_frame.html')

@app.route('/follower_side_start')
def follower_side_start():
   return render_template('follower_side_start.html')

@app.route('/popup_link')
def popup_link():
   return render_template('popup_link.html')


