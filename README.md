# Information

This is a minimal django app, replicating stack exchange
## Files and Directory Structure

- **website**: main django project directory
- **posts**: reusable django app that display posts
- **other**: contains python code to injest given xml data into db.sqlite3

## Dependency
- sqlite3
- libsqlite3-dev
- python3

## Setup

- `$ git clone https://github.com/AkashDhiman/django-app.git`
- `$ cd django-app`
- `$ pip3 install -r requirements.txt`
- `$ python3 manage.py migrate`
- `$ python3 other/xml-to-sqlite.py`
- `$ python3 manage.py runserver`
- now head over to `127.0.0.1:8000/posts/` to see list of posts
- you may click on any of the post to view them in detail
- you can also search using the options provided on the same page.
- These search parameter work with GET request the parameters being
  - order = [creation-date, score, view-count]
  - body = [search string for body]
  - title = [search string for title]


## Other Information
- The code has been design to avoid xss attack by using bleach, during rendering of html content
- /posts/search/ is another url that provides search functionality, it works by redirecting to index and doesn't display the posts
