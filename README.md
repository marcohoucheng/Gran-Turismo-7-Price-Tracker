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


# Gran Turismo 7 Shops for 11-September-2024



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|365 GTB4 '71|610,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Alfa Romeo|8C 2900B Touring Berlinetta '38|20,000,000|
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|De Tomaso|Mangusta (Christian Dior)|500,000|
|Mercedes-Benz|CLK-LM '98|8,500,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|542,000|
|Peugeot|205 Turbo 16 Evolution 2 '86|1,100,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|42,100|
|Honda|Civic Type R (EK) '98|58,100|
|Nissan|Silvia Q's (S13) '88|31,800|
|Toyota|Prius G '09|18,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Viper SRT10 Coupe '06|114,400|
|Ferrari|Dino 246 GT '71|338,000|
|Fiat|500 F '68|15,500|
|Honda|NSX Type R '92|398,200|
|Nissan|Silvia K's Type S (S14) '94|51,400|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|51,900|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|169,000|
|Alfa Romeo|MiTo '09|22,700|
|Audi|R8 4.2 '07|135,900|
|Chevrolet|Corvette ZR-1 (C4) '89|77,800|
|Chevrolet|Corvette ZR1 (C6) '09|99,000|
|DMC|DeLorean S2 '04|472,300|
|Dodge|Super Bee '70|61,100|
|MINI|MINI Cooper S '05|24,100|
|MINI|Mini-Cooper 'S' '65|40,800|
|Mazda|RX-7 GT-X (FC) '90|53,800|
|Mazda|RX-7 Spirit R Type A (FD) '02|216,300|
|Mercedes-Benz|SLR McLaren '09|495,200|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|174,200|
|Nissan|180SX Type X '96|48,900|
|Nissan|R33 GT-R V-spec '97|154,300|
|Porsche|911 GT3 (996) '01|161,700|
|Renault|Clio V6 24V '00|81,900|
|Toyota|Celica GT-Four (ST205) '94|65,100|
