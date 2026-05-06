import tkinter as tk
from datetime import datetime

# =========================================================
# GLOBAL STATE FLAGS (Blinking & Emergency)
# =========================================================

blink_on = True                     # Controls blinking of next station ring
alert_blink_on = True               # Toggles emergency text visibility
alert_blinking = False              # Emergency blinking active flag

# =========================================================
# STATIC DATA (Stations & Directions)
# =========================================================

# Direction labels (Arabic + English)
DIRECTIONS = {
    "forward": {
        "ar": "العاصمة → عدلي منصور",
        "en": "Adly Mansour → Capital"
    },
    "backward": {
        "ar": "عدلي منصور → العاصمة",
        "en": "Capital → Adly Mansour"
    }
}

# Metro stations data
stations = [
    {
        "ar": "عدلي منصور",
        "en": "Adly Mansour",
        "info_ar": "محطة عدلي منصور التبادلية",
        "info_en": "Adly Mansour Interchange Station"
    },
    {
        "ar": "العبور",
        "en": "Obour",
        "info_ar": "مدينة العبور وكارفور العبور",
        "info_en": "Obour City and Carrefour Obour"
    },
    {
        "ar": "المستقبل",
        "en": "Almustakbal",
        "info_ar": "قريبة من جامعة المستقبل",
        "info_en": "Near Almustakbal University"
    },
    {
        "ar": "الشروق",
        "en": "Alshorouk",
        "info_ar": "ملاهي الشروق",
        "info_en": "Alshorouk Park"
    },
    {
        "ar": "بدر",
        "en": "Badr",
        "info_ar": "قريبة من مدينة بدر",
        "info_en": "Near Badr city"
    },
    {
        "ar": "العاشر من رمضان",
        "en": "Asher of Ramadan",
        "info_ar": "منطقة حيوية وكثيفة السكان",
        "info_en": "Busy residential district"
    },
    {
        "ar": "حدائق العاصمة",
        "en": "Hadaik alasima",
        "info_ar": "قريبة من اشهر الكومباوندات",
        "info_en": "Near the most famous compounds"
    },
    {
        "ar": "العاصمة",
        "en": "Capital",
        "info_ar": "مركز العاصمة واهم المنشئات",
        "info_en": "Capital center and major facilities"
    },
]

# =========================================================
# RUNTIME STATE
# =========================================================

current_index = 0                   # Index of next station
direction = "forward"               # forward / backward
emergency_active = False             # Emergency state flag

# =========================================================
# MAIN DISPLAY WINDOW
# =========================================================

display = tk.Tk()
display.title("Metro Passenger Display")
display.configure(bg="#F5F5F2")
display.state("zoomed")
display.minsize(900, 500)

# =========================================================
# CLOCK (Bottom Right)
# =========================================================

time_label = tk.Label(
    display,
    fg="#000000",
    bg="#F5F5F2",
    font=("Arial", 16)
)
time_label.place(relx=0.98, rely=0.98, anchor="se")

# =========================================================
# MAP CANVAS
# =========================================================

canvas = tk.Canvas(display, bg="#F5F5F2", highlightthickness=0)
canvas.pack(fill="x", padx=20, pady=30)

# =========================================================
# TEXT LABELS (Main UI)
# =========================================================

alert_label = tk.Label(
    display,
    fg="red",
    bg="#F5F5F2",
    font=("Arial", 24, "bold")
)
alert_label.pack()

next_station_label = tk.Label(
    display,
    fg="#000000",
    bg="#F5F5F2",
    font=("Arial", 32, "bold"),
    justify="center",
    anchor="center"
)
next_station_label.pack(pady=(30, 60))

direction_label = tk.Label(
    display,
    fg="#6E6E6E",
    bg="#F5F5F2",
    font=("Arial", 18)
)
direction_label.pack(pady=(10, 25))

info_label = tk.Label(
    display,
    fg="#6E6E6E",
    bg="#F5F5F2",
    font=("Arial", 16)
)
info_label.pack(pady=(0, 30))

# =========================================================
# DRAWING FUNCTIONS
# =========================================================

