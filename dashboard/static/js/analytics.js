async function loadAnalytics() {

    try {

        const response =
            await fetch("/api/analytics");

        const analytics =
            await response.json();

        document.getElementById(
            "total-distance"
        ).innerText =
            analytics.total_distance.toFixed(2) + " km";

        document.getElementById(
            "avg-speed"
        ).innerText =
            analytics.average_speed.toFixed(2) + " km/h";

        document.getElementById(
            "breaches"
        ).innerText =
            analytics.breaches;

        document.getElementById(
            "threat-events"
        ).innerText =
            analytics.threat_events;

        createCharts(
            analytics
        );

    }

    catch(error) {

        console.error(
            "Analytics Error:",
            error
        );
    }
}

let speedChart;
let threatChart;

function createCharts(analytics) {

    if(speedChart) {

        speedChart.destroy();
    }

    if(threatChart) {

        threatChart.destroy();
    }

    const speedCtx =
        document.getElementById(
            "speedChart"
        );

    speedChart =
        new Chart(speedCtx, {

            type: "line",

            data: {

                labels:
                    analytics.speed_history.map(
                        (_, index) =>
                            index + 1
                    ),

                datasets: [

                    {

                        label:
                            "Vehicle Speed",

                        data:
                            analytics.speed_history,

                        borderColor:
                            "#00E5FF",

                        backgroundColor:
                            "rgba(0,229,255,0.1)",

                        tension: 0.4,

                        fill: true

                    }

                ]

            },

            options: {

                responsive: true,

                plugins: {

                    legend: {

                        labels: {

                            color: "#ffffff"

                        }

                    }

                },

                scales: {

                    x: {

                        ticks: {

                            color: "#ffffff"

                        }

                    },

                    y: {

                        ticks: {

                            color: "#ffffff"

                        }

                    }

                }

            }

        });

    const threatCtx =
        document.getElementById(
            "threatChart"
        );

    threatChart =
        new Chart(threatCtx, {

            type: "bar",

            data: {

                labels:
                    analytics.threat_history.map(
                        (_, index) =>
                            index + 1
                    ),

                datasets: [

                    {

                        label:
                            "Threat Events",

                        data:
                            analytics.threat_history,

                        backgroundColor:
                            "#FF4D6D"

                    }

                ]

            },

            options: {

                responsive: true,

                plugins: {

                    legend: {

                        labels: {

                            color: "#ffffff"

                        }

                    }

                },

                scales: {

                    x: {

                        ticks: {

                            color: "#ffffff"

                        }

                    },

                    y: {

                        ticks: {

                            color: "#ffffff"

                        }

                    }

                }

            }

        });
}

loadAnalytics();

setInterval(
    loadAnalytics,
    5000
);