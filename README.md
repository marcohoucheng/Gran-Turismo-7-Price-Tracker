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


# Gran Turismo 7 Shops for 28-April-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|300,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|330 P4 '67|20,000,000|
|Honda|RA272 '65|2,500,000|
|NISMO|400R '95|1,800,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Camaro Z28 '69|119,000|
|Chevrolet|Chevelle SS 454 Sport Coupé '70|163,000|
|Ferrari|365 GTB4 '71|640,000|
|Jeep|Willys MB '45|30,100|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|167,000|
|Porsche|911 Carrera RS (901) '73|745,000|
|Porsche|Spyder type 550/1500RS '55|4,500,000|


## Used shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|DMC|DeLorean S2 '04|451,600|
|MINI|MINI Cooper S '05|21,900|
|Mazda|RX-7 GT-X (FC) '90|61,100|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|168,100|
|Nissan|180SX Type X '96|48,500|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|46,800|
|Volkswagen|Golf I GTI '83|46,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|137,500|
|Audi|TT Coupe 3.2 quattro '03|45,400|
|Audi|TTS Coupe '09|63,100|
|BMW|M3 '03|72,800|
|BMW|M3 '07|69,900|
|BMW|M3 '89|75,700|
|Chevrolet|Corvette ZR-1 (C4) '89|86,100|
|Daihatsu|Copen '02|13,000|
|Ferrari|F430 '06|201,100|
|Ferrari|Testarossa '91|450,000|
|Honda|Civic Type R (EK) '97|65,000|
|Honda|Civic Type R (EK) '98|65,000|
|Honda|Civic Type R (EK) Touring Car|140,000|
|Honda|NSX Type R '02|431,600|
|MINI|Mini-Cooper 'S' '65|40,600|
|Nissan|Fairlady Z 300ZX TT 2seater '89|62,300|
|Nissan|GT-R NISMO (R32) '90|390,000|
|Nissan|Silvia K's Type S (S14) '94|53,900|
|Porsche|911 Carrera RS (964) '92|226,500|
|Renault|Clio V6 24V '00|82,300|
|Suzuki|Swift Sport '07|12,200|
|TVR|Tuscan Speed 6 '00|72,500|
|Toyota|Sports 800 '65|48,100|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|48,900|