def draw_map():
    """Draws the metro line, stations, and next-station highlight."""
    canvas.delete("all")

    width = display.winfo_width()
    spacing = (width - 200) // (len(stations) - 1)
    y = 70  # Metro line vertical position

    for i, station in enumerate(stations):
        x = 100 + i * spacing

        # Station color based on direction and progress
        if direction == "forward":
            color = "red" if i < current_index else "green"
        else:
            color = "red" if i > current_index else "green"

        # Station node
        canvas.create_oval(x-12, y-12, x+12, y+12, fill=color, outline="")

        # Blinking ring for next station
        if i == current_index and blink_on:
            canvas.create_oval(x-18, y-18, x+18, y+18, outline="blue", width=3)

        # Arabic name (top)
        canvas.create_text(
            x, y-30,
            text=station["ar"],
            fill="#000000",
            font=("Arial", 13, "bold")
        )

        # English name (bottom)
        canvas.create_text(
            x, y+35,
            text=station["en"],
            fill="#000000",
            font=("Arial", 11, "bold")
        )

        # Connecting line
        if i < len(stations) - 1:
            canvas.create_line(
                x+12, y,
                x+spacing-12, y,
                fill="#555",
                width=4
            )

# =========================================================
# UI UPDATE LOGIC
# =========================================================

def update_display():
    """Refreshes all dynamic UI elements."""
    alert_label.config(
        text="🚨 نداء طارئ | EMERGENCY ANNOUNCEMENT 🚨" if emergency_active else ""
    )

    next_station_label.config(
        text=(
            "المحطة التالية | Next Station:\n"
            f"{stations[current_index]['ar']} — {stations[current_index]['en']}"
        )
    )

    direction_label.config(
        text=(
            "الاتجاه | Direction:\n"
            f"{DIRECTIONS[direction]['ar']} | {DIRECTIONS[direction]['en']}"
        )
    )

    info_label.config(
        text=(
            "معلومات | Information:\n"
            f"{stations[current_index]['info_ar']} | "
            f"{stations[current_index]['info_en']}"
        )
    )

    draw_map()
    display.update_idletasks()

# =========================================================
# CONTROL ACTIONS
# =========================================================

def next_station():
    """Moves to the next station based on current direction."""
    global current_index

    if direction == "forward" and current_index < len(stations) - 1:
        current_index += 1
    elif direction == "backward" and current_index > 0:
        current_index -= 1

    update_display()

def switch_direction():
    """Switches travel direction and resets index."""
    global direction, current_index

    if direction == "forward":
        direction = "backward"
        current_index = len(stations) - 1
    else:
        direction = "forward"
        current_index = 0

    update_display()

def emergency_toggle():
    """Toggles emergency mode and blinking."""
    global emergency_active, alert_blinking, alert_blink_on

    emergency_active = not emergency_active

    if emergency_active:
        alert_blinking = True
        alert_blink_on = True
        blink_alert_label()
    else:
        alert_blinking = False
        alert_label.config(text="")

    update_display()

# =========================================================
# BACKGROUND TASKS (Clock & Blinking)
# =========================================================

def update_time():
    now = datetime.now()
    time_label.config(text=now.strftime("%Y-%m-%d  |  %H:%M:%S"))
    display.after(1000, update_time)

def blink_next_station():
    global blink_on
    blink_on = not blink_on
    draw_map()
    display.after(500, blink_next_station)

def blink_alert_label():
    global alert_blink_on

    if not alert_blinking:
        return

    alert_label.config(
        text="🚨 نداء طارئ | EMERGENCY ANNOUNCEMENT 🚨" if alert_blink_on else ""
    )

    alert_blink_on = not alert_blink_on
    display.after(500, blink_alert_label)

# =========================================================
# CONTROL PANEL WINDOW
# =========================================================

control = tk.Toplevel(display)
control.title("Control Panel")
control.geometry("350x300")

tk.Button(control, text="Next Station", font=("Arial", 14),
          command=next_station).pack(pady=15)

tk.Button(control, text="Switch Direction", font=("Arial", 14),
          command=switch_direction).pack(pady=15)

tk.Button(control, text="Emergency", font=("Arial", 14),
          bg="red", fg="white",
          command=emergency_toggle).pack(pady=15)

# =========================================================
# APPLICATION START
# =========================================================

update_display()
display.bind("<Configure>", lambda e: draw_map())
update_time()
blink_next_station()
display.mainloop()