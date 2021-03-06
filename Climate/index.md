# Clowderwood Climate

- [Clowderwood Climate](#clowderwood-climate)
  - [Processes and practices](#processes-and-practices)
  - [Site map](#site-map)
    - [Acurite directories (raw data)](#acurite-directories-raw-data)
      - [v2](#v2)
      - [v1](#v1)
    - [Raingauge directories (raw data)](#raingauge-directories-raw-data)

We began recording rain and then temperature and humitdity at Clowderwood in 2018 and 2019. Windspeed is impractical to record because of the way wind is caught in the clearing and is redirected by the pines.

## Processes and practices

Recording climate extremes at airtable ([private link](https://airtable.com/tblGdP3Iq4ST0KGyF/viwoJZrH9rx84CDb3?blocks=hide)) and periodically exporting to extremes.csv.

For rain measurements, using a 4" diameter high capacity manual rain gauge as recommended by [CoCoRaHS](https://www.cocorahs.org/) checked daily, in general. The goal is to check between 7 and 8 am and log at [airtable](https://airtable.com/shr0qeDlQyZvvLDNt), and ideally be up to date at CoCoRaHS station number NC-CH-41. Some records are logged as 8 am when made later in the day when we are aware no precipitation has occured. Contributions to CoCoRaHS began 2019-04-19.

For temperature and humidity, we have a [3-Sensor Temperature and Humidity Smart Home Environment System with My AcuRite](https://www.acurite.com/environment-system-with-temperature-and-humidity-01059.html)
Model #: 01006M. (Note the [Wayback Machine's last saved 2017 version of that page](https://www.acurite.com/environment-system-with-temperature-and-humidity-01059.html) is for a different model. [Private Evernote link](https://www.evernote.com/shard/s6/nl/757910/f52ba591-3caa-4a91-a629-9fe7e0a55157/)). An additional AcuRite 06044M Wireless Temperature and Humidity Monitor Sensor is used for interior measurements. At least once a month, the data from the Acurite dashboard ([private link](https://www.myacurite.com/#/dashboard/922231)) is downloaded.

## Site map

### Acurite directories (raw data)

These contain the export of the Acurite sensors from the Acurite dashboard ([private link](https://www.myacurite.com/#/dashboard/922231)), named by the date the extract occurred. One is limited to extracting a month's worth of data at a time. Gaps and overlaps occur between files.

The exports include the following headers, many of which are unused:

> Temperature ( F ),Humidity ( RH ),Dew Point ( F ),Heat Index ( F ),Feels Like,Wind Chill,Barometric Pressure ( INHG ),Accumulated Rain,Wind Speed,Wind Average,Wind Direction,Wired Sensor Temperature,Wired Sensor Humidity,Soil & Liquid Temperature,Water Detected,UV Index,Light Intensity,Measured Light,Lightning Strike Count,Lightning Closest Strike Distance

The timestamp format is "2019/11/16 12:00 AM"  Data is recorded every five minutes.

#### v2

- Temp & Humidity Sensors:
  - Sensor labels  
    - Back Fence
    - Garage
    - Greenhouse
    - In home  (w/display)
  - Sensors record: Temperature ( F ), Humidity ( RH ), Dew Point ( F ), Heat Index ( F ), and Barometric Pressure ( INHG )

#### v1

This period includes a number of changes before the stable v2 set up. The initial purchase came with three sensors. These were installed on the back porch (Porch), inside the greenhouse (Greenhouse), and inside (Home).  I purchased  on October 25, 2019 a fourth sensor for inside use, and then moved the previously inside sensor to the back fence. This allowed a short period to compare the previously outside "Porch" sensor had significant differences from the back fence sensor.

At some point before Nov 12, 2019 I moved what had been the deck thermometer into garage. I also moved back fence sensor much closer to SE corner where it is likely in more shade and less likely to be affected by sun.

Initially the back porch sensor was connected to [Wunderground](https://www.wunderground.com/dashboard/pws/KNCPITTS52/graph/2019-08-31/2019-08-31/monthly). When the porch sensor was moved to the garage, I forgot to switch Wunderground to the new outside sensor. Eventually, on 2020-02-02 i just disconnected Acurite from Wunderground.

The Evernote directory contains the summaries i was keeping using data from Wunderground. By 2019-12, i had realized the best thing to do was at least a monthly export.

### Raingauge directories (raw data)

The 2019 airtable export includes the following headers
> Observation, precip (in), Notes, spilled, frozen precipitation measure?, Trace, Group by month, Group by day

The 2020 file also contains a field "Recorded" to document when the entry was made at Airtable.

The v1 data is recorded at the end of the brick walkway of the house. For some time, the gauge was just left on the sidewalk. Once the apple tree was cut down, the gauge was mounted properly on the stump.
