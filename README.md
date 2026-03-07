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


# Gran Turismo 7 Shops for 07-March-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray Racer Concept '59|7,000,000|
|Nissan|R92CP '92|2,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|300 SEL 6.8 AMG '71|700,000|
|Ferrari|F40 '92|3,200,000|
|Ford|Mark IV Race Car '67|6,750,000|
|Pontiac|GTO 'The Judge' '69|209,000|
|Renault|R8 Gordini '66|32,500|
|Toyota|2000GT '67|982,000|
|Toyota|Land Cruiser FJ40V '74|44,100|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|Civic Type R (EK) Touring Car|115,800|
|Nissan|Silvia K's Dia Selection (S13) '90|52,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|Z4 3.0i '03|45,500|
|Honda|Integra Type R (DC2) '98|65,900|
|Lancia|Delta HF Integrale Evoluzione '91|98,500|
|Mitsubishi|Lancer Evolution IX MR GSR '06|97,400|
|Nissan|Silvia K's Type S (S14) '94|43,200|
|Porsche|911 Carrera RS (993) '95|214,800|
|Suzuki|Cappuccino (EA11R) '91|16,900|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|52,100|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|SLS AMG '10|308,300|
|Alfa Romeo|8C Competizione '08|286,800|
|Alfa Romeo|Giulia Sprint GT Veloce '67|165,200|
|Ferrari|Dino 246 GT '71|343,200|
|Ford|Mustang Mach 1 '71|44,500|
|Lamborghini|Countach 25th Anniversary '88|690,200|
|Mazda|RX-7 GT-X (FC) '90|52,900|
|Mitsubishi|Lancer Evolution V GSR '98|74,700|
|Nissan|Fairlady 240ZG (HS30) '71|103,100|
|Peugeot|205 GTI '88|50,700|
|Porsche|911 Carrera RS CS (993) '95|441,300|
|Porsche|911 Turbo (930) '81|213,700|
|RUF|CTR3 '07|783,800|
|Renault|Avantime 3.0 V6 24V '02|44,900|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|105,800|
|Toyota|Supra 3.0GT Turbo A '88|115,200|
|Volkswagen|Volkswagen 1200 '66|34,000|
