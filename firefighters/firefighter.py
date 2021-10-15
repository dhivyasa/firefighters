from abc import ABC, abstractmethod

from firefighters.city_node import CityNode
from firefighters.building import Building


class FireFighter(ABC):

    @property
    @abstractmethod
    def location(self) -> CityNode:
        """
        Get the firefighter's current location. Initially, the firefighter should be at the FireStation

        :return: CityNode representing the firefighter's current location
        """
        pass

    @property
    @abstractmethod
    def distance_traveled(self) -> int:
        """
        Get the total distance traveled by this firefighter. Distances should be represented using TaxiCab
        Geometry: https://en.wikipedia.org/wiki/Taxicab_geometry

        :return: the total distance traveled by this firefighter
        """
        pass


class FireFighterImpl(FireFighter):

    def __init__(self, location: CityNode):
        self._location = location
        self._total_distance = 0

    @property
    def location(self) -> CityNode:
        return self._location

    @location.setter
    def location(self, new_location: CityNode):
        self._location = new_location

    def extinguish_fire(self, building: Building):
        building.extinguish_fire()

    @property
    def distance_traveled(self) -> int:
        return self._total_distance

    @distance_traveled.setter
    def distance_traveled(self, distance:int):
         self._total_distance += distance


    def distance_from(self, another_location: CityNode)->int:
        """
        Calculate the the taxi-cab distance of this firefighter
        from given location
        """
        return abs(self.location.x_coordinate - another_location.x_coordinate
        ) + abs(self.location.y_coordinate - another_location.y_coordinate)
