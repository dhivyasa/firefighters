class FireproofBuildingException(Exception):
    def __init__(self):
        super().__init__("This building is fireproof and cannot be set on fire")


class InvalidDimensionException(RuntimeError):
    def __init__(self, invalid_dimension: int):
        super().__init__(f"Invalid dimension for a city: {invalid_dimension}")


class NoFireFoundException(Exception):
    def __init__(self):
        super().__init__("This building cannot be extinguished because there is no fire!")


class OutOfCityBoundsException(RuntimeError):
    def __init__(self):
        super().__init__("This node is out of bounds!")
