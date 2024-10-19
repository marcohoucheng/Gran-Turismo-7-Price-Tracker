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


# Gran Turismo 7 Shops for 19-October-2024



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Charger R/T 426 Hemi '68|158,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|Sport quattro S1 Pikes Peak '87|1,900,000|
|Chevrolet|Camaro Z28 '69|133,000|
|Citroen|DS 21 Pallas '70|47,600|
|De Tomaso|Mangusta '69|315,000|
|Honda|RA272 '65|2,500,000|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|280,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Porsche|Spyder type 550/1500RS '55|4,850,000|
|Shelby|Cobra 427 '66|2,500,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '89|86,100|
|Honda|S800 '66|48,700|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|169,000|
|Ferrari|F430 '06|207,400|
|Ford|Mustang Mach 1 '71|50,000|
|MINI|MINI Cooper S '05|23,300|
|MINI|Mini-Cooper 'S' '65|40,800|
|Mazda|RX-7 GT-X (FC) '90|58,900|
|Nissan|180SX Type X '96|58,400|
|Nissan|GT-R NISMO (R32) '90|393,800|
|Porsche|911 Carrera RS (964) '92|220,000|
|Toyota|Prius G '09|18,500|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|58,200|
|Alfa Romeo|MiTo '09|22,700|
|Audi|TT Coupe 3.2 quattro '03|43,300|
|Audi|TTS Coupe '09|67,600|
|BMW|M3 '03|72,700|
|BMW|M3 '07|70,200|
|DMC|DeLorean S2 '04|458,900|
|Dodge|Viper GTS '02|106,400|
|Ferrari|430 Scuderia '07|363,500|
|Honda|Civic Type R (EK) '98|58,100|
|Honda|NSX Type R '02|440,400|
|Nissan|Fairlady Z 300ZX TT 2seater '89|60,300|
|Nissan|Silvia Q's (S13) '88|31,800|
|Renault|Clio V6 24V '00|72,800|
|Renault|R5 Turbo '80|151,900|
|TVR|Tuscan Speed 6 '00|70,100|
