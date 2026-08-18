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


# Gran Turismo 7 Shops for 18-August-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|F40 '92|3,400,000|
|Ferrari|F50 '95|4,700,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB3S '53|6,000,000|
|Ferrari|330 P4 '67|20,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Alfa Romeo|8C 2900B Touring Berlinetta '38|20,000,000|
|De Tomaso|Mangusta (Christian Dior)|500,000|
|Ferrari|365 GTB4 '71|595,000|
|McLaren|McLaren F1 '94|20,000,000|
|Mercedes-Benz|CLK-LM '98|8,500,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|537,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 Sport Evolution '89|162,800|
|Mitsubishi|Lancer Evolution III GSR '95|84,600|
|Nissan|180SX Type X '96|65,000|
|Nissan|R32 GT-R V-spec II '94|200,000|
|Subaru|Impreza Sedan WRX STi '04|41,100|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '07|68,500|
|Chevrolet|Corvette Stingray (C3) '69|62,000|
|Dodge|Viper GTS '02|102,800|
|Ferrari|F430 '06|206,600|
|Lancia|Delta HF Integrale Evoluzione '91|104,400|
|Nissan|SILVIA spec-R Aero (S15) '02|59,800|
|Nissan|Silvia K's Type S (S14) '94|47,200|
|Porsche|911 Carrera RS (964) '92|218,000|
|Suzuki|Cappuccino (EA11R) '91|19,800|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|58,200|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|47,000|
|Alfa Romeo|Giulia Sprint GT Veloce '67|164,900|
|BMW|M3 '03|65,500|
|BMW|M3 '89|73,100|
|Fiat|500 F '68|18,300|
|Ford|Sierra RS 500 Cosworth '87|183,500|
|Mercedes-Benz|SLR McLaren '09|505,500|
|Nissan|Fairlady 240ZG (HS30) '71|107,800|
|Nissan|GT-R NISMO (R32) '90|397,700|
|Nissan|R33 GT-R V-spec '97|155,800|
|Nissan|Silvia K's Dia Selection (S13) '90|50,700|
|Peugeot|205 GTI '88|53,500|
|Subaru|Impreza 22B-STi '98|164,100|
|TVR|Tuscan Speed 6 '00|76,700|
|Volkswagen|Scirocco R '10|38,600|
