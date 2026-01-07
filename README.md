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


# Gran Turismo 7 Shops for 07-January-2026



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Charger R/T 426 Hemi '68|147,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|300,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Ferrari|F40 '92|3,200,000|
|Honda|NSX GT500 '00|1,650,000|
|Honda|RA272 '65|2,500,000|
|McLaren|MP4/4 '88|12,000,000|
|McLaren|McLaren F1 GTR - BMW '95|17,000,000|
|Mercedes-Benz|300 SL Coupe '54|1,650,000|
|Mercedes-Benz|S Barker Tourer '29|13,000,000|
|Porsche|917K '70|20,000,000|
|Porsche|Spyder type 550/1500RS '55|4,950,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|BMW|M3 '07|77,600|
|Dodge|Viper GTS '02|106,600|
|Renault|Clio V6 24V '00|82,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|43,300|
|Honda|Civic Si Extra (EF) '87|50,700|
|Honda|S800 '66|52,000|
|Nissan|Fairlady Z (Z34) '08|37,100|
|Renault|R4 GTL '85|25,500|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 500 '09|26,400|
|Audi|TTS Coupe '09|58,300|
|BMW|M3 '97|90,000|
|De Tomaso|Pantera '71|166,500|
|Ferrari|430 Scuderia '07|378,100|
|Ford|Ford GT '06|397,100|
|Honda|Beat '91|14,900|
|Honda|NSX Type R '02|432,900|
|MINI|MINI Cooper S '05|23,600|
|Mazda|Eunos Roadster (NA) '89|30,500|
|Nissan|180SX Type X '96|57,400|
|Nissan|Fairlady Z 300ZX TT 2seater '89|56,200|
|Nissan|GT-R NISMO (R32) '90|400,000|
|Toyota|Corolla Levin 1600GT APEX (AE86) '83|50,700|
|Toyota|Sports 800 '65|49,200|
|Toyota|Supra RZ '97|181,700|
|Volvo|240 SE Estate '93|41,400|
