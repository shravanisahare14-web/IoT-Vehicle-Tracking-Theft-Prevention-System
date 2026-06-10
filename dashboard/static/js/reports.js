async function loadReports() {


try {

    const response =
        await fetch(
            "/api/reports"
        );

    const data =
        await response.json();

    const report =
        data.summary;

    document.getElementById(
        "current-speed"
    ).innerText =
        report.speed + " km/h";

    document.getElementById(
        "threat-level"
    ).innerText =
        report.threat;

    document.getElementById(
        "distance"
    ).innerText =
        report.distance + " km";

    document.getElementById(
        "avg-speed"
    ).innerText =
        report.average_speed + " km/h";

    document.getElementById(
        "r-lat"
    ).innerText =
        report.latitude;

    document.getElementById(
        "r-lon"
    ).innerText =
        report.longitude;

    document.getElementById(
        "engine-status"
    ).innerText =
        report.engine;

    document.getElementById(
        "threat-events"
    ).innerText =
        report.threat_events;

    document.getElementById(
        "breaches"
    ).innerText =
        report.breaches;

    document.getElementById(
        "max-speed"
    ).innerText =
        report.max_speed + " km/h";

    document.getElementById(
        "min-speed"
    ).innerText =
        report.min_speed + " km/h";

    const table =
        document.getElementById(
            "reports-body"
        );

    table.innerHTML = "";

    data.events
        .slice()
        .reverse()
        .forEach(event => {

            table.innerHTML += `

            <tr>

                <td>${event.timestamp}</td>

                <td>${event.event}</td>

                <td>${event.status}</td>

            </tr>

            `;
        });

}

catch(error) {

    console.error(
        "Reports Error:",
        error
    );
}


}

loadReports();

setInterval(
loadReports,
5000
);
