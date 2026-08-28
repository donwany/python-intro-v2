# 🍽️ The Restaurant Analogy for APIs

- **You (the customer)** → the client (your app or code)  
- **The kitchen (chef)** → the server (where data or functionality lives)  
- **The waiter** → the API  

---

## 🧑‍🍳 What’s happening behind the scenes?

You don’t walk into a restaurant and go straight into the kitchen to cook your own food, right?

Instead:

1. **You look at the menu**  
   → This is like reading API documentation (what options are available)

2. **You tell the waiter your order**  
   → This is your API request

3. **The waiter takes your request to the kitchen**  
   → The API sends your request to the server

4. **The kitchen prepares your food**  
   → The server processes your request

5. **The waiter brings your food back**  
   → The API returns a response

---

## 🔑 Key Insight

The **waiter (API)**:

- Knows what you’re allowed to ask for  
- Knows how to talk to the kitchen  
- Brings back only what you requested  

You never deal with:

- How the food is cooked (internal logic)  
- Where ingredients come from (databases)  

---

## 🧾 Example in Tech Terms

Let’s say you're using a weather app:

1. **You (client)** ask: *“What’s the weather in Dallas?”*  
2. **API (waiter)** sends request to weather server  
3. **Server** processes it  
4. **API returns**: *“75°F, sunny”*

---

## 📌 1. What is a REST API?

A RESTful API is an Application Programming Interface that adheres to the design principles of the **REpresentational State Transfer (REST)** architectural style. It provides a standardized and flexible way for different software systems (clients and servers) to communicate with each other over the internet, typically using HTTP protocol.

   - Roy Fielding during his PhD dissertation
   - RESTful - "following the REST principles"
---
## Core Concepts

### 🔹 Resources and URLs
In a REST API, data and functionality are considered **resources**, each identified by a unique Uniform Resource Locator (URL).

- `https://elbowpay.com/users` → collection of users  
- `https://elbowpay.com/users/123` → specific user  

---
### 🔹 HTTP Methods
The API uses standard HTTP methods to perform actions on these resources:

| Method  | Description                                     |
|---------|-------------------------------------------------|
| `GET`   | Retrieves data from the server (Read)           |
| `POST`  | Sends data to create a new resource (Create)    |
| `PUT`   | Updates an existing resource completely (Update)|
| `DELETE`| Removes a resource from the server (Delete)     |
| `HEADERS` | Get header information                        |
| `OPTIONS` | Get options available (GET, POST, etc)        |

`PATCH` - Update specific resource

CRUD (Create, Read, Update and Delete)

A RESTful API might look like:

  - GET https://api.elbowpay.com/users → get all users
  - GET https://api.elbowpay.com/users/1 → get user with ID 1
  - POST https://api.elbowpay.com/users → create a user
  - DELETE https://api.elbowpay.com/users/1 → delete user
---

### 🔹 Representations
The server sends a representation of the resource’s state to the client.

Common formats:
- JSON (most popular)
- XML

---
### 🔹 Statelessness
Each request from the client must contain **all the information needed** to process it.

- No session is stored on the server  
- Improves **scalability**  
- Improves **reliability**

