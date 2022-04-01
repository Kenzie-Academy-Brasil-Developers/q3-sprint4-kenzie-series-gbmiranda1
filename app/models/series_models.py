import psycopg2
import os

HOST = os.getenv("HOST")
DATABASE = os.getenv("DATABASE")
USER = os.getenv("db_USER")
PASSWORD = os.getenv("PASSWORD")

class Series:
    def __init__(self, **kwargs) -> None:
        self.serie = kwargs["serie"].title()
        self.seasons = kwargs["seasons"]
        self.released_date = kwargs["released_date"]
        self.genre = kwargs["genre"].title()
        self.imdb_rating = kwargs["imdb_rating"]

    def createTableModels():
        conn = psycopg2.connect(
            host=HOST, database=DATABASE, user=USER, password=PASSWORD
        )

        query = """
                CREATE TABLE IF NOT EXISTS ka_series(
                    id BIGSERIAL constraint pk_series PRIMARY KEY,
                    serie VARCHAR(100) NOT NULL UNIQUE,
                    seasons INTEGER NOT NULL,
                    released_date DATE NOT NULL,
                    genre VARCHAR(50) NOT NULL,
                    imdb_rating FLOAT NOT NULL
                );
            """

        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()

    def getSeries():
        query = "SELECT * FROM ka_series"

        conn = psycopg2.connect(
            host=HOST, database=DATABASE, user=USER, password=PASSWORD
        )

        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    
    def getByIdSeries(serie_id):
        query = f"SELECT * FROM ka_series WHERE id = {serie_id}"

        conn = psycopg2.connect(
            host=HOST, database=DATABASE, user=USER, password=PASSWORD
        )

        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data

    def createSeries(payload):

        data = tuple(payload.__dict__.values())

        query = "INSERT INTO ka_series (serie, seasons, released_date, genre, imdb_rating) VALUES (%s, %s, %s, %s, %s) RETURNING *;"

        conn = psycopg2.connect(
            host=HOST, database=DATABASE, user=USER, password=PASSWORD
        )
      

        cur = conn.cursor()
        
        print(data)
        cur.execute(query, data)

        conn.commit()
        created_series = cur.fetchone()
        
        cur.close()
        conn.close()
        
        return created_series