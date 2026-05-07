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


# Gran Turismo 7 Shops for 07-May-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chaparral|2J '70|2,500,000|
|Porsche|917K '70|20,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Porsche|356 A/1500 GS Carrera '56|606,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Chevelle SS 454 Sport Coupé '70|150,000|
|Chevrolet|Corvette (C2) '63|248,000|
|Ferrari|500 Mondial Pinin Farina Coupe '54|2,000,000|
|Jaguar|E-type Coupe '61|186,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|
|Porsche|911 Turbo S Leichtbau (964) '93|1,200,000|
|Porsche|962 C '88|1,250,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|49,700|
|DMC|DeLorean S2 '04|468,100|
|Ferrari|308 GTB '75|166,500|
|Fiat|500 1.2 8V Lounge SS '08|12,800|
|Nissan|Fairlady Z (Z34) '08|38,900|
|Toyota|Sports 800 '65|47,700|
|Volvo|240 SE Estate '93|43,900|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|147,100|
|Dodge|Viper SRT10 Coupe '06|114,400|
|Ferrari|458 Italia '09|243,300|
|Ford|Escort RS Cosworth '92|122,100|
|Honda|Civic Si Extra (EF) '87|57,200|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|179,900|
|Renault|R4 GTL '85|29,200|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|21,800|
|Honda|Beat '91|17,100|
|Honda|NSX Type R '92|388,500|
|Lamborghini|Murcielago LP 640 '09|318,500|
|Lancia|Stratos '73|524,500|
|Mazda|Eunos Roadster (NA) '89|27,900|
|Mitsubishi|FTO GP Version R '97|30,100|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|61,000|
|Nissan|Sileighty '98|81,900|
|Porsche|911 GT3 (996) '01|156,200|
|Porsche|911 GT3 (997) '09|140,400|
|Renault|Twingo '93|14,000|
|Toyota|Celica GT-Four (ST205) '94|67,500|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|51,800|
