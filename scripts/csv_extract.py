import csv
import re
import sqlite3

db_file = 'test2.db'

stops_insert_sql = "INSERT INTO stops (id, on_street, cross_street, extra_info, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?)"
routes_insert_sql = "INSERT INTO stop_routes (stop_id, route) VALUES (?, ?)"
boardings_insert_sql = "INSERT INTO boardings (stop_id, boardings, alightings) VALUES (?, ?, ?)"	

def insert(cursor, row, programMode):
	if programMode == 'test':
		print(' '.join(row['routes']))
		print(row['stop_id'], row['on_street'], row['cross_street'], row['extra_info'], str(row['latitude']), str(row['longitude']))
		print(row['stop_id'], str(row['boardings']), str(row['alightings']))
	elif programMode == 'prod':
		print("Inserting row...", row['stop_id'], row['on_street'], row['cross_street'])
		try:
			cursor.execute(stops_insert_sql, (row['stop_id'], row['on_street'], row['cross_street'], row['extra_info'], row['latitude'], row['longitude']))
			cursor.execute(boardings_insert_sql, (row['stop_id'], row['boardings'], row['alightings']))
			routeInsertValues = [(row['stop_id'], route) for route in row['routes']]
			cursor.executemany(routes_insert_sql, routeInsertValues)
		except:
			print("Something went wrong!")

def run(programMode):
	extra_info_pattern = re.compile('\(.*\)')
	
	print("Connecting to database...")
	conn = sqlite3.connect(db_file)
	c = conn.cursor()	

	with open('CTA_-_Ridership_-_Avg._Weekday_Bus_Stop_Boardings_in_October_2012.csv', newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
					stop_id = row['stop_id']
					on_street = row['on_street']
					cross_street = row['cross_street']
					location = row['location']
					routes = row['routes']
					extra_info = ''
					boardings = row['boardings']
					alightings = row['alightings']

					#Sanitize data
					#Separate extra cross street info into separate field
					match = extra_info_pattern.search(cross_street)
					if match != None:
							extra_info = match.group(0).strip('()')
							cross_street = extra_info_pattern.sub('', cross_street)
					#Separate latitude and longitude
					latitude, longitude = row['location'].strip('()').split(', ')
					#Split routes (perform separate insert into other table for each route)
					routes = routes.split(',')
					#Title case street names
					on_street = on_street.lower().title()
					cross_street = cross_street.lower().title()

					#TODO insert into DB
					row = { 'stop_id': stop_id,
							'on_street': on_street,
							'cross_street': cross_street,
							'extra_info': extra_info,
							'latitude': float(latitude),
							'longitude': float(longitude),
							'routes': routes,
							'boardings': float(boardings),
							'alightings': float(alightings)
						  }
					insert(c, row, programMode)
				
	conn.commit()
	conn.close()

if __name__ == '__main__':
	programMode = 'prod'
	run(programMode)