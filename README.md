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


# Gran Turismo 7 Shops for 13-January-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Camaro Z28 '69|128,000|
|De Tomaso|Mangusta '69|315,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|NISMO|400R '95|1,600,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|Sport quattro S1 Pikes Peak '87|1,800,000|
|Citroen|DS 21 Pallas '70|47,100|
|Ferrari|365 GTB4 '71|610,000|
|Ferrari|F40 '92|3,100,000|
|Ferrari|F50 '95|4,450,000|
|Ferrari|GTO '84|3,500,000|
|Honda|RA272 '65|2,500,000|
|Jeep|Willys MB '45|30,100|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|290,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Shelby|Cobra 427 '66|2,500,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|MINI|Mini-Cooper 'S' '65|40,800|
|Toyota|Supra 3.0GT Turbo A '88|112,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Fiat|500 1.2 8V Lounge SS '08|14,400|
|Honda|Civic Type R (EK) '97|50,200|
|Honda|NSX Type R '02|440,400|
|Volkswagen|Scirocco R '10|40,300|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C Competizione '08|313,400|
|Alpine|A110 '72|142,200|
|BMW|M3 Sport Evolution '89|165,200|
|Daihatsu|Copen '02|15,700|
|Dodge|Viper GTS '02|106,400|
|Ferrari|308 GTB '75|200,000|
|Ferrari|512 BB '76|350,000|
|Ferrari|Dino 246 GT '71|400,000|
|Ferrari|Testarossa '91|450,000|
|Ford|Sierra RS 500 Cosworth '87|183,500|
|Honda|S2000 '99|98,700|
|Lamborghini|Diablo GT '00|790,200|
|Mazda|RX-7 Spirit R Type A (FD) '02|217,000|
|Mercedes-Benz|SLR McLaren '09|492,000|
|Mitsubishi|Lancer Evolution III GSR '95|96,400|
|Mitsubishi|Lancer Evolution IX MR GSR '06|95,000|
|Mitsubishi|Lancer Evolution V GSR '98|80,700|
|Nissan|R33 GT-R V-spec '97|155,400|
|Nissan|Silvia K's Aero (S14) '96|57,800|
|Nissan|Silvia K's Type S (S14) '94|51,400|
|Porsche|911 Turbo (930) '81|220,000|
|Suzuki|Swift Sport '07|11,800|
|Toyota|Sports 800 '65|47,200|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|99,100|
|Volkswagen|Golf I GTI '83|40,500|
