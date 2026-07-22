import sys
import pandas as pd

def add(a, b):
    """add two numbers"""
    return a + b 


# df_sales = pd.read_csv("sales.csv")
# df_data = pd.read_csv("data.csv")


if __name__ == "__main__":

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    
    filename = str(sys.argv[3])
    algorithm = str(sys.argv[4])

    if algorithm == "random_forest":
        print("training random forest model")
    elif algorithm == "xgboost":
        print("training xgboost model")
    elif algorithm == "logistic_regression":
        print("training logistic regression model")

    df_sales = pd.read_csv(filename)
    results = add(a, b)

    print(f"total sum is: {results}")
    print(f"yours sales data: {df_sales.head()}")