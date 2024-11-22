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


# Gran Turismo 7 Shops for 22-November-2024



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|800,000|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|280,000|
|Plymouth|XNR Ghia Roadster '60|1,600,000|
|Porsche|959 '87|1,950,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C2) '63|239,000|
|Ferrari|500 Mondial Pinin Farina Coupe '54|2,600,000|
|Ferrari|F40 '92|3,100,000|
|Ferrari|F50 '95|4,450,000|
|Jaguar|E-type Coupe '61|227,000|
|Jaguar|XJR-9 '88|3,000,000|
|Mazda|787B '91|3,300,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Mercedes-Benz|W 196 R '55|20,000,000|
|Nissan|Fairlady Z 432 '69|312,000|
|Nissan|R92CP '92|2,000,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|
|Porsche|962 C '88|1,300,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TTS Coupe '09|67,600|
|BMW|M3 '07|70,200|
|Nissan|GT-R NISMO (R32) '90|393,800|
|Porsche|911 Carrera RS (964) '92|220,000|
|Renault|Clio V6 24V '00|72,800|
|Suzuki|Cappuccino (EA11R) '91|16,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|22,700|
|BMW|M3 Sport Evolution '89|200,000|
|Dodge|Super Bee '70|63,200|
|Ford|Sierra RS 500 Cosworth '87|200,000|
|Mitsubishi|Lancer Evolution III GSR '95|100,000|
|Mitsubishi|Lancer Evolution IV GSR '96|55,000|
|Mitsubishi|Lancer Evolution V GSR '98|90,000|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|200,000|
|Nissan|Sileighty '98|89,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|58,200|
|Autobianchi|A112 Abarth '85|29,800|
|DMC|DeLorean S2 '04|458,900|
|Ferrari|F430 '06|207,400|
|Ferrari|Testarossa '91|450,000|
|Ford|Escort RS Cosworth '92|147,100|
|Ford|Ford GT '06|397,100|
|Honda|Civic Type R (EK) '98|58,100|
|Honda|S800 '66|48,700|
|Lancia|Delta HF Integrale Evoluzione '91|98,900|
|MINI|MINI Cooper S '05|23,300|
|Mazda|RX-7 GT-X (FC) '90|58,900|
|Nissan|180SX Type X '96|58,400|
|Nissan|Fairlady Z Version S (Z33) '07|30,800|
|Nissan|Silvia Q's (S13) '88|31,800|
|Renault|R5 Turbo '80|151,900|
|TVR|Tuscan Speed 6 '00|70,100|
|Toyota|Celica GT-Four (ST205) '94|67,700|
|Toyota|Supra RZ '97|194,000|
