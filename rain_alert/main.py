import requests
import smtplib
parameters = {
    "lat": -34.6863791, #LATITUDE FROM YOUR CITY
    "lon": -58.6572849, #LONGITUDE FROM YOUR CITY
    "APPID": "4fe884576ecc143a3d858ffd7049a93f", # YOU APP ID, CREATE A ACCOUNT IN openweathermap for a API authentication
}

my_email = "MY EMAIL" # HERE PUT YOUR EMAIL
password = "" #HERE PUT YOUR CODE VERIFICATION EMAIL


def will_rain():
    if id_weather < 600:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:Weather Data\n\n Today, it's gonna rain")


request = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
request.raise_for_status()
weather_data = request.json()["weather"]
id_weather = weather_data[0]["id"]
will_rain()



