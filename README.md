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


# Gran Turismo 7 Shops for 24-August-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|500 Mondial Pinin Farina Coupe '54|2,600,000|
|Porsche|962 C '88|1,300,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|Mark IV Race Car '67|6,750,000|
|Plymouth|Superbird '70|402,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|800,000|
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Chevrolet|Corvette (C2) '63|239,000|
|Ferrari|F40 '92|3,100,000|
|Honda|NSX GT500 '00|1,500,000|
|McLaren|McLaren F1 GTR - BMW '95|15,000,000|
|Nissan|GT-R GT500 '99|2,500,000|
|Plymouth|XNR Ghia Roadster '60|1,600,000|
|Porsche|356 A/1500 GS Carrera '56|618,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|
|Porsche|959 '87|1,950,000|
|Toyota|Supra GT500 '97|1,800,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|310,900|
|Mazda|Eunos Roadster (NA) '89|28,600|
|Nissan|R34 GT-R V-spec II Nur '02|401,100|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|55,000|
|Volkswagen|Sambabus Typ 2 '62|67,400|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|308 GTB '75|165,200|
|Fiat|500 1.2 8V Lounge SS '08|12,900|
|Honda|Civic Type R (EK) '97|48,200|
|Lamborghini|Countach 25th Anniversary '88|701,600|
|Mitsubishi|Lancer Evolution III GSR '95|91,100|
|TVR|Tuscan Speed 6 '00|95,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|22,200|
|Alfa Romeo|8C Competizione '08|290,200|
|BMW|M3 Sport Evolution '89|168,400|
|Ford|Sierra RS 500 Cosworth '87|185,400|
|Honda|Beat '91|14,400|
|Honda|S2000 '99|106,000|
|Lamborghini|Diablo GT '00|779,000|
|McLaren|MP4-12C '10|194,100|
|Mitsubishi|GTO Twin Turbo '91|45,300|
|Nissan|GT-R NISMO (R32) '90|386,600|
|Nissan|R33 GT-R V-spec '97|154,300|
|Nissan|Silvia K's Aero (S14) '96|59,900|
|Nissan|Silvia K's Dia Selection (S13) '90|55,200|
|Porsche|911 Carrera RS (993) '95|229,200|
|Porsche|911 Turbo (930) '81|220,000|
|RUF|CTR3 '07|770,800|
|Renault|R4 GTL '85|26,700|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|106,700|
|Toyota|Supra 3.0GT Turbo A '88|107,000|
|Volkswagen|Volkswagen 1200 '66|28,800|
