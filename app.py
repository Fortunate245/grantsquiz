from flask import Flask,request,redirect,url_for,render_template
import random
app=Flask(__name__)


quiz_questions_answers={

}

#list of questions
questions=list(quiz_questions_answers.keys())

for question_number in range(len(quiz_questions_answers)):
        correct_answer=quiz_questions_answers[questions[question_number]]
        wrong_answer=list(quiz_questions_answers.values())
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_answer=random.sample(wrong_answer,2)
        answerOptions=wrong_answer + [correct_answer]
        random.shuffle(answerOptions)
    



@app.route('/')
def index():
    if request.method=='POST':
        return  redirect(url_for('story'))

    return render_template('index.html')



@app.route('/story')
def story():
    if request.method=='POST':
        return  redirect(url_for('instrutions'))

    return render_template('story.html')


@app.route('/instruction')
def instruction():
    if request.method=='POST':
        return  redirect(url_for('quiz'))

    return render_template('instructions.html')

@app.route('/quiz')
def quiz():
    if request.method=='POST':
        return  redirect(url_for('evaluation'))

    return render_template('quiz.html')


@app.route('/evaluation')
def evaluation():
    if request.method=='POST':
        return  redirect(url_for('index'))

    return render_template('evaluation.html')



