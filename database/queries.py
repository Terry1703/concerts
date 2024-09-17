import sqlite3


def get_connection():
    return sqlite3.connect('concerts.db')

# Band Methods
def band_concerts(band_name):
    conn = get_connection(concerts)
    c = conn.cursor()
    
    c.execute('''
    SELECT * FROM concerts WHERE band_name = ?
    ''', (band_name,))
    
    concerts = c.fetchall()
    conn.close()
    return concerts

def band_venues(band_name):
    conn = get_connection()
    c = conn.cursor()
    
    c.execute('''
    SELECT DISTINCT venue_title FROM concerts WHERE band_name = ?
    ''', (band_name,))
    
    venues = c.fetchall()
    conn.close()
    return [venue[0] for venue in venues]

def band_play_in_venue(band_name, venue_title, date):
    conn = get_connection()
    c = conn.cursor()
    
    c.execute('''
    INSERT INTO concerts (band_name, venue_title, date) VALUES (?, ?, ?)
    ''', (band_name, venue_title, date))
    
    conn.commit()
    conn.close()

def band_all_introductions(band_name):
    conn = get_connection()
    c = conn.cursor()
    
    c.execute('''
    SELECT venues.city FROM concerts
    JOIN venues ON concerts.venue_title = venues.title
    WHERE concerts.band_name = ?
    ''', (band_name,))
    
    cities = c.fetchall()
    conn.close()
    
    introductions = [f"Hello {city[0]}!!!!! We are {band_name} and we're from (band hometown)" for city in cities]
    return introductions

def band_most_performances():
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
    return band_name

# Venue Methods
def venue_concerts(venue_title):
    conn = get_connection()
    c = conn.cursor()
    
    c.execute('''
    SELECT * FROM concerts WHERE venue_title = ?
    ''', (venue_title,))
    
    concerts = c.fetchall()
    conn.close()
    return concerts

def venue_bands(venue_title):
    conn = get_connection()
    c = conn.cursor()
    
    c.execute('''
    SELECT DISTINCT band_name FROM concerts WHERE venue_title = ?
    ''', (venue_title,))
    
    bands = c.fetchall()
    conn.close()
    return [band[0] for band in bands]

def venue_concert_on(venue_title, date):
    conn = get_connection()
    c = conn.cursor()
    
    c.execute('''
    SELECT * FROM concerts
    WHERE venue_title = ? AND date = ?
    ORDER BY id
    LIMIT 1
    ''', (venue_title, date))
    
    concert = c.fetchone()
    conn.close()
    return concert

def venue_most_frequent_band(venue_title):
    conn = get_connection()
    c = conn.cursor()
    
    c.execute('''
    SELECT band_name, COUNT(*) as performance_count
    FROM concerts
    WHERE venue_title = ?
    GROUP BY band_name
    ORDER BY performance_count DESC
    LIMIT 1
    ''', (venue_title,))
    
    band_name = c.fetchone()[0]
    conn.close()
    return band_name

# Concert Methods
def concert_band(concert_id):
    conn = get_connection()
    c = conn.cursor()
    
    c.execute('''
    SELECT band_name FROM concerts WHERE id = ?
    ''', (concert_id,))
    
    band_name = c.fetchone()[0]
    conn.close()
    return band_name

def concert_venue(concert_id):
    conn = get_connection()
    c = conn.cursor()
    
    c.execute('''
    SELECT venue_title FROM concerts WHERE id = ?
    ''', (concert_id,))
    
    venue_title = c.fetchone()[0]
    conn.close()
    return venue_title

def concert_hometown_show(concert_id):
    conn = get_connection()
    c = conn.cursor()
    
    c.execute('''
    SELECT bands.hometown, venues.city
    FROM concerts
    JOIN bands ON concerts.band_name = bands.name
    JOIN venues ON concerts.venue_title = venues.title
    WHERE concerts.id = ?
    ''', (concert_id,))
    
    hometown, city = c.fetchone()
    conn.close()
    return hometown == city

def concert_introduction(concert_id):
    conn = get_connection()
    c = conn.cursor()
    
    c.execute('''
    SELECT bands.name, bands.hometown, venues.city
    FROM concerts
    JOIN bands ON concerts.band_name = bands.name
    JOIN venues ON concerts.venue_title = venues.title
    WHERE concerts.id = ?
    ''', (concert_id,))
    
    band_name, band_hometown, venue_city = c.fetchone()
    conn.close()
    
    return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"
