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


# Gran Turismo 7 Shops for 29-March-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,600,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray Racer Concept '59|4,000,000|
|Jaguar|XJ220 '92|554,000|
|Mercedes-Benz|300 SL (W194) '52|20,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Challenger R/T '70|214,000|
|Ferrari|GTO '84|3,500,000|
|Ford|GT40 Mark I '66|6,700,000|
|Lamborghini|Miura P400 Bertone Prototype '67|4,300,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Mercedes-Benz|Unimog Type 411 '62|46,000|
|Subaru|Impreza Rally Car '98|650,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Lamborghini|Countach 25th Anniversary '88|655,200|
|Nissan|R34 GT-R V-spec II Nur '02|388,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|3.0 CSL '73|250,000|
|BMW|3.0 CSL '73|250,000|
|Honda|Integra Type R (DC2) '95|62,100|
|Honda|NSX Type R '02|435,000|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|56,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|47,000|
|Autobianchi|A112 Abarth '85|29,700|
|BMW|3.0 CSL '71|138,000|
|BMW|M3 Sport Evolution '89|172,000|
|BMW|Z4 3.0i '03|53,700|
|Dodge|Viper GTS '02|107,300|
|Ferrari|308 GTB '75|176,700|
|Ferrari|430 Scuderia '07|363,800|
|Ford|Sierra RS 500 Cosworth '87|181,200|
|Honda|Civic SiR-II (EG) '93|48,000|
|Honda|Civic Type R (EK) '98|52,100|
|Honda|S2000 '99|98,400|
|Lamborghini|Diablo GT '00|830,900|
|Lancia|Delta HF Integrale Evoluzione '91|98,500|
|Mitsubishi|Lancer Evolution III GSR '95|83,500|
|Mitsubishi|Lancer Evolution IX MR GSR '06|97,900|
|Nissan|R33 GT-R V-spec '97|155,200|
|RUF|CTR3 '07|788,800|
|Renault|Kangoo 1.4 '01|13,500|
|Volkswagen|Scirocco R '10|38,700|
