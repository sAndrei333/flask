import json

from flask import Flask

app = Flask(__name__)
with open('candidates.json', 'r', encoding='utf-8') as file:
    data = json.loads(file.read())

'''def candidates(self, id, name, skills):
    self.id = id
    self.name = name
    self.skills = skills'''
@app.route('/mainpage/')
def mainpage():
   return print(data)
@app.route('/name/')
def name():


    pass





app.run(debug = True)
