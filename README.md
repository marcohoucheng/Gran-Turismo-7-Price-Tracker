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


# Gran Turismo 7 Shops for 04-January-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|330 P4 '67|20,000,000|
|Porsche|911 Carrera RS (901) '73|799,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|GT40 Mark I '66|6,700,000|
|Honda|RA272 '65|2,500,000|
|Lamborghini|Miura P400 Bertone Prototype '67|4,300,000|
|McLaren|MP4/4 '88|12,000,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|
|Shelby|Cobra Daytona Coupe '64|20,000,000|
|Subaru|Impreza Rally Car '98|650,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|GIULIA TZ2 carrozzata da ZAGATO '65|3,800,000|
|Alpine|A220 Race Car '68|330,000|
|Dodge|Challenger R/T '70|214,000|
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,600,000|
|Shelby|G.T.350 '65|455,000|


## Used shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|206,500|
|Ford|Ford GT '06|397,100|
|Ford|Mustang Mach 1 '71|50,000|
|Honda|Civic SiR-II (EG) '93|50,800|
|Lamborghini|Countach 25th Anniversary '88|800,000|
|Nissan|Fairlady Z 300ZX TT 2seater '89|60,300|
|Nissan|Fairlady Z Version S (Z33) '07|30,800|
|Nissan|Silvia K's Dia Selection (S13) '90|52,100|
|Renault|R4 GTL '85|24,700|
|Toyota|Supra RZ '97|194,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|23,900|
|Audi|TT Coupe 3.2 quattro '03|43,300|
|Audi|TTS Coupe '09|67,600|
|BMW|M3 '07|70,200|
|BMW|M3 '89|86,100|
|Chevrolet|Corvette Stingray (C3) '69|54,700|
|De Tomaso|Pantera '71|172,800|
|Ferrari|430 Scuderia '07|363,500|
|Ferrari|F430 '06|207,400|
|Honda|Beat '91|17,000|
|Honda|Integra Type R (DC2) '95|60,300|
|Mazda|Eunos Roadster (NA) '89|28,600|
|Nissan|GT-R NISMO (R32) '90|393,800|
|Nissan|SILVIA spec-R Aero (S15) '02|58,400|
|Porsche|911 Carrera RS (964) '92|220,000|
|Renault|Clio V6 24V '00|72,800|
|Subaru|Impreza 22B-STi '98|178,300|
|TVR|Tuscan Speed 6 '00|70,100|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|58,400|
|Toyota|MR2 GT-S '97|58,100|
|Volkswagen|Sambabus Typ 2 '62|54,300|
|Volvo|240 SE Estate '93|41,800|
