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


# Gran Turismo 7 Shops for 08-June-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Pontiac|GTO 'The Judge' '69|242,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Ford|Mustang Boss 429 '69|294,000|
|Lamborghini|Miura P400 Bertone Prototype '67|4,300,000|
|Porsche|911 Carrera RS (901) '73|799,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C1) '58|107,000|
|Ferrari|250 GTO '62|20,000,000|
|Jaguar|XJ13 '66|12,000,000|
|Jaguar|XJR-9 '88|3,000,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|
|Toyota|2000GT '67|982,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|230,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|47,400|
|Audi|TTS Coupe '09|55,000|
|BMW|M3 '07|72,500|
|Honda|NSX Type R '02|440,400|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|139,200|
|Ferrari|512 BB '76|289,100|
|Lancia|Stratos '73|534,900|
|Nissan|Fairlady Z (Z34) '08|35,400|
|Nissan|Sileighty '98|76,500|
|Porsche|911 Carrera RS (993) '95|260,000|
|Porsche|911 Carrera RS (993) '95|260,000|
|Toyota|Celica GT-Four (ST205) '94|72,300|
|Toyota|Supra RZ '97|197,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|58,300|
|Autobianchi|A112 Abarth '85|29,800|
|DMC|DeLorean S2 '04|429,600|
|Dodge|Viper GTS '02|103,100|
|Fiat|500 F '68|18,300|
|Ford|Ford GT '06|408,700|
|Honda|Civic Si Extra (EF) '87|70,000|
|Honda|Civic SiR-II (EG) '93|60,000|
|Honda|Civic Type R (EK) '97|65,000|
|Honda|Civic Type R (EK) '98|65,000|
|Honda|Civic Type R (EK) Touring Car|140,000|
|Lancia|Delta HF Integrale Evoluzione '91|98,900|
|MINI|MINI Cooper S '05|22,300|
|Nissan|180SX Type X '96|53,800|
|Nissan|Fairlady Z Version S (Z33) '07|30,300|
|Nissan|Silvia K's Type S (S14) '94|46,800|
|Renault|Clio V6 24V '00|75,200|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|58,200|
