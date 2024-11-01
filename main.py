import json

from flask import Flask, template_rendered, render_template
from jinja2.lexer import integer_re

app = Flask(__name__)
with open('candidates.json', 'r', encoding='utf=8') as file:
    cand = json.loads((file.read()))


@app.route('/')
def user():
    return render_template('25.10.2024.html', cand=cand)


@app.route('/id/<int:id>')
def id(id):
    for user in cand:
        if id == user['id']:
            return render_template('page_id.html', cand=cand, id=id)


@app.route('/skills/<skills>')
def skills(skills):


    return render_template('skills.html', cand=cand, skills=skills)


app.run(debug=True)
