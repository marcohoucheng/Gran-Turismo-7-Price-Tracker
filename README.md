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


# Gran Turismo 7 Shops for 23-February-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|De Tomaso|Mangusta (Christian Dior)|500,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C2) '63|234,000|
|Porsche|959 '87|1,950,000|
|Porsche|959 '87|1,950,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB3S '53|6,000,000|
|Chaparral|2J '70|2,500,000|
|Chevrolet|Chevelle SS 454 Sport Coupé '70|162,000|
|Ferrari|330 P4 '67|20,000,000|
|Ford|1932 Ford Roadster Hot Rod|400,000|
|Jaguar|E-type Coupe '61|218,000|
|McLaren|McLaren F1 '94|20,000,000|
|Porsche|917K '70|18,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|McLaren|MP4-12C '10|184,100|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|Sierra RS 500 Cosworth '87|198,100|
|Honda|Civic Si Extra (EF) '87|62,300|
|Honda|Civic Si Extra (EF) '87|57,500|
|Honda|S2000 '99|103,800|
|Mitsubishi|Lancer Evolution IX MR GSR '06|95,000|
|Nissan|R33 GT-R V-spec '97|155,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|56,700|
|Alfa Romeo|8C Competizione '08|313,400|
|Alfa Romeo|MiTo '09|23,900|
|Autobianchi|A112 Abarth '85|30,400|
|BMW|3.0 CSL '71|135,200|
|Honda|Civic Type R (EK) '98|47,000|
|Honda|S800 '66|43,000|
|Lamborghini|Countach 25th Anniversary '88|694,000|
|Lamborghini|Diablo GT '00|790,200|
|Lancia|Delta HF Integrale Evoluzione '91|99,700|
|Mazda|RX-7 Spirit R Type A (FD) '02|217,000|
|Mercedes-Benz|SLR McLaren '09|492,000|
|Mitsubishi|Lancer Evolution V GSR '98|68,900|
|Nissan|Silvia K's Aero (S14) '96|58,800|
|Porsche|911 Carrera RS (993) '95|228,000|
|Porsche|911 Turbo (930) '81|219,000|
|Suzuki|Cappuccino (EA11R) '91|17,800|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|99,100|
|Toyota|Supra 3.0GT Turbo A '88|106,300|
