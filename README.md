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


# Gran Turismo 7 Shops for 04-May-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C2) '63|248,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|650,000|
|Ferrari|F50 '95|4,700,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Renault|Espace F1 '95|2,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|356 A/1500 GS Carrera '56|606,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|
|Porsche|911 Turbo S Leichtbau (964) '93|1,200,000|
|Porsche|959 '87|1,950,000|
|Porsche|962 C '88|1,250,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mitsubishi|Lancer Evolution VIII MR GSR '04|61,000|
|Porsche|911 GT3 (996) '01|156,200|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Convertible (C3) '69|48,900|
|Chevrolet|Corvette ZR-1 (C4) '89|86,500|
|Citroen|BX 19 TRS '87|23,100|
|Dodge|Super Bee '70|61,100|
|Lamborghini|Gallardo LP 560-4 '08|252,500|
|McLaren|MP4-12C '10|195,700|
|Mitsubishi|Lancer Evolution IV GSR '96|39,800|
|Nissan|R32 GT-R V-spec II '94|173,400|
|Nissan|Silvia Q's (S13) '88|34,900|
|Nissan|Skyline GTS-R (R31) '87|169,000|
|Renault|Kangoo 1.4 '01|14,100|
|Renault|R5 Turbo '80|152,900|
|Toyota|Prius G '09|20,700|
|Volkswagen|Sambabus Typ 2 '62|55,300|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|147,100|
|BMW|Z8 '01|269,600|
|Dodge|Viper SRT10 Coupe '06|114,400|
|Ferrari|458 Italia '09|243,300|
|Ford|Escort RS Cosworth '92|122,100|
|Honda|Beat '91|17,100|
|Honda|Civic Si Extra (EF) '87|57,200|
|Honda|NSX Type R '92|388,500|
|Honda|S800 '66|42,300|
|Lancia|Stratos '73|524,500|
|Mazda|efini RX-7 Type R (FD) '91|69,600|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|179,900|
|Nissan|Sileighty '98|81,900|
|Renault|R4 GTL '85|29,200|
|Renault|Twingo '93|14,000|
