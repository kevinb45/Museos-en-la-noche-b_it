$(document).ready(function(){


    initialize();

    function initialize() {
        var styleArray = [
            {
                featureType: 'all',
                stylers: [
                    {saturation: -80}
                ]
            }, {
                featureType: 'road.arterial',
                elementType: 'geometry',
                stylers: [
                    {hue: '#00ffee'},
                    {saturation: 50}
                ]
            }, {
                featureType: 'poi.business',
                elementType: 'labels',
                stylers: [
                    {visibility: 'off'}
                ]
            }
        ];
        var latlng;
        var zoom = 15;
            latlng = new google.maps.LatLng(-33.783200992, -57.292555326);

        var opciones = {
            zoom: zoom,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.TERRAIN,
            styles: styleArray,
        };
        var map = new google.maps.Map(document.getElementById('map'), opciones);
        var infowindow = new google.maps.InfoWindow();
        var i;
        


        
        var address = $(".museo-item").data("address");
        var title = $(".museo-item").data("title");
        var target =$(".museo-item").data("target");

        geocoder = new google.maps.Geocoder();
        codeAddress(geocoder, map, address,title,target);


        


    function codeAddress(geocoder, map, address , title ,target) {
        geocoder.geocode({'address': address}, function(results, status) {
        if (status === 'OK') {
            var image = 'https://mt.googleapis.com/vt/icon/name=icons/onion/SHARED-mymaps-container-bg_4x.png,icons/onion/SHARED-mymaps-container_4x.png,icons/onion/1834-museum-jp_4x.png&highlight=ff000000,F57C00&scale=2.0';

            map.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
            map: map,
            position: results[0].geometry.location,
            icon: image
            });
            google.maps.event.addListener(marker, 'click', (function (marker, i) {
                    return function () {
                        infowindow.setContent(
                                '<center><b>' + title + '</b> <br/> ' +
                                address + ' <br/> ' +
                                '<br/></center>'
                                );
                        infowindow.open(map, marker);
                        
                    }
                })(marker, i));

        }
        });
    }   
}
});