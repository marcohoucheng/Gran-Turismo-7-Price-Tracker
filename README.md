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


# Gran Turismo 7 Shops for 25-October-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Toyota|Supra GT500 '97|1,600,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|365 GTB4 '71|610,000|
|Ferrari|365 GTB4 '71|610,000|
|Lamborghini|Countach LP400 '74|1,250,000|
|Toyota|GT-One (TS020) '99|2,500,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Lancia|Lancia Delta HF Integrale Rally Car '92|327,700|
|Maserati|Merak SS '80|61,500|
|McLaren|MP4/4 '88|12,000,000|
|Mercedes-Benz|W 196 R '55|20,000,000|
|Nissan|Skyline Super Silhouette Group 5 '84|1,150,000|
|Porsche|Carrera GTS (904) '64|2,200,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Daihatsu|Copen '02|14,400|
|RUF|CTR3 '07|787,400|
|Suzuki|Swift Sport '07|12,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|26,400|
|BMW|M3 '89|75,100|
|Chevrolet|Corvette ZR-1 (C4) '89|105,000|
|Chevrolet|Corvette ZR-1 (C4) '89|105,000|
|Ford|Sierra RS 500 Cosworth '87|196,400|
|Mazda|RX-7 Spirit R Type A (FD) '02|216,400|
|Nissan|R33 GT-R V-spec '97|161,000|
|Subaru|Impreza 22B-STi '98|163,100|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|50,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C Competizione '08|294,800|
|Alpine|A110 '72|129,600|
|BMW|M3 Sport Evolution '89|165,000|
|Fiat|500 1.2 8V Lounge SS '08|13,000|
|Honda|Civic Type R (EK) '97|53,500|
|Honda|S2000 '99|98,400|
|MINI|Mini-Cooper 'S' '65|38,100|
|Mercedes-Benz|SLR McLaren '09|512,200|
|Mitsubishi|Lancer Evolution III GSR '95|80,900|
|Mitsubishi|Lancer Evolution IX MR GSR '06|98,100|
|Porsche|911 Carrera RS (993) '95|217,200|
|Subaru|Impreza Sedan WRX STi '04|42,300|
|Toyota|Sports 800 '65|49,200|
|Volkswagen|Scirocco R '10|38,100|
