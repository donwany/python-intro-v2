from errors import InvalidRateError, InvalidDistanceError


class FareEstimator:
    def __init__(self, base_fare: float):
        self.base_fare = base_fare

    def estimate(self, distance, rate):
        # validate our inputs
        if distance <= 0:
            raise InvalidDistanceError("Distance must be greater than zero.")
        if rate <= 0:
            raise InvalidRateError("Rate must be greater than zero.")
        return self.base_fare + (distance * rate)
