bus.json structure:  {
	"bus_number" : [
			["bus_route", ["station1", "station2" ... ]], 
			["bus_reverse_route", ["station1", "station2" ...]]
		       ],
	
	"bus_number" : ... 
	
  }


station.json structure: {
	"station_name" : ['bus_number', 'bus_number_r', 'bus_number_f', ...],
	"station_name" : ...
  }
  

Here - bus_number - Visit the station both in the forward and backward directions.
	bus_number_r - Visit the station exclusively on the reverse route.
	bus_number_f - Visit the station exclusively on the straight route.
	

