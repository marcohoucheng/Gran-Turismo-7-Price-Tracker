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


# Gran Turismo 7 Shops for 02-August-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Shelby|Cobra Daytona Coupe '64|20,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|McLaren|McLaren F1 GTR - BMW '95|15,000,000|
|Mercedes-Benz|S Barker Tourer '29|13,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Charger R/T 426 Hemi '68|158,000|
|Honda|NSX GT500 '00|1,500,000|
|Jaguar|D-type '54|6,000,000|
|Jaguar|XJ13 '66|12,000,000|
|Lamborghini|Countach LP400 '74|1,350,000|
|McLaren|McLaren F1 '94|20,000,000|
|Mercedes-Benz|300 SL Coupe '54|1,700,000|
|Nissan|GT-R GT500 '99|2,500,000|
|Porsche|356 A/1500 GS Carrera '56|618,000|
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,600,000|
|Subaru|Impreza Rally Car '98|650,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Toyota|Celica GT-Four (ST205) '94|65,100|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|Civic SiR-II (EG) '93|52,500|
|Pontiac|Firebird Trans Am '78|87,900|
|Volvo|240 SE Estate '93|47,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|310,900|
|Alpine|A110 '72|142,200|
|BMW|M3 '97|74,600|
|BMW|Z8 '01|267,200|
|Chevrolet|Corvette Convertible (C3) '69|58,200|
|Daihatsu|Copen '02|15,700|
|Dodge|Super Bee '70|61,100|
|Ferrari|430 Scuderia '07|366,700|
|Ferrari|Dino 246 GT '71|338,000|
|Honda|Civic Type R (EK) Touring Car|122,400|
|Lamborghini|Gallardo LP 560-4 '08|253,100|
|Lamborghini|Murcielago LP 640 '09|318,700|
|Lancia|Stratos '73|539,300|
|Maserati|GranTurismo S '08|137,700|
|Mazda|RX-7 GT-X (FC) '90|53,800|
|McLaren|MP4-12C '10|194,100|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|174,200|
|Nissan|Fairlady Z 300ZX TT 2seater '89|70,000|
|Nissan|R34 GT-R V-spec II Nur '02|401,100|
|Nissan|Sileighty '98|81,600|
|Nissan|Silvia K's Type S (S14) '94|51,400|
|Nissan|Skyline GTS-R (R31) '87|162,200|
|Porsche|911 GT3 (997) '09|140,200|
|RUF|CTR3 '07|770,800|
|Suzuki|Swift Sport '07|11,800|
|Toyota|Sports 800 '65|46,300|
|Volkswagen|Golf I GTI '83|40,500|
