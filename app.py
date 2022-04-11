from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "abcd1234"
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def home_page():
    """Return a page that shows the user the title of the survey, the instructions, and a button to start the survey"""
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("home.html", survey_title=title, survey_instructions=instructions)