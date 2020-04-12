var mymap = L.map('mapid').setView([
    53.93040936805014,
    27.629070281982425
], 13);
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: '123' //ENTER YOUR ACCESS TOKEN HERE
}).addTo(mymap);
circleLatLng = [53.92822054315163, 27.68365859985352]
var circle = L.circle(circleLatLng, {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 300
}).addTo(mymap);
p = new L.Popup({ autoClose: false, closeOnClick: false })
                .setContent("EPAM")
                .setLatLng(circleLatLng);
circle.bindPopup(p).openPopup();

mapMarkers1 = [];
busIcon = L.icon({
    iconUrl: '../static/bus.svg',

    iconSize:     [38, 95], // size of the icon
    shadowSize:   [50, 64], // size of the shadow
    iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62],  // the same for the shadow
    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
});

mymap.on('click', function(e) {
    alert("Lat, Lon : " + e.latlng.lat + ", " + e.latlng.lng)
});

var source = new EventSource('/buses');
source.addEventListener('message', function(e){

  console.log('Message');
  obj = JSON.parse(e.data);
  console.log(obj);

  for (var i = 0; i < mapMarkers1.length; i++) {
      mymap.removeLayer(mapMarkers1[i]);
  }
  bus = L.marker([obj.latitude, obj.longitude], {icon: busIcon}).addTo(mymap);
  p = new L.Popup(
      { autoClose: false, closeOnClick: false }
  ).setContent("25 bus").setLatLng([obj.latitude, obj.longitude]);
  bus.bindPopup(p).openPopup();
  mapMarkers1.push(bus);
}, false);
