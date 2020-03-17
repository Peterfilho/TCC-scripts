# TCC-scripts

### How to run

run `python3 create_database.py`

>**NOTE**: *to edit database need to edit file `create_database` or if you want to use yourself database
then change the name of this on* `api_main.py`

this will get a `locale.db`

Now you need to run `api_main.py` using `python3 api_main.py
`
### API Resources

**GET all users**
Example
http://127.0.0.1:5000/api/v1/resources/users/all

**GET users by id**
Example:
http://127.0.0.1:5000/api/v1/resources/users?id=1

**GET users by department**
Example:
http://127.0.0.1:5000/api/v1/resources/users?department=COINT

**GET users by role**
Example:
http://127.0.0.1:5000/api/v1/resources/users?role=Professor
