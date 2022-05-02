// set the dimensions and margins of the graph
var margin = {top: 0, right: 30, bottom: 35, left: 100},
width = 700 - margin.left - margin.right,
height = 500 - margin.top - margin.bottom;

var initialScale = 4500;

// The svg
var svg = d3.select("#vlat2_11").append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)

var path = d3.geoPath();

// Map and projection
var projection = d3.geoMercator()
.center([127, 36])
.scale(initialScale)
.translate([width/2 , height/2]);

var data = d3.map();
var colorScale = d3.scaleThreshold()
.domain([2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
.range(d3.schemeOranges[7]);

d3.queue()
.defer(d3.json, "https://raw.githubusercontent.com/nini12091/vlat2/main/vlat2_11(korea).json")
.defer(d3.csv, "https://raw.githubusercontent.com/nini12091/vlat2/main/vlat2_11.csv", function(d) { data.set(d.name, +d.loss); })
.await(ready);

function ready(error, topo){

// Draw the map
svg.append("g")
    .selectAll("path")
    .data(topo.features)
    .enter()
    .append("path")
        .style("stroke", "gray")
        .attr("d", d3.geoPath()
            .projection(projection)
            )
        .attr("fill", function (d) {
            d.total = data.get(d.properties.name) || 0;
            return colorScale(d.total);
            });


svg.append("g")
    .selectAll("text")
    .data(topo.features)
    .enter()
    .append("text")
    .attr("transform", translateTolabel)
    .attr('text-anchor', 'middle')
    .attr("font-size", "13px")
    .attr("fill", "black")
    .text(function(d) { return d.properties.name; });

function translateTolabel(d) {
    var arr = d3.geoPath().projection(projection).centroid(d);
    if (d.properties.code == 31) {
        //서울 경기도 이름 겹쳐서 경기도 내리기
        arr[1] +=
            d3.event && d3.event.scale
                ? d3.event.scale / height + 20
                : initialScale / height + 20;
    } else if (d.properties.code == 34) {
        //충남은 조금 더 내리기
        arr[1] +=
            d3.event && d3.event.scale
                ? d3.event.scale / height + 5
                : initialScale / height + 5;
    } else if (d.properties.code == 25) {
        //대전광역시 내리기
        arr[1] +=
            d3.event && d3.event.scale
                ? d3.event.scale / height + 5
                : initialScale / height + 5;
    }else if (d.properties.code == 11) {
        //서울특별시 내리기
        arr[1] +=
            d3.event && d3.event.scale
                ? d3.event.scale / height + 1
                : initialScale / height + 1;
    }
    return 'translate(' + arr + ')';
} 

var x = d3.scaleLinear()
    .domain([2.0,5.0])
    .range([0,width/3]);

var xAxis = d3.axisBottom(x)
    .tickSize(13)
    .tickValues(colorScale.domain())

svg.select("g")
    .call(xAxis)
    .attr("font-size", "13px")

svg.append("g")
    .selectAll("rect")
    .data(colorScale.range().map(function(color) {
        var d = colorScale.invertExtent(color);
        if (d[0] == null) d[0] = x.domain()[0];
        if (d[1] == null) d[1] = x.domain()[1];
        return d;
    }))
    .enter().insert("rect", ".tick")
        .attr("height", 10)
        .attr("x", function(d) { return x(d[0]); })
        .attr("y", 0)
        .attr("width", function(d) { return x(d[1]) - x(d[0]); })
        .attr("fill", function(d) { return colorScale(d[0]); });

}