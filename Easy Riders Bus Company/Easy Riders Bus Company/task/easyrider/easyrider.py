import json
import datetime
import re

input_data = json.loads(input())

validation = {"bus_id": 0,
        "stop_id": 0,
        "stop_name": 0,
        "next_stop": 0,
        "stop_type": 0,
        "a_time": 0}


bus_line = {
			128: ['Sesame Street', 'Sunset Boulevard', 'Elm Street', 'Prospekt Avenue'],
			256: ['Sesame Street', 'Fifth Avenue', 'Elm Street', 'Pilotow Street'],
			512: ['Bourbon Street', 'Sunset Boulevard']
			}


def bus_id_validation(input_data):
	return isinstance(input_data['bus_id'], int)


def stop_id_validation(input_data):
	return isinstance(input_data['stop_id'], int)


def stop_name_validation(input_data):
	template = r"[A-Z][a-zA-Z]+\s?\w+?\s(Avenue|Street|Road|Boulevard)$"
	if re.match(template, input_data['stop_name']) == None:
		return False
	else:
		return True


def next_stop_validation(input_data):
	return isinstance(input_data['next_stop'], int)


def stop_type_validation(input_data):
	if input_data['stop_type'] in ("S", "O", "F", ""):
		return True
	else:
		return False


def a_time_validation(input_data):
	template = r'[0-2][0-9]:[0-5][0-9]$'
	if re.match(template, input_data['a_time']):
		return True
	else:
		return False


def validation_calculation():
	for el in input_data:
		if bus_id_validation(el) == False:
			validation["bus_id"] += 1
		if stop_id_validation(el)== False:
			validation['stop_id'] += 1
		if next_stop_validation(el) == False:
			validation["next_stop"] += 1
		if stop_type_validation(el) == False:
			validation['stop_type'] += 1
		if a_time_validation(el) == False:
			validation['a_time'] += 1
		if stop_name_validation(el) == False:
			validation['stop_name'] += 1
	print(f"Format validation: {sum(validation.values())} errors")
	print(f"stop_name: {validation['stop_name']}\nstop_type: {validation['stop_type']}\na_time: {validation['a_time']}")



validation_calculation()
