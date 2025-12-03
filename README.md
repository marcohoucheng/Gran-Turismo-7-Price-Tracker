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


# Gran Turismo 7 Shops for 03-December-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|AMG|300 SEL 6.8 AMG '71|700,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|McLaren F1 GTR Race Car '97|20,000,000|
|Suzuki|V6 Escudo Pikes Peak Special spec.98|1,700,000|
|Toyota|Celica GT-FOUR Rally Car (ST205) '95|210,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette (C1) '58|122,000|
|Ferrari|250 GTO '62|20,000,000|
|Honda|RA272 '65|2,500,000|
|Jaguar|XJR-9 '88|3,000,000|
|Pontiac|GTO 'The Judge' '69|209,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|
|Toyota|2000GT '67|982,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Daihatsu|Copen '02|14,400|
|Mercedes-Benz|SLR McLaren '09|512,200|
|Nissan|R33 GT-R V-spec '97|161,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|26,400|
|BMW|M3 '03|61,100|
|BMW|M3 '07|77,600|
|Chevrolet|Corvette Stingray (C3) '69|58,600|
|Dodge|Viper GTS '02|106,600|
|Nissan|Fairlady Z 300ZX TT 2seater '89|56,200|
|Nissan|SILVIA spec-R Aero (S15) '02|58,600|
|Porsche|911 Carrera RS (964) '92|207,000|
|Renault|Clio V6 24V '00|82,800|
|Volvo|240 SE Estate '93|41,400|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alpine|A110 '72|129,600|
|BMW|M3 '89|75,100|
|Ferrari|Dino 246 GT '71|400,000|
|Ferrari|F430 '06|209,600|
|Fiat|500 1.2 8V Lounge SS '08|13,000|
|Ford|Sierra RS 500 Cosworth '87|196,400|
|Honda|Civic Type R (EK) '97|53,500|
|MINI|Mini-Cooper 'S' '65|38,100|
|Nissan|GT-R NISMO (R32) '90|386,700|
|Subaru|Impreza 22B-STi '98|163,100|
|TVR|Tuscan Speed 6 '00|75,900|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|50,700|
|Toyota|Sports 800 '65|49,200|
|Volkswagen|Scirocco R '10|38,100|
