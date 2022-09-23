// Initialize websocket connection
var socket = io.connect('ec2-3-90-249-25.compute-1.amazonaws.com:3000');

// Create charts

// Rata-Rata Line Chart

var avgSuhu;
var avgSuhuData = [
    {
      values: [],      //representasi nilai titik x dan y
      key: 'Avg Suhu', //Nilai serinya di chart
      color: '#7cb342'
    }
    ];

nv.addGraph(function(){
    avgSuhu = nv.models.lineChart()
                  .margin({left: 50, right: 30})
                  .useInteractiveGuideline(true)
                  .showLegend(true)
                  .showYAxis(true)
                  .showXAxis(true);

    avgSuhu.xAxis
            .axisLabel('Time')
            .tickFormat(function(d){return d3.time.format('%H:%M:%S')(new Date(d));});

    avgSuhu.yAxis
            .axisLabel('Rata-rata')
            .tickFormat(d3.format('.2f'));

    d3.select('#avgsuhu')
        .append('svg')
        .datum(avgSuhuData)
        .transition().duration(100)
        .call(avgSuhu);

    nv.utils.windowResize(function() { avgSuhu.update(); });
    return avgSuhu;
});

var avgKelembapan;
var avgKelembapanData = [
    {
      values: [],      //values - represents the array of {x,y} data points
      key: 'Avg Kelembapan', //key  - the name of the series.
      color: '#7cb342'  //color - optional: choose your own line color.
    }
    ];

nv.addGraph(function(){
    avgKelembapan = nv.models.lineChart()
                  .margin({left: 50, right: 30})
                  .useInteractiveGuideline(true)
                  .showLegend(true)
                  .showYAxis(true)
                  .showXAxis(true);

    avgKelembapan.xAxis
            .axisLabel('Time')
            .tickFormat(function(d){return d3.time.format('%H:%M:%S')(new Date(d));});

    avgKelembapan.yAxis
            .axisLabel('Rata -rata')
            .tickFormat(d3.format('.2f'));

    d3.select('#avgkelembapan')
        .append('svg')
        .datum(avgKelembapanData)
        .transition().duration(100)
        .call(avgKelembapan);

    nv.utils.windowResize(function() { avgKelembapan.update(); });
    return avgKelembapan;
});

var avgph;
var avgphData = [
    {
      values: [],      //values - represents the array of {x,y} data points
      key: 'Avg pH', //key  - the name of the series.
      color: '#7cb342'  //color - optional: choose your own line color.
    }
    ];

nv.addGraph(function(){
    avgph = nv.models.lineChart()
                  .margin({left: 50, right: 30})
                  .useInteractiveGuideline(true)
                  .showLegend(true)
                  .showYAxis(true)
                  .showXAxis(true);

    avgph.xAxis
            .axisLabel('Time')
            .tickFormat(function(d){return d3.time.format('%H:%M:%S')(new Date(d));});

    avgph.yAxis
            .axisLabel('Rata-rata pH')
            .tickFormat(d3.format('.2f'));

    d3.select('#avgph')
        .append('svg')
        .datum(avgphData)
        .transition().duration(100)
        .call(avgph);

    nv.utils.windowResize(function() { avgph.update(); });
    return avgph;
});

var minsuhu;
var minsuhuData = [
    {
      values: [],      //values - represents the array of {x,y} data points
      key: 'Min Suhu', //key  - the name of the series.
      color: '#7cb342'  //color - optional: choose your own line color.
    }
    ];

nv.addGraph(function(){
    minsuhu = nv.models.lineChart()
                  .margin({left: 50, right: 30})
                  .useInteractiveGuideline(true)
                  .showLegend(true)
                  .showYAxis(true)
                  .showXAxis(true);

    minsuhu.xAxis
            .axisLabel('Time')
            .tickFormat(function(d){return d3.time.format('%H:%M:%S')(new Date(d));});

    minsuhu.yAxis
            .axisLabel('Nilai Minimum Suhu')
            .tickFormat(d3.format('.2f'));

    d3.select('#minsuhu')
        .append('svg')
        .datum(minsuhuData)
        .transition().duration(100)
        .call(minsuhu);

    nv.utils.windowResize(function() { minsuhu.update(); });
    return minsuhu;
});

