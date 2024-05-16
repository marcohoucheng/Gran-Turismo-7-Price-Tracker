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


# Gran Turismo 7 Shops for 16-May-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Toyota|Supra GT500 '97|1,800,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Nissan|Fairlady Z 432 '69|190,000|
|Shelby|Cobra Daytona Coupe '64|20,000,000|
|Toyota|GT-One (TS020) '99|2,500,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|892,000|
|Ferrari|250 GT Berlinetta passo corto '61|8,400,000|
|Maserati|Merak SS '80|68,000|
|McLaren|MP4/4 '88|10,000,000|
|Nissan|Skyline Super Silhouette Group 5 '84|1,150,000|
|Porsche|Carrera GTS (904) '64|2,300,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Fiat|500 1.2 8V Lounge SS '08|13,300|
|Honda|Beat '91|16,800|
|Lamborghini|Murcielago LP 640 '09|337,200|
|Mitsubishi|Lancer Evolution V GSR '98|77,500|
|Nissan|Silvia K's Dia Selection (S13) '90|49,700|
|Porsche|911 GT3 (997) '09|142,500|
|Volkswagen|Volkswagen 1200 '66|35,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Super Bee '70|71,900|
|Ferrari|Dino 246 GT '71|343,900|
|Honda|S2000 '99|100,100|
|Lancia|Delta HF Integrale Evoluzione '91|101,900|
|Nissan|Sileighty '98|72,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|308,300|
|BMW|3.0 CSL '71|141,500|
|BMW|3.0 CSL '73|211,200|
|BMW|Z8 '01|259,100|
|Ford|Sierra RS 500 Cosworth '87|193,500|
|Honda|Civic Type R (EK) '97|58,100|
|Honda|Civic Type R (EK) Touring Car|115,400|
|Maserati|GranTurismo S '08|147,400|
|Mazda|Eunos Roadster (NA) '89|26,500|
|McLaren|MP4-12C '10|197,300|
|Mitsubishi|GTO Twin Turbo '91|40,000|
|Nissan|Fairlady 240ZG (HS30) '71|98,500|
|Nissan|R34 GT-R V-spec II Nur '02|396,600|
|Porsche|911 Turbo (930) '81|215,600|
|RUF|CTR3 '07|801,800|
|Subaru|Impreza Sedan WRX STi '04|47,100|
