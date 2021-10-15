from abc import ABC, abstractmethod

from firefighters.city_node import CityNode
from firefighters.exceptions import NoFireFoundException, FireproofBuildingException


class Building(ABC):

    @property
    @abstractmethod
    def location(self) -> CityNode:
        """Get the location of this building

        :return: CityNode representing the location
        """
        pass

    @property
    @abstractmethod
    def is_burning(self) -> bool:
        """Find out if the building is currently on fire

        :return: True if the building is burning, otherwise False
        """
        pass

    @property
    @abstractmethod
    def is_fireproof(self) -> bool:
        """Find out if the building is fireproof

        :return: True if the building is fireproof, otherwise False
        """
        pass

    @abstractmethod
    def extinguish_fire(self) -> None:
        """Extinguish the fire in the building

        :raise: NoFireFoundException if the building is not on fire
        """
        pass

    @abstractmethod
    def set_fire(self) -> None:
        """Sets the building on fire. This method should only be used to set up the scenario.

        :raise: FireproofBuildingException if the building is fireproof
        """
        pass


class BuildingImpl(Building):

    def __init__(self, location: CityNode, fireproof: bool = False):
        self._location = location
        self._is_fireproof = fireproof
        self._is_burning = False

    @property
    def location(self) -> CityNode:
        return self._location

    @property
    def is_burning(self) -> bool:
        return self._is_burning

    @property
    def is_fireproof(self) -> bool:
        return self._is_fireproof

    def extinguish_fire(self) -> None:
        if self._is_burning:
            self._is_burning = False
        else:
            raise NoFireFoundException()

    def set_fire(self) -> None:
        if not self._is_fireproof:
            self._is_burning = True
        else:
            raise FireproofBuildingException()
