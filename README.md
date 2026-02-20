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


# Gran Turismo 7 Shops for 20-February-2026



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|De Tomaso|Mangusta (Christian Dior)|500,000|
|McLaren|McLaren F1 '94|20,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Alfa Romeo|8C 2900B Touring Berlinetta '38|20,000,000|
|Chevrolet|Camaro Z28 '69|111,000|
|Mercedes-Benz|CLK-LM '98|8,500,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|537,000|
|Peugeot|205 Turbo 16 Evolution 2 '86|1,000,000|
|Toyota|2000GT '67|982,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|134,500|
|Chevrolet|Corvette Stingray (C3) '69|62,000|
|Nissan|SILVIA spec-R Aero (S15) '02|59,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|26,400|
|Audi|TT Coupe 3.2 quattro '03|49,800|
|De Tomaso|Pantera '71|173,100|
|Ferrari|512 BB '76|286,400|
|Ford|Ford GT '06|412,900|
|Mazda|Eunos Roadster (NA) '89|31,200|
|Nissan|180SX Type X '96|49,700|
|Nissan|Fairlady Z (Z34) '08|35,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TTS Coupe '09|63,100|
|BMW|3.0 CSL '73|250,000|
|BMW|M3 '07|72,500|
|Dodge|Viper GTS '02|104,900|
|Ferrari|430 Scuderia '07|363,800|
|Fiat|500 1.2 8V Lounge SS '08|12,700|
|Honda|Civic Type R (EK) '97|47,000|
|Honda|Integra Type R (DC2) '95|56,400|
|Honda|NSX Type R '02|444,300|
|Lamborghini|Countach 25th Anniversary '88|800,000|
|MINI|MINI Cooper S '05|22,900|
|MINI|Mini-Cooper 'S' '65|43,600|
|Nissan|Fairlady Z 300ZX TT 2seater '89|58,000|
|Renault|Clio V6 24V '00|73,600|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|51,200|
|Toyota|MR2 GT-S '97|54,900|
|Toyota|Sports 800 '65|45,900|
|Toyota|Supra RZ '97|179,100|
|Volvo|240 SE Estate '93|46,600|
