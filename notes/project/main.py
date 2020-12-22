from django import db
from flask import Flask, request, render_template
from project.note import Note
from flask_sqlalchemy import SQLAlchemy

from waitress import serve

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/')
def test():
    return render_template("notes_html.html")


@app.route('/', methods=["POST"])
def submit():
    heading = request.form['heading']
    content = request.form['content']
    note = Note(heading, content)
    return f"Heading - {note.heading} Content - {note.content} created at - {note.created_at}"



if __name__ == "__main__":
    app.run(debug=True)

'''
upper part:
form - add notes 
down part:
list of notes - visualized? or urls
list of notes - sorted by time of creation using datetime 

'''


