
function drawRoutesPerStopChart() {
	$.get("/most_routes_at_stop")
		.then(function(ajaxData){ 
			// Create the data table.
			var data = new google.visualization.DataTable();
			data.addColumn('string', 'Bus Stop');
			data.addColumn('number', 'Routes');
			data.addRows(ajaxData);

			// Set chart options
			var options = {'title':'Bus Stops With The Most Routes',
						   'width':800,
						   'height':600};

			// Instantiate and draw our chart, passing in some options.
			var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
			chart.draw(data, options);
  });
}

function drawLongestRoutesChart() {
	$.get("/longest_routes")
		.then(function(ajaxData){ 
			// Create the data table.
			var data = new google.visualization.DataTable();
			data.addColumn('string', 'Route');
			data.addColumn('number', 'Number of Stops');
			data.addRows(ajaxData);

			// Set chart options
			var options = {'title':'Longest Bus Routes',
						   'width':800,
						   'height':600};

			// Instantiate and draw our chart, passing in some options.
			var chart = new google.visualization.BarChart(document.getElementById('chart_div2'));
			chart.draw(data, options);
  });
}
  
function drawBoardingsChart() {
	$.get("/most_boardings")
		.then(function(ajaxData){ 
			// Create the data table.
			var data = new google.visualization.DataTable();
			data.addColumn('string', 'Stop');
			data.addColumn('number', 'Boardings');
			data.addColumn('number', 'Alightings')
			data.addRows(ajaxData);

			// Set chart options
			var options = {'title':'Stops Wih Most Boardings',
						   'width':800,
						   'height':600};

			// Instantiate and draw our chart, passing in some options.
			var chart = new google.visualization.BarChart(document.getElementById('chart_div3'));
			chart.draw(data, options);
  });
}

function drawAlightingsChart() {
	$.get("/most_alightings")
		.then(function(ajaxData){ 
			// Create the data table.
			var data = new google.visualization.DataTable();
			data.addColumn('string', 'Stop');
			data.addColumn('number', 'Alightings');
			data.addColumn('number', 'Boardings')
			data.addRows(ajaxData);

			// Set chart options
			var options = {'title':'Stops With Most Alightings',
						   'width':800,
						   'height':600};

			// Instantiate and draw our chart, passing in some options.
			var chart = new google.visualization.BarChart(document.getElementById('chart_div4'));
			chart.draw(data, options);
  });
}

function drawTransfersChart() {
	$.get("/rail_transfers")
		.then(function(ajaxData){ 
			// Create the data table.
			var data = new google.visualization.DataTable();
			data.addColumn('string', 'Rail Line Transferred To');
			data.addColumn('number', 'Number of Transfers');
			data.addRows(ajaxData);
			
			// Set chart options
			var options = {'title':'Transfers To Train By Rail Line',
						   'width':800,
						   'height':600,
						   'colors': ['#f9461c', '#565a5c', '#c60c30', '#62361b', '#00a1de', '#009b3a', '#522398']
						   };

			// Instantiate and draw our chart, passing in some options.
			var chart = new google.visualization.PieChart(document.getElementById('piechart'));
			chart.draw(data, options);
  });
}

function drawTransfersFromChart() {
	$.get("/transfers_from_train")
		.then(function(ajaxData){ 
			// Create the data table.
			var data = new google.visualization.DataTable();
			data.addColumn('string', 'Rail Line Transferred To');
			data.addColumn('number', 'Number of Transfers');
			data.addRows(ajaxData);
			
			// Set chart options
			var options = {'title':'Transfers From Train By Rail Line',
						   'width':800,
						   'height':600,
						   'colors': ['#565a5c', '#00a1de', '#62361b', '#009b3a', '#f9461c', '#c60c30', '#522398']
						   };

			// Instantiate and draw our chart, passing in some options.
			var chart = new google.visualization.PieChart(document.getElementById('piechart2'));
			chart.draw(data, options);
  });
}

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawRoutesPerStopChart);
google.charts.setOnLoadCallback(drawLongestRoutesChart);
google.charts.setOnLoadCallback(drawBoardingsChart);
google.charts.setOnLoadCallback(drawAlightingsChart);
google.charts.setOnLoadCallback(drawTransfersChart);
google.charts.setOnLoadCallback(drawTransfersFromChart);