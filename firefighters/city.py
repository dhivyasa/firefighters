from abc import ABC, abstractmethod
from typing import List

from firefighters.building import Building, BuildingImpl
from firefighters.city_node import CityNode
from firefighters.exceptions import InvalidDimensionException, OutOfCityBoundsException
from firefighters.fire_station import FireStation


class City(ABC):

    @property
    @abstractmethod
    def fire_station(self) -> FireStation:
        """Get the city's FireStation. The FireStation is fireproof

        :return: Building representing the FireStation
        """
        pass

    @property
    @abstractmethod
    def fire_dispatch(self):
        """Get the city's FireDispatch.

        :return: the city's FireDispatch
        """
        pass

    @property
    @abstractmethod
    def x_dimension(self) -> int:
        """Get the X dimension of the city

        :return: the X dimension of the city
        """
        pass

    @property
    @abstractmethod
    def y_dimension(self) -> int:
        """Get the Y dimension of the city

        :return: the Y dimension of the city
        """
        pass

    @abstractmethod
    def get_building(self, x_coordinate: int, y_coordinate: int) -> Building:
        """Get the building at the given coordinates

        :param x_coordinate:
        :param y_coordinate:
        :return: the Building at these coordinates
        :raise: OutOfCityBoundsException if the coordinates are out of bounds for this city
        """
        pass

    @abstractmethod
    def get_building_from_node(self, city_node: CityNode) -> Building:
        """Get the building at the given coordinates

        :param city_node:
        :return: the Building at these coordinates
        :raise: OutOfCityBoundsException if the coordinates are out of bounds for this city
        """
        pass


class CityImpl(City):

    def __init__(self, x_dimension: int, y_dimension: int, fire_station_location: CityNode):
        from firefighters.firedispatch import FireDispatchImpl

        self.__validate_city_dimension(x_dimension, y_dimension)
        self._fire_station = FireStation(fire_station_location)
        self._building_grid = self.__init_building_grid(x_dimension, y_dimension)
        self._fire_dispatch = FireDispatchImpl(self)

    @property
    def fire_station(self) -> Building:
        return self._fire_station

    @property
    def fire_dispatch(self):
        return self._fire_dispatch

    @property
    def x_dimension(self) -> int:
        return len(self._building_grid)

    @property
    def y_dimension(self) -> int:
        return len(self._building_grid[0])

    def get_building(self, x_dimension: int, y_dimension: int) -> Building:
        self.__validate_coordinate(x_dimension, y_dimension)
        return self._building_grid[x_dimension][y_dimension]

    def get_building_from_node(self, city_node: CityNode) -> Building:
        return self.get_building(city_node.x_coordinate, city_node.y_coordinate)

    def __init_building_grid(self, x_dimension: int, y_dimension: int) -> List[List[Building]]:
        grid = list()
        for row in range(x_dimension):
            y_list = list()
            for col in range(y_dimension):
                y_list.append(self.__init_building(row, col))
            grid.append(y_list)

        return grid

    def __init_building(self, x: int, y: int) -> Building:
        if x == self._fire_station.location.x_coordinate and y == self._fire_station.location.y_coordinate:
            return self._fire_station
        else:
            return BuildingImpl(CityNode(x, y))

    @staticmethod
    def __validate_city_dimension(x: int, y: int) -> None:
        if x < 2:
            raise InvalidDimensionException(x)
        elif y < 2:
            raise InvalidDimensionException(y)

    def __validate_coordinate(self, x: int, y: int):
        if x < 0 or y < 0 or x >= self.x_dimension or y >= self.y_dimension:
            raise OutOfCityBoundsException()
