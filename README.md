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


# Gran Turismo 7 Shops for 01-March-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB3S '53|6,000,000|
|Dodge|Charger R/T 426 Hemi '68|158,000|
|Dodge|Charger R/T 426 Hemi '68|158,000|
|Ferrari|330 P4 '67|20,000,000|
|McLaren|McLaren F1 '94|20,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|De Tomaso|Mangusta (Christian Dior)|500,000|
|Ferrari|365 GTB4 '71|610,000|
|Mercedes-Benz|CLK-LM '98|8,500,000|
|Mercedes-Benz|Unimog Type 411 '62|46,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|542,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|Z8 '01|258,700|
|Ferrari|Dino 246 GT '71|343,200|
|Ferrari|Testarossa '91|372,400|
|Honda|Civic Type R (EK) Touring Car|123,400|
|Mazda|RX-7 GT-X (FC) '90|50,500|
|Nissan|Silvia K's Dia Selection (S13) '90|51,900|
|Nissan|Silvia Q's (S13) '88|33,900|
|Porsche|911 Carrera RS CS (993) '95|437,300|
|Toyota|Prius G '09|18,900|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '71|135,200|
|Ford|Escort RS Cosworth '92|150,000|
|Ford|Escort RS Cosworth '92|150,000|
|Honda|Integra Type R (DC2) '98|56,300|
|Lancia|Delta HF Integrale Evoluzione '91|99,700|
|McLaren|MP4-12C '10|184,100|
|Mitsubishi|GTO Twin Turbo '91|45,100|
|RUF|CTR3 '07|771,300|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|52,600|
|Subaru|Impreza Sedan WRX STi '04|43,500|
|Suzuki|Cappuccino (EA11R) '91|17,800|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|99,100|
|Toyota|Supra 3.0GT Turbo A '88|106,300|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|313,200|
|BMW|M3 '97|86,700|
|BMW|Z4 3.0i '03|44,600|
|Ford|Mustang Mach 1 '71|36,500|
|Honda|Civic SiR-II (EG) '93|48,200|
|Maserati|GranTurismo S '08|141,800|
|Nissan|Fairlady 240ZG (HS30) '71|99,100|
|Nissan|R34 GT-R V-spec II Nur '02|396,400|
|Peugeot|205 GTI '88|61,600|
|Renault|R5 Turbo '80|154,700|
|Volkswagen|Volkswagen 1200 '66|34,000|
