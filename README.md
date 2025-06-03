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


# Gran Turismo 7 Shops for 03-June-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Lamborghini|Miura P400 Bertone Prototype '67|4,300,000|
|Porsche|911 Carrera RS (901) '73|799,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|De Tomaso|Mangusta (Christian Dior)|500,000|
|Mercedes-Benz|CLK-LM '98|8,500,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Alfa Romeo|8C 2900B Touring Berlinetta '38|20,000,000|
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Ford|Mustang Boss 429 '69|294,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|542,000|
|Peugeot|205 Turbo 16 Evolution 2 '86|1,000,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|230,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|139,200|
|Porsche|911 Carrera RS (993) '95|260,000|
|Porsche|911 Carrera RS (993) '95|260,000|
|Toyota|Supra RZ '97|197,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|143,500|
|Daihatsu|Copen '02|13,300|
|Dodge|Super Bee '70|67,800|
|Ferrari|458 Italia '09|252,200|
|Honda|NSX Type R '92|399,200|
|Nissan|R32 GT-R V-spec II '94|171,400|
|Pontiac|Firebird Trans Am '78|87,800|
|Suzuki|Swift Sport '07|12,800|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|165,800|
|Chevrolet|Corvette Convertible (C3) '69|56,000|
|Ferrari|512 BB '76|289,100|
|Ford|Escort RS Cosworth '92|129,800|
|Honda|Civic Type R (EK) '98|58,100|
|Lamborghini|Murcielago LP 640 '09|320,700|
|Lancia|Stratos '73|534,900|
|MINI|Mini-Cooper 'S' '65|39,300|
|Mitsubishi|Lancer Evolution IV GSR '96|41,200|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|176,100|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|60,300|
|Nissan|Fairlady Z (Z34) '08|35,400|
|Nissan|Sileighty '98|76,500|
|Nissan|Skyline GTS-R (R31) '87|171,900|
|Porsche|911 GT3 (996) '01|154,800|
|Porsche|911 GT3 (997) '09|138,900|
|Toyota|Celica GT-Four (ST205) '94|72,300|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|58,200|
