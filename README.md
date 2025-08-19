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


# Gran Turismo 7 Shops for 19-August-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|F40 '92|3,100,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Jaguar|E-type Coupe '61|205,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB3S '53|6,000,000|
|Chaparral|2J '70|2,500,000|
|Chevrolet|Chevelle SS 454 Sport Coupé '70|146,000|
|De Tomaso|Mangusta (Christian Dior)|500,000|
|Ferrari|330 P4 '67|20,000,000|
|Ferrari|365 GTB4 '71|610,000|
|Ford|1932 Ford Roadster Hot Rod|350,000|
|McLaren|McLaren F1 '94|20,000,000|
|Porsche|917K '70|18,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray (C3) '69|71,500|
|Honda|NSX Type R '92|389,500|
|Lancia|Delta HF Integrale Evoluzione '91|103,200|
|Lancia|Stratos '73|495,200|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|164,100|
|Nissan|Sileighty '98|72,800|
|Nissan|Silvia K's Type S (S14) '94|46,100|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|164,900|
|BMW|Z8 '01|265,100|
|Chevrolet|Corvette ZR-1 (C4) '89|86,400|
|Honda|Civic Type R (EK) '98|47,000|
|Mazda|RX-7 GT-X (FC) '90|54,900|
|Porsche|911 Carrera RS CS (993) '95|409,200|
|Suzuki|Swift Sport '07|13,600|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|143,800|
|Audi|R8 4.2 '07|141,600|
|Autobianchi|A112 Abarth '85|29,100|
|Chevrolet|Corvette Convertible (C3) '69|47,500|
|Chevrolet|Corvette ZR1 (C6) '09|100,800|
|Citroen|BX 19 TRS '87|30,000|
|Citroen|BX 19 TRS '87|30,000|
|Citroen|BX 19 TRS '87|30,000|
|Dodge|Super Bee '70|60,200|
|Dodge|Viper SRT10 Coupe '06|111,400|
|Ferrari|458 Italia '09|248,100|
|Ferrari|Dino 246 GT '71|327,300|
|Honda|Civic Type R (EK) Touring Car|122,800|
|Lamborghini|Gallardo LP 560-4 '08|257,000|
|MINI|Mini-Cooper 'S' '65|43,600|
|Mitsubishi|Lancer Evolution IV GSR '96|41,300|
|Nissan|R32 GT-R V-spec II '94|178,300|
|Nissan|Skyline GTS-R (R31) '87|172,000|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|50,700|
