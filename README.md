
# Flask

Flask is a microframework with a very well designed API, designed to provide the minimum amount of functionality that is needed to create web applications.



## Chapter 1: Set up a Flask environment

**Pip basics:**  
- To install a package with pip: ```$ pip install [package-name]```

- If you want to remove a package that you are no longer using: ```$ pip uninstall [package-name]```

- Find a package: ```$ pip search [search-term]```

- Create a list of packages: ```$ pip freeze > requirements.txt ```

- To install all the packages from this file: ```$ pip install -r requirements.txt ```

- Create a python 3 virtualenv: ```$ python3 -m venv env```

- Install virtualenv: ```pip install virtualenv ```

- Activate virtual environment: ```$ source env/bin/activate ``` 

## Chapter 2: Creating Models with SQLAlchemy

Data is stored and retrieved from a **relational database management system** (RDBMS).  
In order to create models on top of our database, we will use a Python package named **SQLAlchemy**

**Setting up SQLAlchemy**  
Flask SQLAlchemy can be used with multiple database engines, such as ORACLE, MSSQL, MySQL, PostgreSQL, SQLite, and Sybase, but we need to install additional specific packages for these engines. 
```
# MySQL: PyMySQL
# Postgres: psycopg2
# MSSQL: pyodbc
# Oracle: cx_Oracle 
``` 

**CRUD**

In every storage mechanism for data, there are four basic types of functions: create, read, update, and delete (CRUD).  
These allow us to perform all the basic ways of manipulating and viewing the data that is needed for our web apps.

To use these functions, we will use an object in the database named a **session**

- Creating models 
```
>>> user = User(username='fake_name')
>>> db.session.add(user)
>>> db.session.commit() 
```
- Reading models 
Data can be queried using **Model.query**. For those who use SQLAlchemy, this is shorthand for db.session.query(Model)  

Use **all()** to get all rows from the user table as a list:
```
>>> users = User.query.all()
``` 

When the number of items in the database increases, this query process becomes slower.
we have the **limit** function to specify the total number of rows
```
>>> users = User.query.limit(10).all()
```
By default, SQLAlchemy returns the records ordered by their primary keys. To control this, we have the **order_by** function
```
# ascending
>>> users = User.query.order_by(User.username).all()
# descending
>>> users = User.query.order_by(User.username.desc()).all() 
``` 

To return just one record, we use **first()** instead of **all()**
```
>>> user = User.query.first() 
>>> user.username 
```

To return one model by its primary key, use **query.get()**
```
>>> user = User.query.get(1) 
>>> user.username 
```

All these functions are chainable:
```
>>> users = User.query.order_by(User.username.desc()).limit(10).first() 
```

The **pagination method** is different from the first() and all() methods because it returns a pagination object rather than a list of models
```
>>> User.query.paginate(1, 10) 
<flask_sqlalchemy.Pagination at 0x105118f50>
```

This object has several useful properties:
```
>>> page = User.query.paginate(1, 10) 
# returns the entities in the page 
>>> page.items [<User 'fake_name'>] 
# what page does this object represent 
>>> page.page 
1 
# How many pages are there 
>>> page.pages 
1 
# are there enough models to make the next or previous page 
>>> page.has_prev, page.has_next (False, False) 
# return the next or previous page pagination object 
# if one does not exist returns the current page 
>>> page.prev(), page.next() 
(<flask_sqlalchemy.Pagination at 0x10812da50>, <flask_sqlalchemy.Pagination at 0x1081985d0>) 
```

- Filtering queries 
Filtering results by a set of rules. To get a list of models that satisfy a set of qualities, we use the **query.filter_by** filter  
To get a list of all users with a username of fake_name
```
>>> users = User.query.filter_by(username='fake_name').all()
```

This example is filtering on one value, but multiple values can be passed to the filter_by filter. Just like our previous functions, filter_by is chainable.
```
>>> users = User.query.order_by(User.username.desc()).filter_by(username='fake_name').limit(2).all() 
```
With common Python types, such as integers, strings, and dates, the == operator can be used for equality comparisons. If you had an integer, float, or date column, an inequality statement could also be passed with the >, <, <=, and >= operators

We can also translate complex SQL queries with SQLAlchemy functions. For example, to use IN, OR, or NOT SQL comparisons
```
>>> from sqlalchemy.sql.expression import not_, or_
>>> user = User.query.filter(User.username.in_(['fake_name']),User.password == None).first()
# find all of the users with a password
>>> user = User.query.filter(not_(User.password == None)).first()
# all of these methods are able to be combined
>>> user = User.query.filter(or_(not_(User.password == None), User.id >= 1)).first() 
```
In SQLAlchemy, comparisons to None are translated to comparisons to NULL.

- Updating models 
To update the values of models that already exist, apply the **update** method to a query object.
```
>>> User.query.filter_by(username='fake_name').update({'password': 'test' }) 
# The updated models have already been added to the session 
>>> db.session.commit()
```

- Deleting models 
```
>>> user = User.query.filter_by(username='fake_name').first() 
>>> db.session.delete(user) 
>>> db.session.commit() 
```

- Relationships between models
Relationships between models in SQLAlchemy are links between two or more models that allow models to reference each other automatically.
 