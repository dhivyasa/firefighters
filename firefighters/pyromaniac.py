from typing import List

from firefighters.city import City
from firefighters.city_node import CityNode


class Pyromaniac:

    @staticmethod
    def set_fires(victim_city: City, victim_locations: List[CityNode]) -> None:
        """
        Sets fires at each victim_locations in the given victim_city

        :param victim_city: City to be set on fire
        :param victim_locations: Locations to be set on fire
        :raise: FireproofBuildingException if one of the buildings in question is fireproof
        """

        for location in victim_locations:
            Pyromaniac.set_fire(victim_city, location)

    @staticmethod
    def set_fire(victim_city: City, victim_location: CityNode) -> None:
        """
        Sets a fire at the victim_location in the given victim_city

        :param victim_city: City to be set on fire
        :param victim_location: Location to be set on fire
        :raise: FireproofBuildingException if one of the buildings in question is fireproof
        """

        victim_city.get_building_from_node(victim_location).set_fire()
