"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It puts together all parts of the assignment.

@file onboard_navigation.py
"""
import city
import country
import csv_parsing
import itinerary
import map_plotting
import path_finding
import vehicles

def validate_input(prompt, valid_inputs):
	"""
	Repeatedly ask user for input until they enter an input
	within a set valid of options.

	:param prompt: The prompt to display to the user, string.
	:param valid_inputs: The range of values to accept, list
	:return: The user's input, string.
	"""
	
	input_option = input(prompt)
	while input_option not in valid_inputs:
		print("Invalid input, please try again.")
		input_option = input(prompt)
	return input_option

def validate_speed(prompt) -> float:
	while True:
		speed = input(prompt)
		try:
			if (isinstance(float(speed), float)):
				break
		except:
			continue
	return float(speed)

def get_exact_city(origin_city_list):
	for possible_origin in origin_city_list:
		possible_country_list = []
		possible_country_list.append(country.find_country_of_city(possible_origin).name)
	origin_country_cities = country.Country.name_to_countries[validate_input(f"Enter which country this city belongs to ({possible_country_list}): ", possible_country_list)].cities
	origin_city = next(city_country for city_country in origin_city_list if city_country in origin_country_cities)
	return origin_city

def main():
	csv_parsing.create_cities_countries_from_csv("./worldcities_truncated.csv")
	vehicle_choice = validate_input("Which Vehicle would you like to choose (CrappyCrepeCar, DiplomacyDinghyDonut, TeleportingTarteTrolley): ", ["CrappyCrepeCar", "TeleportingTarteTrolley", "DiplomacyDinghyDonut"])
	if vehicle_choice == "CrappyCrepeCar":
		speed = validate_speed("Enter the speed of the CrappyCrepeCar: ")
		vehicle_chosen = vehicles.CrappyCrepeCar(int(speed))
	elif vehicle_choice == "DiplomacyDinghyDonut":
		in_country_speed = validate_speed("Enter the in country speed of the DiplomacyDinghyDonut: ")
		between_primary_speed = validate_speed("Enter the between primary country speed of the DiplomacyDinghyDonut: ")
		vehicle_chosen = vehicles.DiplomacyDonutDinghy(in_country_speed, between_primary_speed)
	else:
		travel_time = validate_speed("Enter the time the TeleportingTarteTrolley takes: ")
		max_distance = validate_speed("Enter the max distance of the TeleportingTarteTrolley: ")
		vehicle_chosen = vehicles.TeleportingTarteTrolley(travel_time, max_distance)
	origin_city = city.City.name_to_cities[validate_input("What is your origin city: ", city.City.name_to_cities.keys())]
	origin_city = get_exact_city(origin_city)
	destination_city = city.City.name_to_cities[validate_input("What is your destination city: ", city.City.name_to_cities.keys())]
	destination_city = get_exact_city(destination_city)
	path = path_finding.find_shortest_path(vehicle_chosen, origin_city, destination_city)
	print(path)
	map_plotting.plot_itinerary(path)


if __name__ == "__main__":
	main()
	