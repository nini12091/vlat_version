// set the dimensions and margins of the graph
var margin = {top: 20, right: 30, bottom: 65, left: 80},
  width = 700 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#vlat2_10")
.append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform",
      "translate(" + margin.left + "," + margin.top + ")"); 

d3.csv("https://raw.githubusercontent.com/nini12091/vlat2/main/vlat2_10.csv", 

  function(data) {

  // Add X axis
  var x = d3.scaleLinear()
      .domain([120,450])
      .range([0, width-90])
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x))
    .attr("font-size", "14px");

  // Add Y axis
  var y = d3.scaleLinear()
    .domain([120, 600])
    .range([ height, 0 ]);
  svg.append("g")
    .call(d3.axisLeft(y))
    .attr("font-size", "14px");

  // Add Z axis
  var z = d3.scaleLinear()
    .domain([1.5, 3.5])
    .range([12, 30]);

  var sizeLegend = d3.legendSize()
    .scale(z)
    .shape("circle")
    .shapePadding(20)
    .cells(3)
    .labelOffset(5);


  // gridlines in x axis function
  function make_x_gridlines() {		
    return d3.axisBottom(x)
      .ticks(6)
  }

  // gridlines in y axis function
  function make_y_gridlines() {		
      return d3.axisLeft(y)
          .ticks(10)
  }

  // add the X gridlines
  svg.append("g")			
    .attr("class", "grid")
    .attr("transform", "translate(0," + height + ")")
    .attr('fill','none')
    .attr('stroke', '#DCDCDC')
    .attr('stroke-width',0.1)
    .attr('shape-rendering','crispEdges')
    .call(make_x_gridlines()
        .tickSize(-height)
        .tickFormat("")
    )

  // add the Y gridlines
  svg.append("g")			
    .attr("class", "grid")
    .attr('fill','none')
    .attr('stroke', '#DCDCDC')
    .attr('stroke-width',0.1)
    .attr('shape-rendering','crispEdges')
    .call(make_y_gridlines()
        .tickSize(-width)
        .tickFormat("")
    )

  // Add X axis name
  svg.append("text")
    .attr("y", 380 + margin.bottom)
    .attr("x",(width / 2))
    .attr("dy", "1em") 
    .attr("font-size", "15px")
    .style("text-anchor", "middle")
    .text("총 지하철 역의 수");

  // Add Y axis name
  svg.append("text")
    .attr('transform','rotate(-90)')
    .attr("y", 20 - margin.left)
    .attr("x",0 - (height / 2))
    .attr("dy", "1em") 
    .attr("font-size", "15px")
    .style("text-anchor", "middle")
    .text("지하철의 길이");

  // Show the dot
  svg.append('g')
    .selectAll("dot")
    .data(data)
    .enter()
    .append("circle")
      .attr("cx", function (d) { return x(d.station); } )
      .attr("cy", function (d) { return y(d.t_length); } )
      .attr("r", function (d) {return z(d.ridership); } )
      .style("fill", "#4682B4")
      .style("opacity", "0.7")
      .attr("stroke", "black")

  // Show the text
  svg
    .selectAll("legend")
    .data(data)
    .enter()
    .append("text")
      .attr('x', function(d) { return x(d.station) + 15})
      .attr('y', function(d) { return y(d.t_length) + 15 } )
      .text( function(d){ return d.country } )
      .style("font-size", 13)
      .style("font-weight", "bold")
      .attr('alignment-baseline', 'middle')

  svg.append("g")
    .attr("transform", "translate(530, 35)")
    .attr('stroke', 'black')
    .attr('stroke-width',1)
    .attr('fill','none')
    .call(sizeLegend);

  svg.append("text")
    .attr("x", 510)
    .attr("y", 20)
    .attr("font-size", "14px")
    .text("지하철 이용률");

})