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


# Gran Turismo 7 Shops for 20-July-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|De Tomaso|Mangusta '69|315,000|
|Jeep|Willys MB '45|30,100|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|911 Carrera RS (901) '73|750,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Camaro Z28 '69|133,000|
|Honda|RA272 '65|2,500,000|
|NISMO|400R '95|1,800,000|
|Shelby|Cobra 427 '66|2,500,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette ZR1 (C6) '09|98,400|
|Mitsubishi|GTO Twin Turbo '91|40,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '71|141,500|
|BMW|M3 '03|72,800|
|BMW|M3 Sport Evolution '89|179,700|
|Nissan|Fairlady 240ZG (HS30) '71|98,500|
|Nissan|Silvia K's Type S (S14) '94|60,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C Competizione '08|287,200|
|Audi|R8 4.2 '07|137,600|
|BMW|3.0 CSL '73|211,200|
|Chevrolet|Corvette ZR-1 (C4) '89|86,100|
|Dodge|Super Bee '70|71,900|
|Ferrari|Dino 246 GT '71|343,900|
|Fiat|500 1.2 8V Lounge SS '08|13,300|
|Ford|Sierra RS 500 Cosworth '87|193,500|
|Honda|Beat '91|16,800|
|Honda|Civic Type R (EK) '97|58,100|
|Honda|NSX Type R '02|431,600|
|Honda|S2000 '99|100,100|
|Lamborghini|Diablo GT '00|789,300|
|Mazda|Eunos Roadster (NA) '89|26,500|
|Mazda|RX-7 Spirit R Type A (FD) '02|214,300|
|Nissan|R33 GT-R V-spec '97|155,200|
|Nissan|Sileighty '98|72,400|
|Nissan|Silvia K's Dia Selection (S13) '90|49,700|
|Subaru|Impreza Sedan WRX STi '04|47,100|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|97,800|
|Volkswagen|Volkswagen 1200 '66|35,800|
