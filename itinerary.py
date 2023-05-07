"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class Itinerary.

@file itinerary.py
"""
import math
from city import City, create_example_cities, get_cities_by_name

class Itinerary():
    """
    A sequence of cities.
    """

    def __init__(self, cities: list[City]) -> None:
        """
        Creates an itinerary with the provided sequence of cities,
        conserving order.
        :param cities: a sequence of cities, possibly empty.
        :return: None
        """
        #TODO
        self.cities = cities

    def total_distance(self) -> int:
        """
        Returns the total distance (in km) of the itinerary, which is
        the sum of the distances between successive cities.
        :return: the total distance.
        """
        #TODO
        total_distance = 0
        for i in range(len(self.cities) - 1):
            total_distance += self.cities[i].distance(self.cities[i + 1])
        return total_distance

    def append_city(self, city: City) -> None:
        """
        Adds a city at the end of the sequence of cities to visit.
        :param city: the city to append
        :return: None.
        """
        #TODO
        self.cities.append(city)

    def min_distance_insert_city(self, city: City) -> None:
        """
        Inserts a city in the itinerary so that the resulting
        total distance of the itinerary is minimised.
        :param city: the city to insert
        :return: None.

        """
        #TODOa
        min_dist_and_index = [-1, float("inf")]
        for j in range(len(self.cities)):
            self.cities.insert(j, city) # Creates a hypothetical itinerary
            min_dist_and_index = [j,self.total_distance()] if self.total_distance() < min_dist_and_index[1] else min_dist_and_index #If the distance of the hypothetical itinerary is shorter than another hypotheical itinerary, then change min_dist_and_index, else, leave it as is.
            self.cities.pop(j) #Takes the city out of that position so that the already established itinerary is not permanently changed

        self.cities.insert(min_dist_and_index[0], city)
        
    
            


    def __str__(self) -> str:
        """
        Returns the sequence of cities and the distance in parentheses
        For example, "Melbourne -> Kuala Lumpur (6368 km)"

        :return: a string representing the itinerary.

        list comp
        """
        #TODO
        if (len(self.cities) > 0):
            return " -> ".join([city.name for city in self.cities]) + " (" + str(self.total_distance()) + " km)" #Using list comprehension and join to put a -> between every city
        else:
            return "(0 km)"


if __name__ == "__main__":
    create_example_cities()

    test_itin = Itinerary([get_cities_by_name("Melbourne")[0],
                           get_cities_by_name("Sydney")[0],
                           get_cities_by_name("Brisbane")[0]])
    print(test_itin)

    # # #we try adding a city
    # test_itin.append_city(get_cities_by_name("Baoding")[0])
    # print(test_itin)

    #we try inserting a city
    test_itin.min_distance_insert_city(get_cities_by_name("Perth")[0])
    print(test_itin)

    #we try inserting another city
    test_itin.min_distance_insert_city(get_cities_by_name("Adelaide")[0])
    print(test_itin)
    
