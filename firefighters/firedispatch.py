from abc import ABC, abstractmethod
from typing import List

from firefighters.city import City
from firefighters.city_node import CityNode
from firefighters.firefighter import FireFighterImpl, FireFighter


class FireDispatch(ABC):

    @property
    @abstractmethod
    def firefighters(self) -> List[FireFighter]:
        """
        Get the list of firefighters

        :return: List of hired firefighters
        """
        pass

    @firefighters.setter
    @abstractmethod
    def firefighters(self, num_firefighters: int) -> None:
        """
        Hires a number of firefighters

        :param num_firefighters:
        """
        pass

    @abstractmethod
    def dispatch_firefighters(self, burning_buildings: List[CityNode]):
        """
        The FireDispatch will be notified of burning buildings via this method. It will then dispatch the
        firefighters and extinguish the fires. We want to optimize for total distance traveled by
        all firefighters.

        :param burning_buildings: list of locations with burning buildings
        """
        pass


class FireDispatchImpl(FireDispatch):
    """
    FireDispatch is constructed with a 
    reference to its city. It is responsible for initializing and dispatching the firefighters.
    """

    def __init__(self, city: City):
        self._fire_station = city.fire_station
        self._fire_fighters = []
        self.city = city

    def __call__(self, num_firefighters:int) -> FireDispatch:
        """Return callable object initialized with the number of firefighters"""
        self.firefighters = num_firefighters
        return self

    @property
    def firefighters(self) -> List[FireFighter]:
        return self._fire_fighters

    @firefighters.setter
    def firefighters(self, num_firefighters: int) -> None:
        """
        Initialize firefighters at City's firestation as starting location
        """

        for i in range(num_firefighters):
            a_firefighter = FireFighterImpl(self._fire_station.location)
            self._fire_fighters.append(a_firefighter)


    def dispatch_firefighters(self, burning_buildings: List[CityNode]):
        """
        Find distance between firefighters and burning buildings. 
        A firefighter goes to the building closest to him and extinguishes 
        the fire
        """

        for burning_building in burning_buildings:
            distances = []
            for fire_fighter in self._fire_fighters:
                  distances.append(fire_fighter.distance_from(burning_building))

            closest_distance = min(distances)
            closest_fighter = self._fire_fighters[distances.index(closest_distance)]
            closest_fighter.distance_traveled = closest_distance
            closest_fighter.location = burning_building
            closest_fighter.extinguish_fire(self.city.get_building_from_node(burning_building))


