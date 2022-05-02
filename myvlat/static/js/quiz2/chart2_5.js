// set the dimensions and margins of the graph
var margin = 30
width = 690
height = 500

var radius = Math.min(width, height) / 2 - margin

var svg = d3.select("#vlat2_5")
.append("svg")
.attr("width", width)
.attr("height", height)
.append("g")
.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

var color = d3.scaleOrdinal(['#A52A2A','#4682B4','#808000','#6A5ACD','#FF8C00','#B0B5B5']);

var pie = d3.pie()
.sort(null)
.value(function(d) { return d.percent; });

var path = d3.arc()
.outerRadius(radius - 10)
.innerRadius(0);

var label = d3.arc()
.outerRadius(radius + 20)
.innerRadius(radius);

d3.csv("https://raw.githubusercontent.com/nini12091/vlat2/main/vlat2_5.csv", 

function(d) {

d.percent = +d.percent;
return d;
}, function(error, data){
if (error) throw error;

var arc = svg.selectAll(".arc")
  .data(pie(data))
  .enter().append("g")
    .attr("class", "arc");

arc.append("path")
    .attr("d", path)
    .attr("fill", function(d) { return color(d.data.company); })

arc.append("text")
    .attr("transform", function(d) { return "translate(" + label.centroid(d) + ")"; })
    .attr("dx", "-1em")
    .attr("font-size", "18px")
    .attr("dy", "0.5em")
    .text(function(d) { return d.data.company; });
  
  
});