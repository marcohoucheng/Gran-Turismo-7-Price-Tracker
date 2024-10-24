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


# Gran Turismo 7 Shops for 24-October-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|800,000|
|Jaguar|D-type '54|6,000,000|
|Mercedes-Benz|S Barker Tourer '29|13,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|Sport quattro S1 Pikes Peak '87|1,900,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|NSX GT500 '00|1,500,000|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|280,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|
|Porsche|Spyder type 550/1500RS '55|4,850,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C Competizione '08|313,400|
|BMW|3.0 CSL '71|140,400|
|BMW|M3 Sport Evolution '89|200,000|
|Ford|Sierra RS 500 Cosworth '87|200,000|
|Volkswagen|Scirocco R '10|40,300|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|430 Scuderia '07|363,500|
|Honda|NSX Type R '02|440,400|
|Renault|Clio V6 24V '00|72,800|
|Renault|R5 Turbo '80|151,900|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|58,200|
|Audi|TT Coupe 3.2 quattro '03|43,300|
|Autobianchi|A112 Abarth '85|29,800|
|BMW|M3 '89|86,100|
|Chevrolet|Corvette Stingray (C3) '69|54,700|
|De Tomaso|Pantera '71|172,800|
|Dodge|Viper GTS '02|106,400|
|Honda|Integra Type R (DC2) '95|60,300|
|Honda|S800 '66|48,700|
|Lamborghini|Diablo GT '00|790,200|
|Lancia|Delta HF Integrale Evoluzione '91|98,900|
|Mazda|RX-7 Spirit R Type A (FD) '02|217,000|
|Mercedes-Benz|SLR McLaren '09|492,000|
|Mitsubishi|Lancer Evolution IX MR GSR '06|95,000|
|Nissan|Fairlady 240ZG (HS30) '71|106,400|
|Nissan|R33 GT-R V-spec '97|155,400|
|Nissan|SILVIA spec-R Aero (S15) '02|58,400|
|Subaru|Impreza 22B-STi '98|178,300|
|Suzuki|Cappuccino (EA11R) '91|16,000|
|Toyota|MR2 GT-S '97|58,100|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|99,100|
|Volvo|240 SE Estate '93|50,000|
