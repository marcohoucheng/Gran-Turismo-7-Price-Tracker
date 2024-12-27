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


# Gran Turismo 7 Shops for 27-December-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Lamborghini|Miura P400 Bertone Prototype '67|4,300,000|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Jaguar|XJR-9 '88|3,000,000|
|Mazda|787B '91|3,300,000|
|Mercedes-Benz|Sauber Mercedes C9 '89|3,500,000|
|Nissan|R92CP '92|2,000,000|
|Porsche|962 C '88|1,300,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Aston Martin|DB5 '64|892,000|
|Chevrolet|Corvette Stingray Racer Concept '59|4,000,000|
|Ferrari|F50 '95|4,450,000|
|Ferrari|GTO '84|3,500,000|
|Ford|GT40 Mark I '66|6,700,000|
|McLaren|McLaren F1 '94|20,000,000|
|Mercedes-Benz|300 SL (W194) '52|20,000,000|
|NISMO|400R '95|1,600,000|
|Plymouth|Superbird '70|402,000|


## Used shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|DMC|DeLorean S2 '04|458,900|
|Honda|Civic SiR-II (EG) '93|50,800|

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|58,200|
|Autobianchi|A112 Abarth '85|29,800|
|Chevrolet|Corvette ZR-1 (C4) '89|90,600|
|Ferrari|Dino 246 GT '71|333,900|
|Lamborghini|Gallardo LP 560-4 '08|249,200|
|Lancia|Stratos '73|499,300|
|Porsche|911 GT3 (997) '09|137,000|
|Renault|R5 Turbo '80|151,900|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|R8 4.2 '07|137,100|
|BMW|3.0 CSL '71|140,400|
|BMW|M3 '97|90,000|
|Dodge|Super Bee '70|63,200|
|Ferrari|512 BB '76|288,600|
|Honda|NSX Type R '92|402,700|
|Honda|S800 '66|48,700|
|Lamborghini|Murcielago LP 640 '09|340,400|
|Lancia|Delta HF Integrale Evoluzione '91|98,900|
|Mazda|RX-7 GT-X (FC) '90|58,900|
|Mitsubishi|Lancer Evolution VI GSR T.M. SCP '99|162,400|
|Nissan|180SX Type X '96|58,400|
|Nissan|Fairlady 240ZG (HS30) '71|106,400|
|Nissan|Fairlady Z (Z34) '08|33,000|
|Nissan|SILVIA spec-R Aero (S15) '02|62,000|
|Nissan|Sileighty '98|89,700|
|Nissan|Silvia K's Aero (S14) '96|60,000|
|Nissan|Silvia K's Dia Selection (S13) '90|65,000|
|Nissan|Silvia K's Type S (S14) '94|60,000|
|Porsche|911 Carrera RS CS (993) '95|438,500|
|Porsche|911 GT3 (996) '01|155,600|
|Suzuki|Cappuccino (EA11R) '91|16,000|
|Toyota|Celica GT-Four (ST205) '94|67,700|
|Volvo|240 SE Estate '93|50,000|
