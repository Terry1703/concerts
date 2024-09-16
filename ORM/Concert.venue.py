def get_venue_for_concert(conn, concert_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT venues.title, venues.city
        FROM concerts
        JOIN venues ON concerts.venue_title = venues.title
        WHERE concerts.id = ?
    """, (concert_id,))
    return cursor.fetchone()
