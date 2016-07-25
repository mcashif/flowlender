"use strict";
var $ = jQuery.noConflict();

var mapStyles = [ {"featureType":"road","elementType":"labels","stylers":[{"visibility":"simplified"},{"lightness":20}]},{"featureType":"administrative.land_parcel","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"landscape.man_made","elementType":"all","stylers":[{"visibility":"on"}]},{"featureType":"transit","elementType":"all","stylers":[{"saturation":-100},{"visibility":"on"},{"lightness":10}]},{"featureType":"road.local","elementType":"all","stylers":[{"visibility":"on"}]},{"featureType":"road.local","elementType":"all","stylers":[{"visibility":"on"}]},{"featureType":"road.highway","elementType":"labels","stylers":[{"visibility":"simplified"}]},{"featureType":"poi","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"road.arterial","elementType":"labels","stylers":[{"visibility":"on"},{"lightness":50}]},{"featureType":"water","elementType":"all","stylers":[{"hue":"#a1cdfc"},{"saturation":30},{"lightness":49}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"hue":"#f49935"}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"hue":"#fad959"}]}, {featureType:'road.highway',elementType:'all',stylers:[{hue:'#dddbd7'},{saturation:-92},{lightness:60},{visibility:'on'}]}, {featureType:'landscape.natural',elementType:'all',stylers:[{hue:'#c8c6c3'},{saturation:-71},{lightness:-18},{visibility:'on'}]},  {featureType:'poi',elementType:'all',stylers:[{hue:'#d9d5cd'},{saturation:-70},{lightness:20},{visibility:'on'}]} ];

// Set map height to 100% ----------------------------------------------------------------------------------------------

var $body = $('body');
if( $body.hasClass('map-fullscreen') ) {
    if( $(window).width() > 768 ) {
        $('.map-canvas').height( $(window).height() - $('.header').height() );
    }
    else {
        $('.map-canvas #map').height( $(window).height() - $('.header').height() );
    }
}

var _latitude = 24.443159;
var _longitude = -93.867188;
var map;
var markerClicked = 0;
var activeMarker = false;
var lastClicked = false;
var sorting = "promotor";
var outside = false;

