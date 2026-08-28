#!/bin/bash 

API_KEY=""

BASE_URL="https://api.openweathermap.org/data/2.5/weather"

CITY="Dallas"

curl -X GET "$BASE_URL?q=$CITY&appid=$API_KEY&units=metric"

curl -X GET "$BASE_URL?q=$CITY&appid=$API_KEY&units=imperial" | jq

curl -s "$BASE_URL?q=Dallas&appid=$API_KEY&units=metric" | jq '
{
  city: .name,
  temperature: .main.temp,
  condition: .weather[0].description
}'