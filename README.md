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


# Gran Turismo 7 Shops for 06-July-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|GT40 Mark I '66|6,700,000|
|Nissan|R92CP '92|2,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Shelby|Cobra 427 '66|2,500,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray Racer Concept '59|4,000,000|
|Ferrari|GTO '84|3,500,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Lamborghini|Miura P400 Bertone Prototype '67|3,750,000|
|Mazda|787B '91|3,300,000|
|Mercedes-Benz|300 SL (W194) '52|20,000,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Plymouth|Superbird '70|402,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|De Tomaso|Pantera '71|162,200|
|Honda|Integra Type R (DC2) '95|61,200|
|Nissan|Silvia Q's (S13) '88|31,900|
|Toyota|MR2 GT-S '97|58,100|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Daihatsu|Copen '02|13,000|
|Dodge|Viper SRT10 Coupe '06|115,000|
|Fiat|500 F '68|17,800|
|Ford|Sierra RS 500 Cosworth '87|200,000|
|Honda|NSX Type R '92|398,700|
|Mitsubishi|Lancer Evolution IX MR GSR '06|99,700|
|Nissan|Fairlady Z (Z34) '08|36,000|
|Porsche|911 Carrera RS CS (993) '95|409,500|
|Toyota|Sports 800 '65|48,100|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|167,300|
|Alfa Romeo|MiTo '09|22,400|
|Alpine|A110 '72|137,500|
|Audi|TT Coupe 3.2 quattro '03|45,400|
|BMW|M3 '89|75,700|
|Chevrolet|Corvette Stingray (C3) '69|51,500|
|Dodge|Viper GTS '02|105,600|
|Ferrari|512 BB '76|309,000|
|MINI|Mini-Cooper 'S' '65|40,600|
|Porsche|911 GT3 (996) '01|155,500|
|Renault|Clio V6 24V '00|82,300|
|Subaru|Impreza 22B-STi '98|177,300|
