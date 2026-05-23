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


# Gran Turismo 7 Shops for 23-May-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C1) '58|110,000|
|Jaguar|XJR-9 '88|3,000,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|200,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|De Tomaso|Mangusta (Christian Dior)|500,000|
|Mercedes-Benz|CLK-LM '98|8,500,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Alfa Romeo|8C 2900B Touring Berlinetta '38|20,000,000|
|Ford|Mustang Boss 429 '69|335,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|537,000|
|Peugeot|205 Turbo 16 Evolution 2 '86|1,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|168,600|
|Mitsubishi|Lancer Evolution III GSR '95|82,200|
|Subaru|Impreza Sedan WRX STi '04|41,400|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Autobianchi|A112 Abarth '85|29,200|
|BMW|M3 '07|81,700|
|Chevrolet|Corvette Stingray (C3) '69|53,700|
|Dodge|Viper GTS '02|105,200|
|Ferrari|F430 '06|203,100|
|Honda|Civic Type R (EK) '98|56,700|
|Nissan|SILVIA spec-R Aero (S15) '02|60,600|
|Porsche|911 Carrera RS (964) '92|210,300|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '03|65,900|
|BMW|M3 '89|74,100|
|BMW|M3 Sport Evolution '89|166,100|
|Ford|Sierra RS 500 Cosworth '87|181,200|
|Lancia|Delta HF Integrale Evoluzione '91|100,100|
|Mercedes-Benz|SLR McLaren '09|491,700|
|Nissan|GT-R NISMO (R32) '90|396,300|
|Nissan|R33 GT-R V-spec '97|158,300|
|Nissan|Silvia K's Type S (S14) '94|44,700|
|Peugeot|205 GTI '88|57,600|
|Subaru|Impreza 22B-STi '98|165,000|
|Suzuki|Cappuccino (EA11R) '91|19,900|
|TVR|Tuscan Speed 6 '00|75,900|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|53,300|
|Volkswagen|Scirocco R '10|37,500|
