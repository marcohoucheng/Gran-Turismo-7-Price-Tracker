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


# Gran Turismo 7 Shops for 16-March-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|Mark IV Race Car '67|6,750,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C1) '58|119,000|
|Ferrari|250 GTO '62|20,000,000|
|Mercedes-Benz|Unimog Type 411 '62|46,000|
|Porsche|Spyder type 550/1500RS '55|4,850,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|300 SEL 6.8 AMG '71|700,000|
|Ferrari|F40 '92|3,100,000|
|Jaguar|XJR-9 '88|3,000,000|
|Pontiac|GTO 'The Judge' '69|242,000|
|Renault|R8 Gordini '66|32,500|
|Toyota|2000GT '67|992,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '89|88,300|
|Volkswagen|Golf I GTI '83|46,200|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|23,500|
|BMW|Z4 3.0i '03|44,600|
|Ford|Escort RS Cosworth '92|123,900|
|Honda|NSX Type R '92|404,400|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|65,900|
|Peugeot|205 GTI '88|61,600|
|Porsche|911 GT3 (997) '09|142,600|
|Porsche|911 Turbo (930) '81|250,000|
|Porsche|911 Turbo (930) '81|250,000|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|51,900|
|Volvo|240 SE Estate '93|41,200|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|49,800|
|DMC|DeLorean S2 '04|451,400|
|Daihatsu|Copen '02|14,100|
|Ferrari|512 BB '76|289,400|
|Fiat|500 1.2 8V Lounge SS '08|13,500|
|Honda|Civic Type R (EK) '97|49,300|
|Lamborghini|Murcielago LP 640 '09|337,100|
|MINI|MINI Cooper S '05|20,700|
|Nissan|180SX Type X '96|55,100|
|Nissan|Fairlady Z (Z34) '08|32,300|
|Nissan|Fairlady Z 300ZX TT 2seater '89|60,200|
|Nissan|Fairlady Z Version S (Z33) '07|27,700|
|Pontiac|Firebird Trans Am '78|98,300|
|Porsche|911 GT3 (996) '01|158,400|
|Renault|Clio V6 24V '00|75,000|
|Suzuki|Swift Sport '07|14,500|
|Toyota|Celica GT-Four (ST205) '94|80,900|
|Toyota|Sports 800 '65|47,400|
|Toyota|Supra RZ '97|184,000|
