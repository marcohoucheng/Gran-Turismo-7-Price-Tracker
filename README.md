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


# Gran Turismo 7 Shops for 19-July-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Lamborghini|Countach LP400 '74|1,250,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|883,000|
|Jaguar|D-type '54|5,300,000|
|Jaguar|XJ13 '66|12,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mazda|RX500 '70|600,000|
|McLaren|MP4/4 '88|12,000,000|
|Mercedes-Benz|W 196 R '55|20,000,000|
|Porsche|Carrera GTS (904) '64|2,250,000|
|Toyota|GT-One (TS020) '99|2,500,000|
|Toyota|Supra GT500 '97|1,600,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Maserati|GranTurismo S '08|147,200|
|Porsche|911 Turbo (930) '81|224,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|308,300|
|Chevrolet|Corvette Z06 (C5) '01|50,900|
|Ford|Mustang Mach 1 '71|43,100|
|Lamborghini|Countach 25th Anniversary '88|661,000|
|Mazda|RX-7 GT-X (FC) '90|61,100|
|Porsche|911 Carrera RS (993) '95|224,100|
|Porsche|911 Carrera RS CS (993) '95|413,100|
|Renault|Avantime 3.0 V6 24V '02|39,300|
|Renault|Twingo '93|12,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|205,300|
|Dodge|Super Bee '70|60,500|
|Dodge|Viper SRT10 Coupe '06|115,800|
|Ferrari|Dino 246 GT '71|343,200|
|Honda|Civic Type R (EK) Touring Car|115,400|
|Honda|S800 '66|49,300|
|Lamborghini|Diablo GT '00|786,300|
|Mitsubishi|GTO Twin Turbo '91|45,600|
|Mitsubishi|Lancer Evolution V GSR '98|64,800|
|Nissan|R34 GT-R V-spec II Nur '02|396,600|
|Nissan|Silvia K's Aero (S14) '96|57,000|
|Nissan|Silvia Q's (S13) '88|28,900|
|Nissan|Skyline GTS-R (R31) '87|171,600|
|Renault|Kangoo 1.4 '01|12,900|
|Renault|R5 Turbo '80|149,600|
|Toyota|Prius G '09|19,600|
|Toyota|Supra 3.0GT Turbo A '88|116,700|
|Volkswagen|Sambabus Typ 2 '62|56,400|
