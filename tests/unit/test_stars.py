from pyospackage_pancakereport.stars import airplanes, shooting_stars, aeroplane

def test_airplanes(capsys):
    airplanes()
    captured = capsys.readouterr()
    assert captured.out == "Airplanes in the night sky...\n"

def test_shooting_stars(capsys):
    shooting_stars()
    captured = capsys.readouterr()
    assert captured.out == "I could really use a wish right now.\n"

def test_aeroplane(capsys):
    aeroplane("bjork")
    captured = capsys.readouterr()
    assert captured.out == "I'm taking an aeroplane across the world to follow my heart.\n"
    aeroplane("charli xcx")
    captured = capsys.readouterr()
    assert captured.out == "I didn't know charli xcx has an aeroplane song.\n"
    aeroplane("   ")
    captured = capsys.readouterr()
    assert "Error: Please provide a valid artist name" in captured.out
    aeroplane(123)
    captured = capsys.readouterr()
    assert "Error: Make sure you pass in an artist's name as a string." in captured.out