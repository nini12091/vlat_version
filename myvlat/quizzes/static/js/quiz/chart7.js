// set the dimensions and margins of the graph
var margin = {top: 20, right: 20, bottom: 65, left: 80},
  width = 700 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#vlat7")
.append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform",
      "translate(" + margin.left + "," + margin.top + ")"); 

d3.csv("https://raw.githubusercontent.com/nini12091/vlat/main/vlat7.csv", 

function(data){

// Add X axis 
const x = d3.scaleLinear()
  .range([ 0, width ])
  .domain([160, 200])
svg.append("g")
  .attr("transform", "translate(0," + height +")")
  .call(d3.axisBottom(x))
  .attr("font-size", "14px")

// Add Y axis  
var y = d3.scaleLinear()
  .domain([40, 130])
  .range([ height, 0]);
svg.append("g")
  .call(d3.axisLeft(y))
  .attr("font-size", "14px");

// gridlines in x axis function
function make_x_gridlines() {		
  return d3.axisBottom(x)
    .ticks(8)
}

// gridlines in y axis function
function make_y_gridlines() {		
    return d3.axisLeft(y)
      .ticks(10)
}

  // Add X axis name
svg.append("text")
  .attr("y", 380 + margin.bottom)
  .attr("x",(width / 2))
  .attr("dy", "1em") 
  .attr("font-size", "15px")
  .style("text-anchor", "middle")
  .text("키(cm)");

// Add Y axis name
svg.append("text")
  .attr('transform','rotate(-90)')
  .attr("y", 20 - margin.left)
  .attr("x",0 - (height / 2))
  .attr("dy", "1em") 
  .attr("font-size", "15px")
  .style("text-anchor", "middle")
  .text("몸무게(kg)");

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

svg.append('g')
  .selectAll("dot")
  .data(data)
  .enter()
  .append("circle")
    .attr("cx", function (d) { return x(d.height); } )
    .attr("cy", function (d) { return y(d.weight); } )
    .attr("r", 5)
    .attr('stroke', 'gray')
    .style("fill", "#1E90FF")
})