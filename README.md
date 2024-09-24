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


# Gran Turismo 7 Shops for 24-September-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray Racer Concept '59|4,000,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Mazda|787B '91|3,300,000|
|NISMO|400R '95|1,800,000|
|Renault|R8 Gordini '66|32,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Toyota|2000GT '67|992,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|300 SEL 6.8 AMG '71|700,000|
|Ferrari|F40 '92|3,100,000|
|Jaguar|XJR-9 '88|3,000,000|
|Pontiac|GTO 'The Judge' '69|268,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|S2000 '99|106,000|
|Lamborghini|Murcielago LP 640 '09|318,700|
|Mitsubishi|Lancer Evolution IV GSR '96|55,000|
|Nissan|Silvia K's Aero (S14) '96|59,900|
|Nissan|Silvia K's Dia Selection (S13) '90|55,200|
|Toyota|Supra 3.0GT Turbo A '88|107,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|Integra Type R (DC2) '95|62,300|
|Lancia|Delta HF Integrale Evoluzione '91|98,900|
|Nissan|Fairlady 240ZG (HS30) '71|106,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|310,900|
|Abarth|Abarth 500 '09|22,200|
|BMW|M3 Sport Evolution '89|168,400|
|BMW|Z8 '01|267,200|
|Ferrari|308 GTB '75|165,200|
|Fiat|500 1.2 8V Lounge SS '08|12,900|
|Honda|Beat '91|14,400|
|Honda|Civic Type R (EK) '97|48,200|
|Honda|Civic Type R (EK) Touring Car|122,400|
|Maserati|GranTurismo S '08|137,700|
|McLaren|MP4-12C '10|194,100|
|Mitsubishi|Lancer Evolution III GSR '95|91,100|
|Nissan|R34 GT-R V-spec II Nur '02|401,100|
|Porsche|911 GT3 (997) '09|140,200|
|RUF|CTR3 '07|770,800|
|Renault|R4 GTL '85|26,700|
|Volkswagen|Scirocco R '10|37,900|
|Volkswagen|Volkswagen 1200 '66|28,800|
