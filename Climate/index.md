# Clowderwood Climate

- [Clowderwood Climate](#clowderwood-climate)
  - [Processes and practices](#processes-and-practices)
  - [Observation notes](#observation-notes)
    - [Pollen.com](#pollencom)
    - [2020 Rain gauge and CoCoRaHS](#2020-rain-gauge-and-cocorahs)
    - [2022 Frost data re-think](#2022-frost-data-re-think)
  - [Site map](#site-map)
    - [Acurite directories (raw data)](#acurite-directories-raw-data)
      - [v2](#v2)
      - [v1](#v1)
    - [Rain gauge directories (raw data)](#rain-gauge-directories-raw-data)

We began recording rain and then temperature and humidity at Clowderwood in 2018 and 2019. Wind speed is impractical to record because of the way wind is caught in the clearing and is redirected by the pines.

## Processes and practices

Recording climate extremes at airtable ([private link](https://airtable.com/tblGdP3Iq4ST0KGyF/viwoJZrH9rx84CDb3?blocks=hide)) and periodically exporting to extremes.csv.

For rain measurements, using a 4" diameter high capacity manual rain gauge as recommended by [CoCoRaHS](https://www.cocorahs.org/) checked daily, in general. The goal is to check between 7 and 8 am and log at [airtable](https://airtable.com/shr0qeDlQyZvvLDNt), and ideally be up to date at CoCoRaHS station number NC-CH-41. Some records are logged as 8 am when made later in the day when we are aware no precipitation has occurred. Contributions to CoCoRaHS began 2019-04-19.

For temperature and humidity, we have a [3-Sensor Temperature and Humidity Smart Home Environment System with My AcuRite](https://www.acurite.com/environment-system-with-temperature-and-humidity-01059.html)
Model #: 01006M. (Note the [Wayback Machine's last saved 2017 version of that page](https://www.acurite.com/environment-system-with-temperature-and-humidity-01059.html) is for a different model. [Private Evernote link](https://www.evernote.com/shard/s6/nl/757910/f52ba591-3caa-4a91-a629-9fe7e0a55157/)). An additional AcuRite 06044M Wireless Temperature and Humidity Monitor Sensor is used for interior measurements. InSeptember-October 2023 the external gauges were replaced and "AcuRite 06054M Temperature and Humidity Solar Radiation Shield , White" were installed on them. A new site at the rain gauge was added, and the site at the edge of the woods continues. At least once a month, the data from the Acurite dashboard ([private link](https://www.myacurite.com/#/dashboard/922231)) is downloaded.

Starting 2023-11-15, i began to also record cloud observations when checking the rain gauge as part of the NASA GLOBE program. (Site Name: 17SPV637595, Site ID: 251124, "FlowerCatcher13".) I can go to <https://vis.globe.gov/GLOBE/>, click "Data counts" at the top to create a date range,  click on the user icon on the left to view my sites, then click on the red dot at Clowderwood to view the record. I can see the past month's data and download a cvs.

## Observation notes

### Pollen.com

On 2022-02-26 created a filter for my email to copy all pollen.com emails into a folder. I'll stop transcribing the data as i have for a year or so and will plan to data mine the email collection in the future.

### 2020 Rain gauge and CoCoRaHS

Missing: 10/31 probably dry; 11/9 thru 11/25 (other stations reported rain: 11/23, 11/14, 11/13 major rain reported -loss here, i think, 11/12, 11/11, 11/10 ; 11/27 thru 12/3 (other stations report on 12/01, 11/30 - heavy -11/28, 11/27

[ ] 3 Dec 7:50 full frost,
[ ] 2 Dec 7:30 full frost -- blue skies & clear
[ ] 1 Dec 7:53 no frost 0.16
[ ] 30 Nov 8:20 .89+.48
[ ] FROST 2020-11-17 7:55  100% Frost o
[ ] 20201124 FROST 8 am >75% frost on garage roof, frost on car
[ ] 1/26/2020 last CoCoRaHS << this might be 2021

### 2022 Frost data re-think

Wrote CoCoRaHS and [downloaded copy of records (without notes)](CoCoRaHSReports/rescue%20of%20frost%20data-Grid%20view.csv)

> Hi,
>
> I would like to raise a quality concern with my Frost reports for station NC-CH-41.  I have been using a roof as my observation structure and early this fall i began to be suspicious that i might have not discerned heavy dew from light frost at times. There is also a tree that shelters a bit of the roof and I'm not sure how reflective the percent coverage is of weather conditions since the tree's state -- more leaves cause more protection and less frost -- affects the results.
>
> If this sounds like data that is problematic, i welcome you deleting the frost reports for my station.
>
> I'm not sure what i will use to replace the roof in reporting. My current plan is to observe generally in my own notes this year and then decide in Oct 2023 what the best place is. It might even be better for me to separate the frost observation from the rain measurement.
>
> Thanks for your assistance.

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

### Rain gauge directories (raw data)

The 2019 airtable export includes the following headers
> Observation, precip (in), Notes, spilled, frozen precipitation measure?, Trace, Group by month, Group by day

The 2020 file also contains a field "Recorded" to document when the entry was made at Airtable.

The v1 data is recorded at the end of the brick walkway of the house. For some time, the gauge was just left on the sidewalk. Once the apple tree was cut down, the gauge was mounted properly on the stump.
