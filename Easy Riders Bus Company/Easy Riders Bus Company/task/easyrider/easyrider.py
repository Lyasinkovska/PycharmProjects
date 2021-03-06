import json
import re
from itertools import combinations
from datetime import datetime as dt

input_data = json.loads(input())
'''input_data_1 = [
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "O",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]



input_data2 = [
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]'''
validation = {"bus_id": 0,
        "stop_id": 0,
        "stop_name": 0,
        "next_stop": 0,
        "stop_type": 0,
        "a_time": 0}

def validation_calculation():
	for _ in input_data:
		if not isinstance(input_data['bus_id'], int):
			validation["bus_id"] += 1
		if not isinstance(input_data['stop_id'], int):
			validation['stop_id'] += 1
		if not isinstance(input_data['next_stop'], int):
			validation["next_stop"] += 1
		if not input_data['stop_type'] in ("S", "O", "F", ""):
			validation['stop_type'] += 1
		if not re.match(r'[0-2][0-9]:[0-5][0-9]$', input_data['a_time']):
			validation['a_time'] += 1
		if re.match(r"[A-Z][a-zA-Z]+\s?\w+?\s(Avenue|Street|Road|Boulevard)$", input_data['stop_name']) == None:
			validation['stop_name'] += 1

	print(f"Format validation: {sum(validation.values())} errors")
	print(f"stop_name: {validation['stop_name']}\nstop_type: {validation['stop_type']}\na_time: {validation['a_time']}")


def stops_number():
	bus_stops = {}
	for data in input_data:
		if data['bus_id'] not in bus_stops:
			bus_stops[data["bus_id"]] = 1
		else:
			bus_stops[data["bus_id"]] += 1
	print("Line names and number of stops:")
	for bus_id in bus_stops:
		print(f'bus_id: {bus_id}, stops: {bus_stops[bus_id]}')


def stops_combinations(stops, r=2):
	return list(combinations(stops, r))


def transfer_stops(all_stops):
	transfer_stops = set()
	for combination in stops_combinations(all_stops):
		transfer_stops.update(set(combination[0]) & set(combination[1]))
	return transfer_stops


def start_stop(input_data):
	bus_lines = {}

	for data in input_data:
		if data['bus_id'] not in bus_lines:
			bus_lines[data["bus_id"]] = {'start_stops': [], 'opt_stops': [], 'finish_stops': [], 'all_stops': []}
			if data['stop_type'] == "S":
				bus_lines[data["bus_id"]]['start_stops'].append(data['stop_name'])
			elif data['stop_type'] == "F":
				bus_lines[data["bus_id"]]['finish_stops'].append(data['stop_name'])
			elif data['stop_type'] == "O":
				bus_lines[data["bus_id"]]['opt_stops'].append(data['stop_name'])
			bus_lines[data["bus_id"]]['all_stops'].append(data['stop_name'])
		else:
			if data['stop_type'] == "S":
				bus_lines[data["bus_id"]]['start_stops'].append(data['stop_name'])
			elif data['stop_type'] == "F":
				bus_lines[data["bus_id"]]['finish_stops'].append(data['stop_name'])
			elif data['stop_type'] == "O" or data['stop_type'] == "":
				bus_lines[data["bus_id"]]['opt_stops'].append(data['stop_name'])
			bus_lines[data["bus_id"]]['all_stops'].append(data['stop_name'])

	start_stops = set()
	finish_stops = set()
	all_stops = []
	opt_stops = []
	for line in bus_lines:
		if not bus_lines[line]['start_stops'] or not bus_lines[line]['finish_stops']:
			print(f"There is no start or end stop for the line: {line}.")
		else:
			start_stops.update(bus_lines[line]['start_stops'])
			finish_stops.update(bus_lines[line]['finish_stops'])
			all_stops.append(bus_lines[line]['all_stops'])
			opt_stops.extend(bus_lines[line]['opt_stops'])

	transfer_stop = transfer_stops(all_stops)
	on_demand_stops = sorted(set(opt_stops)&transfer_stop)
	print("On demand stops test:")
	if on_demand_stops:
		print(f"Wrong stop type: {on_demand_stops}")
	else:
		print("OK")


	'''print(f'Start stops: {len(start_stops)} {sorted(start_stops)}\n'
		  f'Transfer stops: {len(transfer_stop)} {sorted(transfer_stop)}\n'
		  f'Finish stops: {len(finish_stops)} {sorted(finish_stops)}\n')'''


def bus_ids():
	buses = {}
	for bus in input_data:
		if bus['bus_id'] not in buses:
			buses[bus['bus_id']] = [(bus['stop_name'], bus['a_time'])]
		else:
			buses[bus['bus_id']].append((bus['stop_name'], bus['a_time']))
	return buses


def check_time():
	buses = bus_ids()
	print(f"Arrival time test:")
	for bus in buses:
		new_time = None
		for bus_time in buses.get(bus):
			station, time = bus_time[0], bus_time[1]
			if new_time is None or new_time < time:
				new_time = time
				if new_time == buses.get(bus)[-1][1]:
					print("OK")
			elif new_time > time:
				print(f"bus_id line {bus}: wrong time on station {station}")
				break


start_stop(input_data)

