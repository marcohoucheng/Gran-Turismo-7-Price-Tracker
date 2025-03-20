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


# Gran Turismo 7 Shops for 20-March-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|300 SEL 6.8 AMG '71|700,000|
|Pontiac|GTO 'The Judge' '69|242,000|
|Renault|R8 Gordini '66|32,500|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|F40 '92|3,100,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Jaguar|XJR-9 '88|3,000,000|
|Mercedes-Benz|300 SL (W194) '52|20,000,000|
|Nissan|R92CP '92|2,000,000|
|Plymouth|Superbird '70|402,000|
|Shelby|Cobra 427 '66|2,500,000|
|Shelby|G.T.350 '65|455,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '07|79,400|
|Porsche|911 Carrera RS (964) '92|207,000|
|Toyota|MR2 GT-S '97|56,200|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|49,800|
|Nissan|Fairlady Z 300ZX TT 2seater '89|60,200|
|Nissan|Fairlady Z Version S (Z33) '07|27,700|
|Renault|Clio V6 24V '00|75,000|
|Toyota|Sports 800 '65|47,400|
|Toyota|Supra RZ '97|184,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|133,200|
|BMW|M3 '89|88,300|
|Chevrolet|Corvette Stingray (C3) '69|59,400|
|Daihatsu|Copen '02|14,100|
|Ferrari|Dino 246 GT '71|400,000|
|Ferrari|Dino 246 GT '71|400,000|
|Ferrari|F430 '06|208,000|
|Ford|Ford GT '06|397,000|
|MINI|Mini-Cooper 'S' '65|36,200|
|Nissan|GT-R NISMO (R32) '90|392,800|
|Nissan|Silvia K's Type S (S14) '94|44,900|
|Pontiac|Firebird Trans Am '78|98,300|
|Subaru|Impreza 22B-STi '98|166,500|
|Suzuki|Swift Sport '07|14,500|
|TVR|Tuscan Speed 6 '00|84,600|
|Volkswagen|Golf I GTI '83|46,200|