function setMap(){

  var mapCenter = new google.maps.LatLng(_latitude,_longitude);
  var mapOptions = {
      zoom: 4,
      center: mapCenter,
      disableDefaultUI: false,
      scrollwheel: false,
      styles: mapStyles,
      mapTypeControlOptions: {
          style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR,
          position: google.maps.ControlPosition.BOTTOM_CENTER
      },
      panControl: false,
      zoomControl: true,
      zoomControlOptions: {
          style: google.maps.ZoomControlStyle.LARGE,
          position: google.maps.ControlPosition.LEFT_BOTTOM
      }
  };

  var mapElement = document.getElementById('map');
  return new google.maps.Map(mapElement, mapOptions);
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Homepage map - Google
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function createHomepageGoogleMap(json){


        map=setMap();

        var newMarkers = [];
        for (var i = 0; i < json.data.length; i++) {

            // Google map marker content -----------------------------------------------------------------------------------
            if( json.data[i].color ) var color = json.data[i].color;
            else color = '';

            var markerContent = document.createElement('DIV');
            markerContent.innerHTML =
                    '<div class="map-marker ' + color + '">' +
                        '<div class="icon">' +
                        '<img src="' + json.data[i].small_image +  '">' +
                        '</div>' +
                    '</div>';
            // Create marker on the map ------------------------------------------------------------------------------------
            var marker = new RichMarker({
                position: new google.maps.LatLng( json.data[i].latitude, json.data[i].longitude ),
                map: map,
                draggable: false,
                content: markerContent,
                flat: true
            });
            newMarkers.push(marker);

            // Create infobox for marker -----------------------------------------------------------------------------------
            var infoboxContent = document.createElement("div");
            var infoboxOptions = {
                content: infoboxContent,
                disableAutoPan: false,
                pixelOffset: new google.maps.Size(-18, -42),
                zIndex: null,
                alignBottom: true,
                boxClass: "infobox",
                enableEventPropagation: true,
                closeBoxMargin: "0px 0px -30px 0px",
                closeBoxURL: "/static/assets/img/close.png",
                infoBoxClearance: new google.maps.Size(1, 1)
            };

            // Infobox HTML element ----------------------------------------------------------------------------------------
            var category = json.data[i].category;
            infoboxContent.innerHTML = drawInfobox(category, infoboxContent, json, i);
            // Create new markers ------------------------------------------------------------------------------------------
            newMarkers[i].infobox = new InfoBox(infoboxOptions);
            // Show infobox after click ------------------------------------------------------------------------------------
            google.maps.event.addListener(marker, 'click', (function(marker, i) {
                return function() {
                    google.maps.event.addListener(map, 'click', function(event) {
                        lastClicked = marker;
                        outside=false;
                    });
                    activeMarker = marker;
                    if( activeMarker != lastClicked ){

                        for (var h = 0; h < newMarkers.length; h++) {
                            newMarkers[h].content.className = 'marker-loaded';
                            newMarkers[h].infobox.close();
                        }

                        marker.infobox.open(map, this);
                        marker.infobox.setOptions({ boxClass:'fade-in-marker'});
                        marker.content.className = 'marker-active marker-loaded';

                        if(!outside)
                          markerClicked = 1;

                        var item="#"+json.data[i].id+"li"
                        $(".items-list").mCustomScrollbar('scrollTo',  item);

                    }
                  }
            })(marker, i));
            // Fade infobox after close is clicked -------------------------------------------------------------------------
            google.maps.event.addListener(newMarkers[i].infobox, 'closeclick', (function(marker, i) {
                return function() {
                    activeMarker = 0;
                    newMarkers[i].content.className = 'marker-loaded';
                    newMarkers[i].infobox.setOptions({ boxClass:'fade-out-marker' });
                }
              })(marker, i));
            }

            // Close infobox after click on map --------------------------------------------------------------------------------
            google.maps.event.addListener(map, 'click', function(event) {
                if( activeMarker != false && lastClicked != false ){
                    if( markerClicked == 1 && !outside){
                        activeMarker.infobox.open(map);
                        activeMarker.infobox.setOptions({ boxClass:'fade-in-marker'});
                        activeMarker.content.className = 'marker-active marker-loaded';
                    }
                    else {
                        outside = false;
                        markerClicked = 0;
                        activeMarker.infobox.setOptions({ boxClass:'fade-out-marker' });
                        activeMarker.content.className = 'marker-loaded';
                        setTimeout(function() {
                            activeMarker.infobox.close();
                        }, 350);
                    }
                    markerClicked = 0;
                    outside=false;
                }

                if( activeMarker != false ){
                    google.maps.event.addListener(activeMarker, 'click', function(event) {
                        markerClicked = 1;
                    });
                }
                markerClicked = 0;
                outside=false;
            });


            addEvents(newMarkers, json);

            redrawMap('google', map);

            UserLocationAutoComplete();

}


function UserLocationAutoComplete(){

          // Geolocation of user -----------------------------------------------------------------------------------------
          $('.geolocation').on("click", function() {
              if (navigator.geolocation) {
                  navigator.geolocation.getCurrentPosition(success);
              } else {
                  console.log('Geo Location is not supported');
              }
          });

          function success(position) {
              var locationCenter = new google.maps.LatLng( position.coords.latitude, position.coords.longitude);
              _latitude = position.coords.latitude;
              _longitude = position.coords.longitude;
              map.setCenter( locationCenter );
              map.setZoom(4);

  			var markerContent = document.createElement('DIV');
  			markerContent.innerHTML =
  				'<div class="map-marker">' +
  					'<div class="icon">' +
  					'</div>' +
  				'</div>';

  			// Create marker on the map ------------------------------------------------------------------------------------
  			var marker = new RichMarker({
  				position: locationCenter,
  				map: map,
  				draggable: false,
  				content: markerContent,
  				flat: true
  			});

  			marker.content.className = 'marker-loaded';

              var geocoder = new google.maps.Geocoder();
              geocoder.geocode({
                  "latLng": locationCenter
              }, function (results, status) {
                  if (status == google.maps.GeocoderStatus.OK) {
                      var lat = results[0].geometry.location.lat(),
                          lng = results[0].geometry.location.lng(),
                          placeName = results[0].address_components[0].long_name,
                          latlng = new google.maps.LatLng(lat, lng);

                      $("#location").val(results[0].formatted_address);
                  }
              });

          }

          // Autocomplete address ----------------------------------------------------------------------------------------

          var input = document.getElementById('location') ;
          var autocomplete = new google.maps.places.Autocomplete(input, {
              types: ["geocode"]
          });
          autocomplete.bindTo('bounds', map);
          google.maps.event.addListener(autocomplete, 'place_changed', function() {
              var place = autocomplete.getPlace();
              if (!place.geometry) {
                  return;
              }
              if (place.geometry.viewport) {
                  map.fitBounds(place.geometry.viewport);
                  map.setZoom(4);
              } else {
                  map.setCenter(place.geometry.location);
                  map.setZoom(4);
              }

              //marker.setPosition(place.geometry.location);
              //marker.setVisible(true);
              _latitude=place.geometry.location.lat();
              _longitude=place.geometry.location.lng();

              var address = '';
              if (place.address_components) {
                  address = [
                      (place.address_components[0] && place.address_components[0].short_name || ''),
                      (place.address_components[1] && place.address_components[1].short_name || ''),
                      (place.address_components[2] && place.address_components[2].short_name || '')
                  ].join(' ');
              }
          });
}

function addEvents(newMarkers, json){

              google.maps.event.addListener(map, 'idle', function() {
                dynamicLoadMarkers(map, newMarkers, json);
              });

              $('input').on('ifChecked', function(event){
                      dynamicLoadMarkers(map, newMarkers, json);
              });

              $('input').on('ifUnchecked', function(event){
                      dynamicLoadMarkers(map, newMarkers, json);
              });

              $('#type').on('change', function () {
                      dynamicLoadMarkers(map, newMarkers, json);
              });

              $("#searchForm").submit(function(e) {
                  e.preventDefault();
                  dynamicLoadMarkers(map, newMarkers, json);
              });

              $('#distance').on('change', function () {
                    dynamicLoadMarkers(map, newMarkers, json);
              });

              $('#daysx').on('change', function () {
                  dynamicLoadMarkers(map, newMarkers, json);
              });

              $('#display-date').on('click',function(){
                    if(!$('#display-date').hasClass('active')){

                        $('#display-date .active').removeClass('icon');
                        $(this).addClass('icon active');

                        $('#display-name').removeClass('icon active');
                        $('#display-name').addClass('icon');

                        $('#display-promotor').removeClass('icon active');
                        $('#display-promotor').addClass('icon');
                    }
                      sorting="date";
                      dynamicLoadMarkers(map, newMarkers, json);
               });

               $('#display-name').on('click',function(){

                  if(!$('#display-name').hasClass('active')){

                    $('#display-name .active').removeClass('icon');
                    $(this).addClass('icon active');

                    $('#display-date').removeClass('icon active');
                    $('#display-date').addClass('icon');

                    $('#display-promotor').removeClass('icon active');
                    $('#display-promotor').addClass('icon');
                  }
                      sorting="name";
                      dynamicLoadMarkers(map, newMarkers, json);
               });


               $('#display-promotor').on('click',function(){

                  if(!$('#display-promotor').hasClass('active')){

                    $('#display-promotor .active').removeClass('icon');
                    $(this).addClass('icon active');

                    $('#display-date').removeClass('icon active');
                    $('#display-date').addClass('icon');

                    $('#display-name').removeClass('icon active');
                    $('#display-name').addClass('icon');
                  }
                      sorting="promotor";
                      dynamicLoadMarkers(map, newMarkers, json);
               });

}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Functions
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function pushItemsToArray(json, a, category, visibleItemsArray){
    var itemPrice;
    var priceIcon= "/static/assets/icons/store/apparel/umbrella-2.png" ;
    visibleItemsArray.push({id:json.data[a].id, name:json.data[a].title , promotor: json.data[a].promotor , date:json.data[a].event_date,
        html: '<li id="' + json.data[a].id + "li" +'">' +
            '<div class="item" id="' + json.data[a].id + '">' +
                '<a href="/detail/' + json.data[a].id +'" class="image">' +
                    '<div class="inner">' +
                        '<div class="item-specific">' +
                            drawItemSpecific(category, json, a) +
                        '</div>' +
                        '<img src="' + json.data[a].small_image+ '" alt="">' +
                    '</div>' +
                '</a>' +
                '<div class="wrapper">' +
                    '<a href="#" id="' + json.data[a].id + '"><h3>' + json.data[a].promotor + '</h3></a>' +
                    '<h4>' + json.data[a].title + '</h4>' +
                    drawPrice(json.data[a].event_date) +
                    '<div class="info">' +
                        '<div class="type">' +
                            '<span>' + json.data[a].city + ","+ json.data[a].city + ","+ json.data[a].zip_code+ '</span>' +
                        '</div>' +
                    '</div>' +
                    '<div class="info">' +
                        '<div class="type">' +
                             '<a id="' + json.data[a].id +'"class="som">' +
                             '<span>' +"Show on Map..."+ '</span></a>' +
                        '</div>' +
                    '</div>' +
                '</div>' +
            '</div>' +
        '</li>'
    });

    function drawPrice(price){
        if( price ){
            itemPrice = '<div class="price">' + price +  '</div>';
            return itemPrice;
        }
        else {
            return '';
        }
    }
}

// Center map to marker position if function is called (disabled) ------------------------------------------------------

function centerMapToMarker(){
    $.each(json.data, function(a) {
        if( json.data[a].id == id ) {
            var _latitude = json.data[a].latitude;
            var _longitude = json.data[a].longitude;
            var mapCenter = new google.maps.LatLng(_latitude,_longitude);
            map.setCenter(mapCenter);
        }
    });
}


// MKS-

function isBracketUnselected(){

      if($("#SE").prop("checked") || $("#DE").prop("checked") || $("#RR").prop("checked"))
          return true;

      return false;

}

function isRulesUnselected(){

      if($("#PNT").prop("checked") || $("#SON").prop("checked") || $("#NTL").prop("checked"))
          return true;

      return false;

}

function everySectionHasOnSelection(){


  if(isBracketUnselected() && isRulesUnselected())
      return true;


}

function checkBRacket(bracket){

  if(bracket=="Single Elimination" && $("#SE").prop("checked"))
      return true;

  if(bracket=="Double Elimination" && $("#DE").prop("checked"))
      return true;

  if(bracket=="Round Robin" && $("#RR").prop("checked"))
      return true;

  return false;
}

function checkRule(rule){

  if(rule=="Points" && $("#PNT").prop("checked"))
      return true;

  if(rule=="Submission Only" && $("#SON").prop("checked"))
      return true;


  if(rule=="Time Limit" && $("#NTL").prop("checked"))
      return true;

  return false;
}


function checkDivision(kids,adult,abs){


    if($("#AD").prop("checked") && $("#KD").prop("checked") && $("#ABD").prop("checked"))
            return (adult && kids && abs);

    if($("#AD").prop("checked") && $("#KD").prop("checked"))
            return (adult && kids);

    if($("#KD").prop("checked") && $("#ABD").prop("checked"))
            return (kids && abs);

    if($("#AD").prop("checked") && $("#ABD").prop("checked"))
            return (adult && abs);

    if($("#AD").prop("checked") )
            return adult;

    if($("#KD").prop("checked"))
            return kids;

    if($("#ABD").prop("checked"))
            return abs;

    return true;

}

function getType(gi, nogi, both){

  var type= $('#type').find('option:selected').val();

  if(type=="0")
      return true;

//gi
  if(type=="1" && (gi || both) )
      return true;
//nogi
  if(type=="2" && (nogi || both))
      return true;
//both
  if(type=="3" && both)
      return true;

  return false;


}

function getCheckBoxStatus(json,i){

  if(!everySectionHasOnSelection())
      return false;

     if( getType(json.data[i].GI , json.data[i].NOGI, (json.data[i].NOGI && json.data[i].GI)))
     {

        return checkDivision(json.data[i].KIDS,json.data[i].ADULTS,json.data[i].ABSOLUTE) && checkBRacket(json.data[i].bracket) && checkRule(json.data[i].rule);// && checkDivision(json.data[i].KIDS,json.data[i].ADULTS,json.data[i].ABSOLUTE);

     }

    return false;

}

function getDistanceDateStatus(lat,lng,date){


  var distance= $('#distance').find('option:selected').val();

  if(distance=="0")
      return true && CheckDays(date);
  else{

          var dis=getDistance(lat,lng,_latitude,_longitude);
          if(dis<=parseInt(distance))
             return true && CheckDays(date);
       }

  return false;

}

function daysDifference(d1, d2)
{
  var ndays;
  var tv1 = d1.valueOf();  // msec since 1970
  var tv2 = d2.valueOf();

  ndays = (tv2 - tv1) / 1000 / 86400;
  ndays = Math.round(ndays - 0.5);
  return ndays;
}

function CheckDays(date){

  var dataDate = new Date(date);
  var currentDate = new Date();
  var daysX=daysDifference(currentDate,dataDate);

  var timeX= $('#daysx').find('option:selected').val();

  if(timeX=="0")
      return true;
  else{
          if(daysX<=parseInt(timeX))
             return true;
       }

  return false;

}

function dynamicLoadMarkers(map, loadedMarkers, json){

              var visibleArray = [];
              var visibleItemsArray = [];
              var visibleItemsArrayX = [];
              var category;

              for (var i = 0; i < json.data.length; i++) {
                  if ( map.getBounds().contains(loadedMarkers[i].getPosition()) &&  getCheckBoxStatus(json,i) && getDistanceDateStatus(json.data[i].latitude,json.data[i].longitude,json.data[i].event_date)){
                      category = json.data[i].category;
                      pushItemsToArray(json, i, category, visibleItemsArray);
                      visibleArray.push(loadedMarkers[i]);
                      $.each( visibleArray, function (i) {
                          setTimeout(function(){
                              if ( map.getBounds().contains(visibleArray[i].getPosition()) ){
                                  if( !visibleArray[i].content.className ){
                                      visibleArray[i].setMap(map);
                                      visibleArray[i].content.className += 'bounce-animation marker-loaded';
                                  }
                              }
                          }, i * 50);
                      });
                  } else {
                      loadedMarkers[i].content.className = '';
                      loadedMarkers[i].setMap(null);
                  }
              }

              // Create list of items in Results sidebar ---------------------------------------------------------------------

             sortArray(visibleItemsArray,visibleItemsArrayX);

              $('.items-list .results').html( visibleItemsArrayX );

              var $singleItem = $('.results .item');
              var $showonmap = $('.som');

              $singleItem.hover(
                  function(){
                      loadedMarkers[ $(this).attr('id') - 1 ].content.className = 'marker-active marker-loaded';
                  },
                  function() {
                      loadedMarkers[ $(this).attr('id') - 1 ].content.className = 'marker-loaded';
                  }
              );

              $showonmap.click(

                function(){

                    outside = true;
                    activeMarker = true;
                    lastClicked = true;
                    google.maps.event.trigger(loadedMarkers[ $(this).attr('id') - 1 ], 'click');

                }

              );

}

function sortArray(visibleItemsArray, visiableItemArrayX,sortbyDate){

      if(sorting=="date"){

                         visibleItemsArray.sort(function(a, b){
                         var dateA=new Date(a.date), dateB=new Date(b.date)
                         return dateA-dateB //sort by date ascending
                        })

                    }

      if(sorting=="name"){

                           visibleItemsArray.sort(function(a, b){
                           var nameA=a.name.toLowerCase(), nameB=b.name.toLowerCase()
                           if (nameA < nameB) //sort string ascending
                            return -1
                           if (nameA > nameB)
                            return 1
                           return 0 //default return value (no sorting)
                          })
        }

        if(sorting=="promotor"){

                             visibleItemsArray.sort(function(a, b){
                             var nameA=a.promotor.toLowerCase(), nameB=b.promotor.toLowerCase()
                             if (nameA < nameB) //sort string ascending
                              return -1
                             if (nameA > nameB)
                              return 1
                             return 0 //default return value (no sorting)
                            })
          }


        for (var key in visibleItemsArray) {

              visiableItemArrayX.push(visibleItemsArray[key].html);
        }

}


// Redraw map after item list is closed --------------------------------------------------------------------------------

function redrawMap(mapProvider, map){
    $('.map .toggle-navigation').click(function() {
        $('.map-canvas').toggleClass('results-collapsed');
        $('.map-canvas .map').one("transitionend webkitTransitionEnd oTransitionEnd MSTransitionEnd", function(){
            if( mapProvider == 'osm' ){
                map.invalidateSize();
            }
            else if( mapProvider == 'google' ){
                google.maps.event.trigger(map, 'resize');
            }
        });
    });
}



////////////////////////////////////////////////////////////
var rad = function(x){
  return x * Math.PI / 180;
};
var getDistance = function(lat1,lng1, lat2,lng2){
  var R = 6378137; // Earth’s mean radius in meter
  var dLat = rad(lat2 - lat1);
  var dLong = rad(lng2 - lng1);
  var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(rad(lat1)) * Math.cos(rad(lat2)) *
    Math.sin(dLong / 2) * Math.sin(dLong / 2);
  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  var d = R * c;
  return d/1000; // returns the distance in KM
};
////////////////////////////////////////////////////////////


/////////////
function drawInfobox(category, infoboxContent, json, i){

    if(json.data[i].color)          { var color = json.data[i].color }
        else                        { color = '' }
    if( json.data[i].event_date )        { var price = '<div class="price">' + json.data[i].event_date +  '</div>' }
        else                        { price = '' }
    if(json.data[i].id)             { var id = json.data[i].id }
        else                        { id = '' }
    if(json.data[i].url)            { var url = json.data[i].url }
        else                        { url = '' }
    if(json.data[i].type)           { var type = json.data[i].type }
        else                        { type = '' }
    if(json.data[i].title)          { var title = json.data[i].title }
        else                        { title = '' }
    if(json.data[i].location)       { var location = json.data[i].location }
        else                        { location = '' }
    if(json.data[i].small_image)     { var gallery = json.data[i].small_image }
        else                        { gallery[0] = '../img/default-item.jpg' }

    var ibContent = '';
    ibContent =
    '<div class="infobox ' + color + '">' +
        '<div class="inner">' +
            '<div class="image">' +
                '<div class="item-specific">' + drawItemSpecific(category, json, i) + '</div>' +
                '<div class="overlay">' +
                    '<div class="wrapper">' +
                        '<a href="/detail/' + json.data[i].id + '" class="detail">More Info</a>' +
                        '<hr>' +
                        '<a href="' + json.data[i].event_web +  '" class="detail">Go to Web</a>' +
                    '</div>' +
                '</div>' +
                '<a href="' + url +  '" class="description">' +
                    '<div class="meta">' +
                        price +
                        '<h2>' + title +  '</h2>' +
                        '<figure>' + location +  '</figure>' +
                        '<i class="fa fa-angle-right"></i>' +
                    '</div>' +
                '</a>' +
                '<img src="' + gallery +  '">' +
            '</div>' +
        '</div>' +
    '</div>';

    return ibContent;
}
/////////////

function drawItemSpecific(category, json, i){

    var dis=Math.floor(getDistance(json.data[i].latitude ,json.data[i].longitude ,_latitude,_longitude));
    var val=dis+'KM';

    var itemSpecific = '';
     itemSpecific += '<h1>'+val+ '</h1>';
            return itemSpecific;

}

////////////

function itemDetailMap(latitude,longitude){
    var mapCenter = new google.maps.LatLng(latitude,longitude);
    var mapOptions = {
        zoom: 8,
        center: mapCenter,
        disableDefaultUI: true,
        scrollwheel: false,
        styles: mapStyles,
        panControl: false,
        zoomControl: false,
        draggable: true
    };
    var mapElement = document.getElementById('map-detail');
    var map = new google.maps.Map(mapElement, mapOptions);
    var icon = '';

    // Google map marker content -----------------------------------------------------------------------------------

    var markerContent = document.createElement('DIV');
    markerContent.innerHTML =
        '<div class="map-marker">' +
            '<div class="icon">' +
            icon +
            '</div>' +
        '</div>';

    // Create marker on the map ------------------------------------------------------------------------------------

    var marker = new RichMarker({
        position: new google.maps.LatLng( latitude, longitude ),
        map: map,
        draggable: false,
        content: markerContent,
        flat: true
    });

    marker.content.className = 'marker-loaded';
}
