def get_concerts_for_venue(conn, venue_title):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM concerts
        WHERE venue_title = ?
    """, (venue_title,))
    return cursor.fetchall()
