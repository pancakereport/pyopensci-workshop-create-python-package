"""
This module is based on songs about airplanes, aeroplanes, 
and jet planes.
"""

def airplanes():
    print("Airplanes in the night sky...")

def shooting_stars():
    print("I could really use a wish right now.")

def aeroplane(artist):
    # Defensive Check: Is it a string?
    if not isinstance(artist, str):
        print("Error: Make sure you pass in an artist's name as a string.")
        return 
    
    # Defensive Check: Is it empty?
    artist = artist.strip()
    if not artist:
        print("Error: Please provide a valid artist name (non-empty string).")
        return
    
    lyrics = {
        "frou frou": "Just flying with my aeroplane.",
        "red hot chili peppers": "And music is my aeroplane.",
        "bjork": "I'm taking an aeroplane across the world to follow my heart."
    }
    clean_artist = artist.lower()

    message = lyrics.get(
        clean_artist, 
        f"I didn't know {artist} has an aeroplane song."
    )
    
    print(message)

def jet_plane_leaving():
    print("I'm leaving on a jet plane")
    print("Don't know when I'll be back again")

def jet_plane_ride():
    print("Gonna take her for a ride on a big jet plane.")