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


# Gran Turismo 7 Shops for 15-February-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Jaguar|XJ220 '92|554,000|
|Mazda|787B '91|3,300,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Nissan|Fairlady Z 432 '69|312,000|
|Nissan|Fairlady Z 432 '69|312,000|
|Porsche|962 C '88|1,300,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C2) '63|234,000|
|Ferrari|500 Mondial Pinin Farina Coupe '54|2,600,000|
|Ferrari|F50 '95|4,450,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Plymouth|XNR Ghia Roadster '60|1,600,000|
|Porsche|356 A/1500 GS Carrera '56|618,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|23,900|
|Ferrari|308 GTB '75|176,100|
|Fiat|500 F '68|16,000|
|Mitsubishi|Lancer Evolution III GSR '95|95,600|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray (C3) '69|51,700|
|Ferrari|F430 '06|207,400|
|Honda|Civic Si Extra (EF) '87|61,600|
|Honda|NSX Type R '92|450,000|
|Honda|NSX Type R '92|450,000|
|Porsche|911 Carrera RS (964) '92|220,000|
|Toyota|MR2 GT-S '97|52,600|
|Volkswagen|Golf I GTI '83|43,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|132,600|
|Audi|TTS Coupe '09|67,600|
|BMW|M3 '03|72,700|
|BMW|M3 '07|70,200|
|BMW|M3 Sport Evolution '89|165,000|
|Daihatsu|Copen '02|13,300|
|De Tomaso|Pantera '71|174,800|
|Dodge|Viper GTS '02|106,400|
|Ferrari|430 Scuderia '07|363,500|
|Honda|Integra Type R (DC2) '95|67,400|
|Honda|NSX Type R '02|440,400|
|MINI|Mini-Cooper 'S' '65|39,300|
|Nissan|GT-R NISMO (R32) '90|393,800|
|Nissan|SILVIA spec-R Aero (S15) '02|59,800|
|Nissan|Silvia K's Type S (S14) '94|53,600|
|Suzuki|Swift Sport '07|12,800|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|58,200|
|Volkswagen|Scirocco R '10|37,500|
