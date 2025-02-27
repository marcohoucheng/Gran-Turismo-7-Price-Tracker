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


# Gran Turismo 7 Shops for 27-February-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|542,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chaparral|2J '70|2,500,000|
|Ford|1932 Ford Roadster Hot Rod|400,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB3S '53|6,000,000|
|De Tomaso|Mangusta (Christian Dior)|500,000|
|Dodge|Charger R/T 426 Hemi '68|158,000|
|Dodge|Charger R/T 426 Hemi '68|158,000|
|Ferrari|330 P4 '67|20,000,000|
|Ferrari|365 GTB4 '71|610,000|
|McLaren|McLaren F1 '94|20,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|313,200|
|Maserati|GranTurismo S '08|141,800|
|Renault|R5 Turbo '80|154,700|
|Volkswagen|Volkswagen 1200 '66|34,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|56,700|
|Alfa Romeo|8C Competizione '08|313,400|
|Autobianchi|A112 Abarth '85|30,400|
|Honda|S800 '66|43,000|
|Lamborghini|Countach 25th Anniversary '88|694,000|
|Lamborghini|Diablo GT '00|790,200|
|Mitsubishi|Lancer Evolution V GSR '98|68,900|
|Nissan|Silvia K's Aero (S14) '96|58,800|
|Porsche|911 Carrera RS (993) '95|228,000|
|Porsche|911 Turbo (930) '81|219,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '71|135,200|
|BMW|M3 '97|86,700|
|Ford|Escort RS Cosworth '92|150,000|
|Ford|Escort RS Cosworth '92|150,000|
|Ford|Mustang Mach 1 '71|36,500|
|Honda|Civic SiR-II (EG) '93|48,200|
|Honda|Integra Type R (DC2) '98|56,300|
|Lancia|Delta HF Integrale Evoluzione '91|99,700|
|McLaren|MP4-12C '10|184,100|
|Mitsubishi|GTO Twin Turbo '91|45,100|
|Nissan|Fairlady 240ZG (HS30) '71|99,100|
|Nissan|R34 GT-R V-spec II Nur '02|396,400|
|RUF|CTR3 '07|771,300|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|52,600|
|Subaru|Impreza Sedan WRX STi '04|43,500|
|Suzuki|Cappuccino (EA11R) '91|17,800|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|99,100|
|Toyota|Supra 3.0GT Turbo A '88|106,300|
