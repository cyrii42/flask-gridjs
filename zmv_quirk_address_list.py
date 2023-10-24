from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quirk_list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

ROWS_PER_PAGE = 15


class quirk_list(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    student_last = db.Column(db.String(64), index=True)
    student_first = db.Column(db.String(64), index=True)
    # name = db.Column(db.String(64), index=True)
    # age = db.Column(db.Integer, index=True)
    # address = db.Column(db.String(256))
    # phone = db.Column(db.String(20))
    # email = db.Column(db.String(120), index=True)



db.create_all()


@app.route('/')
def index():
    users = quirk_list.query
    return render_template('basic_quirk_table.html', users=users, rows_per_page=ROWS_PER_PAGE)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="4579")

