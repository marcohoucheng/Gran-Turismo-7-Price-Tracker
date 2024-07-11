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


# Gran Turismo 7 Shops for 11-July-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Shelby|G.T.350 '65|469,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Lamborghini|Miura P400 Bertone Prototype '67|3,750,000|
|Plymouth|Superbird '70|402,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|GIULIA TZ2 carrozzata da ZAGATO '65|3,800,000|
|Dodge|Challenger R/T '70|214,000|
|Ferrari|365 GTB4 '71|610,000|
|Ford|GT40 Mark I '66|6,700,000|
|Mercedes-Benz|300 SL (W194) '52|20,000,000|
|Nissan|R92CP '92|2,000,000|
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,600,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TTS Coupe '09|63,100|
|BMW|M3 Sport Evolution '89|179,700|
|Ferrari|308 GTB '75|166,400|
|Honda|NSX Type R '02|431,600|
|Porsche|911 Carrera RS (964) '92|226,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|22,400|
|BMW|M3 '89|75,700|
|Nissan|SILVIA spec-R Aero (S15) '02|61,100|
|Subaru|Impreza 22B-STi '98|177,300|
|Toyota|MR2 GT-S '97|58,100|
|Toyota|Prius G '09|21,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|57,000|
|Autobianchi|A112 Abarth '85|31,800|
|BMW|M3 '07|69,900|
|De Tomaso|Pantera '71|162,200|
|Ferrari|F430 '06|201,100|
|Ferrari|Testarossa '91|450,000|
|Ford|Ford GT '06|399,300|
|Honda|Civic Type R (EK) '98|47,400|
|Honda|Integra Type R (DC2) '95|61,200|
|Honda|S800 '66|49,600|
|Lancia|Delta HF Integrale Evoluzione '91|101,900|
|Nissan|Fairlady Z Version S (Z33) '07|26,800|
|Nissan|GT-R NISMO (R32) '90|390,000|
|Nissan|Silvia Q's (S13) '88|31,900|
|Renault|R5 Turbo '80|147,400|
|TVR|Tuscan Speed 6 '00|72,500|
|Toyota|Supra RZ '97|192,300|
|Volkswagen|Scirocco R '10|42,000|
