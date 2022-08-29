# HackerNews Challenge
## About
The goal is to make a web app to make it easier to navigate the news:

Make a scheduled job to sync the published news to a DB every 5 minutes. You can start with the latest 100 items, and sync every new item from there. Note: there are several types of news (items), with relations between them;
Implement a view to list the latest news;
Allow filtering by the type of item;
Implement a search box for filtering by text;
As there are hundreds of news you probably want to use pagination or lazy loading when you display them.
It is also important to expose an API so that our data can be consumed:

GET  : List the items, allowing filters to be specified;
POST  : Add new items to the database (not present in Hacker News);

Only display top-level items in the list, and display their children (comments, for example) on a detail page;
In the API, allow updating and deleting items if they were created in the API (but never data that was retrieved from Hacker News);
## Documentation
> You can read about my thought process and code documentation [here](/docs/)

## Local Development Setup
1. Download / Clone the repo to your PC
2. Create a virtual environment.

In the root directory of the repo folder, perform the following steps
3. Install the project dependencies in the virtual environment.
If you have [`pipenv`](https://pipenv.pypa.io/en/latest/) installed, you can simply run
```
pipenv install
```
**NB:** Add value to the env var in the .env.sample and rename it to .env
4. Activate the virtual environment, and run this command in the terminal to seed the db with 100 latest items from hackernews
```
python manage.py populate_db
```
5. Start Redis server
```
redis-server
```

**NB:** Redis was setup as the message broker in the project configuration. It is important you have a message broker setup for celery to work.
6. Create one or two new terminal to start the celery worker and celery beat
### Specific for  windows OS
```
One terminal for worker
celery -A config worker -l INFO --pool=solo

Another terminal for beat
celery -A config beat -l INFO
```

### Other OS
```
For worker
celery -A config worker -l INFO
```

### To start Worker and Beat together in one terminal
```
celery -A core worker -B -l INFO
```
7. Start the development server by running and access it at http://127.0.0.1:8000/
```
python manage.py runserver
```
### http://127.0.0.1:8000/
The home list all items - story, comment, job, poll, option
You can filter specific item type by clicking the item type in the nav bar
A search box that allow filtering by all item by  their text field.

### http://127.0.0.1:8000/<hnid>
The detail page for item whose id from hacker news is passed in the url. Show their kids if they have saved to or available in the db.

### http://127.0.0.1:8000/graphql
Displays GraphiQL API browser for running the graphql queries

The below urls are RESTful API endpoints to create and list item. They support 
- GET
- POST
### http://127.0.0.1:8000/api/v1/stories
### http://127.0.0.1:8000/api/v1/comments
### http://127.0.0.1:8000/api/v1/jobs
### http://127.0.0.1:8000/api/v1/polls
### http://127.0.0.1:8000/api/v1/pollopts

The below urls are RESTful API endpoints to create and list item. They support 
- GET
- PATCH
- DELETE
- PUT
### http://127.0.0.1:8000/api/v1/stories/<hnid>
### http://127.0.0.1:8000/api/v1/comments/<hnid>
### http://127.0.0.1:8000/api/v1/jobs/<hnid>
### http://127.0.0.1:8000/api/v1/polls/<hnid>
### http://127.0.0.1:8000/api/v1/pollopts/<hnid>

However, you can't delete items saved from hacker news api. 
Only items created via the api can be deleted.

You can access the swagger API documentation with UI at http://127.0.0.1:8000/doc
You can access the Redoc API documentation with UI at http://127.0.0.1:8000/redoc