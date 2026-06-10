#include <WiFi.h>
#include <HTTPClient.h>
#include <TinyGPSPlus.h>

TinyGPSPlus gps;

HardwareSerial gpsSerial(1);

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";

String serverURL =
"http://YOUR_SERVER_IP:5000/api/update_location";

void setup()
{
    Serial.begin(115200);

    gpsSerial.begin(
        9600,
        SERIAL_8N1,
        16,
        17
    );

    WiFi.begin(
        ssid,
        password
    );

    Serial.println(
        "Connecting WiFi..."
    );

    while (
        WiFi.status()
        != WL_CONNECTED
    )
    {
        delay(1000);

        Serial.print(".");
    }

    Serial.println(
        "\nWiFi Connected"
    );
}

void loop()
{
    while (
        gpsSerial.available()
    )
    {
        gps.encode(
            gpsSerial.read()
        );
    }

    if (
        gps.location.isValid()
    )
    {
        float lat =
            gps.location.lat();

        float lon =
            gps.location.lng();

        float speed =
            gps.speed.kmph();

        sendData(
            lat,
            lon,
            speed
        );
    }

    delay(3000);
}

void sendData(
    float lat,
    float lon,
    float speed
)
{
    if (
        WiFi.status()
        == WL_CONNECTED
    )
    {
        HTTPClient http;

        http.begin(
            serverURL
        );

        http.addHeader(
            "Content-Type",
            "application/json"
        );

        String payload =
            "{";

        payload +=
            "\"lat\":"
            + String(lat, 6)
            + ",";

        payload +=
            "\"lon\":"
            + String(lon, 6)
            + ",";

        payload +=
            "\"speed\":"
            + String(speed, 2)
            + ",";

        payload +=
            "\"engine\":\"ON\"";

        payload += "}";

        int responseCode =
            http.POST(
                payload
            );

        Serial.print(
            "HTTP Response: "
        );

        Serial.println(
            responseCode
        );

        http.end();
    }
}