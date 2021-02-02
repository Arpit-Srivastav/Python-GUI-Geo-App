import tkinter as tk
from tkinter import font
import requests

h = 500
w = 600

def format_response(geo_value):
    try:
        name = geo_value[0]['name']
        name_hindi = geo_value[0]['local_names']['hi']
        name_french = geo_value[0]['local_names']['fr']
        latitude = geo_value[0]['lat']
        longitude = geo_value[0]['lon']
        country = geo_value[0]['country']

        final_str = "City: %s \nशहर: %s \nVille: %s \nLatitude: %s \nLongitude: %s \nCountry Code: %s" % (name, name_hindi, name_french, latitude, longitude, country)
    except:
        final_str = "Oops!! \nLocation cannot be found :( !!"

    return final_str


def get_geo(city):
    geo_key = "ec322ec2c5650f6ca414eebde213f3df"
    url = "https://api.openweathermap.org/geo/1.0/direct"
    params = { 'AppID': geo_key, 'q': city}
    response = requests.get(url, params=params)
    geo_value = response.json() # json will convert the response into Python Dictionary
#    print(geo_value)
#    print(geo_value[0]['name'])
#    print(geo_value[0]['local_names']['hi'])
#    print(geo_value[0]['local_names']['fr'])
#    print(geo_value[0]['lat'])
#    print(geo_value[0]['lon'])
#    print(geo_value[0]['country'])
    label['text'] = format_response(geo_value)

root = tk.Tk()

canvas = tk.Canvas(root, height=h, width=w)
canvas.pack()

background_image = tk.PhotoImage(file = "Earth.png") # or put complete path of the image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1 , relheight=1)

frame = tk.Frame(root, bg="#6666ff", bd=5)
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor="n") # anchor="n" to put frame in centre

entry = tk.Entry(frame, font=('Arial Baltic',14))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Go!!!", font=('Arial',12), command=lambda: get_geo(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n") # anchor="n" to put frame in centre

label = tk.Label(lower_frame, font=('Arial Baltic',16) ,anchor="nw", justify="left", bd=4)
label.place(relwidth=1, relheight=1)

#print(tk.font.families()) # to know all the fonts present in tkinter

root.mainloop()
