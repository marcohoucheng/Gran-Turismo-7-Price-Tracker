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


# Gran Turismo 7 Shops for 02-September-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Camaro Z28 '69|115,000|
|McLaren|McLaren F1 '94|20,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Peugeot|205 Turbo 16 Evolution 2 '86|1,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Ferrari|250 GTO '62|20,000,000|
|Ford|Mustang Boss 429 '69|294,000|
|Jaguar|XJ13 '66|12,000,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|
|Toyota|2000GT '67|982,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|230,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mitsubishi|Lancer Evolution IV GSR '96|55,000|
|Volvo|240 SE Estate '93|50,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|47,600|
|BMW|3.0 CSL '71|143,000|
|DMC|DeLorean S2 '04|442,600|
|Ferrari|512 BB '76|308,600|
|Ford|Ford GT '06|411,600|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|25,600|
|Audi|TTS Coupe '09|57,300|
|BMW|3.0 CSL '73|206,600|
|BMW|M3 '07|80,400|
|Citroen|BX 19 TRS '87|23,100|
|De Tomaso|Pantera '71|177,300|
|Dodge|Viper GTS '02|103,600|
|Ferrari|308 GTB '75|179,000|
|Ferrari|430 Scuderia '07|343,200|
|Honda|NSX Type R '02|444,200|
|Honda|S800 '66|58,000|
|MINI|MINI Cooper S '05|20,500|
|Nissan|180SX Type X '96|49,200|
|Nissan|Fairlady 240ZG (HS30) '71|97,400|
|Nissan|Fairlady Z 300ZX TT 2seater '89|58,100|
|Nissan|Silvia K's Aero (S14) '96|60,000|
|Nissan|Silvia Q's (S13) '88|34,900|
|Renault|Avantime 3.0 V6 24V '02|39,000|
|Renault|Clio V6 24V '00|81,600|
|Renault|Kangoo 1.4 '01|14,100|
|Renault|R5 Turbo '80|152,900|
|Toyota|MR2 GT-S '97|50,500|
|Toyota|Prius G '09|20,700|
|Toyota|Supra RZ '97|189,800|
