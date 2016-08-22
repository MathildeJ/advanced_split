import re
from flask import Flask, request, make_response, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/splitscreen')
def splitscreen():
   return render_template('splitscreen.html')

@app.route('/splitscreen/<session_id>')
def index_session_id(session_id):
   return render_template('follower_side.html')

@app.route('/splitscreen/third_frame')
def splitscreen_test():
   return render_template('third_frame.html')

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
