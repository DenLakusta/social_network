# Social network test task

Object of this task is to create a simple REST API.<br />

**Requirements and used technologies:**
 1. **djangorestframework** - base framework
 2. **djangorestframework-simplejwt** - package for JWT tokens implementation  
 3. **drf-yasg** - package for swagger creation
 4. **psycopg2-binary** - for using PostgreSQL
 5. **python-dotenv** - package to use enviroment variables (DB credentials and other secrets) 
 6. **django-filter** - packeage for creating custom filters
 
 All requirement are stored in requirements.txt file
 
 Clone the repository, start virtualenv enviroment, activate it and install requirements


```pip install -r requirements.txt```

PostgreSQL server should be started and configured for using API.
Database credentials and Django **SECRET_KEY** should be saved in **.env** file



.env file example:<br />
```export SECRET_KEY='your_key'```<br />
```export DB_NAME=name_of_db```<br />
```export DB_USER=your_user```<br />
```export DB_PASSWORD=your_password```<br />
```export DB_HOST=host(localhost for local usage)```<br />
```export DB_PORT=5432```


### Basic Features:

user signup: ```http://127.0.0.1:8000/api/users/signup/```(JWT token will be recieved in response)<br />
user login: ```http://127.0.0.1:8000/api/token/```(JWT token will be recieved in response)<br />
post creation: ```http://127.0.0.1:8000/api/posts/post/create/```<br />
post like: ```http://127.0.0.1:8000/api/likes/like/1/``` (1 - post id)<br />
post unlike: ```http://127.0.0.1:8000/api/likes/unlike/1/```<br />
likes analytics: ```http://127.0.0.1:8000/api/users/like_analytics/?date_start=2020-05-23&date_to=2020-05-26```<br />
current user activity: ```http://127.0.0.1:8000/api/users/last_activity/```<br />
swagger url: ```http://127.0.0.1:8000/swagger/```<br />
