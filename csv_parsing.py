"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a parser that reads a CSV file and creates instances 
of the class City and the class Country.

@file city_country_csv_reader.py
"""
import csv
from city import City
from country import Country

def create_cities_countries_from_csv(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.

    :param path_to_csv: The path to the CSV file.
    """
    #TODO
    with open(path_to_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers  = next(csv_reader)
        indexes = {}
        country_cnt = 0
        for i in range(len(headers)):
            indexes[headers[i]] = i
        for row in csv_reader:
            if (row[indexes["population"]] == ''):
                row[indexes["population"]] = 0
            city = City(row[indexes["city"]], (row[indexes["lat"]], row[indexes["lng"]]),row[indexes["capital"]], row[indexes["population"]], int(row[indexes["id"]]))
            country_cnt += 1
            if  row[indexes["country"]] not in Country.name_to_countries:
                country = Country(row[indexes["country"]], row[indexes["iso3"]])
                country.add_city(city)
                
            else:
                Country.name_to_countries[row[indexes["country"]]].add_city(city)
    # print(country_cnt)

if __name__ == "__main__":
    create_cities_countries_from_csv("GPS assignment/worldcities_truncated.csv")
    for country in Country.name_to_countries.values():
        country.print_cities()
    
    for city_list in City.name_to_cities.keys():
        if len(City.name_to_cities[city_list]) > 1:
            print(city_list)