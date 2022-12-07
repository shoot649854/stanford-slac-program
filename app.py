from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Item %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ML-Research')
def research():
    return render_template('ML-Research.html')


# @app.route('/gallery')
# def gallery():
#     return render_template('gallery.html')


# @app.route('/image-classification')
# def image_classification():
#     return render_template('img-classif.html')


if __name__ == "__main__":
    app.run(debug=True)