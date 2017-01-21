import sqlite3
from flask import Flask, jsonify, render_template
import queries

DB_NAME = 'database/test2.db'

conn = sqlite3.connect(DB_NAME)
c = conn.cursor()
queries.add_get_station_fn(conn)

app = Flask(__name__)

def query_results(query):
	c.execute(query)
	results = c.fetchall()
	return results

@app.route('/most_routes_at_stop')
def get_most_routes_at_stop():
	queryList = query_results(queries.num_routes)
	results = [[l[1] + " and " +l[2], l[3]] for l in queryList]
	return jsonify(results)
	

@app.route('/longest_routes')
def longest_routes():
	queryList = query_results(queries.longest_route)
	results = [["#" + l[0] + " - " + l[1], l[2]] for l in queryList]
	return jsonify(results)

@app.route('/most_boardings')
def most_boardings():
	queryList = query_results(queries.most_boardings)
	results = [[l[1] + " and " +l[2], l[3], l[4]] for l in queryList]
	return jsonify(results)
	
@app.route('/most_alightings')
def most_alightings():
	queryList = query_results(queries.most_alightings)
	results = [[l[1] + " and " +l[2], l[3], l[4]] for l in queryList]
	return jsonify(results)
	
@app.route('/rail_transfers')
def rail_transfers():
	queryList = query_results(queries.rail_transfers)
	results = [[l[0], l[1]] for l in queryList]
	return jsonify(results)
	
@app.route('/transfers_from_train')
def rail_transfers_from_train():
	queryList = query_results(queries.rail_transfers_from_train)
	results = [[l[0], l[1]] for l in queryList]
	return jsonify(results)

@app.route('/')
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.run()