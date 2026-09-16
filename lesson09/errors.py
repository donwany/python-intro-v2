# custom error class
class FareEstimatorError(Exception):
    pass


class InvalidRateError(FareEstimatorError):
    pass


class InvalidDistanceError(FareEstimatorError):
    pass
