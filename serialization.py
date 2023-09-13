"""
Module for routines that get info from json files
"""
import json
import re
from typing import Dict, List, Optional

# CONSTANTS
# Get bus json object
with open("./serialized/bus.json", "r") as file:
    BUS_JSON: dict = json.load(file)

# Get station json object
with open("./serialized/station.json", "r") as file:
    STATION_JSON: dict = json.load(file)

BUS_ICON = "🚍"
TROLLEY_ICON = "🚎"
STRAIGHT_ICON = "⇨"
REVERSE_ICON = "⇦"

"""
DATA STRUCTURE

IMAGES:
./serialized/images - Images for routes. 
/routes - Straight routes images, filenames like in BUS_JSON.keys()
/reverse_routes - Reverse routes images, filenames like in BUS_JSON.keys()

BUS_JSON:
keys like 10a, t10 - for trolley
{
 "bus_number" : [
	["bus_route_name", ["station1", "station2" ... ]], 
	["bus_reverse_route_name", ["station1", "station2" ...]]
 ],
	
 "bus_number" : ... 
}

STATION_JSON:
bus_number like BUS_JSON.keys()
{
 "station_name" : ['bus_number', 'bus_number_r', 'bus_number_f', ...],
 "station_name" : ...
}

Here - bus_number - Visit station on forward and baskward
	bus_number_r - Visit station only on reverse route
	bus_number_f - Visit station only on straight route
	
"""

# BUS_JSON GETTERS


def get_bus_straight_route_info(bus_key: str) -> Optional[Dict[str, str]]:
    full_route = BUS_JSON.get(bus_key)
    if full_route:
        full_route_info = full_route[0]
        route_name = full_route_info[0]
        stations_list = full_route_info[1]
        return {
            "route_name": route_name,
            "station_list": stations_list,
            "image": f"serialized/images/routes/{bus_key}.jpg",
        }
    else:
        return None


def get_bus_reverse_route_info(bus_key: str) -> Optional[Dict[str, str]]:
    full_route = BUS_JSON.get(bus_key)
    if full_route:
        full_route_info = full_route[1]
        route_name = full_route_info[0]
        stations_list = full_route_info[1]
        return {
            "route_name": route_name,
            "station_list": stations_list,
            "image": f"serialized/images/reverse_routes/{bus_key}.jpg",
        }
    else:
        return None


def bus_numbers_sort(bus_numbers: List[str]) -> List[str]:
    """
    Sort numbers of transport, assuming that they are like 10A or t11A like
    """
    buses = []
    trolleys = []
    for transport in bus_numbers:
        if not transport.startswith("t"):
            buses.append(transport)
        else:
            trolleys.append(transport)
    buses.sort(key=lambda x: int(re.findall(r"\d+", x)[0]))
    trolleys.sort(key=lambda x: int(re.findall(r"\d+", x[1:])[0]))
    buses.extend(trolleys)

    return buses


def get_all_buses_list() -> List[str]:
    result = bus_numbers_sort(list(BUS_JSON.keys()))
    return result


def convert_bus_key_to_label(bus_key: str) -> str:
    bus_number = bus_key
    if bus_key.startswith("t"):
        icon = TROLLEY_ICON
        bus_number = bus_number[1:]
    else:
        icon = BUS_ICON
    label = f"{icon} {bus_number}"
    return label


def convert_label_to_bus_key(label: str) -> str:
    """
    Works fine for route bus labels and simple bus labels
    """
    bus_key = label.split(" ")[-1]
    if label.startswith(TROLLEY_ICON):
        bus_key = "t" + bus_key
    return bus_key


def convert_bus_key_to_bus_number(bus_key: str) -> str:
    result = bus_key
    if bus_key.startswith("t"):
        result = result[1:]
    return result


# STATION_JSON GETTERS


def get_all_stations_list() -> List[str]:
    result = list(STATION_JSON.keys())
    return result


def convert_station_json_bus_to_bus_key(station_json_bus: str) -> str:
    if "_" in station_json_bus:
        bus_key = station_json_bus.split("_")[0]
    else:
        bus_key = station_json_bus
    return bus_key


def get_station_json_bus_info(station_json_bus: str) -> Dict[str, str]:
    """
    Get transport_name like in station_json ex: (t10a_r, 44_f, 35, t10)
    Return dict bus_key - like BUS_JSON.keys() and route type
    """
    bus_key = convert_station_json_bus_to_bus_key(station_json_bus)
    if "f" in station_json_bus:
        route_type = "straight"
    elif "r" in station_json_bus:
        route_type = "reverse"
    else:
        route_type = "both"
    result = {"bus_key": bus_key, "route_type": route_type}
    return result


def convert_station_json_bus_info_to_label(station_json_bus: str) -> str:
    """
    Return list of labels for transport from station_json[station_name] list
    (convert data like t10A_r or 44_f or 35 to labels)
    """
    bus_info = get_station_json_bus_info(station_json_bus)
    if station_json_bus.startswith("t"):
        icon = TROLLEY_ICON
    else:
        icon = BUS_ICON
    if bus_info["route_type"] == "reverse":
        icon += REVERSE_ICON
    elif bus_info["route_type"] == "straight":
        icon += STRAIGHT_ICON
    result = f"{icon} {convert_bus_key_to_bus_number(bus_info['bus_key'])}"
    return result


def get_station_json_bus_list_for_station(station_key: str) -> Optional[List[str]]:
    result = STATION_JSON.get(station_key)
    if result:
        return result
    else:
        return None


def station_json_bus_sort(bus_list: List[str]) -> List[str]:
    buses: List[str] = []
    trolleys: List[str] = []
    for bus in bus_list:
        if not bus.startswith("t"):
            buses.append(bus)
        else:
            trolleys.append(bus)
    buses.sort(key=lambda x: int(re.findall(r"\d+", x.split("_")[0])[0]))
    trolleys.sort(key=lambda x: int(re.findall(r"\d+", x.split("_")[0][1:])[0]))
    buses.extend(trolleys)
    return buses
