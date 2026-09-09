class FareEstimatorError(Exception):
    """Base class for fare estimator errors."""
    pass


class InvalidDistanceError(FareEstimatorError):
    """Raised when distance is invalid."""
    pass


class InvalidRateError(FareEstimatorError):
    """Raised when rate is invalid."""
    pass


class FareEstimator:
    def __init__(self, base_fare=2.5):
        self.base_fare = base_fare

    def estimate(self, distance, rate):
        # Validate inputs
        if distance <= 0:
            raise InvalidDistanceError("Distance must be greater than 0.")
        if rate <= 0:
            raise InvalidRateError("Rate must be greater than 0.")

        return self.base_fare + (distance * rate)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Fare Estimator with error handling")
    parser.add_argument("--distance", type=float, required=True)
    parser.add_argument("--rate", type=float, required=True)
    parser.add_argument("--base", type=float, default=2.5)
    args = parser.parse_args()

    estimator = FareEstimator(base_fare=args.base)

    try:
        fare = estimator.estimate(args.distance, args.rate)
        print(f"✅ Estimated Fare: ${fare:.2f}")
    except InvalidDistanceError as e:
        print(f"❌ Distance Error: {e}")
    except InvalidRateError as e:
        print(f"❌ Rate Error: {e}")
    except FareEstimatorError as e:
        print(f"⚠️ General Fare Error: {e}")
    except Exception as e:
        print(f"🚨 Unexpected Error: {e}")


if __name__ == "__main__":
    main()
