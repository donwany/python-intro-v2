
#!/bin/bash

uv run 2_example.py 1000 50 data.csv xgboost

uv run 2_example.py 100 50 sales.csv random_forest

uv run 2_example.py 10 50 data.csv logistic_regression