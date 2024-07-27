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


# Gran Turismo 7 Shops for 27-July-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|NSX GT500 '00|1,500,000|
|Jaguar|D-type '54|6,000,000|
|Mercedes-Benz|S Barker Tourer '29|13,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|Sport quattro S1 Pikes Peak '87|1,900,000|
|Jeep|Willys MB '45|30,100|
|Porsche|Spyder type 550/1500RS '55|4,850,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|McLaren|McLaren F1 '94|20,000,000|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|280,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Subaru|Impreza Rally Car '98|650,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|McLaren|MP4-12C '10|194,100|
|Nissan|Skyline GTS-R (R31) '87|162,200|
|Porsche|911 Carrera RS (993) '95|229,200|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray (C3) '69|71,500|
|Chevrolet|Corvette ZR1 (C6) '09|98,400|
|Mercedes-Benz|SLR McLaren '09|493,500|
|Mitsubishi|Lancer Evolution V GSR '98|77,500|
|Nissan|Silvia K's Aero (S14) '96|59,300|
|Porsche|911 Turbo (930) '81|215,600|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|97,800|
|Volkswagen|Sambabus Typ 2 '62|57,100|
|Volkswagen|Volkswagen 1200 '66|35,800|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|137,600|
|BMW|M3 '97|74,600|
|Ferrari|430 Scuderia '07|366,700|
|Ford|Mustang Mach 1 '71|36,800|
|Honda|Beat '91|16,800|
|Honda|Civic SiR-II (EG) '93|52,500|
|Honda|Integra Type R (DC2) '98|62,100|
|Lamborghini|Countach 25th Anniversary '88|711,800|
|Lamborghini|Gallardo LP 560-4 '08|253,100|
|Mitsubishi|Lancer Evolution IV GSR '96|44,200|
|Nissan|R32 GT-R V-spec II '94|176,500|
|Nissan|R33 GT-R V-spec '97|155,200|
|Renault|R4 GTL '85|24,100|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|53,600|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|46,800|
|Toyota|Supra 3.0GT Turbo A '88|115,900|
