

var x = document.getElementById('home');
getting locatiom
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(GetTest);
  } else { 
    x.innerHTML =  "Geolocation is not supported by this browser.";ent.getElementById("search1").innerHTML 
  }
}

function PrintPosition(position) {
  document.getElementById("home").innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
}
//just a test
function getTest() {
  document.getElementById('home').innerHTML = "hello";
}

//taking search input as ajax
$('#search1').on('submit', function(event){
  event.preventDefault();
  console.log("form submitted!")  // sanity check
  getLocation();
});

function sendPosition(position) {
  $.ajax({
    type: "POST",
    url: '{{ 'results/' }}',
    data: { csrfmiddlewaretoken: '{{ csrf_token }}', position: position },
    success: function callback(response){
                console.log(response);
             }
 });
}