# ezBlog
An easy Blog written by python, flask, flask-blogging and using maupassant theme.

## How to use
0. virtualenv is recommanded.

1. install requirements
  ```
  pip install -r requirements.txt
  ```

2. create user
  ```
  python manage_user.py <command> <username> <password>

  command: create or delete
  ```

3. start the app
  ```
  python ezBlog.py (or you can make it run in background)
  ```

4. login and write blog  
  Open {{app.config["BLOGGING_SITEURL"]}}/login/ and input your username and password
  ({{app.config["BLOGGING_SITEURL"]}} is set in ezBlog.py)

5. Enjoy it!
