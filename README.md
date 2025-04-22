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


# Gran Turismo 7 Shops for 22-April-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|F40 '92|3,100,000|
|Ferrari|F50 '95|4,450,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mercedes-Benz|S Barker Tourer '29|13,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Charger R/T 426 Hemi '68|158,000|
|Jaguar|XJ13 '66|12,000,000|
|McLaren|McLaren F1 GTR - BMW '95|16,000,000|
|Mercedes-Benz|300 SL Coupe '54|1,700,000|
|Nissan|Fairlady Z 432 '69|312,000|
|Nissan|GT-R GT500 '99|2,500,000|
|Shelby|Cobra Daytona Coupe '64|20,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|Testarossa '91|450,000|
|Ferrari|Testarossa '91|450,000|
|Ferrari|Testarossa '91|450,000|
|Honda|Civic Type R (EK) '98|46,800|
|Lamborghini|Murcielago LP 640 '09|343,000|
|MINI|Mini-Cooper 'S' '65|40,100|
|Nissan|180SX Type X '96|48,800|
|Nissan|Fairlady Z (Z34) '08|35,300|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|144,600|
|Chevrolet|Corvette Convertible (C3) '69|53,800|
|Chevrolet|Corvette ZR1 (C6) '09|107,400|
|Ferrari|458 Italia '09|243,100|
|Fiat|500 1.2 8V Lounge SS '08|12,700|
|Honda|NSX Type R '92|385,600|
|Lamborghini|Gallardo LP 560-4 '08|253,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|166,200|
|Daihatsu|Copen '02|14,000|
|Ford|Escort RS Cosworth '92|129,000|
|Lancia|Stratos '73|505,300|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|163,600|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|62,400|
|Nissan|Sileighty '98|75,200|
|Peugeot|205 GTI '88|70,000|
|Peugeot|205 GTI '88|70,000|
|Peugeot|205 GTI '88|70,000|
|Pontiac|Firebird Trans Am '78|96,000|
|Porsche|911 GT3 (996) '01|158,500|
|Porsche|911 GT3 (997) '09|139,900|
|Suzuki|Swift Sport '07|14,600|
|Toyota|Celica GT-Four (ST205) '94|78,100|
|Toyota|Sports 800 '65|45,900|
|Volkswagen|Golf I GTI '83|41,000|
