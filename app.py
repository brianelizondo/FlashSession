from flask import Flask, redirect, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "abcd1234"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
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
    question_qty = len(question_obj)
    question_answered = len(responses)

    if question_num == question_answered and question_num < question_qty:
        question_title = satisfaction_survey.questions[question_num].question
        question_choices = satisfaction_survey.questions[question_num].choices
        return render_template("questions.html", question=question_title, choices=question_choices, question_id=question_num)
    elif question_num == question_answered and question_num == question_qty:
        return redirect('/thank_you')
    else:
        return redirect(f'/questions/{question_answered}')

@app.route('/answer', methods=["POST"])
def process_answer():
    """Process to append the answer to the responses list, and then redirect to the next question"""
    responses.append(request.form["answer"])
    next_question = int(request.form["current_q"]) + 1
    return redirect(f'/questions/{ next_question }')

@app.route('/thank_you')
def thank_you():
    """Redirect to a simple 'Thank You!' page"""
    return render_template("thank_you.html")