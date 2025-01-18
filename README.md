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


# Gran Turismo 7 Shops for 18-January-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Jaguar|D-type '54|6,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Camaro Z28 '69|128,000|
|De Tomaso|Mangusta '69|315,000|
|Dodge|Challenger R/T '70|214,000|
|Shelby|Cobra 427 '66|2,500,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|Sport quattro S1 Pikes Peak '87|1,800,000|
|Honda|NSX GT500 '00|1,500,000|
|Jaguar|XJR-9 '88|3,000,000|
|Mazda|787B '91|3,300,000|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|290,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Nissan|R92CP '92|2,000,000|
|Porsche|962 C '88|1,300,000|
|Porsche|Spyder type 550/1500RS '55|4,850,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '97|83,000|
|Mitsubishi|Lancer Evolution IV GSR '96|39,600|
|Nissan|R32 GT-R V-spec II '94|178,600|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C Competizione '08|313,400|
|Alpine|A110 '72|142,200|
|Ford|Escort RS Cosworth '92|150,000|
|Lamborghini|Countach 25th Anniversary '88|694,000|
|Lamborghini|Diablo GT '00|790,200|
|Mercedes-Benz|SLR McLaren '09|492,000|
|Nissan|Silvia K's Aero (S14) '96|57,800|
|Nissan|Silvia K's Type S (S14) '94|51,400|
|Porsche|911 Turbo (930) '81|220,000|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|51,900|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|169,000|
|Alfa Romeo|MiTo '09|22,700|
|Fiat|500 F '68|15,500|
|MINI|Mini-Cooper 'S' '65|40,800|
|McLaren|MP4-12C '10|184,100|
|Mitsubishi|GTO Twin Turbo '91|41,600|
|Mitsubishi|Lancer Evolution V GSR '98|80,700|
|Nissan|R34 GT-R V-spec II Nur '02|396,400|
|Nissan|Silvia Q's (S13) '88|31,800|
|Porsche|911 Carrera RS (993) '95|228,000|
|RUF|CTR3 '07|771,300|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|62,300|
|Subaru|Impreza Sedan WRX STi '04|43,600|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|99,100|
|Toyota|Supra 3.0GT Turbo A '88|112,000|
