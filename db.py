import psycopg2


DB_CONFIG = {
     "dbname": "ebilets_db",
     "user": "postgres",
     "password": "231998",
     "host": "localhost",
     "port": "5432"
 }


def connect_db():
    return psycopg2.connect(**DB_CONFIG)


def init_db():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
             CREATE TABLE IF NOT EXISTS eventes
             (
                id SERIAL PRIMARY KEY,
                name_event VARCHAR(100),
                date_event DATE
             );
         """)

        cur.execute("""
             CREATE TABLE IF NOT EXISTS bilets
             (
                 id SERIAL PRIMARY KEY,
                 bilets INT,
                 type_bilets VARCHAR(100)
                     );
                 """)

        cur.execute("""
             CREATE TABLE IF NOT EXISTS events_bilets
             (
                 id SERIAL PRIMARY KEY,
                 name_event_id INT REFERENCES eventes (id) ON DELETE CASCADE,
                 bilet_id INT REFERENCES bilets (id) ON DELETE CASCADE
                     );
                 """)


def get_all_eventes():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM eventes")
        eventes = cur.fetchall()
        return eventes


def get_all_bilets():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM bilets")
        bilets = cur.fetchall()
        return bilets


def get_events_full_info():
    with connect_db() as conn, conn.cursor() as cur:

        cur.execute("SELECT name_event FROM eventes ")
        event_info = cur.fetchone()

        cur.execute("""
                        SELECT bilets, type_bilets
                        FROM events_bilets 
                            JOIN bilets ON events_bilets.bilet_id = bilets.id
        """)
        bilets = cur.fetchall()

        return {
                "event_info": event_info,
                "bilets": bilets
        }


def create_events(name_event):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO events (name_event) VALUES (%s)", (name_event,))


def search_events(query):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM events WHERE name_event ILIKE %s;", (f"%{query}%",))
        events = cur.fetchall()
        return events

def create_bilets(bilet_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO bilets (bilets, type_bilets) VALUES (%s, 'Занято')", (bilet_id,))


def delite_bilets(bilets):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM bilets WHERE bilets=%s", (bilets,))















