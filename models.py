import sqlite3

def get_connection():
    return sqlite3.connect('concerts.db')

class Band:
    def __init__(self, name):
        self.name = name

    def concerts(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute('''
        SELECT * FROM concerts WHERE band_name = ?
        ''', (self.name,))
        concerts = c.fetchall()
        conn.close()
        return concerts

    def venues(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute('''
        SELECT DISTINCT venue_title FROM concerts WHERE band_name = ?
        ''', (self.name,))
        venues = c.fetchall()
        conn.close()
        return [venue[0] for venue in venues]

    def play_in_venue(self, venue_title, date):
        conn = get_connection()
        c = conn.cursor()
        c.execute('''
        INSERT INTO concerts (band_name, venue_title, date) VALUES (?, ?, ?)
        ''', (self.name, venue_title, date))
        conn.commit()
        conn.close()

    def all_introductions(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute('''
        SELECT venues.city FROM concerts
        JOIN venues ON concerts.venue_title = venues.title
        WHERE concerts.band_name = ?
        ''', (self.name,))
        cities = c.fetchall()
        conn.close()
        introductions = [f"Hello {city[0]}!!!!! We are {self.name} and we're from (band hometown)" for city in cities]
        return introductions

    @staticmethod
    def most_performances():
        conn = get_connection()
        c = conn.cursor()
        c.execute('''
        SELECT band_name, COUNT(*) as performance_count
        FROM concerts
        GROUP BY band_name
        ORDER BY performance_count DESC
        LIMIT 1
        ''')
        band_name = c.fetchone()[0]
        conn.close()
        return Band(band_name)

class Venue:
    def __init__(self, title):
        self.title = title

    def concerts(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute('''
        SELECT * FROM concerts WHERE venue_title = ?
        ''', (self.title,))
        concerts = c.fetchall()
        conn.close()
        return concerts

    def bands(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute('''
        SELECT DISTINCT band_name FROM concerts WHERE venue_title = ?
        ''', (self.title,))
        bands = c.fetchall()
        conn.close()
        return [band[0] for band in bands]

    def concert_on(self, date):
        conn = get_connection()
        c = conn.cursor()
        c.execute('''
        SELECT * FROM concerts
        WHERE venue_title = ? AND date = ?
        ORDER BY id
        LIMIT 1
        ''', (self.title, date))
        concert = c.fetchone()
        conn.close()
        return concert

    def most_frequent_band(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute('''
        SELECT band_name, COUNT(*) as performance_count
        FROM concerts
        WHERE venue_title = ?
        GROUP BY band_name
        ORDER BY performance_count DESC
        LIMIT 1
        ''', (self.title,))
        band_name = c.fetchone()[0]
        conn.close()
        return Band(band_name)

class Concert:
    def __init__(self, id):
        self.id = id

    def band(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute('''
        SELECT band_name FROM concerts WHERE id = ?
        ''', (self.id,))
        band_name = c.fetchone()[0]
        conn.close()
        return Band(band_name)

    def venue(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute('''
        SELECT venue_title FROM concerts WHERE id = ?
        ''', (self.id,))
        venue_title = c.fetchone()[0]
        conn.close()
        return Venue(venue_title)

    def hometown_show(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute('''
        SELECT bands.hometown, venues.city
        FROM concerts
        JOIN bands ON concerts.band_name = bands.name
        JOIN venues ON concerts.venue_title = venues.title
        WHERE concerts.id = ?
        ''', (self.id,))
        hometown, city = c.fetchone()
        conn.close()
        return hometown == city

    def introduction(self):
        conn = get_connection()
        c = conn.cursor()
        c.execute('''
        SELECT bands.name, bands.hometown, venues.city
        FROM concerts
        JOIN bands ON concerts.band_name = bands.name
        JOIN venues ON concerts.venue_title = venues.title
        WHERE concerts.id = ?
        ''', (self.id,))
        band_name, band_hometown, venue_city = c.fetchone()
        conn.close()
        return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"
