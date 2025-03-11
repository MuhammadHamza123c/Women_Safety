# Emergency Alert System Using ESP8266 and Python

## Overview
This project is an emergency alert system that integrates an ESP8266 microcontroller with a Python-based backend. When a user presses a button, the system automatically sends their location to the nearest police station via email.

## Features
- **ESP8266 Web Server**: Listens for button presses and provides GPS coordinates.
- **Python Backend**: Processes data, finds the nearest police station, and sends an alert email.
- **Reverse Geocoding**: Converts latitude and longitude into a human-readable address.
- **Automated Email Alerts**: Notifies authorities with location details.

## Hardware Requirements
- ESP8266 WiFi Module
- Push Button
- LED Indicator
- Power Supply (5V)

## Software Requirements
- Python 3.x
- Arduino IDE (for ESP8266 programming)
- Required Python libraries (see `requirements.txt`)

## Installation & Setup
### ESP8266 Setup
1. Install the [Arduino IDE](https://www.arduino.cc/en/software).
2. Add ESP8266 board suppo
