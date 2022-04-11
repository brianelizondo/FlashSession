from random import choices
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

@app.route('/questions/<question_num>')
def show_question(question_num):
    """Return page to build a route that can handle questions — it should handle URLs like"""
    question_num = int(question_num)
    question_obj = satisfaction_survey.questions
    question_title = satisfaction_survey.questions[question_num].question
    question_choices = satisfaction_survey.questions[question_num].choices
    return render_template("questions.html", question=question_title, choices=question_choices)
