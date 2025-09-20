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


# Gran Turismo 7 Shops for 20-September-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Maserati|Merak SS '80|64,200|
|Shelby|G.T.350 '65|455,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|GTO '84|3,500,000|
|Ford|GT40 Mark I '66|6,700,000|
|Lamborghini|Miura P400 Bertone Prototype '67|4,300,000|
|Mazda|787B '91|3,300,000|
|Mercedes-Benz|300 SL (W194) '52|20,000,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Mercedes-Benz|Unimog Type 411 '62|46,000|
|NISMO|400R '95|1,600,000|
|NISMO|400R '95|1,600,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|542,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Plymouth|Superbird '70|402,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|MINI|Mini-Cooper 'S' '65|43,600|
|Mitsubishi|GTO Twin Turbo '91|45,700|
|Nissan|Silvia K's Aero (S14) '96|57,700|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Fiat|500 1.2 8V Lounge SS '08|12,800|
|Honda|Integra Type R (DC2) '98|61,400|
|Honda|NSX Type R '92|450,000|
|Honda|S2000 '99|104,900|
|Lamborghini|Countach 25th Anniversary '88|706,300|
|Lamborghini|Diablo GT '00|830,500|
|Mitsubishi|Lancer Evolution IX MR GSR '06|95,600|
|Porsche|911 Carrera RS CS (993) '95|500,000|
|RUF|CTR3 '07|792,800|
|Subaru|Impreza Sedan WRX STi '04|49,900|
|Toyota|Sports 800 '65|47,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|164,900|
|BMW|Z4 3.0i '03|43,700|
|Chevrolet|Corvette Z06 (C5) '01|50,200|
|Daihatsu|Copen '02|16,100|
|Honda|Civic Type R (EK) '98|47,000|
|McLaren|MP4-12C '10|187,100|
|Mitsubishi|Lancer Evolution V GSR '98|77,500|
|Nissan|GT-R NISMO (R32) '90|400,000|
|Nissan|R32 GT-R V-spec II '94|200,000|
|Nissan|R33 GT-R V-spec '97|180,000|
|Nissan|R34 GT-R V-spec II Nur '02|387,000|
|Pontiac|Firebird Trans Am '78|86,600|
|Porsche|911 Turbo (930) '81|223,900|
|Subaru|Impreza Coupe WRX Type R STi Ver.VI '99|52,500|
|Suzuki|Swift Sport '07|13,600|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|99,200|
|Toyota|Supra 3.0GT Turbo A '88|114,400|
|Volkswagen|Golf I GTI '83|42,100|
