import json

from flask import Flask, template_rendered, render_template
from jinja2.lexer import integer_re

app = Flask(__name__)
with open('candidates.json', 'r', encoding='utf=8') as file:
    cand = json.loads((file.read()))
@app.route('/')
def user():
    return render_template('25.10.2024.html', cand=cand)
@app.route('/')
def id():

    if id == cand['id']:

        return render_template('page_id', cand=cand, id=1)

def sk():
    sk_list = ['7']



    return render_template('25.10.2024.html', user=cand)
app.run(debug = True)
