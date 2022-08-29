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