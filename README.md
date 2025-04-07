### CODE CHALLANGE 2
# Late Show API

A Flask API for tracking talk show episodes, guests, and their appearances.

## Features

- Manage episodes with dates and numbers

- Track guests with names and occupations

- Record guest appearances on episodes with ratings

- Validate appearance ratings (1-5)

- RESTful endpoints with proper HTTP status codes for error response

### Installations

1. Clone the repository:
   git clone https://git@github.com:simon036/Flask-Late-show-API.git

   cd lateshow-API

2. pipenv install

   pipenv shell

3. Configure the database:

    export DATABASE_URL=sqlite:///app.db

4. Run migrations:

   flask db upgrade

5. Seed the database:

   python seed.py or flask run

The API will run on http://localhost:5555

### API Endpoints
1. GET /episodes

Returns all episodes

2. GET /episodes/:id

Returns a specific episode with appearances

3. GET /guests

Returns all guests

4. POST /appearances

Creates a new appearance

### Testng
Import the Postman collection from challenge-4-lateshow.postman_collection.json to test all endpoints.

###  Database Schema

episodes: Stores show episodes

guests: Stores guest information

appearances: Junction table linking guests to episodes with ratings