# Gran Turismo 7 tracker for in-game dynamic prices for cars

This is a personal project built on Python to obtain in-game stores information of Gran Turismo 7 without the necessarity to manually start the game on PlayStation 5. It has the following functionalities:

- An automated daily email to list updates in game.
- Aggregate data to build a local database of cars' historical prices,
- Return latest information of cars given a wish list.

Data are scraped from https://github.com/ddm999/gt7info. Tools providing similar information are available on https://gtdb.io. However, the site requires an account to receive daily emails. The setup of this project allows for a setup without having to sign up for an account.

The approach of this project is to provide a solution without setting an account.

# Usage

## Daily Email

A scheduled Github Action is currently set up. However, the user can easily set up a similar system. Only `email_update.py` is needed in this case with the appropriate environment varibles for `SENDER_EMAIL`, `PASSWORD` and `RECIPIENTS`. A [screenshot](https://raw.githubusercontent.com/marcohoucheng/Gran-Turismo-7-Price-Tracker/main/data/email_screenshot.png) of the email and the latest html copy is shown below.

## Wish list and local database

1. Build databases by running `build.py`. It will also detect whether `shop.py` and `car.py` should be run.
    - Only the respective shop will be built if ran with flag `used` or `legend`. Nevertheless, `shop.py` and `car.py` will still be triggered if necessary.
2. Run `update.py` to update the local shop databases.
    - Similar to `build.py`, `used` or `legend` flags can be called.
3. `wish.py` checks whether cars in the wish list `wish_list.txt` are available today. If so, then it will return the price. Otherwise, it returns the last available date and the price.
    - This script will automatically run `update.py` when checking whather cars on wish list are available.
4. Running `today.py` returns items available in the shops in terminal. With flag `new` the script will only return new days of the day.


# Gran Turismo 7 Shops for 01-July-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|Spyder type 550/1500RS '55|4,950,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Citroen|DS 21 Pallas '70|44,600|
|Honda|RA272 '65|2,500,000|
|Jeep|Willys MB '45|33,500|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|Sport quattro S1 Pikes Peak '87|1,700,000|
|Chevrolet|Camaro Z28 '69|101,000|
|De Tomaso|Mangusta '69|310,000|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|250,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Porsche|911 Turbo S Leichtbau (964) '93|1,200,000|
|Shelby|Cobra 427 '66|2,700,000|
|Toyota|2000GT '67|982,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '89|73,100|
|Ford|Sierra RS 500 Cosworth '87|183,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|De Tomaso|Pantera '71|173,100|
|Ferrari|512 BB '76|313,400|
|Honda|NSX Type R '02|431,500|
|Pontiac|Firebird Trans Am '78|86,900|
|Suzuki|Swift Sport '07|12,900|
|Toyota|Supra RZ '97|190,800|
|Volkswagen|Golf I GTI '83|41,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Autobianchi|A112 Abarth '85|28,900|
|BMW|M3 '03|65,500|
|BMW|M3 '07|68,500|
|Chevrolet|Corvette Stingray (C3) '69|62,000|
|Dodge|Viper GTS '02|102,800|
|Ferrari|430 Scuderia '07|370,400|
|Honda|Civic Type R (EK) '98|51,700|
|Honda|Integra Type R (DC2) '95|56,400|
|Honda|NSX Type R '92|450,000|
|MINI|MINI Cooper S '05|22,900|
|Mitsubishi|Lancer Evolution IV GSR '96|55,000|
|Nissan|Fairlady Z 300ZX TT 2seater '89|58,000|
|Nissan|SILVIA spec-R Aero (S15) '02|59,800|
|Nissan|Silvia K's Type S (S14) '94|47,200|
|Porsche|911 Carrera RS (964) '92|218,000|
|Renault|Clio V6 24V '00|73,600|
|Suzuki|Cappuccino (EA11R) '91|19,800|
|Toyota|MR2 GT-S '97|54,900|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|58,200|
