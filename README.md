# Summary
MTG Deck Organizer

# Local Database Setup
Install Postgres onto your machine
``` 
psql postgres
create database deck_box
CREATE ROLE mtg_decks_admin LOGIN SUPERUSER PASSWORD 'admin';
```

# Django Setup
First Install all of the requirements:
```
pip install -r requirements
```

Then migrate into the newly created database:
```
python manage.py migrate
```

# Sync Cards into database
Then Sync in the sets and cards into the database
```
python manage.py sync_cards set
python manage.py sync_cards card
```
