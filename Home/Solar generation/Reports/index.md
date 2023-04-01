# Enphase Reports

Power production began 2023-03-22.

## About report types

Enphase reports are available at [the website](https://enlighten.enphaseenergy.com/web/4006647/history/graph/hours?source=my_enlighten)

An initial strategy:

Monthly reporting all year:

* download the Daily production report for the month
* download the per module one month production report for the month
* around the solstices, also download the Recent production (previous seven days) for a snapshot (sun angle changing more slowly)

Weekly reporting for the equinox quarters

* download the Recent production (previous seven days, ideally Saturdays)
* download best day for the week of per module one day production report.
### Daily production

Download menu has a date picker; the file is named `4006647_system_energy_YYYYMMD1_to_YYYYMMD2.csv`.

Report has two columns with headers, "Date/Time" and "Energy Delivered (kWh)", and one row per day. Date is in the format "03/22/2023"

### Recent production

The page says, "Summary of the last week of power production in 5 minute increments of this site," and the report can only be emailed. The report covers the previous week, the seven days before the report is generated. The file is named `4006647_system_power_YYYYMMD2.csv`.

Report has two columns with headers, "Date/Time" and "Power Delivered (W)" and one row every five minutes. "Date/Time" is in the format "03/25/2023 12:55 AM EDT". Quantities less than 1000 are expressed as an integer, while 1k and greater are in quotes and have a comma for marking the thousands place.

### Monthly production

This is a nice summary to view on the site, but less valuable to download.

Download menu has a month picker.

Report has two columns with headers, "Week","Peak Power", and "Energy Produced".

Weeks are seven-day divisions of the month starting on the first day of the month an dare in the format "03/01/2023 - 03/07/2023". For months other than February, the last week is less than seven days.

"Peak Power" and "Energy Produced" don't have units in the header because the entries have units, and the units can vary (W vs kW and Wh vs kWh).

Following the weeks are some summary and comparison rows.

### Per Module One Day and One Month

Download has a day and a month picker, respectively. This is a nice set of reports for observing shade effects and module health; somewhat frustrating that the downloads are day by day.

Perhaps downloading best of each week for the quarter of the year around the equinox could give some sense of panel performance as seasons change.

The date must be determined from the file name, which ends in either the day or month: `4006647_system_module_energy_YYYYMMDD.csv`

Reports have two columns with headers:

* daily: Serial Number,Energy Production (Wh)
* monthly: Serial Number,Energy Production (kWh)

A final total line is provided.
