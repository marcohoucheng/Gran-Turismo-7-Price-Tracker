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


# Gran Turismo 7 Shops for 19-August-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Plymouth|XNR Ghia Roadster '60|1,600,000|
|Porsche|959 '87|1,950,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Toyota|Supra GT500 '97|1,800,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|F50 '95|4,450,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Jaguar|XJ220 '92|615,000|
|Maserati|A6GCS/53 Spyder '54|2,500,000|
|Mazda|RX500 '70|600,000|
|Porsche|356 A/1500 GS Carrera '56|618,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C Competizione '08|290,200|
|Honda|Civic Type R (EK) '97|48,200|
|Lamborghini|Countach 25th Anniversary '88|701,600|
|Renault|R4 GTL '85|26,700|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|De Tomaso|Pantera '71|170,400|
|Honda|Integra Type R (DC2) '95|62,300|
|Honda|S800 '66|48,700|
|Suzuki|Cappuccino (EA11R) '91|16,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|135,900|
|BMW|3.0 CSL '71|140,400|
|BMW|M3 Sport Evolution '89|168,400|
|Ferrari|308 GTB '75|165,200|
|Fiat|500 1.2 8V Lounge SS '08|12,900|
|Honda|S2000 '99|106,000|
|Lamborghini|Diablo GT '00|779,000|
|Lancia|Delta HF Integrale Evoluzione '91|98,900|
|Mazda|RX-7 Spirit R Type A (FD) '02|216,300|
|Mercedes-Benz|SLR McLaren '09|495,200|
|Mitsubishi|Lancer Evolution III GSR '95|91,100|
|Mitsubishi|Lancer Evolution IX MR GSR '06|91,400|
|Nissan|Fairlady 240ZG (HS30) '71|106,400|
|Nissan|R33 GT-R V-spec '97|154,300|
|Nissan|Silvia K's Aero (S14) '96|59,900|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|106,700|
|Toyota|Supra 3.0GT Turbo A '88|107,000|
|Volkswagen|Scirocco R '10|37,900|
|Volkswagen|Volkswagen 1200 '66|28,800|
