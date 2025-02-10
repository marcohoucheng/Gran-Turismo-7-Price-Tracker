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


# Gran Turismo 7 Shops for 10-February-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Maserati|A6GCS/53 Spyder '54|3,000,000|
|Mazda|RX500 '70|600,000|
|Mercedes-Benz|W 196 R '55|20,000,000|
|Toyota|Supra GT500 '97|1,800,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|800,000|
|Jaguar|XJ220 '92|554,000|
|Maserati|Merak SS '80|64,200|
|Mazda|787B '91|3,300,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Porsche|959 '87|1,950,000|
|Porsche|962 C '88|1,300,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '07|70,200|
|Honda|Integra Type R (DC2) '95|67,400|
|Nissan|GT-R NISMO (R32) '90|393,800|
|Porsche|911 Carrera RS (964) '92|220,000|
|Toyota|MR2 GT-S '97|52,600|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|512 BB '76|288,600|
|Ford|Ford GT '06|397,100|
|Nissan|Fairlady Z Version S (Z33) '07|30,800|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|47,400|
|Toyota|Supra RZ '97|194,000|
|Volkswagen|Sambabus Typ 2 '62|63,500|
|Volvo|240 SE Estate '93|48,700|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|44,100|
|BMW|M3 '89|76,900|
|Chevrolet|Corvette Stingray (C3) '69|51,700|
|Daihatsu|Copen '02|13,300|
|Ferrari|F430 '06|207,400|
|Fiat|500 1.2 8V Lounge SS '08|13,800|
|Honda|Civic Si Extra (EF) '87|61,600|
|Honda|Civic Type R (EK) '97|51,900|
|Nissan|Fairlady Z 300ZX TT 2seater '89|55,300|
|Renault|Clio V6 24V '00|89,700|
|Subaru|Impreza 22B-STi '98|174,200|
|TVR|Tuscan Speed 6 '00|70,100|
|Toyota|Sports 800 '65|51,400|
