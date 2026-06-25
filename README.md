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


# Gran Turismo 7 Shops for 25-June-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|Sport quattro S1 Pikes Peak '87|1,700,000|
|Citroen|DS 21 Pallas '70|44,600|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Shelby|G.T.350 '65|501,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Camaro Z28 '69|101,000|
|Ferrari|330 P4 '67|20,000,000|
|Jeep|Willys MB '45|33,500|
|NISMO|400R '95|1,300,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Porsche|356 A/1500 GS Carrera '56|606,000|
|Porsche|911 Carrera RS (901) '73|740,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Autobianchi|A112 Abarth '85|28,900|
|Ferrari|430 Scuderia '07|370,400|
|Honda|Civic Type R (EK) '98|51,700|
|MINI|MINI Cooper S '05|22,900|
|Pontiac|Firebird Trans Am '78|86,900|
|Toyota|Supra RZ '97|190,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Fiat|500 1.2 8V Lounge SS '08|12,500|
|MINI|Mini-Cooper 'S' '65|42,800|
|Mitsubishi|FTO GP Version R '97|26,200|
|Nissan|Fairlady Z (Z34) '08|32,900|
|Nissan|Fairlady Z Version S (Z33) '07|28,000|
|Renault|Twingo '93|14,000|
|Renault|Twingo '93|14,000|
|Renault|Twingo '93|14,000|
|Toyota|Celica GT-Four (ST205) '94|65,500|
|Toyota|Sports 800 '65|43,800|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|137,300|
|Audi|TT Coupe 3.2 quattro '03|49,800|
|Audi|TTS Coupe '09|61,200|
|BMW|3.0 CSL '71|167,000|
|DMC|DeLorean S2 '04|462,300|
|Daihatsu|Copen '02|14,300|
|De Tomaso|Pantera '71|173,100|
|Ferrari|308 GTB '75|178,300|
|Ferrari|512 BB '76|313,400|
|Ford|Ford GT '06|398,300|
|Honda|NSX Type R '02|431,500|
|Mazda|RX-7 GT-X (FC) '90|70,000|
|Nissan|180SX Type X '96|49,700|
|Suzuki|Swift Sport '07|12,900|
