// set the dimensions and margins of the graph
var margin = {top: 20, right: 20, bottom: 90, left: 80},
  width = 700 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#vlat2_8")
.append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform",
      "translate(" + margin.left + "," + margin.top + ")"); 

d3.csv("https://raw.githubusercontent.com/nini12091/vlat2/main/vlat2_8.csv", 

function(data){

// Add X axis 
const x = d3.scaleBand()
  .range([ 0, width])
  .domain(data.map(function(d) { return d.month; }))
  .padding(1);
svg.append("g")
  .attr("transform", "translate(0," + height +")")
  .call(d3.axisBottom(x))
  .selectAll("text")
  .attr("font-size", "14px")
  .attr("transform", "translate(-12,0)" + "rotate(-65)")
  .style("text-anchor", "end");

// Add Y axis  
var y = d3.scaleLinear()
  .domain([4.2, 6.2])
  .range([ height, 0]);
svg.append("g")
  .call(d3.axisLeft(y))
  .attr("font-size", "14px");

// gridlines in x axis function
function make_x_gridlines() {		
  return d3.axisBottom(x)
    .ticks(20)
}

// gridlines in y axis function
function make_y_gridlines() {		
    return d3.axisLeft(y)
      .ticks(10)
}

  // Add X axis name
svg.append("text")
  .attr("y", 350 + margin.bottom)
  .attr("x",(width / 2))
  .attr("dy", "1em") 
  .attr("font-size", "15px")
  .style("text-anchor", "middle")
  .text("월(month)");

// Add Y axis name
svg.append("text")
  .attr('transform','rotate(-90)')
  .attr("y", 25 - margin.left)
  .attr("x",0 - (height / 2))
  .attr("dy", "1em") 
  .attr("font-size", "15px")
  .style("text-anchor", "middle")
  .text("커피 원두 가격");

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

svg.append("path")
  .datum(data)
  .attr("fill", "#4682B4")
  .attr("stroke", "#4682B4")
  .attr("stroke-width", 1.5)
  .style("opacity", 0.7)
  .attr("d", d3.area()
    .x(function(d) { return x(d.month) })
    .y0(y(4.2))
    .y1(function(d) { return y(d.price) })
    )
})