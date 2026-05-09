# Metro Passenger Display

This project is a desktop metro passenger display built with Python and Tkinter. It shows the next station, travel direction, station information, a live clock, and a visual metro line map with station progress indicators.

<img width="1536" height="1024" alt="metro project" src="https://github.com/user-attachments/assets/55226811-78c7-473a-9e53-b90c117fdb6a" />


## Overview

The application opens two windows:

- A main passenger display window
- A control panel window for operating the display

The interface is bilingual, showing station and direction information in Arabic and English.

## Features

- Live digital clock in the main display
- Visual metro line map with station nodes
- Highlighted next station with a blinking blue ring
- Direction switching between forward and backward routes
- Emergency announcement mode with blinking alert text
- Station information display for the currently selected stop
- Automatic map redraw when the main window is resized

## Route

The route defined in `main.py` contains these stations:

1. Adly Mansour
2. Obour
3. Almustakbal
4. Alshorouk
5. Badr
6. Asher of Ramadan
7. Hadaik alasima
8. Capital

## Controls

The control panel provides three actions:

- `Next Station`: moves to the next station based on the current direction
- `Switch Direction`: changes the route direction and resets the station index to the correct terminal
- `Emergency`: toggles emergency announcement mode on and off

## Direction Logic

The app supports two directions:

- `forward`: Adly Mansour -> Capital
- `backward`: Capital -> Adly Mansour

When direction changes:

- Forward mode starts from the first station
- Backward mode starts from the last station

## Display Behavior

Each station on the map is color-coded:

- `Green`: upcoming stations
- `Red`: stations already passed in the current direction
- `Blue blinking ring`: the current next station

The main display also shows:

- Next station name
- Current travel direction
- Station information text
- Emergency banner when enabled

## Requirements

- Python 3
- Tkinter

`datetime` is also used, but it is part of Python's standard library.

## Run

Run the app with:

```bash
python main.py
```

## Notes

- The main display launches maximized.
- The control panel launches as a separate window.
- The station map updates continuously for blinking effects and window resizing.
