import sqlite3
import re

num_routes = '''SELECT stop_id
			,on_street
			,cross_street
			,COUNT(*) AS num_routes 
			 FROM stop_routes 
			 JOIN stops ON stops.id = stop_id
			 GROUP BY stop_id 
			 ORDER BY num_routes DESC LIMIT 10'''

longest_route = '''SELECT route
			,on_street
			,COUNT(*) AS num_stops
			 FROM stop_routes 
			 JOIN stops ON stops.id = stop_id
			 GROUP BY route 
			 ORDER BY num_stops DESC LIMIT 10'''

most_boardings = '''SELECT stop_id
				,on_street
				,cross_street
				,boardings
				,alightings
				FROM boardings
				JOIN stops ON stops.id = stop_id
				ORDER BY boardings DESC LIMIT 10'''

most_alightings = '''SELECT stop_id
				,on_street
				,cross_street
				,alightings
				,boardings
				FROM boardings
				JOIN stops ON stops.id = stop_id
				ORDER BY alightings DESC LIMIT 10'''

rail_transfers = '''SELECT
					GET_STATION(cross_street) AS line
					,SUM(alightings)
					FROM stops
					JOIN boardings ON stop_id = stops.id
					WHERE cross_street LIKE '%blue%line%' 
					OR cross_street LIKE '%red%line%'
					OR cross_street LIKE '%brown%line%'
					OR cross_street LIKE '%purple%line%'
					OR cross_street LIKE '%green%line%'
					OR cross_street LIKE '%orange%line%'
					GROUP BY line
					ORDER BY alightings DESC'''
					
rail_transfers_from_train = '''SELECT
					GET_STATION(cross_street) AS line
					,SUM(boardings)
					FROM stops
					JOIN boardings ON stop_id = stops.id
					WHERE cross_street LIKE '%blue%line%' 
					OR cross_street LIKE '%red%line%'
					OR cross_street LIKE '%brown%line%'
					OR cross_street LIKE '%purple%line%'
					OR cross_street LIKE '%green%line%'
					OR cross_street LIKE '%orange%line%'
					GROUP BY line
					ORDER BY boardings DESC'''
	
def get_station(stop):
	#For now, can't separate multiple line stations into their own values, since we have no way of knowing which train someone wants to catch
	hub_regex = r'.*(blue|red|orange|green|brown|purple|yellow)/((blue|red|orange|green|brown|purple|yellow).*line).*'
	if re.match(hub_regex, stop, re.IGNORECASE) is not None:
		result = "Multiple Lines"
	else:
		regex = r'.*((blue|red|orange|green|brown|purple|yellow).*line).*'
		result = re.match(regex, stop, re.IGNORECASE).group(1)
	return result
	
def add_get_station_fn(conn):
	conn.create_function('GET_STATION', 1, get_station)
						
if __name__ == '__main__':
	DB_NAME = 'database/test2.db'
	conn = sqlite3.connect(DB_NAME)
	add_get_station_fn(conn)
	c = conn.cursor()
	c.execute(rail_transfers_from_train)
	results = c.fetchall()
	print(results)
	conn.close()
