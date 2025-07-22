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


# Gran Turismo 7 Shops for 22-July-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|909,000|
|Pontiac|GTO 'The Judge' '69|242,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Nissan|Fairlady Z 432 '69|312,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|250 GT Berlinetta passo corto '61|7,000,000|
|Jaguar|D-type '54|6,000,000|
|Jaguar|XJ13 '66|12,000,000|
|Lamborghini|Countach LP400 '74|1,350,000|
|Nissan|GT-R GT500 '99|2,200,000|
|Shelby|Cobra Daytona Coupe '64|20,000,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|Integra Type R (DC2) '95|55,600|
|Nissan|Fairlady 240ZG (HS30) '71|97,200|
|Pontiac|Firebird Trans Am '78|110,000|
|Porsche|911 Turbo (930) '81|250,000|
|Toyota|MR2 GT-S '97|51,100|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|47,000|
|Fiat|500 F '68|16,000|
|Honda|Civic SiR-II (EG) '93|56,000|
|Toyota|Supra RZ '97|190,800|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|23,300|
|Audi|TT Coupe 3.2 quattro '03|47,400|
|Audi|TTS Coupe '09|62,200|
|BMW|3.0 CSL '71|148,000|
|BMW|M3 '07|74,300|
|DMC|DeLorean S2 '04|429,600|
|Dodge|Viper GTS '02|102,800|
|Ferrari|308 GTB '75|165,100|
|Ferrari|430 Scuderia '07|375,600|
|Ferrari|512 BB '76|313,400|
|Ford|Ford GT '06|395,200|
|Honda|NSX Type R '02|435,000|
|MINI|MINI Cooper S '05|22,300|
|Nissan|180SX Type X '96|53,800|
|Nissan|Fairlady Z 300ZX TT 2seater '89|60,700|
|Nissan|Fairlady Z Version S (Z33) '07|31,000|
|Nissan|Silvia K's Dia Selection (S13) '90|49,500|
|Peugeot|205 GTI '88|54,700|
|Renault|Clio V6 24V '00|75,200|
|Suzuki|Cappuccino (EA11R) '91|16,500|
|Volkswagen|Volkswagen 1200 '66|35,900|
