import unittest

from firefighters.city import CityImpl
from firefighters.city_node import CityNode
from firefighters.pyromaniac import Pyromaniac


class TestFireFighters(unittest.TestCase):
    def test_single_fire(self):
        basic_city = CityImpl(5, 5, CityNode(0, 0))
        fire_dispatch = basic_city.fire_dispatch()

        fire_node = CityNode(0, 1)
        Pyromaniac.set_fire(basic_city, fire_node)

        fire_dispatch.firefighters(1)
        fire_dispatch.dispatch_firefighters([fire_node])

        self.assertFalse(basic_city.get_building_from_node(fire_node).is_burning)

    def test_single_fire_distance_traveled_diagonal(self):
        self.assertEqual(CityNode(1,1), CityNode(1,1))
        basic_city = CityImpl(2, 2, CityNode(0, 0))
        fire_dispatch = basic_city.fire_dispatch()

        # Set fire on opposite corner from Fire Station
        fire_node = CityNode(1, 1)
        Pyromaniac.set_fire(basic_city, fire_node)

        fire_dispatch.firefighters(1)
        fire_dispatch.dispatch_firefighters([fire_node])

        firefighter = fire_dispatch.firefighters()[0]
        self.assertEqual(2, firefighter.distance_traveled())
        self.assertEqual(fire_node, firefighter.location)
        self.assertFalse(basic_city.get_building_from_node(fire_node).is_burning)

    def test_single_fire_distance_traveled_adjacent(self):
        basic_city = CityImpl(2, 2, CityNode(0, 0))
        fire_dispatch = basic_city.fire_dispatch()

        # Set fire on adjacent X position from Fire Station
        fire_node = CityNode(1, 0)
        Pyromaniac.set_fire(basic_city, fire_node)

        fire_dispatch.firefighters(1)
        fire_dispatch.dispatch_firefighters([fire_node])

        firefighter = fire_dispatch.firefighters()[0]
        self.assertEqual(1, firefighter.distance_traveled())
        self.assertEqual(fire_node, firefighter.location)
        self.assertFalse(basic_city.get_building_from_node(fire_node).is_burning)

    def test_double_fire(self):
        basic_city = CityImpl(2, 2, CityNode(0, 0))
        fire_dispatch = basic_city.fire_dispatch()

        fire_nodes = [CityNode(0, 1), CityNode(1, 1)]
        Pyromaniac.set_fires(basic_city, fire_nodes)

        fire_dispatch.firefighters(1)
        fire_dispatch.dispatch_firefighters(fire_nodes)

        firefighter = fire_dispatch.firefighters()[0]
        self.assertEqual(2, firefighter.distance_traveled())
        self.assertEqual(fire_nodes[1], firefighter.location())
        self.assertFalse(basic_city.get_building_from_node(fire_nodes[0]).is_burning)
        self.assertFalse(basic_city.get_building_from_node(fire_nodes[1]).is_burning)

    def test_double_firefighter_double_fire(self):
        basic_city = CityImpl(2, 2, CityNode(0, 0))
        fire_dispatch = basic_city.fire_dispatch()

        fire_nodes = [CityNode(0, 1), CityNode(1, 0)]
        Pyromaniac.set_fires(basic_city, fire_nodes)

        fire_dispatch.firefighters(2)
        fire_dispatch.dispatch_firefighters(fire_nodes)

        firefighters = fire_dispatch.firefighters()
        total_distance_traveled = 0
        firefighter_present_at_fire_one = False
        firefighter_present_at_fire_two = False
        for firefighter in firefighters:
            total_distance_traveled += firefighter.distance_traveled()
            if firefighter.location() == fire_nodes[0]:
                firefighter_present_at_fire_one = True
            if firefighter.location() == fire_nodes[1]:
                firefighter_present_at_fire_two = True

        self.assertEqual(2, total_distance_traveled)
        self.assertTrue(firefighter_present_at_fire_one)
        self.assertTrue(firefighter_present_at_fire_two)
        self.assertFalse(basic_city.get_building_from_node(fire_nodes[0]).is_burning)
        self.assertFalse(basic_city.get_building_from_node(fire_nodes[1]).is_burning)


if __name__ == '__main__':
    unittest.main()
