#Need to import request if using forms
#Need to import redirect if sending using to another page
#Need to import render_template if using simpler way to render templates
#Not sure if I'll need os or cgi

from flask import Flask, request, redirect, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def index():
    return "Something goes here"

app.run()