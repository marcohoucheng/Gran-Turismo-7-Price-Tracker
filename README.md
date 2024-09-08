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


# Gran Turismo 7 Shops for 08-September-2024



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|1932 Ford Roadster Hot Rod|400,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Alfa Romeo|8C 2900B Touring Berlinetta '38|20,000,000|
|Aston Martin|DB3S '53|6,000,000|
|De Tomaso|Mangusta (Christian Dior)|500,000|
|Ferrari|365 GTB4 '71|610,000|
|McLaren|McLaren F1 '94|20,000,000|
|Mercedes-Benz|CLK-LM '98|8,500,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|542,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mercedes-Benz|SLR McLaren '09|495,200|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Daihatsu|Copen '02|15,700|
|Ferrari|458 Italia '09|243,200|
|Mitsubishi|Lancer Evolution IV GSR '96|39,600|
|Nissan|R32 GT-R V-spec II '94|178,600|
|Nissan|Sileighty '98|81,600|
|Nissan|Silvia K's Dia Selection (S13) '90|65,000|
|Nissan|Skyline GTS-R (R31) '87|162,200|
|Suzuki|Swift Sport '07|11,800|
|Toyota|Sports 800 '65|46,300|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|22,700|
|Alpine|A110 '72|142,200|
|Audi|R8 4.2 '07|135,900|
|Chevrolet|Corvette ZR-1 (C4) '89|77,800|
|Chevrolet|Corvette ZR1 (C6) '09|99,000|
|Dodge|Super Bee '70|61,100|
|Dodge|Viper SRT10 Coupe '06|114,400|
|Ferrari|Dino 246 GT '71|338,000|
|Fiat|500 F '68|15,500|
|Honda|NSX Type R '92|398,200|
|MINI|Mini-Cooper 'S' '65|40,800|
|Mazda|RX-7 GT-X (FC) '90|53,800|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|174,200|
|Nissan|Silvia K's Type S (S14) '94|51,400|
|Porsche|911 Carrera RS CS (993) '95|413,800|
|Porsche|911 GT3 (996) '01|161,700|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|51,900|
