#include <ESP8266WiFi.h>

const char* ssid = "YourSSID";
const char* password = "YourPassword";
WiFiServer server(80);
const int buttonPin = 4;
const int ledPin = 5;
bool buttonPressed = false;

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    pinMode(buttonPin, INPUT_PULLUP);
    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, LOW);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
    }
    server.begin();
}

void loop() {
    WiFiClient client = server.available();
    if (client) {
        delay(100);
        while (client.available()) {
            client.read();
        }
        if (digitalRead(buttonPin) == LOW && !buttonPressed) {
            buttonPressed = true;
            digitalWrite(ledPin, HIGH);
            String response = "{\"Latitude\": 30.184497, \"Longitude\": 71.481924}";
            client.println("HTTP/1.1 200 OK");
            client.println("Content-Type: application/json");
            client.println("Connection: close");
            client.println();
            client.println(response);
        } else {
            client.println("HTTP/1.1 204 No Content");
            client.println("Connection: close");
            client.println();
        }
        delay(100);
        while (digitalRead(buttonPin) == LOW) {
            delay(10);
        }
        buttonPressed = false;
        digitalWrite(ledPin, LOW);
    }
}
