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


# Gran Turismo 7 Shops for 04-May-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|892,000|
|Chevrolet|Camaro Z28 '69|128,000|
|Chevrolet|Chevelle SS 454 Sport Coupé '70|162,000|
|Ferrari|250 GT Berlinetta passo corto '61|7,800,000|
|Toyota|GT-One (TS020) '99|2,500,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Maserati|A6GCS/53 Spyder '54|3,000,000|
|Maserati|Merak SS '80|64,200|
|McLaren|MP4/4 '88|12,000,000|
|Mercedes-Benz|W 196 R '55|20,000,000|
|Nissan|Skyline Super Silhouette Group 5 '84|1,150,000|
|Porsche|Carrera GTS (904) '64|2,300,000|
|Toyota|Supra GT500 '97|1,800,000|


## Used shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TTS Coupe '09|56,300|
|BMW|M3 '07|70,500|
|Honda|Civic Type R (EK) '98|46,800|
|Nissan|Fairlady Z 300ZX TT 2seater '89|53,300|
|Nissan|Silvia K's Type S (S14) '94|48,800|
|Porsche|911 Turbo (930) '81|250,000|
|Porsche|911 Turbo (930) '81|250,000|
|Porsche|911 Turbo (930) '81|250,000|
|Toyota|Sprinter Trueno 1600GT APEX (AE86) '83|48,200|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|48,900|
|Autobianchi|A112 Abarth '85|29,300|
|BMW|3.0 CSL '71|140,900|
|BMW|M3 '03|69,300|
|BMW|M3 Sport Evolution '89|162,000|
|Chevrolet|Corvette Stingray (C3) '69|62,400|
|De Tomaso|Pantera '71|179,000|
|Dodge|Viper GTS '02|103,200|
|Ferrari|308 GTB '75|172,000|
|Ferrari|430 Scuderia '07|370,200|
|Ferrari|F430 '06|197,600|
|Fiat|500 F '68|18,800|
|Honda|Integra Type R (DC2) '95|58,900|
|Honda|NSX Type R '02|447,400|
|Lancia|Delta HF Integrale Evoluzione '91|105,000|
|Nissan|GT-R NISMO (R32) '90|396,100|
|Nissan|SILVIA spec-R Aero (S15) '02|58,700|
|Peugeot|205 GTI '88|59,300|
|Porsche|911 Carrera RS (964) '92|223,100|
|Toyota|MR2 GT-S '97|57,600|
|Volkswagen|Scirocco R '10|39,500|
