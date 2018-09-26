# ezBlog
An easy Blog written by python, flask, flask-blogging and using maupassant theme.

## Example
[My blog](https://traceme.space)
### index page
![index](https://github.com/noobcoderT/ezBlog/blob/master/screenshot/index.png)
### post page
![post-1](https://github.com/noobcoderT/ezBlog/blob/master/screenshot/post-1.png)
![post-2](https://github.com/noobcoderT/ezBlog/blob/master/screenshot/post-2.png)
### archives page
![archives](https://github.com/noobcoderT/ezBlog/blob/master/screenshot/archives.png)
### login page
![login](https://github.com/noobcoderT/ezBlog/blob/master/screenshot/login.png)
### writing post page
![write](https://github.com/noobcoderT/ezBlog/blob/master/screenshot/write.png)

## Introduce
[快速搭建属于自己的博客](https://traceme.space/blog/page/1/)

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

3. modify app config  
  app config is mainly in ezBlog.py file. modify app.config["BLOGGING_SITEURL"] to your own site url. and modify app listen ip and port at the bottom.

4. start the app
  ```
  python ezBlog.py (or you can make it run in background)
  ```

5. login and write blog  
  Open app.config["BLOGGING_SITEURL"]/login/ (for example, http://example.com/login/) and input your username and password
  (app.config["BLOGGING_SITEURL"] is set in ezBlog.py)  
  if you want logout, use app.config["BLOGGING_SITEURL"]/logout/ url.

6. Enjoy it!
