# Instructions for perennial import csvs

* [Instructions for perennial import csvs](#instructions-for-perennial-import-csvs)
  * [Brent and Becky CSV](#brent-and-becky-csv)
  * [Native species CSV](#native-species-csv)
    * [Fields in Perennial table](#fields-in-perennial-table)
    * [Instruction variations](#instruction-variations)
  * [Louisiana Iris collection](#louisiana-iris-collection)
  * [Data collection](#data-collection)
  * [Import from review articles](#import-from-review-articles)
    * [Chicago botanic asters](#chicago-botanic-asters)
      * [Instruction 1 height \& width](#instruction-1-height--width)
      * [Instruction 2 Notes](#instruction-2-notes)
      * [Instruction 3 Header](#instruction-3-header)
      * [Instruction 4 Name](#instruction-4-name)
      * [Instruction 5 Genetics](#instruction-5-genetics)
      * [Instruction 6 Flower (color)](#instruction-6-flower-color)
      * [Instruction 7 Bloom time](#instruction-7-bloom-time)
      * [Instruction 8 terms](#instruction-8-terms)

## Brent and Becky CSV

I will be pasting in text from a vendor, and each selection i would like you to create a row in a csv file. Most of the plants are named by the vendor `[Genus] - [Species] '[Selection]'`  with a few variations.

CSV fields:

``` list
Name:  '[Selection]' [Genus] -- or -- [Scientific name] -- else -- [As listed]
Scientific name: [Scientific name] '[Selection]'
Family: [Taxonomic family]
Plan code: `Add2`
Code: `Want2025` 
Bloom time: >> construct comma separated list from `Bloomtime` according to attached pdf list of terms
Flower: >> construct from `Color` according to attached pdf list of terms
height (ft): >> see instruction 1
Δh (ft): >> see instruction 1
Notes: >> see instruction 2
Header:  >> see instruction 3
Genetics: >> see instruction 4
Terms:  >> see instruction 4
price >> if there are two prices, use the lesser

```

Instruction 1: Usually height data is given as a range. Here, if the range is 5 to 10 ft, the values would be 7.5 with a delta of 2.5. Convert inches to feet.

Instruction 2:  Construct the note

1. Interpretation:
   1. Where it says `This item may be purchased in any quantity that is divisible by 10`  the `quantity sold` is 10
   2. There is a `general description` such as "Large, rich, amethyst-violet on the inside; outside gray; squirrel resistant; vigorous; 5/7 cm."
   3. `Area` is `Per sq. ft.: 10-15`
   4. `Sun` is `Sun: Full Sun, Part Shade`
   5. `Moisture` is `Moisture: Average, Dry`
2. Construct the Notes field as:

    ``` text
    {general description} {Area}.
    {Sun}; {Moisture}
    B&B sells in units of {quantity sold}. 
    ```

Instruction 3: For most plant families, the Header field is populated as follows

`Header: [Taxonomic family]: [Species] spp ([Species type])`

For the plants in family Liliaceae, use patterns like the following when taxonomy is contentious

* Liliaceae (alt Asphodelaceae)
* Liliaceae (alt Asphodelaceae)
* Liliaceae (alt Asparagaceae, Agavaceae)

For the plants in families Apiaceae, Asteraceae, Fabaceae, Lamiaceae, Poaceae, and Rosaceae use this as a pattern for the Header value

"Rosaceae-Amygdaloideae-Amygdaleae: Prunus spp (plums and cherries)"

Instruction 4:

If listed without a selection name but a scientific name

* Genetics: `Species`
* Terms:  `species`

If listed with a selection and a scientific name

* Genetics: `Selection`
* Terms:  `unknown`

Otherwise leave genetics blank and terms unknown

* Genetics: ""
* Terms:  `unknown`

## Native species CSV

Before submitting to AI:

1. Update the first list with plants of interest
2. Copy the field list and change as needed.
3. Verify correct "Code:" value.
4. Add any notes to Instruction 2 for Notes

Please prepare a csv for the following

``` list
Rhododendron canescens
Rhododendron periclymenoides
Rhododendron austrinum
Rhododendron viscosum
Rhododendron minus
```

CSV fields:

``` list
Name:  [Scientific name] ([common name])
Scientific name: [Scientific name]
Family: [Taxonomic family]
Plan code: `Added`
Code: `Interesting` 
Genetics: `Species` 
Terms:  `species` 
Use: `naturalizing` 
height (ft): >> see instruction 1
Δh (ft): >> see instruction 1
width (ft): >> see instruction 1
Δw(ft): >> see instruction 1
Notes: >> see instruction 2
Header:  >> see instruction 3
```

Instruction 1: I prefer height and width from <https://plants.ces.ncsu.edu/> . Usually this data is given as a range. Here, if the range is 5 to 10 ft, the values would be 7.5 with a delta of 2.5. Convert inches to feet.

Instruction 2: Populate with the following tags if information available at <https://plants.ces.ncsu.edu/>

* `#similar-to-redbuds` if would grow in similar conditions to redbuds (shade, moisture, clay soil)
* `evergreen` if evergreen
* `under walnut` if tolerates walnuts and noted so at NCSU ("Resistance To Challenges")
* `#low-flammability` or `#high-flamabiliyt` First reference the NCSU Plants toolbox <https://plants.ces.ncsu.edu/>. Note when the tags differ from the "Fire risk rating" and prefer the "#fire low flammability" even if "Fire risk rating" is "medium flammability", checking other sources
* `#rabbit-resistant` `#deer-resistant` if noted so at NCSU
* `#deer-rutgersA` `#deer-rutgersB` `#deer-rutgersC`  etc if listed in a group at <https://njaes.rutgers.edu/deer-resistant-plants/>

Instruction 3: For most plant families, the Header field is populated as follows

`Header: [Taxonomic family]: [Species] spp ([Species type])`

For the plants in family Liliaceae, use patterns like the following when taxonomy is contentious

* Liliaceae (alt Asphodelaceae)
* Liliaceae (alt Asphodelaceae)
* Liliaceae (alt Asparagaceae, Agavaceae)

For the plants in families Apiaceae, Asteraceae, Fabaceae, Lamiaceae, Poaceae, and Rosaceae use this as a pattern for the Header value

"Rosaceae-Amygdaloideae-Amygdaleae: Prunus spp (plums and cherries)"

### Fields in Perennial table

``` list
Name:  [Scientific name] ([common name])
Scientific name: [Scientific name]
Family: [Taxonomic family]
Plan code: `Added`
Code: `Have` 
Genetics: `Species` 
Terms:  `species` 
Use: `naturalizing` 
height (ft): >> see instruction 1
Δh (ft): >> see instruction 1
width (ft): >> see instruction 1
Δw(ft): >> see instruction 1
Notes: >> see instruction 2
Header:  >> see instruction 3
```

### Instruction variations

* Instruction 2: Populate as indicated above with the following

## Louisiana Iris collection

``` list
Name:  [Scientific name] ([common name])
Scientific name: [Scientific name]
Family: [Taxonomic family]
Plan code: `Added`
Code: `Have` 
Genetics: `Species` 
Terms:  `species` 
Use: `naturalizing` 
height (ft): >> see instruction 1
Δh (ft): >> see instruction 1
width (ft): >> see instruction 1
Δw(ft): >> see instruction 1
Notes: >> see instruction 2
Header:  >> see instruction 3
```

## Data collection

``` text

Hardy https://www.plantdelights.com/products/lantana-camara-miss-huff

Low growing: https://woodlanders.net/products/lantana-camara-hybrida?_pos=1&_psq=lantana&_ss=e&_v=1.0 
Lantana camara "Hybrida"
This Lantana hybrid performs best in zones 8 and 9 when placed in a sheltered location. It holds up well in hot summers and supports garden structure with minimal care.

Use it in borders, slopes, or large containers. With regular water and rich soil, this yellow flowering plant produces color throughout the warm season and fills gaps with dense foliage.
===

Bandana® 'Yellow Improved'
Lantana camara
Lantana camara PP25,451 << not sure that is right>>

    Nice compact, mounding habit
    Nice groundcover for very hot, dry areas
    Tolerates poor soil conditions
    Loads of flowers all summer!

    Height: 18-24 in
    Spread: 18-24 in
    Zone: 8-11


Height: 1' - 1.5'
Spread: 1’ - 1.5'
Spacing: 1.5'

USDA Hardiness Zone: 9- 11

Bandana&reg: Yellow Lantana is recommended for the following landscape applications:

    Mass Planting
    Border Edging
    General Garden Use
    Container Planting
    Hanging Baskets

. Lantana is killed at 28° F, so must be protected from frosts and moved indoors for the winter if you wish to keep the plant
```

## Import from review articles

### Chicago botanic asters

Hawke, Richard G. A Comparative Study of Cultivated Asters. Plant Evaluation Notes, no. 36. Chicago Botanic Garden, 2013. <https://www.chicagobotanic.org/downloads/planteval_notes/no36_asters.pdf>.

``` csv
Overall Rating, Aster, Flower Color, Flower Size, Bloom Period, Flower Coverage, Plant Height, Plant Width, Mildew Resistance, Rust Resistance
```

Use the table in the  article to create a csv with these columns:

``` list
Name:  >> see instruction 4
Scientific name:  {Aster}
Code: `UNK` 
Genetics: >> see instruction 5
Terms:  >> see instruction 8
Use: `naturalizing , landscaping`
height (ft): >> see instruction 1
width (ft): >> see instruction 1
Notes: >> see instruction 2
Header:  >> see instruction 3
Bloom time: >> see  instruction 7
Flower: >> see instruction 6
```

#### Instruction 1 height & width

Convert inches to feet.

#### Instruction 2 Notes

Construct the note as follows

`Hawke 2013: {Overall Rating} Flower color: {Flower Color}, coverage: {Flower Coverage}, size: {Flower size}. Mildew resistance: {Mildew Resistance}, rust resistance: {Rust Resistance}. [also height & width]. {Chicago winter comment}`

For `Chicago winter comment` please note along the lines "Score likely lower due to Chicago winter response" when the lack of cold tolerance is likely to be a contributor to the low score.

#### Instruction 3 Header

One of the four:

* Asteraceae-Asteroideae-Astereae: Symphyotrichum spp
* Asteraceae-Asteroideae-Astereae: Aster spp.
* Asteraceae-Asteroideae-Astereae: Doellingeria spp.
* Asteraceae-Asteroideae-Astereae: Eurybia spp.

#### Instruction 4 Name

Replace the single quotes such as in in "Symphyotrichum ‘Cassie’" with parentheses: "Symphyotrichum (Cassie)".

#### Instruction 5 Genetics

When no cultivar name present, `Species`
When genus and species present, `Selection`
When just genus, `Hybrid`

#### Instruction 6 Flower (color)

``` map
white -> white
lavender  -> purple
dark lavender  -> purple
violet  -> purple
lavender-blue  -> blue purple
violet-blue  -> blue purple
light purple  -> purple
pale pink -> pink
bright purple  ->  purple
purple-pink -> pink purple
red-purple  -> rose
purple -> purple
magenta  -> rose
pale lavender  -> purple
vivid pink -> rose
pale blue  -> blue
pale lavender-blue  ->  blue purple
lilac-purple  -> purple
cerise-pink -> rose
rosy pink -> rose
light violet-blue
deep pink -> rose
purple-red -> vermillion
light red -> pink
purple-blue  -> blue
light blue  -> blue
blue-purple  -> blue purple
```

#### Instruction 7 Bloom time

These are the seasonal maps i use for here in zone 8a North Carolina. Estimate the Chicago date mapping to North Carolina as best you can.

``` map
early spring <- Feb March
spring <- mid March into April
late spring <- May
early summer <- June
summer <- July
late summer <- Aug
early autumn <- Sept
autumn <- Oct
late autumn <- Nov

```

#### Instruction 8 terms

Use the csv analysis you did previously.
