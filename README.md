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


# Gran Turismo 7 Shops for 20-October-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Lancia|Lancia Delta HF Integrale Rally Car '92|327,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|982,000|
|Jaguar|D-type '54|6,000,000|
|Jaguar|XJ13 '66|12,000,000|
|Lamborghini|Countach LP400 '74|1,250,000|
|Nissan|Skyline Super Silhouette Group 5 '84|1,150,000|
|Shelby|Cobra Daytona Coupe '64|20,000,000|
|Toyota|GT-One (TS020) '99|2,500,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mazda|RX-7 Spirit R Type A (FD) '02|216,400|
|Volkswagen|Scirocco R '10|38,100|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '07|77,600|
|Dodge|Viper GTS '02|106,600|
|Honda|Civic Si Extra (EF) '87|50,700|
|Honda|S800 '66|52,000|
|Nissan|Fairlady Z 300ZX TT 2seater '89|56,200|
|Renault|Clio V6 24V '00|82,800|
|Renault|R4 GTL '85|25,500|
|Toyota|MR2 GT-S '97|51,500|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|26,400|
|BMW|M3 '03|61,100|
|BMW|M3 '89|75,100|
|Chevrolet|Corvette Stingray (C3) '69|58,600|
|Ferrari|F430 '06|209,600|
|Ford|Sierra RS 500 Cosworth '87|196,400|
|Honda|Beat '91|14,900|
|Mazda|Eunos Roadster (NA) '89|30,500|
|Mercedes-Benz|SLR McLaren '09|512,200|
|Nissan|R33 GT-R V-spec '97|161,000|
|Nissan|SILVIA spec-R Aero (S15) '02|58,600|
|Porsche|911 Carrera RS (964) '92|207,000|
|Subaru|Impreza 22B-STi '98|163,100|
|TVR|Tuscan Speed 6 '00|75,900|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|50,700|
|Toyota|Sports 800 '65|49,200|
|Toyota|Supra 3.0GT Turbo A '88|130,000|
|Toyota|Supra RZ '97|220,000|
|Toyota|Supra RZ '97|220,000|
|Volvo|240 SE Estate '93|41,400|
