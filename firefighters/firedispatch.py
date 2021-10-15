from abc import ABC, abstractmethod
from typing import List

from firefighters.city import City
from firefighters.city_node import CityNode
from firefighters.firefighter import FireFighter


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
        # TODO
        raise NotImplementedError()

    @property
    def firefighters(self) -> List[FireFighter]:
        # TODO
        raise NotImplementedError()

    @firefighters.setter
    def firefighters(self, num_firefighters: int) -> None:
        # TODO
        raise NotImplementedError()

    def dispatch_firefighters(self, burning_buildings: List[CityNode]):
        # TODO
        raise NotImplementedError()
