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


# Gran Turismo 7 Shops for 09-February-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mercedes-Benz|W 196 R '55|20,000,000|
|Plymouth|Superbird '70|402,000|
|Plymouth|Superbird '70|402,000|
|Plymouth|Superbird '70|402,000|
|Plymouth|Superbird '70|402,000|
|Plymouth|Superbird '70|402,000|
|Porsche|Carrera GTS (904) '64|2,300,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|800,000|
|Jaguar|XJ220 '92|554,000|
|Maserati|A6GCS/53 Spyder '54|3,000,000|
|Maserati|Merak SS '80|64,200|
|Mazda|787B '91|3,300,000|
|Mazda|RX500 '70|600,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Porsche|959 '87|1,950,000|
|Porsche|962 C '88|1,300,000|
|Toyota|Supra GT500 '97|1,800,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray (C3) '69|51,700|
|Daihatsu|Copen '02|13,300|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|512 BB '76|288,600|
|Honda|Beat '91|15,900|
|Mazda|Eunos Roadster (NA) '89|30,600|
|Nissan|180SX Type X '96|46,900|
|Nissan|Fairlady Z (Z34) '08|33,000|
|Pontiac|Firebird Trans Am '78|110,000|
|Pontiac|Firebird Trans Am '78|110,000|
|Pontiac|Firebird Trans Am '78|110,000|
|Pontiac|Firebird Trans Am '78|110,000|
|Pontiac|Firebird Trans Am '78|110,000|
|Toyota|Celica GT-Four (ST205) '94|73,400|
|Volkswagen|Sambabus Typ 2 '62|63,500|
|Volvo|240 SE Estate '93|48,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|44,100|
|BMW|M3 '89|76,900|
|Ferrari|F430 '06|207,400|
|Fiat|500 1.2 8V Lounge SS '08|13,800|
|Ford|Ford GT '06|397,100|
|Honda|Civic Si Extra (EF) '87|61,600|
|Honda|Civic Type R (EK) '97|51,900|
|Nissan|Fairlady Z 300ZX TT 2seater '89|55,300|
|Nissan|Fairlady Z Version S (Z33) '07|30,800|
|Renault|Clio V6 24V '00|89,700|
|Subaru|Impreza 22B-STi '98|174,200|
|TVR|Tuscan Speed 6 '00|70,100|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|47,400|
|Toyota|Sports 800 '65|51,400|
|Toyota|Supra RZ '97|194,000|
