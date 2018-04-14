# Workjapan Task

## How to run in local machine

### Reqirement

* Install [Python 2.7](https://www.python.org/download/releases/2.7/)
* Install pip 
```
sudo apt-get install python-pip python-dev build-essential 
```
* (Optional) Setup [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) 
* Install packages in requirements file
```
pip install -r requirements.txt
```

### Run the project
* python manage.py migrate
* python manage.py runserver


## Create/Update/Delete APIs 

### Create a company (POST)

Request url
```
http://127.0.0.1:8000/create
```

**Request body format (Json)**
```
{
    "city": "Chennai",
    "state": "TN",
    "postal_code": "522212",
    "company_name": "Test Company",
    "locality": "Anna nagar",
    "building_number": "332"
}
```
**Response body if Success**
Response code - 200
Response Type - Json
```
{
    "city": "Chennai",
    "state": "TN",
    "postal_code": "522212",
    "company_name": "Test Company",
    "locality": "Anna nagar",
    "building_number": "332"
}
```
**Response body if any error**
Response code - 400
Response Type - Json
```
{
    "error" : <message>
}
```

### Update a company (PUT)

Request url
```
http://127.0.0.1:8000/update/<company name>
```

**Request body format (Json)**
```
{
    "city": "Chennai",
    "state": "TN",
    "postal_code": "533313",
    "locality": "Anna nagar",
    "building_number": "332"
}
```
**Response body if Success**
Response code - 200
Response Type - Json
```
{
    "city": "Chennai",
    "state": "TN",
    "postal_code": "533313",
    "company_name": "Test Company",
    "locality": "Anna nagar",
    "building_number": "332"
}
```
**Response body if any error**
Response code - 400
Response Type - Json
```
{
    "error" : <message>
}
```

### Delete a company (DELETE)

Request url
```
http://127.0.0.1:8000/delete/<company name>
```

**Request body format**
```
Not required
```
**Response body if Success**
Response code - 200
Response Type - Json
```
{
    "success" : "Company address deleted successfully"
}
```
**Response body if any error**
Response code - 400
Response Type - Json
```
{
    "error" : <message>
}
```

## Access/Retrive company

Request url
```
http://127.0.0.1:8000/filter?<urlparams>
```

Url parameters can single or multiple attributes values to filter the companies. If filter no parameters it return full list.

```
http://127.0.0.1:8000/filter?city=Bangalore&building_number=533313
```

**Response (Json)**
```
{
    "data": [
        {
          ..
        },
        {
          ..
        },
        ..
    ]
}
```

To match similar substring use attribute name ends with **~** symbol. Like company_name~=test

## Unique values

Request url
```
http://127.0.0.1:8000/unique/<attribute>?<urlparams>
```
Expeted url parameters in columns in company model + limit and condition_type.
condition_type if limit is graterthan use 'gt' or lessthan use 'lt' or equals use 'eq'. 
By default limit is 1 and condition_type is 'gt'

**Example**
```
http://127.0.0.1:8000/unique/city?company_name~=test&condition_type=lt&limit=10
```

**Response (Json)**
```
{
    "data": [
        {
            "city": "Bangalore",
            "city_count": 2
        },
        {
            "city": "Hyderabad",
            "city_count": 2
        }
    ]
}
```
