class CityNode:
    """Represents a location in the city"""

    def __init__(self, x_coordinate: int, y_coordinate: int):
        """Build a CityNode given coordinates

        :param x_coordinate:
        :param y_coordinate:
        """

        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate

    @property
    def x_coordinate(self) -> int:
        """Get the X coordinate of this node

        :return: the X coordinate of this node
        """

        return self._x_coordinate

    @property
    def y_coordinate(self) -> int:
        """Get the Y coordinate of this node

        :return: the Y coordinate of this node
        """

        return self._y_coordinate

    def __str__(self) -> str:
        return f"CityNode{{x_coordinate={self._x_coordinate}, y_coordinate={self._y_coordinate}}}"

    def __eq__(self, other) -> bool:
        if other is None or not isinstance(other, CityNode):
            return False

        return self._x_coordinate == other._x_coordinate and self._y_coordinate == other._y_coordinate
