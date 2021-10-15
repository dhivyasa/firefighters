from firefighters.building import BuildingImpl
from firefighters.city_node import CityNode


class FireStation(BuildingImpl):
    def __init__(self, location: CityNode):
        super().__init__(location, True)
