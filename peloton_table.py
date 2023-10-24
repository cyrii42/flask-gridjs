from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

import peloton.constants as peloton_constants

# import peloton.helpers as helpers

# sql_engine = helpers.create_mariadb_engine("peloton")

mariadb_url = f"mysql+pymysql://{peloton_constants.MARIADB_USER}:{peloton_constants.MARIADB_PASS}@{peloton_constants.MARIADB_SERVER}/peloton"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = mariadb_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

ROWS_PER_PAGE = 15


# class Kid(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True)
#     age = db.Column(db.Integer, index=True)
#     address = db.Column(db.String(256))
#     phone = db.Column(db.String(20))
#     email = db.Column(db.String(120), index=True)

class Ride(db.Model):
    __tablename__ = "peloton"
    workout_id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    workout_type: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)


print(f"sdfohiasdopfihaspdfoihsapdfi: {Ride.query}")
db.create_all()


@app.route('/')
def index():
    users = Ride.query
    return render_template('basic_table.html', users=users, rows_per_page=ROWS_PER_PAGE)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="4579")
