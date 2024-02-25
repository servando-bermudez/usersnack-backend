# Usersnap Assessment Backend

## Description

Usersnap is trying to expand to new markets and will therefore be opening up a pizza delivery
service next year. The project name of this endeavor is »Usersnack«. As a first step, the web-
application has the following views:

- Pizzas Overview
  List all the available Pizzas

- Pizza Detail View
  Detail view of the Pizza. You should be able to select multiple extras from the list before
  ordering (see the attached data.json file for available extras). You should calculate the final
  price and be able to order.

## The Mission (Accepted)

Your mission applicant, should you decide to accept it, is to build the backend API for this
application – your solution should include interactions with a database of your choosing.
Please also include documentation on how to use your api.
Ideally, we can check out your api somewhere on the internet.

View the given wireframes as a rough outline of functionality and content. It's up to you how
the end result looks, feels and works. We appreciate creative solutions. The Usersnap
technology stack is Python on the backend and ReactJS on the frontend. Please use a
technology stack that you’re comfortable with, since the technical interview includes live
coding, where you’ll add a very small feature to your existing codebase.
Expect your code to be reviewed as if we would want to check it into our codebase.

### Dataset Example

```json
{
  "pizzas": [
    {
      "name": "Cheese & Tomato",
      "price": 11.9,
      "ingredients": ["tomato", "cheese"],
      "img": "cheesetomato.jpg"
    },
    {
      "name": "Mighty Meaty",
      "price": 16.9,
      "ingredients": [
        "tomato",
        "pepperoni",
        "ham",
        "onion",
        "mushrooms",
        "sausage"
      ],
      "img": "mighty-meaty-pizza.jpg"
    },
    {
      "name": "Pepperoni Passion",
      "price": 16.9,
      "ingredients": ["tomato", "pepperoni", "cheese"],
      "img": "pepperoni-passion-pizza.jpg"
    },
    {
      "name": "Texas BBQ",
      "price": 16.9,
      "ingredients": [
        "bbq sauce",
        "bacon",
        "onion",
        "roast chicken",
        "green peppers"
      ],
      "img": "texas-bbq-pizza.jpg"
    },
    {
      "name": "Vegi Supreme",
      "price": 16.9,
      "ingredients": ["tomato", "onion", "green peppers", "mushrooms"],
      "img": "vegisupreme-pizza.jpg"
    },
    {
      "name": "American Hot",
      "price": 15.9,
      "ingredients": ["tomato", "onion", "pepperoni", "jalapeno"],
      "img": "ahot_thumbnail.jpg"
    },
    {
      "name": "Chicken and Rasher Bacon",
      "price": 16.9,
      "ingredients": ["tomato", "chicken breast", "bacon", "onion"],
      "img": "CHICKEN_RASHER_BACON.jpg"
    },
    {
      "name": "Chicken Feast",
      "price": 15.9,
      "ingredients": ["tomato", "chicken", "mushrooms"],
      "img": "chickenfeast.jpg"
    },
    {
      "name": "Four Vegi",
      "price": 15.9,
      "ingredients": ["tomato", "spinach", "onion", "mushrooms"],
      "img": "FourVegi.jpg"
    },
    {
      "name": "Hot & Spicy",
      "price": 15.9,
      "ingredients": ["tomato", "onion", "beef", "green peppers", "jalapeno"],
      "img": "hot-n-spicy-pizza.jpg"
    },
    {
      "name": "Meateor",
      "price": 16.9,
      "ingredients": [
        "bbq sauce",
        "cheese",
        "pork meatballs",
        "sausage",
        "pepperoni",
        "bacon"
      ],
      "img": "meateor.jpg"
    },
    {
      "name": "New Yorker",
      "price": 16.9,
      "ingredients": ["tomato", "pepperoni", "bacon", "mushrooms"],
      "img": "new-yorker.jpg"
    },
    {
      "name": "Tandoori Hot",
      "price": 16.9,
      "ingredients": [
        "tomato",
        "chicken",
        "onion",
        "green peppers",
        "jalapeno"
      ],
      "img": "tandoori-hot-pizza.jpg"
    },
    {
      "name": "The Sizzler",
      "price": 16.9,
      "ingredients": [
        "tomato",
        "garlic sauce",
        "onion",
        "pepperoni",
        "jalapeno",
        "green peppers"
      ],
      "img": "TheSizzler80x56.jpg"
    }
  ],
  "extras": [
    { "name": "ham", "price": 2 },
    { "name": "onion", "price": 1 },
    { "name": "bacon", "price": 2 },
    { "name": "cheese", "price": 1.4 },
    { "name": "green peppers", "price": 1.2 },
    { "name": "mushrooms", "price": 1.2 }
  ]
}
```

## Live Documentation

For a Live example of this backend running please go to [Redoc OpenAPI Documentation](https://usersnackbackend.applikuapp.com/documentation/schema/redoc/)

From there you can download the Schema and import it in Postman or any suit of your choice.

A raw way of testing the endpoints is going directly to the endpoint of your choice and an interactive view will present.

Example: [List Pizza](https://usersnackbackend.applikuapp.com/pizzas/)

## There's no fun on seeing just plain old data

There's a Frontend connected to all this at [Usersnacks](https://usersnackfrontend.applikuapp.com/)

## Setup Instructions

This is a Django Project with a Docker set up for local development

### Environment Variables

```base
DJANGO_SECRET_KEY=supersecretekey
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost


# Database Settings
DATABASE_URL=postgres://random-user:random-password@postgres-database:5432/usersnacks-db
CONN_MAX_AGE=60
POSTGRES_USER=random-user
POSTGRES_PASSWORD=random-password
POSTGRES_DB=usersnacks-db

# Redis Settings
REDIS_URLS=redis://redis-database:6379/0

# Celery Settings
CELERY_BROKER_URL=redis://redis-database:6379/0
```

### Installation

This command will install all the necessary requirements and install the database volume

```bash
make build
```

### Run Database

This command will initiate the Database.
On the first run given that we've set: `POSTGRES_USER` `POSTGRES_PASSWORD` `POSTGRES_DB` - The database will be created automatically

```bash
make run-databases
```

### Run Migrations

This command will apply those unapplied migrations

```bash
make migrate-python
```

### Load Initial Data

This command will create a Superuser or Admin user so we can have access to the admin panel (not needed for the usage of the overall app).

Then, it'll create the initial data based on the Dataset example from above.

Note: This command will only create the initial data once, if it finds there's already data in the database will skip the process.

```bash
make load-initial-data
```

### Run Server

```bash
make run-server
```

### Additional Commands

For more commands please refer to the [Makefile](Makefile)
