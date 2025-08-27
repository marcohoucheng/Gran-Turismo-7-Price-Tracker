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


# Gran Turismo 7 Shops for 27-August-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|Mustang Boss 429 '69|294,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|230,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|1500 Biposto Bertone B.A.T 1 '52|1,000,000|
|Alfa Romeo|8C 2900B Touring Berlinetta '38|20,000,000|
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Citroen|DS 21 Pallas '70|47,100|
|Ferrari|F50 '95|4,450,000|
|Mercedes-Benz|CLK-LM '98|8,500,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|542,000|
|Peugeot|205 Turbo 16 Evolution 2 '86|1,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|25,600|
|BMW|3.0 CSL '71|143,000|
|De Tomaso|Pantera '71|177,300|
|Ferrari|512 BB '76|308,600|
|Nissan|180SX Type X '96|49,200|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|Civic SiR-II (EG) '93|50,100|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|164,100|
|Nissan|Sileighty '98|72,800|
|Peugeot|205 GTI '88|53,300|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|53,200|
|Audi|TT Coupe 3.2 quattro '03|47,600|
|Audi|TTS Coupe '09|57,300|
|BMW|M3 '97|90,000|
|DMC|DeLorean S2 '04|442,600|
|Ferrari|308 GTB '75|179,000|
|Ferrari|Testarossa '91|450,000|
|Fiat|500 F '68|17,800|
|Ford|Escort RS Cosworth '92|124,600|
|Ford|Ford GT '06|411,600|
|Honda|NSX Type R '02|444,200|
|Lamborghini|Murcielago LP 640 '09|327,700|
|Lancia|Stratos '73|495,200|
|Mitsubishi|Lancer Evolution VIII MR GSR '04|61,600|
|Nissan|Fairlady 240ZG (HS30) '71|97,400|
|Nissan|Fairlady Z (Z34) '08|35,800|
|Nissan|Fairlady Z Version S (Z33) '07|27,000|
|Nissan|Silvia K's Dia Selection (S13) '90|52,100|
|Porsche|911 GT3 (996) '01|156,800|
|Porsche|911 GT3 (997) '09|142,700|
|Suzuki|Cappuccino (EA11R) '91|16,500|
|Toyota|Celica GT-Four (ST205) '94|66,600|
|Volkswagen|Volkswagen 1200 '66|28,800|
