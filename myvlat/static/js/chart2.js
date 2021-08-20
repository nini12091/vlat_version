// set the dimensions and margins of the graph
var margin = {top: 20, right: 30, bottom: 100, left: 70},
  width = 700 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#vlat2")
.append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform",
      "translate(" + margin.left + "," + margin.top + ")"); 

d3.csv("https://raw.githubusercontent.com/nini12091/vlat/main/vlat2.csv", 

function(data){

// Add X axis 
var x = d3.scaleBand()
  .range([ 0, width ])
  .domain(data.map(function(d) { return d.country; } ))
  .padding(0.2);
svg.append("g")
  .attr("transform", "translate(0," + height + ")")
  .call(d3.axisBottom(x))
  .selectAll("text")
  .attr("font-size", "14px")
  .attr("transform", "translate(-12,0)" + "rotate(-65)")
  .style("text-anchor", "end");

// Add Y axis  
var y = d3.scaleLinear()
  .domain([0, 22])
  .range([ height, 0]);
svg.append("g")
  .call(d3.axisLeft(y))
  .attr("font-size", "14px");

// gridlines in y axis function
function make_y_gridlines() {		
    return d3.axisLeft(y)
        .ticks(10)
}

  // Add X axis name
svg.append("text")
  .attr("y", 342 + margin.bottom)
  .attr("x",(width / 2))
  .attr("dy", "1em") 
  .attr("font-size", "14px")
  .style("text-anchor", "middle")
  .text("국가");

// Add Y axis name
svg.append("text")
  .attr('transform','rotate(-90)')
  .attr("y", 20 - margin.left)
  .attr("x",0 - (height / 2))
  .attr("dy", "1em") 
  .attr("font-size", "14px")
  .style("text-anchor", "middle")
  .text("인터넷 평균 속도");

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

// Bars
svg.selectAll("mybar")
  .data(data)
  .enter()
  .append("rect")
    .attr("x", function(d) { return x(d.country); })
    .attr("y", function(d) { return y(d.value); })
    .attr("width", x.bandwidth())
    .attr("height", function(d) { return height - y(d.value); })
    .attr("fill", "#4682B4")

})