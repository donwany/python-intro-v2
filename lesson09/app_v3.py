# classes, functions, exceptions (try/except), argparse
import argparse
from errors import InvalidDistanceError, InvalidRateError, FareEstimatorError
from fares import FareEstimator
from utils import parser, add_tax

# make use of args variable
args = parser()


def main():
    try:
        print(f"Running application version: {args.version}")
        estimator = FareEstimator(base_fare=args.base)
        fare = estimator.estimate(distance=args.distance, rate=args.rate)
        tax = add_tax(fare)
        total_fare = fare + tax
        print(f"Tax is: ${tax}")
        print(f"Total Uber fare including tax is: ${total_fare:.2f}")
        print("Thanks for riding with us ...")
    except InvalidRateError as ex:
        print(f"Rate error: {ex}")
    except InvalidDistanceError as ex:
        print(f"Distance error: {ex}")
    except FareEstimatorError as ex:
        print(f"General fare error: {ex}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")


if __name__ == '__main__':
    main()
