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


# Gran Turismo 7 Shops for 22-November-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB3S '53|6,000,000|
|De Tomaso|Mangusta (Christian Dior)|500,000|
|McLaren|McLaren F1 '94|20,000,000|
|Porsche|911 Carrera RS (901) '73|740,000|
|Porsche|911 Carrera RS (901) '73|740,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Alfa Romeo|8C 2900B Touring Berlinetta '38|20,000,000|
|Mercedes-Benz|CLK-LM '98|8,500,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|537,000|
|Peugeot|205 Turbo 16 Evolution 2 '86|1,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|512 BB '76|299,300|
|Honda|Beat '91|14,900|
|Honda|Civic Si Extra (EF) '87|50,700|
|MINI|MINI Cooper S '05|23,600|
|Renault|R4 GTL '85|25,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|Testarossa '91|450,000|
|Ferrari|Testarossa '91|450,000|
|Ford|Escort RS Cosworth '92|128,900|
|Lancia|Stratos '73|539,800|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|65,700|
|Nissan|Sileighty '98|84,800|
|Porsche|911 GT3 (996) '01|161,700|
|Porsche|911 GT3 (997) '09|140,900|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|43,300|
|Audi|TTS Coupe '09|58,300|
|Citroen|BX 19 TRS '87|22,700|
|DMC|DeLorean S2 '04|462,400|
|De Tomaso|Pantera '71|166,500|
|Ferrari|308 GTB '75|176,100|
|Ford|Ford GT '06|397,100|
|Honda|NSX Type R '02|432,900|
|Honda|S800 '66|52,000|
|Nissan|180SX Type X '96|57,400|
|Nissan|Fairlady Z (Z34) '08|37,100|
|Nissan|Fairlady Z Version S (Z33) '07|26,800|
|Nissan|Silvia Q's (S13) '88|31,500|
|Renault|Kangoo 1.4 '01|14,200|
|Renault|R5 Turbo '80|161,400|
|Toyota|Celica GT-Four (ST205) '94|65,500|
|Toyota|Prius G '09|19,400|
|Volkswagen|Sambabus Typ 2 '62|63,000|
