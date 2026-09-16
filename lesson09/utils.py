import argparse


def add_tax(fare, tax=0.10):
    return fare * tax


def parser():
    # make use of argparse
    parser = argparse.ArgumentParser(description="Uber Fare Estimator")
    parser.add_argument("--base", "-b", required=False, default=2.5, type=float, help="base fare")
    parser.add_argument("--distance", "-d", required=False, default=100, type=float, help="distance to travel")
    parser.add_argument("--rate", "-r", required=True, type=float, help="fare rate")
    parser.add_argument("--version", "-V", default="0.0.1", type=str, help="display version of our app")
    args = parser.parse_args()
    return args
