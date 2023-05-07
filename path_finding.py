"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a function to create a path, encoded as an Itinerary, that is shortest for some Vehicle.

@file path_finding.py
"""
import math
import networkx

import country
from city import City, get_city_by_id
from itinerary import Itinerary
from vehicles import Vehicle, create_example_vehicles, CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley
from csv_parsing import create_cities_countries_from_csv
import matplotlib.pyplot as plt


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Itinerary | None:
    """
    Returns a shortest path between two cities for a given vehicle as an Itinerary,
    or None if there is no path.

    :param vehicle: The vehicle to use.
    :param from_city: The departure city.
    :param to_city: The arrival city.
    :return: A shortest path from departure to arrival, or None if there is none.
    """
    #TODO
    graph = networkx.Graph()
    for city in City.id_to_cities.values():
        for next_city in City.id_to_cities.values():
            if city.city_id != next_city.city_id: 

                if (isinstance(vehicle, CrappyCrepeCar)):
                    #For the CrappyCrepeCar, it can travel between any two cities and therefore we add a edge between every city.
                    graph.add_weighted_edges_from([(city, next_city, vehicle.compute_travel_time(city, next_city))])
                if (isinstance(vehicle, DiplomacyDonutDinghy)):
                    #For the DiplomacyDonutDinghy, it can travel only between cities in the same country and primary cities between two countries
                    if(vehicle.compute_travel_time(city, next_city) != math.inf):        
                        graph.add_weighted_edges_from([(city, next_city, vehicle.compute_travel_time(city, next_city))])
                if(isinstance(vehicle, TeleportingTarteTrolley)):
                    #For the TeleportingTarteTrolley, it can travely only between cities within a certain distance
                    if (vehicle.compute_travel_time(city, next_city) != math.inf):
                        graph.add_weighted_edges_from([(city, next_city, vehicle.compute_travel_time(city, next_city))])
    
    try:
        short_path = networkx.shortest_path(graph, source=from_city, target=to_city)
        itinerary = Itinerary(short_path) # Create an itinerary object of the calculated shortest path.

        return itinerary 
    except networkx.exception.NodeNotFound: # An error will be returned when a path cannot be found
        return None



if __name__ == "__main__":
    create_cities_countries_from_csv("GPS assignment/worldcities_truncated.csv")
    vehicles = create_example_vehicles()

    from_cities = set()
    for city_id in [1036533631, 1036142029, 1458988644]:
        from_cities.add(get_city_by_id(city_id))


    #we create some vehicles
    vehicles = create_example_vehicles()
    # for city in City.id_to_cities.values():
    #     print(city.name)
    to_cities = set(from_cities)
    # print(find_shortest_path(vehicles[1], get_city_by_id(1036533631), get_city_by_id(1036074917)))
    for from_city in from_cities:
        to_cities -= {from_city}
        for to_city in to_cities:
            print(f"{from_city} to {to_city}:")
            for test_vehicle in vehicles:
                shortest_path = find_shortest_path(test_vehicle, from_city, to_city)
                print(f"\t{test_vehicle.compute_itinerary_time(shortest_path)}"
                      f" hours with {test_vehicle} with path {shortest_path}.")