var minkelembapan;
var minkelembapanData = [
    {
      values: [],      //values - represents the array of {x,y} data points
      key: 'Min pH', //key  - the name of the series.
      color: '#7cb342'  //color - optional: choose your own line color.
    }
    ];

nv.addGraph(function(){
    minkelembapan = nv.models.lineChart()
                  .margin({left: 50, right: 30})
                  .useInteractiveGuideline(true)
                  .showLegend(true)
                  .showYAxis(true)
                  .showXAxis(true);

    minkelembapan.xAxis
            .axisLabel('Time')
            .tickFormat(function(d){return d3.time.format('%H:%M:%S')(new Date(d));});

    minkelembapan.yAxis
            .axisLabel('Nilai Minimum Kelembapan')
            .tickFormat(d3.format('.2f'));

    d3.select('#minkelembapan')
        .append('svg')
        .datum(minkelembapanData)
        .transition().duration(100)
        .call(minkelembapan);

    nv.utils.windowResize(function() { minkelembapan.update(); });
    return minkelembapan;
});

var minph;
var minphData = [
    {
      values: [],      //values - represents the array of {x,y} data points
      key: 'Min pH', //key  - the name of the series.
      color: '#7cb342'  //color - optional: choose your own line color.
    }
    ];

nv.addGraph(function(){
    minph = nv.models.lineChart()
                  .margin({left: 50, right: 30})
                  .useInteractiveGuideline(true)
                  .showLegend(true)
                  .showYAxis(true)
                  .showXAxis(true);

    minph.xAxis
            .axisLabel('Time')
            .tickFormat(function(d){return d3.time.format('%H:%M:%S')(new Date(d));});

    minph.yAxis
            .axisLabel('Nilai Minimum pH')
            .tickFormat(d3.format('.2f'));

    d3.select('#minph')
        .append('svg')
        .datum(minphData)
        .transition().duration(100)
        .call(minph);

    nv.utils.windowResize(function() { minph.update(); });
    return minph;
});

var maxsuhu;
var maxsuhuData = [
    {
      values: [],      //values - represents the array of {x,y} data points
      key: 'Max Suhu', //key  - the name of the series.
      color: '#7cb342'  //color - optional: choose your own line color.
    }
    ];

nv.addGraph(function(){
    maxsuhu = nv.models.lineChart()
                  .margin({left: 50, right: 30})
                  .useInteractiveGuideline(true)
                  .showLegend(true)
                  .showYAxis(true)
                  .showXAxis(true);

    maxsuhu.xAxis
            .axisLabel('Time')
            .tickFormat(function(d){return d3.time.format('%H:%M:%S')(new Date(d));});

    maxsuhu.yAxis
            .axisLabel('Nilai Maksimum Suhu')
            .tickFormat(d3.format('.2f'));

    d3.select('#maxsuhu')
        .append('svg')
        .datum(maxsuhuData)
        .transition().duration(100)
        .call(maxsuhu);

    nv.utils.windowResize(function() { maxsuhu.update(); });
    return maxsuhu;
});

var maxkelembapan;
var maxkelembapanData = [
    {
      values: [],      //values - represents the array of {x,y} data points
      key: 'Max Kelembapan', //key  - the name of the series.
      color: '#7cb342'  //color - optional: choose your own line color.
    }
    ];

nv.addGraph(function(){
    maxkelembapan = nv.models.lineChart()
                  .margin({left: 50, right: 30})
                  .useInteractiveGuideline(true)
                  .showLegend(true)
                  .showYAxis(true)
                  .showXAxis(true);

    maxkelembapan.xAxis
            .axisLabel('Time')
            .tickFormat(function(d){return d3.time.format('%H:%M:%S')(new Date(d));});

    maxkelembapan.yAxis
            .axisLabel('Nilai Maksimum Kelembapan')
            .tickFormat(d3.format('.2f'));

    d3.select('#maxkelembapan')
        .append('svg')
        .datum(maxkelembapanData)
        .transition().duration(100)
        .call(maxkelembapan);

    nv.utils.windowResize(function() { maxkelembapan.update(); });
    return maxkelembapan;
});

