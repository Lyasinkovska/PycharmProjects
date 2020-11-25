import json
import datetime

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
	if not isinstance(input_data['stop_name'], str) or input_data['stop_name'] == "":
		return False
	else:
		if input_data['stop_name'].split()[0].isupper() and input_data['stop_name'].split()[1] in \
				("Road", "Avenue", "Boulevard", "Street"):
			return True


def next_stop_validation(input_data):
	return isinstance(input_data['next_stop'], int)


def stop_type_validation(input_data):
	if isinstance(input_data['stop_type'], str) and len(input_data['stop_type']) <= 1:
		return True
	elif input_data['stop_type'] in ("S", "O", "F"):
		return True
	else:
		return False


def a_time_validation(input_data):
	if isinstance(input_data['a_time'], str) and input_data['a_time'] != "":
		timeformat = "%H:%M"
		try:
			return datetime.datetime.strptime(input_data['a_time'], timeformat)
		except ValueError:
			return False
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
	j = f"Type and required field validation: {sum(validation.values())} errors \nbus_id: {validation['bus_id']}\n" \
		f"stop_id: {validation['stop_id']}\nstop_name: {validation['stop_name']}\nnext_stop: {validation['next_stop']}\n" \
		f"stop_type: {validation['stop_type']}\na_time: {validation['a_time']}"
	print(j)


validation_calculation()
