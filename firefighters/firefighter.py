from abc import ABC, abstractmethod

from firefighters.city_node import CityNode


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

    @property
    def location(self) -> CityNode:
        # TODO
        raise NotImplementedError()

    @property
    def distance_traveled(self) -> int:
        # TODO
        raise NotImplementedError()
