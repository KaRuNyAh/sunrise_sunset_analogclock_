from tkinter import *
import datetime
from suntime import Sun
from geopy.geocoders import Nominatim
import time
import math

root = Tk()
root.title('enjoy timing')
root.geometry("400x400")
myLabell1 = Label(root, text="one precious thing we can't get back is time", padx=40, pady=40)
myLabell1.grid()
MODES = [
    ("malaysia", "sun1"),
    ("uk", "sun2"),
    ("delhi", "sun3"),
    ("usa", "sun4"),
]
times = StringVar()
times.set("hi")
global output
global place
global rd
global top
for place, sunset in MODES:
    Radiobutton(root, text=place, variable=times, value=place).grid()

def open():
    def live_clock():
        if times.get() == "delhi":
            h, m = 0, 0
        if times.get() == "malaysia":
            h, m = 2,30
        if times.get() == "uk":
            h, m = -4,-30
        if times.get() == "usa":
            h, m = -9,-30
        hour = int(time.strftime("%I"))+h
        min = int(time.strftime("%M"))+m
        sec = int(time.strftime("%S"))
        sec_x = sec_hand_len * math.sin(math.radians(sec * 6)) + center_x
        sec_y = -1 * sec_hand_len * math.cos(math.radians(sec * 6)) + center_y
        canvas.coords(sec_hand, center_x, center_y, sec_x, sec_y)
        min_x = min_hand_len * math.sin(math.radians(min * 6)) + center_x
        min_y = -1 * min_hand_len * math.cos(math.radians(min * 6)) + center_y
        canvas.coords(min_hand, center_x, center_y, min_x, min_y)
        hour_x = hours_hand_len * math.sin(math.radians(hour * 30)) + center_x
        hour_y = -1 * hours_hand_len * math.cos(math.radians(hour * 30)) + center_y
        canvas.coords(hour_hand, center_x, center_y, hour_x, hour_y)
        canvas.after(1000,live_clock)

    top = Toplevel()
    top.geometry("600x600")
    top.title(times.get())
    buttn = Button(top, text="close window", command=top.destroy)
    buttn.grid(row=4, column=0)
    label = Label(top, text=location())
    label.grid(row=0, column=0)
    label = Label(top, text="tadaaaa:) ")
    label.grid(row=1, column=0)

    canvas = Canvas(top, width=400, height=400, bg="black")
    canvas.grid(row=6, column=0)
    # bg=PhotoImage(file= "clocktime new.png")
    # canvas.create_image(200,200,image=bg)
    sec_hand_len = 90
    min_hand_len = 80
    hours_hand_len = 60
    center_x = 200
    center_y = 200
    sec_hand = canvas.create_line(200, 200, 200 + sec_hand_len, 200 + sec_hand_len, width=1, fill="red")
    min_hand = canvas.create_line(200, 200, 200 + min_hand_len, 200 + min_hand_len, width=3, fill="white")
    hour_hand = canvas.create_line(200, 200, 200 + hours_hand_len, 200 + hours_hand_len, width=5, fill="yellow")
    live_clock()


btn = Button(root, text="open window", command=open)
btn.grid()




def location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(times.get())
    # latitude and longitude fetch
    latitude = location.latitude
    longitude = location.longitude
    sun = Sun(latitude, longitude)
    # date in your machine's local time zone
    time_zone = datetime.date(2021, 7, 24)
    r = sun.get_local_sunrise_time(time_zone)
    d = sun.get_local_sunset_time(time_zone)
    rd = "Sun rise at : " + r.strftime('%H:%M') + "  Dusk at : " + d.strftime('%H:%M')
    return rd


mainloop()
