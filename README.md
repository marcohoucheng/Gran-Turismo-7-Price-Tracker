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


# Gran Turismo 7 Shops for 27-April-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Renault|Espace F1 '95|2,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mazda|RX500 '70|600,000|
|Toyota|Supra GT500 '97|1,600,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|650,000|
|Chevrolet|Chevelle SS 454 Sport Coupé '70|150,000|
|Dodge|Charger R/T 426 Hemi '68|134,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Jaguar|XJ220 '92|548,000|
|Maserati|A6GCS/53 Spyder '54|2,800,000|
|Maserati|Merak SS '80|61,500|
|Plymouth|XNR Ghia Roadster '60|3,000,000|
|Pontiac|GTO 'The Judge' '69|196,000|
|Porsche|911 Turbo S Leichtbau (964) '93|1,200,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|Z8 '01|269,600|
|Citroen|BX 19 TRS '87|23,100|
|Dodge|Super Bee '70|61,100|
|Nissan|R32 GT-R V-spec II '94|173,400|
|Nissan|Skyline GTS-R (R31) '87|169,000|
|Renault|R5 Turbo '80|152,900|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|50,200|
|Alfa Romeo|MiTo '09|22,700|
|BMW|3.0 CSL '71|148,100|
|BMW|M3 '97|72,200|
|Chevrolet|Corvette Z06 (C5) '01|48,700|
|Honda|Civic Type R (EK) Touring Car|115,800|
|Lamborghini|Diablo GT '00|837,800|
|Mitsubishi|GTO Twin Turbo '91|49,300|
|Nissan|Silvia K's Aero (S14) '96|58,600|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|62,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|180,000|
|BMW|3.0 CSL '73|203,800|
|Ferrari|Testarossa '91|393,600|
|Maserati|GranTurismo S '08|138,200|
|McLaren|MP4-12C '10|195,700|
|Nissan|R34 GT-R V-spec II Nur '02|398,700|
|Renault|Kangoo 1.4 '01|14,100|
|Renault|R4 GTL '85|30,000|
|Renault|Twingo '93|14,000|
|Toyota|Prius G '09|20,700|
