''' Rain API Lab '''

import random
from numpy import ma
import requests
from datetime import datetime
from data_rain import RainData
import re



response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')

text = response.text

data = re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text)



days_of_rain = []
total_tips = 0

for day in data:
    total_tips += int(day[1])
    date = datetime.strptime(day[0], '%d-%b-%Y')
    days_of_rain.append(RainData(date, int(day[1])))


most_rain = days_of_rain[0]
for day in days_of_rain:
    if day.tips > most_rain.tips:
        most_rain = day


variance = ma.var([day.tips for day in days_of_rain])

mean = total_tips / len(days_of_rain)

print(f"Start: {days_of_rain[0].date} End: {days_of_rain[-1].date} Variance: {variance} Mean: {mean} Day with most rain: {most_rain.date} with {most_rain.inches} inches")