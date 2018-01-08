#Need to import request if using forms
#Need to import redirect if sending using to another page
#Need to import render_template if using simpler way to render templates
#Not sure if I'll need os or cgi

from flask import Flask, request, redirect, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

"""Your assignment is simply to create a user signup form where users provide a username, password,
and, optionally, an email address. You must have an additional field to verify the password (the 
user must retype it exactly). Then you will validate the input and either redirect them to a welcome
page, or provide error information if any input is invalid."""


@app.route("/", methods=['GET'])
def index():
    return render_template('user-signup.html')

app.run()