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


# Gran Turismo 7 Shops for 17-June-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Shelby|G.T.350 '65|501,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|GIULIA TZ2 carrozzata da ZAGATO '65|3,850,000|
|Chevrolet|Chevelle SS 454 Sport Coupé '70|150,000|
|Ferrari|GTO '84|3,500,000|
|Ford|GT40 Mark I '66|6,700,000|
|Lamborghini|Countach LP400 '74|1,250,000|
|Mazda|787B '91|3,300,000|
|Mercedes-Benz|300 SL (W194) '52|20,000,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Plymouth|Superbird '70|450,000|
|Porsche|911 Turbo S Leichtbau (964) '93|1,200,000|
|Renault|Espace F1 '95|2,000,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Fiat|500 1.2 8V Lounge SS '08|12,500|
|Lamborghini|Murcielago LP 640 '09|316,200|
|Porsche|911 GT3 (997) '09|141,900|
|Toyota|Celica GT-Four (ST205) '94|65,500|
|Toyota|Sports 800 '65|43,800|
|Volvo|240 SE Estate '93|48,600|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette ZR-1 (C4) '89|86,500|
|Nissan|R32 GT-R V-spec II '94|173,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|23,500|
|Audi|R8 4.2 '07|137,900|
|BMW|M3 '97|90,000|
|Chevrolet|Corvette Convertible (C3) '69|47,000|
|Ferrari|458 Italia '09|254,300|
|Ferrari|512 BB '76|350,000|
|Ford|Escort RS Cosworth '92|128,900|
|Honda|Beat '91|15,000|
|Honda|Civic Si Extra (EF) '87|55,100|
|Honda|NSX Type R '92|396,200|
|Lamborghini|Gallardo LP 560-4 '08|251,300|
|Lancia|Stratos '73|539,800|
|Mazda|Eunos Roadster (NA) '89|29,600|
|Mazda|efini RX-7 Type R (FD) '91|69,600|
|Mitsubishi|Lancer Evolution IV GSR '96|46,300|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|165,200|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|69,200|
|Nissan|Sileighty '98|84,800|
|Porsche|911 GT3 (996) '01|158,500|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|50,200|
