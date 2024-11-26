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


# Gran Turismo 7 Shops for 26-November-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|RA272 '65|2,500,000|
|McLaren|McLaren F1 '94|20,000,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chaparral|2J '70|2,500,000|
|Chevrolet|Chevelle SS 454 Sport Coupé '70|162,000|
|Ferrari|330 P4 '67|20,000,000|
|Ferrari|500 Mondial Pinin Farina Coupe '54|2,600,000|
|Ferrari|F40 '92|3,100,000|
|Ferrari|F50 '95|4,450,000|
|Ford|1932 Ford Roadster Hot Rod|400,000|
|Jaguar|E-type Coupe '61|227,000|
|Jaguar|XJR-9 '88|3,000,000|
|Mazda|787B '91|3,300,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Mercedes-Benz|W 196 R '55|20,000,000|
|Nissan|R92CP '92|2,000,000|
|Porsche|917K '70|18,000,000|
|Porsche|962 C '88|1,300,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Corvette Stingray (C3) '69|54,700|
|Honda|Civic SiR-II (EG) '93|50,800|
|Honda|NSX Type R '92|450,000|
|Subaru|Impreza 22B-STi '98|178,300|
|Volkswagen|Volkswagen 1200 '66|28,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|58,200|
|Autobianchi|A112 Abarth '85|29,800|
|DMC|DeLorean S2 '04|458,900|
|Ford|Ford GT '06|397,100|
|Honda|S800 '66|48,700|
|Nissan|Fairlady Z Version S (Z33) '07|30,800|
|Renault|R5 Turbo '80|151,900|
|Suzuki|Cappuccino (EA11R) '91|16,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|43,300|
|Audi|TTS Coupe '09|67,600|
|BMW|3.0 CSL '71|140,400|
|BMW|M3 '07|70,200|
|BMW|M3 '89|86,100|
|Ferrari|430 Scuderia '07|363,500|
|Ferrari|F430 '06|207,400|
|Ford|Escort RS Cosworth '92|147,100|
|Lancia|Delta HF Integrale Evoluzione '91|98,900|
|Nissan|Fairlady 240ZG (HS30) '71|106,400|
|Nissan|Fairlady Z 300ZX TT 2seater '89|60,300|
|Nissan|GT-R NISMO (R32) '90|393,800|
|Porsche|911 Carrera RS (964) '92|220,000|
|Renault|Clio V6 24V '00|72,800|
|TVR|Tuscan Speed 6 '00|70,100|
