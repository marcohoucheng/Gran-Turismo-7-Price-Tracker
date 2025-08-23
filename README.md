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


# Gran Turismo 7 Shops for 23-August-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mercedes-Benz|CLK-LM '98|8,500,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|542,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chaparral|2J '70|2,500,000|
|Ferrari|330 P4 '67|20,000,000|
|Ferrari|F40 '92|3,100,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Aston Martin|DB3S '53|6,000,000|
|De Tomaso|Mangusta (Christian Dior)|500,000|
|Ferrari|365 GTB4 '71|610,000|
|McLaren|McLaren F1 '94|20,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|Civic SiR-II (EG) '93|50,100|
|Lamborghini|Murcielago LP 640 '09|327,700|
|Nissan|Fairlady 240ZG (HS30) '71|97,400|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|141,600|
|Autobianchi|A112 Abarth '85|29,100|
|Chevrolet|Corvette Stingray (C3) '69|71,500|
|Chevrolet|Corvette ZR1 (C6) '09|100,800|
|Dodge|Super Bee '70|60,200|
|Dodge|Viper SRT10 Coupe '06|111,400|
|Ferrari|458 Italia '09|248,100|
|Nissan|R32 GT-R V-spec II '94|178,300|
|Nissan|Skyline GTS-R (R31) '87|172,000|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|50,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Convertible (C3) '69|47,500|
|Ford|Escort RS Cosworth '92|124,600|
|Honda|NSX Type R '92|389,500|
|Lancia|Delta HF Integrale Evoluzione '91|103,200|
|Lancia|Stratos '73|495,200|
|Mitsubishi|Lancer Evolution IV GSR '96|41,300|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|164,100|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|61,600|
|Nissan|Sileighty '98|72,800|
|Nissan|Silvia K's Dia Selection (S13) '90|52,100|
|Nissan|Silvia K's Type S (S14) '94|46,100|
|Peugeot|205 GTI '88|53,300|
|Porsche|911 GT3 (996) '01|156,800|
|Porsche|911 GT3 (997) '09|142,700|
|Suzuki|Cappuccino (EA11R) '91|16,500|
|Volkswagen|Volkswagen 1200 '66|28,800|
