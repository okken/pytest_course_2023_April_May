import cards

def test_one(db):
    db.add_card(cards.Card("learn pytest"))
    assert db.count() == 1


def test_foo():
    pass
