# Thought Process

By reading this, you get to know the following:
- How I broke down the challenge into tasks and sub-tasks
- Why I did something a particular way
- Design Patterns I used and where I used them
- How I structured the code and db design
- Why I chose a particular package, framework or architectural style


## Breakdown of the Challenge
This is a high-level breakdown of the tasks performed to accomplish this challenge.

**NB:** the tasks here can still be broken down to sub tasks.

1. Build a simple SDK for Hacker news API
2. Design the database schema
3. Setup Django Project
4. API development
5. Project documentation and API documentation

### 1. Simple SDK
Calling Hacker news API endpoints within views, tasks and every other place isn't really cool and can become too repetitive. I created a simple SDK for the API . The simple SDK acts as a wrapper to the API calls. It offers the following benefits:
- being able to extend the API functionality.
- handle error appropriately.
- abstract away the API endpoints into methods.
etc

### 2. Database Design
![Database Design Schema](/docs/db.jpg)

The image above is the "ERD + pseudo UML" diagram of the db tables generated using [draw.io](https://draw.io)

After performing the following actions:
- going through Hacker news API [docs](https://hackernews.api-docs.io/)
- studying the schema of the items
- considering the relationships that exist between the items as mentioned in challenge question and 
- analyzing the API response.

I came up with the above design.

### 3. Django Project
Went with the [django](https://django.org) framework as required in the challenge.
##### Logging
Setup logging in order to make tracking task progress and detecting bugs easy.

#### Implement DB Design
Using the "ERD + Pseudo UML" diagram shown in the previous section, suitable models corresponding to the "ERD + pseudo UML" diagram was implemented using django models. The inheritance indicated in the diagram was also considered by taking advantage of abstract django model inheritance.

#### Seeding DB
As mentioned in the challenge, I created utility functions and a custom  management command (named `populate_db`) to populate the db with 100 new items from hacker news.
#### Pages views
I created three views functions.
- Home - represent home page view, list all items in db, support filtering based on item type.
- Detail - retrieve a single item based on the id from hacker news.
- Search - search all items based on the  content of `text` attribute of the item.

The data obtained from these views are displayed using their respective html template files.

#### Periodic Task Setup
Celery was used for scheduling.

### 4. API DEVELOPMENT
Just to mention, [GraphQL](https://graphql.org/) API architectural style is the most suitable style to use considering the model. Using GraphQL helps avoid over-fetching and under-fetching of data. This is really useful here. because not all the fields of each item will be needed for some API call. For instance, the kids field is kinda too large at times which may delay response from the api.

Since the API architectural style wasn't specified, I added support for the REST and GraphQL

**NB:** List API endpoints (i.e collections) are paginated.

### 5. Project Documentation and API DOCUMENTATION