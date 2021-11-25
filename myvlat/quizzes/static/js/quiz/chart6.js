// set the dimensions and margins of the graph
var margin = {top: 20, right: 20, bottom: 65, left: 80},
  width = 700 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#vlat6")
.append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform",
      "translate(" + margin.left + "," + margin.top + ")"); 

d3.csv("https://raw.githubusercontent.com/nini12091/vlat/main/vlat6.csv", 

function(data) {

// Add X axis
var x = d3.scaleLinear()
    .domain([3.0,5.0])
    .range([0, width])
svg.append("g")
  .attr("transform", "translate(0," + height + ")")
  .call(d3.axisBottom(x))
  .attr("font-size", "14px");

// Add histogram axis
var histogram = d3.histogram()
  .value(function(d) { return d.rank; })
  .domain(x.domain())
  .thresholds(x.ticks(10));

// And apply this function to data to get the bins
var bins = histogram(data);

// Y axis: scale and draw:
var y = d3.scaleLinear()
    .range([height, 0])
    .domain([0,350]);   // d3.hist has to be called before the Y axis obviously
svg.append("g")
    .call(d3.axisLeft(y))
    .attr("font-size", "14px");

// gridlines in y axis function
function make_y_gridlines() {		
    return d3.axisLeft(y)
        .ticks(10)
}

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
  .text("택시 등급");

// Add Y axis name
svg.append("text")
  .attr('transform','rotate(-90)')
  .attr("y", 20 - margin.left)
  .attr("x",0 - (height / 2))
  .attr("dy", "1em") 
  .attr("font-size", "15px")
  .style("text-anchor", "middle")
  .text("인원 수");

// append the bar rectangles to the svg element
svg.selectAll("rect")
    .data(bins)
    .enter()
    .append("rect")
      .attr("x", 1)
      .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
      .attr("width", function(d) { return x(d.x1) - x(d.x0) -2 ; })
      .attr("height", function(d) { return height - y(d.length); })
      .style("fill", "#6495ED")

})