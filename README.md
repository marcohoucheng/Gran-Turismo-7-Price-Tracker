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


# Gran Turismo 7 Shops for 14-March-2026



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray Racer Concept '59|7,000,000|
|Dodge|Challenger R/T '70|179,000|
|Jaguar|E-type Coupe '61|172,000|
|McLaren|McLaren F1 '94|20,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Chevelle SS 454 Sport Coupé '70|150,000|
|Ferrari|GTO '84|3,500,000|
|Lamborghini|Miura P400 Bertone Prototype '67|4,300,000|
|Mercedes-Benz|300 SL (W194) '52|20,000,000|
|Mercedes-Benz|Unimog Type 411 '62|46,000|
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,400,000|
|Subaru|Impreza Rally Car '98|650,000|


## Used shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|308,300|
|Lamborghini|Diablo GT '00|837,800|
|MINI|Mini-Cooper 'S' '65|50,000|
|Porsche|911 Turbo (930) '81|213,700|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|62,700|
|TVR|Tuscan Speed 6 '00|95,000|
|Volkswagen|Volkswagen 1200 '66|34,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|50,200|
|Alfa Romeo|MiTo '09|22,700|
|BMW|3.0 CSL '71|148,100|
|BMW|3.0 CSL '73|203,800|
|BMW|M3 '97|72,200|
|Chevrolet|Corvette Z06 (C5) '01|48,700|
|Dodge|Super Bee '70|80,000|
|Ferrari|Dino 246 GT '71|343,200|
|Ferrari|Testarossa '91|393,600|
|Fiat|500 F '68|16,500|
|Fiat|Panda 30 CL '85|11,800|
|Honda|Civic SiR-II (EG) '93|50,200|
|Honda|Civic Type R (EK) Touring Car|115,800|
|Maserati|GranTurismo S '08|138,000|
|Mazda|RX-7 GT-X (FC) '90|52,900|
|Mazda|efini RX-7 Type R (FD) '91|80,000|
|McLaren|MP4-12C '10|184,200|
|Mitsubishi|GTO Twin Turbo '91|49,300|
|Mitsubishi|Lancer Evolution V GSR '98|74,700|
|Nissan|Fairlady 240ZG (HS30) '71|103,100|
|Nissan|R34 GT-R V-spec II Nur '02|394,400|
|Nissan|Silvia K's Aero (S14) '96|58,600|
|Nissan|Silvia K's Dia Selection (S13) '90|52,800|
|Porsche|911 Carrera RS CS (993) '95|441,300|
|Toyota|Supra 3.0GT Turbo A '88|115,200|
