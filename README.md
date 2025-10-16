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


# Gran Turismo 7 Shops for 16-October-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Jaguar|D-type '54|6,000,000|
|Jaguar|XJ13 '66|12,000,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Charger R/T 426 Hemi '68|147,000|
|Mercedes-Benz|300 SL Coupe '54|1,650,000|
|NISMO|400R '95|1,600,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|537,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|982,000|
|Ferrari|250 GT Berlinetta passo corto '61|6,850,000|
|Nissan|Fairlady Z 432 '69|312,000|
|Nissan|GT-R GT500 '99|2,000,000|
|Shelby|Cobra 427 '66|2,700,000|
|Shelby|Cobra Daytona Coupe '64|20,000,000|
|Toyota|Land Cruiser FJ40V '74|44,100|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '03|61,100|
|Nissan|SILVIA spec-R Aero (S15) '02|58,600|
|Toyota|Supra 3.0GT Turbo A '88|130,000|
|Toyota|Supra RZ '97|220,000|
|Toyota|Supra RZ '97|220,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TTS Coupe '09|58,300|
|De Tomaso|Pantera '71|166,500|
|Honda|NSX Type R '02|432,900|
|Nissan|180SX Type X '96|57,400|
|Nissan|GT-R NISMO (R32) '90|400,000|
|Nissan|R32 GT-R V-spec II '94|200,000|
|Nissan|R33 GT-R V-spec '97|180,000|
|Nissan|Silvia Q's (S13) '88|31,500|
|Renault|Kangoo 1.4 '01|14,200|
|Renault|R5 Turbo '80|161,400|
|Toyota|Prius G '09|19,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|Giulia Sprint GT Veloce '67|180,000|
|BMW|M3 '07|77,600|
|Dodge|Viper GTS '02|106,600|
|Ferrari|430 Scuderia '07|378,100|
|Honda|Beat '91|14,900|
|Honda|Civic Si Extra (EF) '87|50,700|
|Honda|Integra Type R (DC2) '95|58,800|
|Honda|S800 '66|52,000|
|MINI|MINI Cooper S '05|23,600|
|Nissan|Fairlady Z 300ZX TT 2seater '89|56,200|
|Porsche|911 Carrera RS (964) '92|207,000|
|Porsche|911 Turbo (930) '81|250,000|
|Renault|Clio V6 24V '00|82,800|
|Renault|R4 GTL '85|25,500|
|Toyota|MR2 GT-S '97|51,500|
|Volkswagen|Sambabus Typ 2 '62|63,000|