var maxph;
var maxphData = [
    {
      values: [],      //values - represents the array of {x,y} data points
      key: 'Max pH', //key  - the name of the series.
      color: '#7cb342'  //color - optional: choose your own line color.
    }
    ];

nv.addGraph(function(){
    maxph = nv.models.lineChart()
                  .margin({left: 50, right: 30})
                  .useInteractiveGuideline(true)
                  .showLegend(true)
                  .showYAxis(true)
                  .showXAxis(true);

    maxph.xAxis
            .axisLabel('Time')
            .tickFormat(function(d){return d3.time.format('%H:%M:%S')(new Date(d));});

    maxph.yAxis
            .axisLabel('Nilai Maksimum pH')
            .tickFormat(d3.format('.2f'));

    d3.select('#maxph')
        .append('svg')
        .datum(maxphData)
        .transition().duration(100)
        .call(maxph);

    nv.utils.windowResize(function() { maxph.update(); });
    return maxph;
});


//--------------------------------------Socket.io event handlers------------------------------------

// Rata-Rata Chart
socket.on('avgsuhu', function (data) {
        var msg = JSON.parse(data);
  avgSuhuData[0].values.push({x: new Date(msg[0]), y: Number(msg[1])});
  if(avgSuhuData[0].values.length > 30) {
    avgSuhuData[0].values.shift();
  }
  avgSuhu.update();
});

socket.on('avgkelembapan', function (data) {
        var msg = JSON.parse(data);
  avgKelembapanData[0].values.push({x: new Date(msg[0]), y: Number(msg[1])});
  if(avgKelembapanData[0].values.length > 30) {
    avgKelembapanData[0].values.shift();
  }
  avgKelembapan.update();
});

socket.on('avgph', function (data) {
        var msg = JSON.parse(data);
  avgphData[0].values.push({x: new Date(msg[0]), y: Number(msg[1])});
  if(avgphData[0].values.length > 30) {
    avgphData[0].values.shift();
  }
  avgph.update();
});

socket.on('minsuhu', function (data) {
        var msg = JSON.parse(data);
  minsuhuData[0].values.push({x: new Date(msg[0]), y: Number(msg[1])});
  if(minsuhuData[0].values.length > 30) {
    minsuhuData[0].values.shift();
  }
  minsuhu.update();
});

socket.on('minkelembapan', function (data) {
        var msg = JSON.parse(data);
  minkelembapanData[0].values.push({x: new Date(msg[0]), y: Number(msg[1])});
  if(minkelembapanData[0].values.length > 30) {
    minkelembapanData[0].values.shift();
  }
  minkelembapan.update();
});

socket.on('minph', function (data) {
        var msg = JSON.parse(data);
  minphData[0].values.push({x: new Date(msg[0]), y: Number(msg[1])});
  if(minphData[0].values.length > 30) {
    minphData[0].values.shift();
  }
  minph.update();
});

socket.on('maxsuhu', function (data) {
        var msg = JSON.parse(data);
  maxsuhuData[0].values.push({x: new Date(msg[0]), y: Number(msg[1])});
  if(maxsuhuData[0].values.length > 30) {
    maxsuhuData[0].values.shift();
  }
  maxsuhu.update();
});

socket.on('maxkelembapan', function (data) {
        var msg = JSON.parse(data);
  maxkelembapanData[0].values.push({x: new Date(msg[0]), y: Number(msg[1])});
  if(maxkelembapanData[0].values.length > 30) {
    maxkelembapanData[0].values.shift();
  }
  maxkelembapan.update();
});

socket.on('maxph', function (data) {
        var msg = JSON.parse(data);
  maxphData[0].values.push({x: new Date(msg[0]), y: Number(msg[1])});
  if(maxphData[0].values.length > 30) {
    maxphData[0].values.shift();
  }
  maxph.update();
});
