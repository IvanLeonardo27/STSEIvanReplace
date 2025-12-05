from app.main import replace_chars

def test_char_replacement():
    assert replace_chars("aku suka nasi", {
        "a": "4",
        "e": "3",
        "i": "1",
        "o": "0",
        "s": "5"
    }) == "4ku 5uk4 n451"
