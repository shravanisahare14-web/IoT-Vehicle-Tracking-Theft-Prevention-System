from flask import (
    Flask,
    render_template,
    jsonify,
    send_file
)

import json
import os
import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from datetime import datetime

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# ==========================================
# PATHS
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

PROJECT_ROOT = os.path.dirname(
    BASE_DIR
)

DATA_DIR = os.path.join(
    PROJECT_ROOT,
    "data"
)

os.makedirs(
    DATA_DIR,
    exist_ok=True
)

LOCATION_FILE = os.path.join(
    DATA_DIR,
    "latest_location.json"
)

ANALYTICS_FILE = os.path.join(
    DATA_DIR,
    "analytics.json"
)

# ==========================================
# PAGES
# ==========================================

@app.route("/")
def dashboard():

    return render_template(
        "index.html"
    )


@app.route("/analytics")
def analytics():

    return render_template(
        "analytics.html"
    )


# ==========================================
# LOCATION API
# ==========================================

@app.route("/api/location")
def get_location():

    if os.path.exists(
        LOCATION_FILE
    ):

        with open(
            LOCATION_FILE,
            "r"
        ) as file:

            return jsonify(
                json.load(file)
            )

    return jsonify({

        "lat": 0,

        "lon": 0,

        "speed": 0,

        "engine": "OFF",

        "threat": "SAFE"

    })


# ==========================================
# ANALYTICS API
# ==========================================

@app.route("/api/analytics")
def get_analytics():

    if os.path.exists(
        ANALYTICS_FILE
    ):

        with open(
            ANALYTICS_FILE,
            "r"
        ) as file:

            return jsonify(
                json.load(file)
            )

    return jsonify({

        "total_distance": 0,

        "average_speed": 0,

        "breaches": 0,

        "threat_events": 0,

        "speed_history": [],

        "threat_history": []

    })


# ==========================================
# EXPORT PDF
# ==========================================

@app.route("/export/pdf")
def export_pdf():

    if not os.path.exists(
        LOCATION_FILE
    ):

        return jsonify({
            "error":
            "latest_location.json not found"
        })

    if not os.path.exists(
        ANALYTICS_FILE
    ):

        return jsonify({
            "error":
            "analytics.json not found"
        })

    with open(
        LOCATION_FILE,
        "r"
    ) as file:

        location = json.load(
            file
        )

    with open(
        ANALYTICS_FILE,
        "r"
    ) as file:

        analytics = json.load(
            file
        )

    pdf_file = os.path.join(
        DATA_DIR,
        "guardiantrack_report.pdf"
    )

    doc = SimpleDocTemplate(
        pdf_file
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "GUARDIANTRACK",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            "Vehicle Security Intelligence Report",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Generated On: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "VEHICLE STATUS",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Engine Status: {location.get('engine','OFF')}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Current Speed: {location.get('speed',0)} km/h",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Threat Status: {location.get('threat','SAFE')}",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(
        Paragraph(
            "LOCATION DATA",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Latitude: {location.get('lat',0)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Longitude: {location.get('lon',0)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(
        Paragraph(
            "ANALYTICS SUMMARY",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Distance Travelled: {round(analytics.get('total_distance',0),2)} km",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Average Speed: {round(analytics.get('average_speed',0),2)} km/h",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Threat Events: {analytics.get('threat_events',0)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Geofence Breaches: {analytics.get('breaches',0)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(
        Paragraph(
            "SYSTEM STATUS",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            "✓ GPS Tracking Active",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            "✓ MQTT Communication Active",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            "✓ Analytics Engine Running",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            "✓ Geofence Monitoring Active",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Generated by GuardianTrack AI",
            styles["Italic"]
        )
    )

    elements.append(
        Paragraph(
            "IoT Vehicle Tracking & Theft Prevention System",
            styles["Italic"]
        )
    )

    doc.build(
        elements
    )

    return send_file(
        pdf_file,
        as_attachment=True
    )


# ==========================================
# EXPORT CSV
# ==========================================

@app.route("/export/csv")
def export_csv():

    with open(
        LOCATION_FILE,
        "r"
    ) as file:

        location = json.load(
            file
        )

    with open(
        ANALYTICS_FILE,
        "r"
    ) as file:

        analytics = json.load(
            file
        )

    csv_file = os.path.join(
        DATA_DIR,
        "guardiantrack_report.csv"
    )

    df = pd.DataFrame({

        "Latitude":
            [location.get("lat", 0)],

        "Longitude":
            [location.get("lon", 0)],

        "Speed":
            [location.get("speed", 0)],

        "Engine":
            [location.get("engine", "OFF")],

        "Threat":
            [location.get("threat", "SAFE")],

        "Distance":
            [round(analytics.get("total_distance", 0), 2)],

        "Average Speed":
            [round(analytics.get("average_speed", 0), 2)],

        "Threat Events":
            [analytics.get("threat_events", 0)],

        "Breaches":
            [analytics.get("breaches", 0)]

    })

    df.to_csv(
        csv_file,
        index=False
    )

    return send_file(
        csv_file,
        as_attachment=True
    )


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )