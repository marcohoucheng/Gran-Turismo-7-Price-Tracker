# Gran Turismo 7 tracker for in-game dynamic prices for cars

This is a personal project built on Python to obtain in-game stores information of Gran Turismo 7 without the necessarity to manually start the game on PlayStation 5. It has the following functionalities:

- An automated daily email to list updates in game.
- Aggregate data to build a local database of cars' historical prices,
- Return latest information of cars given a wish list.

Data are scraped from https://github.com/ddm999/gt7info. Tools providing similar information are available on https://gtdb.io. However, the site requires an account to receive daily emails. The setup of this project allows for a setup without having to sign up for an account.

The approach of this project is to provide a solution without setting an account.

# Usage

## Daily Email

A scheduled Github Action is currently set up. However, the user can easily set up a similar system. Only `email_update.py` is needed in this case with the appropriate environment varibles for `SENDER_EMAIL`, `PASSWORD` and `RECIPIENTS`. A [screenshot](https://raw.githubusercontent.com/marcohoucheng/Gran-Turismo-7-Price-Tracker/main/data/email_screenshot.png) of the email.

## Wish list and local database

1. Build databases by running `build.py`. It will also detect whether `shop.py` and `car.py` should be run.
    - Only the respective shop will be built if ran with flag `used` or `legend`. Nevertheless, `shop.py` and `car.py` will still be triggered if necessary.
2. Run `update.py` to update the local shop databases.
    - Similar to `build.py`, `used` or `legend` flags can be called.
3. `wish.py` checks whether cars in the wish list `wish_list.txt` are available today. If so, then it will return the price. Otherwise, it returns the last available date and the price.
    - This script will automatically run `update.py` when checking whather cars on wish list are available.
4. Running `today.py` returns items available in the shops in terminal. With flag `new` the script will only return new days of the day.

A screenshot of the email

![email](https://raw.githubusercontent.com/marcohoucheng/Gran-Turismo-7-Price-Tracker/main/data/email_screenshot.png)

# Gran Turismo 7 Shops for 19-March-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|RA272 '65|2,500,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|De Tomaso|Mangusta (Christian Dior)|500,000|
|Ferrari|365 GTB4 '71|640,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Alfa Romeo|8C 2900B Touring Berlinetta '38|20,000,000|
|BMW|McLaren F1 GTR Race Car '97|14,000,000|
|Ford|Mustang Boss 429 '69|317,000|
|Mercedes-Benz|CLK-LM '98|8,500,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|542,000|
|Peugeot|205 Turbo 16 Evolution 2 '86|1,100,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|250,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '03|61,900|
|DMC|DeLorean S2 '04|427,500|
|Honda|Integra Type R (DC2) '98|61,400|
|Honda|S800 '66|58,000|
|Pontiac|Firebird Trans Am '78|87,400|
|Porsche|911 Carrera RS (964) '92|220,700|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|203,800|
|Dodge|Viper SRT10 Coupe '06|115,500|
|Ford|Ford GT '06|409,800|
|Honda|Civic Type R (EK) '97|55,600|
|Nissan|Fairlady Z Version S (Z33) '07|27,400|
|Toyota|Supra RZ '97|194,200|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|23,300|
|BMW|M3 '07|70,000|
|Ferrari|F430 '06|200,500|
|Fiat|500 1.2 8V Lounge SS '08|13,800|
|Honda|Beat '91|15,900|
|Mazda|Eunos Roadster (NA) '89|30,700|
|Mitsubishi|Lancer Evolution IV GSR '96|46,600|
|Mitsubishi|Lancer Evolution V GSR '98|69,200|
|Nissan|Fairlady 240ZG (HS30) '71|106,400|
|Nissan|GT-R NISMO (R32) '90|389,500|
|Nissan|R32 GT-R V-spec II '94|179,900|
|Nissan|Silvia K's Aero (S14) '96|59,000|
|Nissan|Silvia K's Dia Selection (S13) '90|48,200|
|Porsche|911 Turbo (930) '81|218,100|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|52,600|
|TVR|Tuscan Speed 6 '00|80,600|
|Toyota|Supra 3.0GT Turbo A '88|105,500|
|Volkswagen|Volkswagen 1200 '66|31,900|
