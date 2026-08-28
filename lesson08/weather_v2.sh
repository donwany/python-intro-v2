#!/bin/bash

API_KEY=""
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