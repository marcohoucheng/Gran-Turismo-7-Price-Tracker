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


# Gran Turismo 7 Shops for 12-January-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|982,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|McLaren|McLaren F1 GTR - BMW '95|17,000,000|
|Mercedes-Benz|S Barker Tourer '29|13,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Charger R/T 426 Hemi '68|147,000|
|Ferrari|250 GT Berlinetta passo corto '61|6,850,000|
|Mercedes-Benz|300 SL Coupe '54|1,650,000|
|Nissan|Fairlady Z 432 '69|312,000|
|Nissan|GT-R GT500 '99|2,000,000|
|Shelby|Cobra Daytona Coupe '64|20,000,000|


## Used shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|26,400|
|Ford|Ford GT '06|397,100|
|MINI|MINI Cooper S '05|23,600|
|Toyota|Supra RZ '97|181,700|
|Volvo|240 SE Estate '93|41,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|129,600|
|Audi|TTS Coupe '09|58,300|
|BMW|M3 '03|61,100|
|BMW|M3 '07|77,600|
|BMW|M3 '89|75,100|
|Chevrolet|Corvette Stingray (C3) '69|58,600|
|Daihatsu|Copen '02|14,400|
|Dodge|Viper GTS '02|106,600|
|Ferrari|430 Scuderia '07|378,100|
|Fiat|500 1.2 8V Lounge SS '08|13,000|
|Ford|Sierra RS 500 Cosworth '87|196,400|
|Honda|Civic Type R (EK) '97|53,500|
|Honda|Integra Type R (DC2) '95|58,800|
|Honda|NSX Type R '02|432,900|
|MINI|Mini-Cooper 'S' '65|38,100|
|Nissan|Fairlady Z 300ZX TT 2seater '89|56,200|
|Nissan|SILVIA spec-R Aero (S15) '02|58,600|
|Porsche|911 Carrera RS (964) '92|207,000|
|Renault|Clio V6 24V '00|82,800|
|Subaru|Impreza 22B-STi '98|163,100|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|50,700|
|Toyota|MR2 GT-S '97|51,500|
|Toyota|Sports 800 '65|49,200|
