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


# Gran Turismo 7 Shops for 31-May-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Jaguar|E-type Coupe '61|227,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|F40 '92|3,100,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C2) '63|249,000|
|Ferrari|500 Mondial Pinin Farina Coupe '54|2,700,000|
|Honda|NSX GT500 '00|1,500,000|
|Nissan|GT-R GT500 '99|2,500,000|
|Porsche|356 A/1500 GS Carrera '56|615,000|
|Porsche|959 '87|1,750,000|
|Porsche|962 C '88|1,500,000|
|Toyota|Supra GT500 '97|1,800,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|22,400|
|BMW|M3 '89|75,700|
|Ford|Ford GT '06|399,300|
|Nissan|GT-R NISMO (R32) '90|390,000|
|TVR|Tuscan Speed 6 '00|72,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|DMC|DeLorean S2 '04|451,600|
|Dodge|Viper GTS '02|105,600|
|Ferrari|512 BB '76|309,000|
|MINI|MINI Cooper S '05|21,900|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|168,100|
|Porsche|911 GT3 (996) '01|155,500|
|Renault|R4 GTL '85|24,100|
|Volkswagen|Golf I GTI '83|46,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|137,500|
|Audi|TT Coupe 3.2 quattro '03|45,400|
|Daihatsu|Copen '02|13,000|
|Ferrari|F430 '06|201,100|
|Honda|Beat '91|20,000|
|Honda|Civic SiR-II (EG) '93|52,100|
|MINI|Mini-Cooper 'S' '65|40,600|
|Mazda|RX-7 GT-X (FC) '90|61,100|
|Nissan|Fairlady Z 300ZX TT 2seater '89|62,300|
|Nissan|Fairlady Z Version S (Z33) '07|26,800|
|Nissan|Silvia K's Type S (S14) '94|53,900|
|Nissan|Skyline GTS-R (R31) '87|176,600|
|Renault|Clio V6 24V '00|82,300|
|Suzuki|Cappuccino (EA11R) '91|20,000|
|Suzuki|Swift Sport '07|12,200|
|Toyota|Sports 800 '65|48,100|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|48,900|
|Toyota|Supra RZ '97|192,300|
|Volvo|240 SE Estate '93|40,800|
