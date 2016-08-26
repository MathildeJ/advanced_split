from __future__ import print_function
import re
import sys
import json
from flask import Flask, request, make_response, render_template
from werkzeug.routing import Rule, Map, BaseConverter, ValidationError
from flask_mandrill import Mandrill

app = Flask(__name__)
app.config['MANDRILL_API_KEY'] = 'your_key_here'
mandrill = Mandrill(app)

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

@app.route('/<regex("[0-9]{3}[-][0-9]{3}[-][0-9]{3}"):session_id>/')
def index_session_id(session_id):
   return render_template('follower_side.html')

@app.route('/popup_link', methods = ['POST', 'GET'])
def popup_link():
   if request.method == 'POST':
      email_address = request.form[ 'emailAddress' ]
      email_link = request.form[ 'inviteLink' ]
      mandrill.send_email(
         from_email='isobel@surfly.com',
         to=[{'email': email_address}],
         html='<p>Hi,</p><p> You have been invited to join a splitscreen session! </p><p> Click <a href='+email_link+'>here</a> to join your friend! </p>',
         subject='Invitation to a splitscreen session',
         )
      return render_template('fourth_frame.html')
   else:
      return render_template('popup_link.html')


