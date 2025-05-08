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


# Gran Turismo 7 Shops for 08-May-2025



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Jaguar|XJ220 '92|554,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Maserati|A6GCS/53 Spyder '54|3,000,000|
|Maserati|Merak SS '80|64,200|
|Mercedes-Benz|W 196 R '55|20,000,000|
|Porsche|Carrera GTS (904) '64|2,300,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|155 2.5 V6 TI '93|800,000|
|Mazda|RX500 '70|600,000|
|McLaren|McLaren F1 '94|20,000,000|
|Porsche|959 '87|1,950,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Honda|Civic Si Extra (EF) '87|70,000|
|Honda|Civic SiR-II (EG) '93|60,000|
|Honda|Civic Type R (EK) '97|65,000|
|Honda|Civic Type R (EK) '98|65,000|
|Honda|Civic Type R (EK) Touring Car|140,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|48,900|
|De Tomaso|Pantera '71|179,000|
|Ferrari|F430 '06|197,600|
|Fiat|500 F '68|18,800|
|Honda|NSX Type R '02|447,400|
|Nissan|GT-R NISMO (R32) '90|396,100|
|Porsche|911 Carrera RS (964) '92|223,100|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|MiTo '09|22,000|
|BMW|3.0 CSL '71|140,900|
|BMW|M3 '03|69,300|
|BMW|M3 '89|100,000|
|BMW|M3 Sport Evolution '89|162,000|
|Ferrari|308 GTB '75|172,000|
|Ferrari|430 Scuderia '07|370,200|
|Ford|Sierra RS 500 Cosworth '87|190,600|
|Honda|Integra Type R (DC2) '95|58,900|
|Lancia|Delta HF Integrale Evoluzione '91|105,000|
|Mitsubishi|Lancer Evolution III GSR '95|92,200|
|Mitsubishi|Lancer Evolution IX MR GSR '06|97,900|
|Nissan|Fairlady 240ZG (HS30) '71|106,400|
|Nissan|R33 GT-R V-spec '97|155,200|
|Nissan|SILVIA spec-R Aero (S15) '02|58,700|
|Peugeot|205 GTI '88|59,300|
|Suzuki|Cappuccino (EA11R) '91|17,700|
|TVR|Tuscan Speed 6 '00|71,700|
|Volkswagen|Scirocco R '10|39,500|
