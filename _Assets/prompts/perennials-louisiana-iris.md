# Louisiana Iris forms

## 

## Research CSV fields

``` list

Name: Final for should be selection in single quotes followed by 

Bloom time: see instruction below

Flower: flower color using the [options from the pdf](/Users/judielaine/Documents/ClowderwoodPublic/Clowderwood/_Assets/prompts/perennial-flower-options.pdf)

Vigor: list of descriptions, sentence case, ending with a period. 

Additional growth: rebloom or bloom times that explicitly reference spring or summer, sentence case, ending with a period. If breeding information is known (Seedling ID, parent selections) suround that information with square brackets. 
Hybridizer: personal names of the person who collected, selected, released, or hybridized the selected cultivar

Release year: year hybridizer released for collection or sale

Color class: if found, do not synthesize. See https://wiki.irises.org/Hist/
ColorCodes 

Standards: the petals of the flower: color, shape, details sentence case, ending with a period. 

Falls: the sepals of the flower: color, shape, details sentence case, ending with a period. 

Features: Descriptions of veining, the style, and signal (in that order) sentence case, ending with a period. 

Awards: as reported, sentence case, ending with a period. 

```

Bloom time: Prefer using the relative bloom season: `early*`, `mid*`, and `late*`. 
ONLY populate if found in a reference. For example:

* "Midseason to late" record `mid*, late*`
* "Early midseason" record "early*, mid*" 

2025-08-30 09:23:46: found both Claude and Gemini struggled to leave this empty.

Other controlled vocabulary found in [options from the pdf](/Users/judielaine/Documents/ClowderwoodPublic/Clowderwood/_Assets/prompts/perennial-flower-options.pdf)

## Derived fields

'Scientific name' : if unknown or assumed to be a hybrid, `Iris x louisiana`

'Genetics': if known to be hybrid (see `Additional growth`), `Hybrid clone`. If known

## Vendor fields

'price', 'size', 'Vendor'

## Fixed fields

'Header': Iridaceae: Iris spp & x (Louisiana)


'Name', 'Bloom time', 'Vigor', 'Scientific name', 'Genetics',
       'Additional growth', 'Hybridizer', 'Release year', 'Color class',
       'Standards', 'Falls', 'Features', 'Awards', 'Header', 'Flower',
       'height (ft)', , 'temp'],
      dtype='object'