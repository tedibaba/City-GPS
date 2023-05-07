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

def validate_input(prompt, valid_inputs, country_or_city):
	"""
	Repeatedly ask user for input until they enter an input
	within a set valid of options.

	:param prompt: The prompt to display to the user, string.
	:param valid_inputs: The range of values to accept, list
	:param country_or_city: Whether a country or city is being validated, boolean.
	:return: The user's input, string.
	"""
	
	input_option = input(prompt)
	while input_option.title() not in valid_inputs:
		print("Invalid input, please try again.")
		input_option = input(prompt)
	if country_or_city:
		return input_option.title()
	else:
		return input_option

def validate_speed(prompt):
	"""
	Repeatedly ask the user to enter the speed of the 
	vehicle until they enter a number.

	:param prompt: The prompt to display to the user, string.
	"return speed: the speed of the vehicle, float.
	"""
	while True:
		speed = input(prompt)
		try:
			float(speed)
			break
		except ValueError:
			continue
	return float(speed)

def get_exact_city(city_list):
	"""
	Gets the exact city from a list of cities with the same name.

	:param city_list: The list of cities to choose from, list.
	:return: the city which belongs to the country they chose, city.
	"""
	possible_country_list = []
	for possible_origin in city_list: #Finding the countries with the same name as the city
		possible_country_list.append(country.find_country_of_city(possible_origin).name)
	country_cities = country.Country.name_to_countries[validate_input(f"Enter which country this city belongs to ({possible_country_list}): ", possible_country_list, True)].cities # Given the country of the city, we find all the cities of that country
	chosen_city = next(city_country for city_country in city_list if city_country in country_cities) # This then finds the exact city belongign to that country using list comprehension
	return chosen_city

def main():
	csv_parsing.create_cities_countries_from_csv("./worldcities_truncated.csv")
	vehicle_choice = validate_input("Which Vehicle would you like to choose (CrappyCrepeCar, DiplomacyDinghyDonut, TeleportingTarteTrolley): ", ["Crappycrepecar", "Diplomacydinghydonut", "Teleportingtartetrolley"], False)#capitalize changes the capital letters in the middle of the word so acceptable words have been changed accordingly
	if vehicle_choice == "CrappyCrepeCar":
		speed = validate_speed("Enter the speed (in km) of the CrappyCrepeCar: ")
		vehicle_chosen = vehicles.CrappyCrepeCar(int(speed))
	elif vehicle_choice == "DiplomacyDinghyDonut":
		in_country_speed = validate_speed("Enter the in country speed (in km) of the DiplomacyDinghyDonut: ")
		between_primary_speed = validate_speed("Enter the between primary country speed (in km) of the DiplomacyDinghyDonut: ")
		vehicle_chosen = vehicles.DiplomacyDonutDinghy(in_country_speed, between_primary_speed)
	else:
		travel_time = validate_speed("Enter the time (in hours) the TeleportingTarteTrolley takes: ")
		max_distance = validate_speed("Enter the max distance (in km) of the TeleportingTarteTrolley: ")
		vehicle_chosen = vehicles.TeleportingTarteTrolley(travel_time, max_distance)
	chosen_city = city.City.name_to_cities[validate_input("What is your origin city: ", city.City.name_to_cities.keys(), True)]
	chosen_city = get_exact_city(chosen_city)
	destination_city = city.City.name_to_cities[validate_input("What is your destination city: ", city.City.name_to_cities.keys(), True)]
	destination_city = get_exact_city(destination_city)

	path = path_finding.find_shortest_path(vehicle_chosen, chosen_city, destination_city)
	if path == None:
		print("No path found")
		exit()
	travel_time = vehicle_chosen.compute_itinerary_time(path)
	print(path)
	print(f"The path takes {travel_time} hours with a {vehicle_chosen}")
	map_plotting.plot_itinerary(path)


if __name__ == "__main__":
	main()
	