## API clients
 - POSTMAN (https://www.postman.com/downloads)
 - INSOMNIA (https://insomnia.rest/download)
 - HTTPie (https://httpie.io/download)
 - SOAPUI (https://www.soapui.org/)
 - SWAGGER (https://swagger.io)

---

## Pretty Print
```python

from pprint import pprint

data = {
    'name': 'Alice',
    'age': 30,
    'children': [
        {'name': 'Bob', 'age': 10},
        {'name': 'Charlie', 'age': 8}
    ],
    'metadata': {'location': 'USA', 'status': 'active', 'tags': ['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6', 'tag7', 'tag8']}
}

print("--- Standard print() output ---")
print(data)

print("\n--- Pretty print() output (default) ---")
pprint(data)

```



## Install Usage:
```bash
pip install requests, httpx
```

## Using Curl

```bash
# -X (-X POST- Specifies HTTP method)
# -H (-H "Content-Type: application/json")
# -d (Data payload (body))

# GET
curl https://jsonplaceholder.typicode.com/posts
curl GET https://jsonplaceholder.typicode.com/posts
curl -X GET https://jsonplaceholder.typicode.com/posts

# POST
curl -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Post",
    "body": "Hello from curl",
    "userId": 1
}'

# PUT (Replace)
curl -X PUT https://jsonplaceholder.typicode.com/posts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "title": "Updated Title",
    "body": "Full replacement",
    "userId": 1
}'

# PATCH (Partial Update)
curl -X PATCH https://jsonplaceholder.typicode.com/posts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Patched Title"
}'

# DELETE
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1

```

## USING HTTPie DEMO
```bash
# pip install httpie

# GET
http GET https://jsonplaceholder.typicode.com/posts

# POST
http POST https://jsonplaceholder.typicode.com/posts \
  title="My Post" \
  body="Hello from curl" \
  userId:=1

# PUT
http PUT https://jsonplaceholder.typicode.com/posts/1 \
  id:=1 \
  title="Updated Title" \
  body="Full replacement" \
  userId:=1

# PATCH
http PATCH https://jsonplaceholder.typicode.com/posts/1 \
  title="Patched Title"

# DELETE
http DELETE https://jsonplaceholder.typicode.com/posts/1
```

## Query Params with Pagination
- curl "URL?key=value&key2=value2"
```python
# https://jsonplaceholder.typicode.com/users?page=1&limit=10
# https://jsonplaceholder.typicode.com/posts?page=1&limit=5
# https://developers.openai.com/api/docs/quickstart?lang=python&language=python

# GET https://api.elbowpay.com/v1/users?age=20&gender=male&page=1&limit=10

# curl "https://jsonplaceholder.typicode.com/posts?page=1&limit=5"
# curl -s "https://jsonplaceholder.typicode.com/posts?page=1&limit=5" | jq
# curl -s "https://jsonplaceholder.typicode.com/users?website=conrad.com&page=1&limit=5" | jq
# curl -s "https://jsonplaceholder.typicode.com/users?address.city=Bartholomebury&page=1&limit=5" | jq

# bash
#!/bin/bash

BASE_URL="https://jsonplaceholder.typicode.com/posts"
LIMIT=5
read -p "Enter page number: " PAGE
curl -s "$BASE_URL?page=$PAGE&limit=$LIMIT" | jq


# python
import requests
url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "page": 1,
    "limit": 5
}

response = requests.get(url, params=params)
data = response.json()

for post in data:
    print(post["id"], post["title"])
```



## Mini Curl Demo Script
```bash
API_KEY="9492a5a5e25c5a5bcc09e1941f9fecef"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

CITY="Dallas"

curl -X GET "$BASE_URL?q=$CITY&appid=$API_KEY&units=metric"

# 🧠 3. Pretty Print JSON (Using jq)
# brew install jq     # mac
curl "$BASE_URL?q=Dallas&appid=$API_KEY&units=metric" | jq

# 🎯 4. Extract Specific Fields (CLI Power 💪)
curl -s "$BASE_URL?q=Dallas&appid=$API_KEY&units=metric" | jq '
{
  city: .name,
  temperature: .main.temp,
  condition: .weather[0].description
}'
```

# 🖥️ 5. Build a Mini CLI Script (Bash Version)
```bash
#!/bin/bash

API_KEY="YOUR_API_KEY"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

while true; do
    read -p "Enter city (or 'exit'): " city

    if [[ "$city" == "exit" ]]; then
        echo "Goodbye!"
        break
    fi

    response=$(curl -s "$BASE_URL?q=$city&appid=$API_KEY&units=metric")

    city_name=$(echo "$response" | jq -r '.name')
    temp=$(echo "$response" | jq -r '.main.temp')
    desc=$(echo "$response" | jq -r '.weather[0].description')

    echo "📍 City: $city_name"
    echo "🌡️ Temp: $temp °C"
    echo "☁️ Condition: $desc"
done

```

## PART 0
```python
# http://ip-api.com/json/99.48.1.100
import requests

url = 'http://ip-api.com/json/'

response = requests.get(url).json()

print(response['city'])
```


## 🟢 PART 1
    - 🌍 Get Location from IP
```python
import requests
import json

def get_location():
    url = 'http://ip-api.com/json/'
    
    response = requests.get(url)
    data = response.json()

    print("Raw Response:")
    print(data)

    print("\nKey-Value Pairs:")
    for key, value in data.items():
        print(f"{key} -- {value}")

    print("\nFormatted JSON:")
    print(json.dumps(data, indent=2))

    print(f"\n📍 You Are In This City: {data['city']}")

if __name__ == "__main__":
    get_location()
```

## 🔵 PART 2 — Understanding HTTP Methods (Using Fake API)
    - GET (Retrieve Data)
    - https://jsonplaceholder.typicode.com/
```python
import requests

def get_posts():
    # url = https://jsonplaceholder.typicode.com/comments
    # url = https://jsonplaceholder.typicode.com/albums
    # url = https://jsonplaceholder.typicode.com/todos
    # url = https://jsonplaceholder.typicode.com/users
    # url = https://jsonplaceholder.typicode.com/photos

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    data = response.json()

    print(f"Total posts: {len(data)}")
    print("First post:")
    print(data[0])

get_posts()
```

## 🟡 POST (Create Data)
    - POST (Create Data)
```python
import requests

def create_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    new_post = {
        "title": "My First API Post",
        "body": "This is created using Python",
        "userId": 1
    }

    response = requests.post(url, json=new_post)

    print("Status Code:", response.status_code)
    print("Response:", response.json())

create_post()
```

## 🔵 PUT (Replace Entire Resource)
```python
def update_post_put():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    updated_post = {
        "id": 1,
        "title": "Updated Title",
        "body": "Completely replaced content",
        "userId": 1
    }

    response = requests.put(url, json=updated_post)

    print("Updated (PUT):", response.json())

update_post_put()
```
## 🟣 PATCH (Update Part of Resource or Partial Update)
```python
def update_post_patch():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    partial_update = {
        "title": "Patched Title Only"
    }

    response = requests.patch(url, json=partial_update)

    print("Updated (PATCH):", response.json())

update_post_patch()
```

## 🔴 DELETE (Remove Data)
```python

def delete_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.delete(url)

    print("Status Code:", response.status_code)
    print("Post deleted!")

delete_post()
```

## 🌦️ PART 3 — REAL API (OpenWeatherMap)
 - 📌 Step 1: Get API Key
 - Go to: https://openweathermap.org/api
    - ✅ 3. Status Codes:
        - Code	    - Meaning
        - 200	    - Success
        - 201	    - Created
        - 404	    - Not Found
        - 500	    - Server Error

```python
import requests

API_KEY = ""

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"\n🌍 City: {data['name']}")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"☁️ Weather: {data['weather'][0]['description']}")
    elif response.status_code != 200:
        print("Something went wrong!")
    else:
        print("Error:", data)

if __name__ == "__main__":
    # city = input("Enter city: ")
    cities = ["Dallas", "London", "Tokyo"]
    for city in cities:
        get_weather(city)
```

## 🌦️ Mini Project: Build a Weather CLI App (Real-World API)
```
🎯 Project Goal
    1 . Build a Command-Line Weather App that:
    2. Takes a city as input
    3. Fetches weather data from OpenWeatherMap
    4. Displays clean, formatted output

🏗️ Project Structure
    weather-cli/
    │── weather.py
    │── .env
    │── utils.py

🔑 Step 1 — Get API Key
 - https://home.openweathermap.org/api_keys
```

## Solution
```python
# ⚙️ Step 2 — .env
# .env

# API_KEY = "YOUR_API_KEY"
# BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# 🧠 Step 3 — Utility Functions
# utils.py

def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit_temp):
  celsius_temp = (fahrenheit_temp - 32) * 5/9
  return celsius_temp


def format_weather(data):
    city = data["name"]
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return {
        "city": city
        "temperature": temp
        "condition": desc
    }

# 🚀 Step 4 — Main CLI App
# weather.py

import os
import requests
from utils import format_weather, kelvin_to_celsius, celsius_to_fahrenheit, fahrenheit_to_celsius
from dotenv import load_dotenv

load_dotenv(".env", override=True)

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code != 200:
            print("❌ Error: City not found or API issue")
            return

        data = response.json()
        kelvin_temp = format_weather(data)

    except requests.exceptions.RequestException as e:
        print("❌ Network error:", e)


def main():
    print("🌦️ Weather CLI App")
    print("----------------------")

    while True:
        city = input("\nEnter city (or 'exit'): ")

        if city.lower() == "exit":
            print("👋 Goodbye!")
            break

        # save history to file
        with open("history.txt", "a") as f:
            f.write(city + "\n")

        get_weather(city)


if __name__ == "__main__":
    main()

# ▶️ Step 5 — Run It
# python weather.py
# uv run weather.py

```

## Bearer Token Demo
 - 🚀 Real-World APIs That Use Bearer Tokens
   - GitHub
   - Stripe
   - OpenAI
   - Anthropic
   - Google

```bash
# ENDPOINT: https://api.github.com/user
# Use: https://reqres.in/

export GITHUB_TOKEN=YOUR_GITHUB_TOKEN

http GET https://api.github.com/user Authorization:"Bearer $GITHUB_TOKEN"

# get user 
curl -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/user

# httpie POST
http POST https://api.github.com/user/repos \
  Authorization:"Bearer $GITHUB_TOKEN" \
  name="my-api-repo_v2" \
  private:=false

# CURL - create repo
curl -X POST https://api.github.com/user/repos \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-api-repo_v10",
    "private": false
}'

# create issues
curl \
--request POST \
--url "https://api.github.com/repos/donwany/my-api-repo_v10/issues" \
--header "Accept: application/json" \
--header "Authorization: Bearer $GITHUB_TOKEN" \
--data '{
  "title": "Created with the REST API",
  "body": "This is a test issue created by the REST API"
}'

# delete repo
curl -X DELETE 'https://api.github.com/repos/donwany/my-api-repo_v6' \
--header 'Authorization: Bearer $GITHUB_TOKEN' \
--header 'Content-Type: application/json'

# get issues
curl -X GET 'https://api.github.com/repos/donwany/my-api-repo_v10' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer $GITHUB_TOKEN' > issues.json



# Python
import requests

url = "https://api.github.com/user"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
response = requests.get(url, headers=headers)
print(response.json())

```

## 🤖 OpenAI API
    - 🔐 1. Set Your API Key
    - ENDPOINT: https://api.openai.com/v1/models

```bash
export OPENAI_API_KEY="your_api_key_here"

# httpie
http GET https://api.openai.com/v1/models Authorization:"Bearer $OPENAI_API_KEY"
# curl
curl https://api.openai.com/v1/models -H "Authorization: Bearer $OPENAI_API_KEY"


http POST https://api.openai.com/v1/chat/completions \
  Authorization:"Bearer $OPENAI_API_KEY" \
  Content-Type:application/json \
  model="gpt-4o-mini" \
  messages:='[
    {"role": "user", "content": "Explain REST APIs in simple terms"}
  ]'


curl -X POST https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [
      {"role": "user", "content": "Explain REST APIs in simple terms"}
    ]
}'

```

```python
# pip install openai
# https://developers.openai.com/api/docs/quickstart
# https://developers.openai.com/api/docs/quickstart?lang=python&language=python

export OPENAI_API_KEY="your_api_key_here"

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5.4",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)

```

## Anthropic
 - Get API keys: https://platform.claude.com
 - Documentation: https://platform.claude.com/docs/en/get-started
```python
export ANTHROPIC_API_KEY='your-api-key-here'

curl https://api.anthropic.com/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 1000,
    "messages": [
      {
        "role": "user",
        "content": "What should I search for to find the latest developments in renewable energy?"
      }
    ]
  }'


# pip install anthropic

import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What should I search for to find the latest developments in renewable energy?",
        }
    ],
)
print(message.content)

```



## Ollama
 - Do a demo on ollama
```bash
https://github.com/ollama/ollama-python
https://github.com/ollama/ollama/blob/main/docs/api.md
```

## Libraries
    - Flask
    - FastAPI
    - Curl

## 📌 2. Building a REST API with Flask
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
items = []

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    items.append(data)
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)
```

## 📌 3. Building a REST API with FastAPI
```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

items = []
@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=1957, debug=True)
```

## References
 - https://github.com/public-apis/public-apis
 - https://ip-api.com/docs/api:json#test
 - github.com/public-apis/public-apis?tab=readme-ov-file