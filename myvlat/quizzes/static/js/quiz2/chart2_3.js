// set the dimensions and margins of the graph
var margin = {top: 20, right: 30, bottom: 70, left: 70},
  width = 700 - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#vlat2_3")
.append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform",
      "translate(" + margin.left + "," + margin.top + ")"); 

d3.csv("https://raw.githubusercontent.com/nini12091/vlat2/main/vlat2_3.csv", 

function(data) {

var subgroups = data.columns.slice(1)

var citys = d3.map(data, function(d){return(d.city)}).keys()

// Add X axis
var x = d3.scaleBand()
    .domain(citys)
    .range([0, width])
    .padding([0.2])
svg.append("g")
  .attr("transform", "translate(0," + height + ")")
  .call(d3.axisBottom(x).tickSizeOuter(0))
  .attr("font-size", "14px");

// Add Y axis
var y = d3.scaleLinear()
  .domain([0, 60])
  .range([ height, 0 ]);
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

// color palette = one color per subgroup
var color = d3.scaleOrdinal()
  .domain(subgroups)
  .range(['#0072B2','#009E73','#D55E00','#CC79A7','#E69F00'])

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
  .attr("x", 530)
  .attr("y", 4)
  .attr("width", 15)
  .attr("height", 15)
  .style("fill", color );

//색상 text
subgroupitem.append("text")
  .attr("x", 550)
  .attr("y", 10)
  .attr("font-size", "13px")
  .attr("dy", ".55em")
  .style("text-anchor", "start")
  .text(function(d) { return d; });

// Add X axis name
svg.append("text")
  .attr("y", 370 + margin.bottom)
  .attr("x",(width / 2))
  .attr("dy", "1em") 
  .attr("font-size", "15px")
  .style("text-anchor", "middle")
  .text("대한민국 시/도");

// Add Y axis name
svg.append("text")
  .attr('transform','rotate(-90)')
  .attr("y", 20 - margin.left)
  .attr("x",0 - (height / 2))
  .attr("dy", "1em") 
  .attr("font-size", "15px")
  .style("text-anchor", "middle")
  .text("호텔 룸서비스 비용");

// Show the bars
svg.append("g")
  .selectAll("g")
  // Enter in the stack data = loop key per key = group per group
  .data(stackedData)
  .enter().append("g")
    .attr("fill", function(d) { return color(d.key); })
    .style("opacity", 0.9)
    .selectAll("rect")
    // enter a second time = loop subgroup per subgroup to add all rectangles
    .data(function(d) { return d; })
    .enter().append("rect")
      .attr("x", function(d) { return x(d.data.city); })
      .attr("y", function(d) { return y(d[1]); })
      .attr("height", function(d) { return y(d[0]) - y(d[1]); })
      .attr("width",x.bandwidth())

})