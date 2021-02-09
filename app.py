from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random
app = Flask(__name__)

ENV = 'prod'

### If the ENV is dev, it uses the psql on my (Drextex's) computer.
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5433/chiped'
else: # When ENV is changed to something else, it should use the Heroku database.
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tlvibsrdjvpuwk:a268e9a77940e8ce8a91671d86eaeb81b6a49f3a514c9479fe7b6cb0922192a3@ec2-52-6-178-202.compute-1.amazonaws.com:5432/d2vdtfkq767lvh'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ChipEd(db.Model):
    ### This table consists of firstname and lastname | used as a test table 
    __tablename__ = 'chiped'
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class codeTable(db.Model):
    ### This table contains the code generated by a teacher. 
    __tablename__ = "codeTable"
    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String)

    def __init__(self,code):
        self.code = code

# Handles main page.
@app.route('/')
def index():
    all_items = db.session.query(ChipEd).all()
    return render_template('index.html', all_cust = all_items)

# Handles teachers' clicks on the teacher-btn object.
@app.route('/code', methods=['POST'])
def code():
    return render_template('success.html')

# Handles students' clicks on the student-btn object.
@app.route('/student', methods=['POST'])
def student():
    return "Feature is still being implemented."


if __name__ == "__main__":
    app.run()
