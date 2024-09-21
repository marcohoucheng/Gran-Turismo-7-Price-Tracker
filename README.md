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


# Gran Turismo 7 Shops for 21-September-2024



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|892,000|
|Ferrari|250 GTO '62|20,000,000|
|Jaguar|XJ13 '66|12,000,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|250,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C1) '58|119,000|
|Jaguar|XJR-9 '88|3,000,000|
|Pontiac|GTO 'The Judge' '69|268,000|
|Toyota|2000GT '67|992,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|308 GTB '75|165,200|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|58,200|
|Alfa Romeo|8C Competizione '08|290,200|
|Ferrari|512 BB '76|350,000|
|Honda|S800 '66|48,700|
|Nissan|R33 GT-R V-spec '97|154,300|
|Nissan|SILVIA spec-R Aero (S15) '02|59,900|
|Porsche|911 Carrera RS (993) '95|229,200|
|Renault|R5 Turbo '80|151,900|
|Subaru|Impreza 22B-STi '98|176,100|
|Suzuki|Cappuccino (EA11R) '91|16,000|
|Toyota|MR2 GT-S '97|53,600|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|310,900|
|BMW|3.0 CSL '71|140,400|
|BMW|M3 '89|86,100|
|BMW|M3 Sport Evolution '89|168,400|
|De Tomaso|Pantera '71|170,400|
|Fiat|500 1.2 8V Lounge SS '08|12,900|
|Honda|Integra Type R (DC2) '95|62,300|
|Lancia|Delta HF Integrale Evoluzione '91|98,900|
|McLaren|MP4-12C '10|194,100|
|Nissan|Fairlady 240ZG (HS30) '71|106,400|
|Nissan|R34 GT-R V-spec II Nur '02|401,100|
|RUF|CTR3 '07|770,800|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|106,700|
|Volkswagen|Scirocco R '10|37,900|
