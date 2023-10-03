# Flask Code Challenge - Superheroes
For this assessment, you'll be working on an API for tracking heroes and their super powers.

There is also a fully built React frontend application, so you can test if your API is working.

The job here is to build out the Flask API to add the functionality described in the deliverables below.

Test you endpoints as stated below

Running the Flask server and using Postman to make requests

# Setup
To download the dependencies for the frontend and backend, run:

pipenv install
npm install --prefix client
There is a code in the code-challenge/seed.py to populate the database.

You can run your Flask API on localhost:5555 by running: python app.py

You can run your React app on localhost:4000 by running: npm start --prefix client

# Project Setup
Clone the repository: git clone <repository-url>.
Navigate to cloned repository: cd super-heroes.
Switch to a virtual environment pipenv shell.
Install dependencies: pipenv install
Navigate to the code-challenge/app directory.
Run the app.py script.



# Models
You need to create the following relationships:

A Hero has many Powers through HeroPower
A Power has many Heros through HeroPower
A HeroPower belongs to a Hero and belongs to a Power Start by creating the models and migrations for the following database tables:
# Validations
The following are the validations added to the models:

# HeroPower
validations to the HeroPower model:

strength must be one of the following values: 'Strong', 'Weak', 'Average'
# Power
validations to Power Model:

description must be present and at least 20 characters long

# Routes

The API is set with the following routes and it is set to return JSON data in the format specified along with the appropriate HTTP verb.

# GET /heroes
Return JSON data in the format below:

[
  { "id": 1, "name": "Kamala Khan", "super_name": "Ms. Marvel" },
  { "id": 2, "name": "Doreen Green", "super_name": "Squirrel Girl" },
  { "id": 3, "name": "Gwen Stacy", "super_name": "Spider-Gwen" }
]
# GET /heroes/:id
If the Restaurant exists, return JSON data in the format below:

{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "powers": [
    {
      "id": 1,
      "name": "super strength",
      "description": "gives the wielder super-human strengths"
    },
    {
      "id": 2,
      "name": "flight",
      "description": "gives the wielder the ability to fly through the skies at supersonic speed"
    }
  ]
}
If the Hero does not exist, return the following JSON data, along with the appropriate HTTP status code:

{
  "error": "Hero not found"
}
# GET /powers
Return JSON data in the format below:

[
  {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  },
  {
    "id": 1,
    "name": "flight",
    "description": "gives the wielder the ability to fly through the skies at supersonic speed"
  }
]
# Get /powers/:id
If the Power exists, return JSON data in the format below:

{
  "id": 1,
  "name": "super strength",
  "description": "gives the wielder super-human strengths"
}
If the Power does not exist, return the following JSON data, along with the appropriate HTTP status code:

{
  "error": "Power not found"
}
# PATCH /powers/:id
This route should update an existing Power. It should accept an object with the following properties in the body of the request:

{
  "description": "Updated description"
}
If the Power exists and is updated successfully (passes validations), update its description and return JSON data in the format below:

{
  "id": 1,
  "name": "super strength",
  "description": "Updated description"
}
If the Power does not exist, return the following JSON data, along with the appropriate HTTP status code:

{
  "error": "Power not found"
}
If the Power is not updated successfully (does not pass validations), return the following JSON data, along with the appropriate HTTP status code:

{
  "errors": ["validation errors"]
}
# POST /hero_powers
This route should create a new HeroPower that is associated with an existing Power and Hero. It should accept an object with the following properties in the body of the request:

{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}
If the HeroPower is created successfully, send back a response with the data related to the Hero:

{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "powers": [
    {
      "id": 1,
      "name": "super strength",
      "description": "gives the wielder super-human strengths"
    },
    {
      "id": 2,
      "name": "flight",
      "description": "gives the wielder the ability to fly through the skies at supersonic speed"
    }
  ]
}
If the HeroPower is not created successfully, return the following JSON data, along with the appropriate HTTP status code:

{
  "errors": ["validation errors"]
}

# Technologies used.
Python3
Flask
SQLAlchemy


# License

Copyright (c) 2023 Michael Owiti Jr.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files , to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.