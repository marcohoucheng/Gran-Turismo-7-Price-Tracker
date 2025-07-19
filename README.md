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


# Gran Turismo 7 Shops for 19-July-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|McLaren|MP4/4 '88|12,000,000|
|McLaren|McLaren F1 GTR - BMW '95|16,000,000|
|Mercedes-Benz|S Barker Tourer '29|13,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Charger R/T 426 Hemi '68|154,000|
|Jaguar|D-type '54|6,000,000|
|Jaguar|XJ13 '66|12,000,000|
|Mercedes-Benz|300 SL Coupe '54|1,700,000|
|Nissan|Fairlady Z 432 '69|312,000|
|Nissan|GT-R GT500 '99|2,200,000|
|Shelby|Cobra Daytona Coupe '64|20,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|47,400|
|Suzuki|Cappuccino (EA11R) '91|16,500|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ford|Escort RS Cosworth '92|129,800|
|Lamborghini|Murcielago LP 640 '09|329,700|
|Lancia|Delta HF Integrale Evoluzione '91|107,800|
|Nissan|Sileighty '98|76,500|
|Nissan|Silvia K's Type S (S14) '94|44,900|
|TVR|Tuscan Speed 6 '00|95,000|
|Toyota|Celica GT-Four (ST205) '94|72,300|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|47,000|
|BMW|3.0 CSL '71|148,000|
|DMC|DeLorean S2 '04|429,600|
|Dodge|Viper GTS '02|102,800|
|Ferrari|512 BB '76|313,400|
|Fiat|500 F '68|16,000|
|Ford|Ford GT '06|395,200|
|Honda|Civic SiR-II (EG) '93|56,000|
|Lancia|Stratos '73|534,900|
|MINI|MINI Cooper S '05|22,300|
|Nissan|180SX Type X '96|53,800|
|Nissan|Fairlady Z (Z34) '08|32,900|
|Nissan|Fairlady Z Version S (Z33) '07|31,000|
|Peugeot|205 GTI '88|54,700|
|Renault|Clio V6 24V '00|75,200|
|Toyota|Supra RZ '97|190,800|
|Volkswagen|Volkswagen 1200 '66|35,900|
