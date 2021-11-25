// set the dimensions and margins of the graph
var margin = {top: 20, right: 20, bottom: 65, left: 95},
  width = 700 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#vlat2_9")
.append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform",
      "translate(" + margin.left + "," + margin.top + ")"); 

d3.csv("https://raw.githubusercontent.com/nini12091/vlat2/main/vlat2_9.csv", 

function(data) {

var subgroups = data.columns.slice(1)

// Add X axis
var x = d3.scaleLinear()
    .domain([2016,2021])
    .range([0, width-60])
svg.append("g")
  .attr("transform", "translate(0," + height + ")")
  .call(d3.axisBottom(x).ticks(6).tickFormat(d3.format("d")))
  .attr("font-size", "14px");

// Add Y axis
var y = d3.scaleLinear()
  .domain([0, 16000])
  .range([ height, 0 ]);
svg.append("g")
  .call(d3.axisLeft(y))
  .attr("font-size", "14px");

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

// color palette = one color per subgroup
var color = d3.scaleOrdinal()
  .domain(subgroups)
  .range(['#4169E1','#6495ED','#ADD8E6'])

//stack the data? --> stack per subgroup
var stackedData = d3.stack()
  .keys(subgroups)
  (data)

// 색상 정보
var subgroupitem = svg.selectAll(".subgroupitem")
  .data(data.columns.slice(1).reverse())
  .enter().append("g")
        .attr("class", "subgroupitem")
        .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

// 색상 모형
subgroupitem.append("rect")
  .attr("x", 535)
  .attr("y", 4)
  .attr("width", 15)
  .attr("height", 15)
  .style("fill", color );

//색상 text
subgroupitem.append("text")
  .attr("x", 555)
  .attr("y", 9)
  .attr("font-size", "14px")
  .attr("dy", ".55em")
  .style("text-anchor", "start")
  .text(function(d) { return d; });

// Add X axis name
svg.append("text")
  .attr("y", 380 + margin.bottom)
  .attr("x",(width / 2))
  .attr("dy", "1em") 
  .attr("font-size", "15px")
  .style("text-anchor", "middle")
  .text("연도");

// Add Y axis name
svg.append("text")
  .attr('transform','rotate(-90)')
  .attr("y", 20 - margin.left)
  .attr("x",0 - (height / 2))
  .attr("dy", "1em") 
  .attr("font-size", "15px")
  .style("text-anchor", "middle")
  .text("인원 수");

// Show the area
svg
  .selectAll("mylayers")
  .data(stackedData)
  .enter()
  .append("path")
    .style("fill", function(d) { return color(d.key); })
    .style("opacity", 0.6)
    .attr("d", d3.area()
      .x(function(d, i) { return x(d.data.year); })
      .y0(function(d) { return y(d[0]); })
      .y1(function(d) { return y(d[1]); })
  )

})