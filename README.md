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


# Gran Turismo 7 Shops for 06-October-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|GIULIA TZ2 carrozzata da ZAGATO '65|3,800,000|
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,600,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|GTO '84|3,500,000|
|Ford|GT40 Mark I '66|6,700,000|
|Lamborghini|Miura P400 Bertone Prototype '67|3,750,000|
|Mercedes-Benz|300 SL (W194) '52|20,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|800,000|
|Dodge|Challenger R/T '70|214,000|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|280,000|
|Nissan|R92CP '92|2,000,000|
|Subaru|Impreza Rally Car '98|650,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|Mustang Mach 1 '71|40,200|
|Honda|Integra Type R (DC2) '98|62,100|
|Nissan|Skyline GTS-R (R31) '87|163,300|
|Porsche|911 GT3 (997) '09|141,200|
|Suzuki|Swift Sport '07|11,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|NSX Type R '92|398,200|
|Mitsubishi|Lancer Evolution V GSR '98|80,100|
|Porsche|911 Carrera RS CS (993) '95|413,800|
|Porsche|911 GT3 (996) '01|161,700|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|55,000|
|Volkswagen|Sambabus Typ 2 '62|67,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|135,900|
|BMW|M3 '97|81,100|
|BMW|M3 Sport Evolution '89|200,000|
|Chevrolet|Corvette ZR-1 (C4) '89|77,800|
|Chevrolet|Corvette ZR1 (C6) '09|99,000|
|Daihatsu|Copen '02|15,700|
|Dodge|Viper SRT10 Coupe '06|114,400|
|Fiat|500 1.2 8V Lounge SS '08|14,400|
|Ford|Sierra RS 500 Cosworth '87|200,000|
|Honda|Civic Type R (EK) '97|50,200|
|Lamborghini|Gallardo LP 560-4 '08|241,700|
|Mitsubishi|Lancer Evolution IV GSR '96|39,600|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|65,800|
|Nissan|R32 GT-R V-spec II '94|178,600|
|Nissan|Silvia Q's (S13) '88|40,000|
|Pontiac|Firebird Trans Am '78|87,900|
|Subaru|Impreza Sedan WRX STi '04|42,000|
|Toyota|Sports 800 '65|46,300|
|Volvo|240 SE Estate '93|47,000|
