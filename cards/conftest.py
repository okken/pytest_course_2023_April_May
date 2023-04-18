import cards
import pytest


@pytest.fixture(scope='session')
def db_top(tmp_path_factory):
    "cards db - no reset"
    # setup
    print('\n----setup for session scope db')
    cards_db_path = tmp_path_factory.mktemp("cards_db")
    cards_db = cards.CardsDB(cards_db_path)
    yield cards_db
    # teardown
    print('\n----teardown for session scope db')
    cards_db.close()

@pytest.fixture()
def db(db_top):
    "cards db - with reset"
    # setup
    cards_db = db_top
    print('\n----setup for function scope db')
    yield cards_db
    # teardown
    print('\n----calling delete_all()')
    cards_db.delete_all()



# @pytest.fixture()
# def db(tmp_path):
#     "cards db - with reset"
#     print(tmp_path)
#     db = cards.CardsDB(tmp_path)
#     #db_top.delete_all()
#     return db