# Pokemon Trainer's Teams

This is a simple REST API to manage Pokemon Trainer's Treams.

Note: The project uses the API `https://pokeapi.co/api/v2/pokemon/` to fill and update **Pokemon's registers**

## Initial Configuration

1. Create and activate virtual environment

   `virtualenv -p python3.8` and then `activate` in the path of the environment
2. Install requirements

    `pip install -r requirements/local.txt`
3. Create .env file and copy .env_example

5. The application uses Django's default database, but you can configure other through DATABASE_URL var
6. Create migrations

    `python manage.py makemigrations --settings=config.settings.local`
6. Migrate

    `python manage.py migrate --settings=config.settings.local`
7. Run the project

    `python manage.py runserver --settings=config.settings.local`

## Run the tests

`python manage.py test --settings=config.settings.local`

# REST API

The REST API is described below.

## Get list of Pokemons

### Request

`GET /api/pokemon/`

**Example** `http://localhost:8000/api/pokemon/`

### Response

    HTTP 200 OK
    Content-Type: application/json
    [
      {
          "id": 1,
          "is_removed": false,
          "created": "2022-09-25T14:35:51.216543-05:00",
          "modified": "2022-09-25T14:35:51.217509-05:00",
          "name": "bulbasaur"
      },
      {
          "id": 2,
          "is_removed": false,
          "created": "2022-09-25T14:35:55.240889-05:00",
          "modified": "2022-09-25T14:35:55.240889-05:00",
          "name": "ivysaur"
      },
    ...
    ]

## Get list of Trainers

### Request

`GET /api/trainer/`

**Example** `http://localhost:8000/api/trainer/`

### Response

    HTTP 200 OK
    Content-Type: application/json
    [
      {
          "id": 2,
          "is_removed": false,
          "created": "2022-09-25T00:59:35.196956-05:00",
          "modified": "2022-09-25T00:59:35.196956-05:00",
          "name": "Alberto"
      }
    ]
 
## Get a specific Trainer

### Request

`GET /api/trainer/id/`

**Example** `http://localhost:8000/api/trainer/2/`

### Response

    HTTP 200 OK
    Content-Type: application/json
    {
      "id": 2,
      "is_removed": false,
      "created": "2022-09-25T00:59:35.196956-05:00",
      "modified": "2022-09-25T00:59:35.196956-05:00",
      "name": "Alberto"
    }
    
## Get a non-existent Trainer

### Request

`GET /api/trainer/id/`

**Example** `http://localhost:8000/api/trainer/0/`

### Response

    HTTP 404 Not Found
    Content-Type: application/json
    {
      "detail": "No encontrado."
    }

## Create new Trainer

### Request

`POST /api/trainer/`

**Example** `http://localhost:8000/api/trainer/` with `form-data = {"name": "Ramon"}`

### Response

    HTTP 201 Created
    Content-Type: application/json

    {
        "id": 5,
        "is_removed": false,
        "created": "2022-09-25T19:22:24.117499-05:00",
        "modified": "2022-09-25T19:22:24.117499-05:00",
        "name": "Ramon"
    }
 
## Update Trainer

### Request

`PUT /api/trainer/id/`

**Example** `http://localhost:8000/api/trainer/5/` with `form-data = {"name": "Ramon Jimenez"}`

### Response

    HTTP 200 OK
    Content-Type: application/json

    {
        "id": 5,
        "is_removed": false,
        "created": "2022-09-25T19:22:24.117499-05:00",
        "modified": "2022-09-25T19:24:08.274561-05:00",
        "name": "Ramon Jimenez"
    }

## Delete Trainer

### Request

`DELETE /api/trainer/id/`

**Example** `http://localhost:8000/api/trainer/5/`

### Response

    HTTP 204 No Content
    Content-Type: application/json
    
## Get list of Teams

### Request

`GET /api/team/`

**Example** `http://localhost:8000/api/team/`

### Response

    HTTP 200 OK
    Content-Type: application/json
    [
        {
          "id": 4,
          "is_removed": false,
          "created": "2022-09-25T16:01:42.261619-05:00",
          "modified": "2022-09-25T16:01:42.261619-05:00",
          "name": "Nuevo",
          "trainer": 2,
          "pokemons": []
      },
      ...
    ]
 
## Get a specific Team

### Request

`GET /api/team/id/`

**Example** `http://localhost:8000/api/team/4/`

### Response

    HTTP 200 OK
    Content-Type: application/json
    {
      "id": 4,
      "is_removed": false,
      "created": "2022-09-25T16:01:42.261619-05:00",
      "modified": "2022-09-25T16:01:42.261619-05:00",
      "name": "Nuevo",
      "trainer": 2,
      "pokemons": []
    }
    
## Get a non-existent Team

### Request

`GET /api/team/id/`

**Example** `http://localhost:8000/api/team/0/`

### Response

    HTTP 404 Not Found
    Content-Type: application/json
    {
      "detail": "No encontrado."
    }

## Create new Team

### Request

`POST /api/team/`

**Example** `http://localhost:8000/api/team/` with `form-data = {"name": "Dinamita", "trainer": 2, "pokemons": 3, "pokemons": 4}`

### Response

    HTTP 201 Created
    Content-Type: application/json

    {
      "id": 7,
      "is_removed": false,
      "created": "2022-09-25T19:31:11.505575-05:00",
      "modified": "2022-09-25T19:31:11.505575-05:00",
      "name": "Dinamita",
      "trainer": 2,
      "pokemons": [
          3,
          4
      ]
  }
  
## Create Team with more than 6 pokemons

### Request

`POST /api/team/`

**Example** `http://localhost:8000/api/team/` with `form-data = {"name": "Forbidden", "trainer": 2, "pokemons": 1, "pokemons": 2, "pokemons": 3, "pokemons": 4, "pokemons": 5, "pokemons": 6, "pokemons": 7}`

### Response

    HTTP 400 Bad Request
    Content-Type: application/json

    {
        "pokemons": [
            "Max 6 pokemons allowed"
        ]
    }
 
## Update Team

### Request

`PUT /api/team/id/`

**Example** `http://localhost:8000/api/team/7/` with `form-data = {"name": "Dinamita Modified", "trainer": 2, "pokemons": 3}`

### Response

    HTTP 200 OK
    Content-Type: application/json

    {
        "id": 7,
        "is_removed": false,
        "created": "2022-09-25T19:31:11.505575-05:00",
        "modified": "2022-09-25T19:33:08.823635-05:00",
        "name": "Dinamita Modified",
        "trainer": 2,
        "pokemons": [
            3
        ]
    }

## Delete Team

### Request

`DELETE /api/team/id/`

**Example** `http://localhost:8000/api/team/7/`

### Response

    HTTP 204 No Content
    Content-Type: application/json
