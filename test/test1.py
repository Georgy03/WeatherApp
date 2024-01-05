from cProfile import label
from cgitb import text
from tkinter import font
from turtle import width
import requests
import tkinter as tk
import json
import time
from tkinter import*
from PIL import ImageTk, Image
from customtkinter import *


def Weather():
    city = search.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + \
        city + "&appid=f40b12fd7d5d619a253d927e42928cf3&units=imperial"
    results = requests.get(api).json()
    condition = results['weather'][0]['main']
    temp = int(results['main']['temp'])
    humidity = results['main']['humidity']
    wind_speed = results['wind']['speed']
    feels_like = results['main']['feels_like']
    final_info = condition + "\n" + str(temp) + " F°" + "\n" + "Humidity:" + str(humidity) + "%" + \
        "\n" + "Wind :" + str(wind_speed) + " mph" + "\n" + \
        "Feels Like " + "\n" + str(feels_like) + " F°"
    return [final_info, condition]
    #test = f"{condition} \n {str(temp)} "


screen = Tk()
screen.title("Weather")
screen.geometry("400x600")
screen.configure(bg="grey")


clear_img = ImageTk.PhotoImage(Image.open("clear.jpg").resize((918, 612)))


clouds_img = ImageTk.PhotoImage(Image.open("clouds.jpg").resize((918, 612)))

thunderstorm_img = ImageTk.PhotoImage(
    Image.open("thunderstorm.jpg").resize((918, 612)))

mist_img = ImageTk.PhotoImage(Image.open("mist.jpg").resize((918, 612)))

haze_img = ImageTk.PhotoImage(Image.open("haze.jpg").resize((918, 612)))

drizzle_img = ImageTk.PhotoImage(Image.open("drizzle.jpg").resize((918, 612)))

rain_img = ImageTk.PhotoImage(Image.open("rain.jpg").resize((918, 612)))

snow_img = ImageTk.PhotoImage(Image.open("rain.jpg").resize((918, 612)))

fog_img = ImageTk.PhotoImage(Image.open("rain.jpg").resize((918, 612)))


backgrounds = {"Clouds": [clouds_img, '#556972'], "thunderstorm": [thunderstorm_img, '#4c389d'], "Mist": [mist_img, '#b9b9b9'], "Haze": [
    haze_img, "#cecac7"], "Drizzle": [drizzle_img, ""], "Rain": [rain_img, ""], "Snow": [snow_img, ""], "Fog": [fog_img, ""], "Clear": [clear_img, "#0061bf"]}


my_canvas = Canvas(screen, width=400, height=600)
my_canvas.pack(fill="both", expand="true")


def background_func(list):
    my_canvas.create_image(-159, -10,
                           image=backgrounds[list[1]][0], anchor="nw")
    search['bg'] = backgrounds[list[1]][1]


def callback(event=None):
    weather = Weather()
    background_func(weather)
    my_canvas.create_text(220, 260, text=weather[0], fill='white', font=main)


main = ("comic sans ms", 20, 'bold')
large = ("comic sans ms", 35, 'bold')

search = tk.Entry(my_canvas, width=300, font=large, bg='#000000', fg="White")
search.pack(pady=20)
search.focus()
search.bind('<Return>', callback)


screen.mainloop()
