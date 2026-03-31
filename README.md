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


# Gran Turismo 7 Shops for 31-March-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Camaro Z28 '69|101,000|
|De Tomaso|Mangusta '69|310,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Jeep|Willys MB '45|33,500|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|Sport quattro S1 Pikes Peak '87|1,700,000|
|Citroen|DS 21 Pallas '70|44,600|
|Honda|RA272 '65|2,500,000|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|250,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Shelby|Cobra 427 '66|2,700,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|134,500|
|Nissan|Fairlady Z 300ZX TT 2seater '89|58,000|
|Renault|Clio V6 24V '00|73,600|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mitsubishi|FTO GP Version R '97|26,200|
|Porsche|911 GT3 (997) '09|138,900|
|Toyota|Celica GT-Four (ST205) '94|65,500|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|26,400|
|Audi|TT Coupe 3.2 quattro '03|49,800|
|Audi|TTS Coupe '09|63,100|
|DMC|DeLorean S2 '04|462,300|
|De Tomaso|Pantera '71|173,100|
|Ferrari|308 GTB '75|178,300|
|Ferrari|512 BB '76|286,400|
|Fiat|500 1.2 8V Lounge SS '08|12,700|
|Ford|Ford GT '06|412,900|
|Honda|Civic Type R (EK) '97|47,000|
|Honda|NSX Type R '02|444,300|
|Lamborghini|Murcielago LP 640 '09|320,700|
|MINI|MINI Cooper S '05|22,900|
|MINI|Mini-Cooper 'S' '65|43,600|
|Mazda|Eunos Roadster (NA) '89|31,200|
|Nissan|180SX Type X '96|49,700|
|Nissan|Fairlady Z (Z34) '08|35,400|
|Nissan|Fairlady Z Version S (Z33) '07|27,300|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|51,200|
|Toyota|Sports 800 '65|45,900|
|Volvo|240 SE Estate '93|46,600|
