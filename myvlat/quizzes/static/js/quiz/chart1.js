// set the dimensions and margins of the graph
var maxWidth = $(window).width()
if (maxWidth > 700){
  maxWidth = 700;
}
else{
  maxWidth = 500;
}

var margin = {top: 20, right: 30, bottom: 65, left: 70},
  width = maxWidth - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#vlat1")
.append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
.append("g")
  .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")"); 

d3.csv("https://raw.githubusercontent.com/nini12091/vlat/main/vlat1.csv", 
// When reading the csv, I must format variables:

function(data){

  // Add X axis 
  var x = d3.scaleBand()
    .range([ 0, width ])
    .domain(data.map(function(d) { return d.month;} ))
    .padding(0.2);
  svg.append('g')
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x))
    .selectAll("text")
    .attr("font-size", "15px")
    .attr("transform", "translate(10,0)")
    .style("text-anchor", "end");

  // Add Y axis
  var y = d3.scaleLinear()
    .domain([34, 66])
    .range([ height, 0 ]);
  svg.append("g")
    .call(d3.axisLeft(y))
    .attr("font-size", "15px");

  // gridlines in x axis function
  function make_x_gridlines() {		
    return d3.axisBottom(x)
      .ticks(5)
  }

  // gridlines in y axis function
  function make_y_gridlines() {		
      return d3.axisLeft(y)
          .ticks(5)
  }

  // Add X axis name
  svg.append("text")
    .attr("y", 385 + margin.bottom)
    .attr("x",(width / 2))
    .attr("dy", "1em") 
    .attr("font-size", "15px")
    .style("text-anchor", "middle")
    .text("월(month)");

  // Add Y axis name
  svg.append("text")
    .attr('transform','rotate(-90)')
    .attr("y", 20 - margin.left)
    .attr("x",0 - (height / 2))
    .attr("dy", "1em") 
    .attr("font-size", "15px")
    .style("text-anchor", "middle")
    .text("석유 가격(달러)");

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

  // Add the line
  svg.append('path')
    .datum(data)
    .attr('fill','none')
    .attr('stroke', '#1E90FF')
    .attr('stroke-width',2)
    .attr('d',d3.line()
      .x(function(d) {return x(d.month) + 20})
      .y(function(d) {return y(d.value)})
      )

  // Add the points
  svg
    .append('g')
    .selectAll('dot')
    .data(data)
    .enter()
    .append('circle')
      .attr('cx', function(d) {return x(d.month) +20})
      .attr('cy', function(d) {return y(d.value)})
      .attr('r', 2)
      .attr('fill','#1E90FF')

})
  