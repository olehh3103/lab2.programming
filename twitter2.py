from geopy.geocoders import Nominatim
import folium
from flask import Flask, redirect, render_template, request, url_for
import urllib.request
import urllib.parse
import urllib.error
import json
import ssl
import twurl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def find_a_location():
    """
    html function which has two methods: "POST", "GET"
    """
    if request.method == "GET":
        return render_template("login.html")
    else:
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    

@app.route("/<usr>")
def user(usr):
    """
    main function which works with twiter user nickname
    and find location from JSON file.
    """
    try:
        # a = input('Enter Twitter Account:')
        url = twurl.augment(TWITTER_URL,
                            {'screen_name': usr, 'count': '10'})
        print('Retrieving', url)
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()
        js = json.loads(data)
        data = js['users']
        counter = 0
        my_map = folium.Map(tiles="Stamen Terrain", zoom_start=10)
        for i in range(len(data)):
            friends_name = data[i]['name']
            location = data[i]['location']
            if location != "":
                print("1")
                try:
                    geolocator = Nominatim(user_agent="olehh")
                    location = geolocator.geocode(location)
                    lat = location.latitude
                    lon = location.longitude
                    folium.Marker(location= [lat, lon], popup=friends_name,
    icon=folium.Icon(color='blue', icon='home', prefix='fa')).add_to(my_map)
                except AttributeError:
                    pass
        # my_map.save('oleh_op.html')
        
    except urllib.error.HTTPError:
        print("name not found")
    return my_map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)

