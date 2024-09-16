from concert.schema import create_schema
from concert.queries import (
    band_concerts, band_venues, band_play_in_venue, band_all_introductions,
    band_most_performances, venue_concerts, venue_bands, venue_concert_on,
    venue_most_frequent_band, concert_band, concert_venue,
    concert_hometown_show, concert_introduction
)

def main():
    # Create the schema
    create_schema()

    # Example Usage
    print("Band Concerts:")
    print(band_concerts('The Rockers'))

    print("\nBand Venues:")
    print(band_venues('The Rockers'))

    print("\nBand Play in Venue:")
    band_play_in_venue('The Rockers', 'Madison Square Garden', '2024-09-15')

    print("\nBand All Introductions:")
    print(band_all_introductions('The Rockers'))

    print("\nBand Most Performances:")
    print(band_most_performances())

    print("\nVenue Concerts:")
    print(venue_concerts('Madison Square Garden'))

    print("\nVenue Bands:")
    print(venue_bands('Madison Square Garden'))

    print("\nVenue Concert on Date:")
    print(venue_concert_on('Madison Square Garden', '2024-09-15'))

    print("\nVenue Most Frequent Band:")
    print(venue_most_frequent_band('Madison Square Garden'))

    print("\nConcert Band:")
    print(concert_band(1))

    print("\nConcert Venue:")
    print(concert_venue(1))

    print("\nConcert Hometown Show:")
    print(concert_hometown_show(1))

    print("\nConcert Introduction:")
    print(concert_introduction(1))

if __name__ == '__main__':
    main()
