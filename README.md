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


# Gran Turismo 7 Shops for 12-December-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|800,000|
|Ferrari|250 GTO '62|20,000,000|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|290,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Alfa Romeo|8C 2900B Touring Berlinetta '38|20,000,000|
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Ferrari|F40 '92|3,100,000|
|Honda|NSX GT500 '00|1,500,000|
|McLaren|McLaren F1 GTR - BMW '95|16,000,000|
|Nissan|GT-R GT500 '99|2,500,000|
|Peugeot|205 Turbo 16 Evolution 2 '86|1,000,000|
|Toyota|Supra GT500 '97|1,800,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|Mustang Boss 429 '69|319,000|
|Jaguar|XJ13 '66|12,000,000|
|Shelby|Cobra 427 '66|2,500,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|250,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 Sport Evolution '89|200,000|
|BMW|M3 Sport Evolution '89|200,000|
|Chevrolet|Corvette ZR1 (C6) '09|99,000|
|Dodge|Viper SRT10 Coupe '06|111,800|
|Ford|Sierra RS 500 Cosworth '87|200,000|
|Ford|Sierra RS 500 Cosworth '87|200,000|
|Ford|Sierra RS 500 Cosworth '87|200,000|
|MINI|Mini-Cooper 'S' '65|40,800|
|Mitsubishi|GTO Twin Turbo '91|41,600|
|Mitsubishi|Lancer Evolution IV GSR '96|39,600|
|Nissan|R32 GT-R V-spec II '94|178,600|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|62,300|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|Civic Type R (EK) '97|50,200|
|Lamborghini|Diablo GT '00|790,200|
|Nissan|GT-R NISMO (R32) '90|400,000|
|Nissan|Silvia K's Aero (S14) '96|57,800|
|Pontiac|Firebird Trans Am '78|87,900|
|Porsche|911 Carrera RS (993) '95|260,000|
|Porsche|911 Turbo (930) '81|220,000|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|99,100|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|313,200|
|Alpine|A110 '72|142,200|
|Daihatsu|Copen '02|15,700|
|Ferrari|Testarossa '91|367,000|
|Fiat|500 1.2 8V Lounge SS '08|14,400|
|Honda|Civic Type R (EK) Touring Car|140,000|
|Maserati|GranTurismo S '08|141,800|
|McLaren|MP4-12C '10|184,100|
|Mitsubishi|Lancer Evolution V GSR '98|80,700|
|Nissan|R34 GT-R V-spec II Nur '02|396,400|
|Nissan|Silvia K's Type S (S14) '94|51,400|
|RUF|CTR3 '07|771,300|
|Subaru|Impreza Sedan WRX STi '04|43,600|
|Suzuki|Swift Sport '07|11,800|
|Toyota|Sports 800 '65|47,200|
|Toyota|Supra 3.0GT Turbo A '88|112,000|
|Volkswagen|Golf I GTI '83|40,500|
