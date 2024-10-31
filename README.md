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


# Gran Turismo 7 Shops for 31-October-2024



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|800,000|
|McLaren|McLaren F1 GTR - BMW '95|15,000,000|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|280,000|
|Mercedes-Benz|S Barker Tourer '29|13,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Charger R/T 426 Hemi '68|158,000|
|Ferrari|250 GT Berlinetta passo corto '61|8,100,000|
|Jaguar|D-type '54|6,000,000|
|Jaguar|XJ13 '66|12,000,000|
|Lamborghini|Countach LP400 '74|1,350,000|
|McLaren|McLaren F1 '94|20,000,000|
|Mercedes-Benz|300 SL Coupe '54|1,700,000|
|Nissan|GT-R GT500 '99|2,500,000|
|Shelby|Cobra Daytona Coupe '64|20,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|313,200|
|Abarth|Abarth 500 '09|23,900|
|Daihatsu|Copen '02|16,000|
|Honda|Beat '91|20,000|
|Mazda|Eunos Roadster (NA) '89|28,600|
|Suzuki|Cappuccino (EA11R) '91|20,000|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|58,400|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C Competizione '08|313,400|
|BMW|M3 Sport Evolution '89|200,000|
|Ford|Sierra RS 500 Cosworth '87|200,000|
|Honda|Integra Type R (DC2) '95|60,300|
|Lamborghini|Countach 25th Anniversary '88|694,000|
|Lamborghini|Diablo GT '00|790,200|
|Lancia|Delta HF Integrale Evoluzione '91|98,900|
|Nissan|Silvia K's Dia Selection (S13) '90|52,100|
|Porsche|911 Carrera RS (993) '95|228,000|
|Volkswagen|Scirocco R '10|40,300|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|206,500|
|Ferrari|308 GTB '75|172,000|
|Honda|Civic SiR-II (EG) '93|50,800|
|Honda|S2000 '99|98,700|
|McLaren|MP4-12C '10|184,100|
|Mitsubishi|Lancer Evolution III GSR '95|96,400|
|Mitsubishi|Lancer Evolution V GSR '98|80,700|
|Nissan|R34 GT-R V-spec II Nur '02|396,400|
|Porsche|911 Turbo (930) '81|220,000|
|RUF|CTR3 '07|771,300|
|Renault|R4 GTL '85|24,700|
|TVR|Tuscan Speed 6 '00|95,000|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|99,100|
|Volkswagen|Sambabus Typ 2 '62|54,300|
