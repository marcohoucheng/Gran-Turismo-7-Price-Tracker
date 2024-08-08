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


# Gran Turismo 7 Shops for 08-August-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|McLaren|MP4/4 '88|12,000,000|
|Nissan|Skyline Super Silhouette Group 5 '84|1,150,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|356 A/1500 GS Carrera '56|618,000|
|Porsche|356 A/1500 GS GT Carrera Speedster '56|1,600,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|892,000|
|Ferrari|250 GT Berlinetta passo corto '61|8,100,000|
|McLaren|McLaren F1 '94|20,000,000|
|Nissan|Fairlady Z 432 '69|312,000|
|Nissan|GT-R GT500 '99|2,500,000|
|Shelby|Cobra Daytona Coupe '64|20,000,000|
|Subaru|Impreza Rally Car '98|650,000|
|Toyota|GT-One (TS020) '99|2,500,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '89|86,100|
|Chevrolet|Corvette ZR1 (C6) '09|99,000|
|Dodge|Viper SRT10 Coupe '06|114,400|
|Honda|Civic Type R (EK) '98|58,100|
|Nissan|Fairlady Z 300ZX TT 2seater '89|52,500|
|Porsche|911 GT3 (996) '01|161,700|
|Toyota|Prius G '09|18,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|Z8 '01|267,200|
|Fiat|500 F '68|15,500|
|Mazda|RX-7 GT-X (FC) '90|53,800|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|51,900|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|169,000|
|Alfa Romeo|MiTo '09|22,700|
|Audi|TT Coupe 3.2 quattro '03|42,100|
|BMW|3.0 CSL '73|250,000|
|BMW|M3 '97|74,600|
|DMC|DeLorean S2 '04|472,300|
|Ferrari|430 Scuderia '07|366,700|
|Ferrari|458 Italia '09|243,200|
|Ferrari|Testarossa '91|392,500|
|Honda|Civic Type R (EK) Touring Car|122,400|
|Honda|NSX Type R '92|398,200|
|Lamborghini|Gallardo LP 560-4 '08|253,100|
|MINI|MINI Cooper S '05|24,100|
|MINI|Mini-Cooper 'S' '65|40,800|
|Nissan|Silvia Q's (S13) '88|31,800|
|Porsche|911 Carrera RS CS (993) '95|413,800|
|Renault|Clio V6 24V '00|81,900|
