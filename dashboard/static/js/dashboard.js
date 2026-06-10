console.log("GuardianTrack AI Initialized");

document.addEventListener("DOMContentLoaded", function () {


const map = L.map("map").setView([17.3850, 78.4867], 15);

L.tileLayer(
    "https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png",
    {
        attribution: "&copy; OpenStreetMap & CARTO",
        subdomains: "abcd",
        maxZoom: 20
    }
).addTo(map);

const vehicleIcon = L.divIcon({
    className: "",
    html: `
        <div class="vehicle-pulse"></div>
        <div class="vehicle-core"></div>
    `,
    iconSize: [40, 40]
});

const vehicleMarker = L.marker(
    [17.3850, 78.4867],
    { icon: vehicleIcon }
).addTo(map);

const geofence = L.circle(
    [17.3850, 78.4867],
    {
        radius: 250,
        color: "#00E5FF",
        fillColor: "#00E5FF",
        fillOpacity: 0.15,
        weight: 3
    }
).addTo(map);

let routeCoordinates = [];
let movementCount = 0;
let previousThreat = "SAFE";

const routeLine = L.polyline(
    routeCoordinates,
    {
        color: "#00E5FF",
        weight: 6,
        opacity: 1
    }
).addTo(map);

async function updateVehicleData() {

    try {

        const response =
            await fetch("/api/location");

        const data =
            await response.json();

        const lat = data.lat;
        const lon = data.lon;

        document.getElementById("lat-value").innerText =
            lat.toFixed(4);

        document.getElementById("lon-value").innerText =
            lon.toFixed(4);

        document.getElementById("speed-value").innerText =
            data.speed + " km/h";

        document.getElementById("engine-value").innerText =
            data.engine;

        document.getElementById("threat-value").innerText =
            data.threat;

        vehicleMarker.setLatLng([lat, lon]);

        map.panTo([lat, lon]);

        routeCoordinates.push([lat, lon]);

        if(routeCoordinates.length > 50){
            routeCoordinates.shift();
        }

        routeLine.setLatLngs(routeCoordinates);

        document.getElementById("geo-status").innerText =
            data.geofence;

        document.getElementById("distance-center").innerText =
            data.distance_from_center + " m";

        document.getElementById("tracking-status").innerText =
            "TRACKING";

        document.getElementById("signal-status").innerText =
            "STRONG";

        document.getElementById("zone-status").innerText =
            data.geofence;

        if (
            previousThreat === "SAFE" &&
            data.threat === "ALERT"
        ) {
            movementCount++;
        }

        previousThreat = data.threat;

        document.getElementById("movement-count").innerText =
            movementCount;

        if (data.threat === "ALERT") {

            document.getElementById("threat-score").innerText =
                "HIGH";

            document.getElementById("last-alert").innerText =
                "GEOFENCE BREACH";

            document.getElementById("engine-lock").innerText =
                "LOCK RECOMMENDED";

            document.getElementById("threat-value").style.color =
                "#FF4D6D";

            document.getElementById("threat-score").style.color =
                "#FF4D6D";

            document.getElementById("geo-status").style.color =
                "#FF4D6D";

            geofence.setStyle({
                color:"#FF4D6D",
                fillColor:"#FF4D6D"
            });

        } else {

            document.getElementById("threat-score").innerText =
                "LOW";

            document.getElementById("last-alert").innerText =
                "NONE";

            document.getElementById("engine-lock").innerText =
                "UNLOCKED";

            document.getElementById("threat-value").style.color =
                "#00E5FF";

            document.getElementById("threat-score").style.color =
                "#00E5FF";

            document.getElementById("geo-status").style.color =
                "#00E5FF";

            geofence.setStyle({
                color:"#00E5FF",
                fillColor:"#00E5FF"
            });
        }

    } catch (error) {

        console.error(
            "API Error:",
            error
        );
    }
}

updateVehicleData();

setInterval(
    updateVehicleData,
    2000
);


});
