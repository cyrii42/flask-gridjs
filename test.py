import sqlalchemy as db

import peloton.constants as peloton_constants
from peloton.classes import PelotonRide

mariadb_url = db.URL.create(
        drivername="mysql+pymysql",
        username=peloton_constants.MARIADB_USER,
        password=peloton_constants.MARIADB_PASS,
        host=peloton_constants.MARIADB_SERVER,
        database="peloton",
    )

print(mariadb_url)