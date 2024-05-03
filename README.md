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


# Gran Turismo 7 Shops for 03-May-2024



## Legend shop

### New
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Charger R/T 426 Hemi '68|158,000|
|Lamborghini|Countach LP400 '74|1,250,000|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Chevrolet|Chevelle SS 454 Sport Coupé '70|163,000|
|Ferrari|365 GTB4 '71|640,000|
|Jaguar|D-type '54|6,000,000|
|Jaguar|XJ13 '66|12,000,000|
|McLaren|McLaren F1 GTR - BMW '95|15,000,000|
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|300,000|
|Mercedes-Benz|300 SL Coupe '54|1,700,000|
|Mercedes-Benz|S Barker Tourer '29|13,000,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|167,000|


## Used shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|45,400|
|BMW|M3 '89|75,700|
|Daihatsu|Copen '02|13,000|
|Fiat|500 F '68|17,800|
|Honda|Civic Type R (EK) '97|65,000|
|Honda|Civic Type R (EK) '98|65,000|
|Honda|Civic Type R (EK) Touring Car|140,000|
|Renault|Clio V6 24V '00|82,300|
|Toyota|Sports 800 '65|48,100|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Alfa Romeo|8C Competizione '08|287,200|
|Alfa Romeo|Giulia Sprint GT Veloce '67|167,300|
|Alfa Romeo|MiTo '09|22,400|
|Alpine|A110 '72|137,500|
|Audi|R8 4.2 '07|137,600|
|Chevrolet|Corvette Stingray (C3) '69|51,500|
|Chevrolet|Corvette ZR-1 (C4) '89|86,100|
|Chevrolet|Corvette ZR1 (C6) '09|98,400|
|De Tomaso|Pantera '71|162,200|
|Ferrari|Testarossa '91|450,000|
|Honda|Integra Type R (DC2) '95|61,200|
|Honda|NSX Type R '02|431,600|
|Lamborghini|Diablo GT '00|789,300|
|MINI|Mini-Cooper 'S' '65|40,600|
|Mazda|RX-7 Spirit R Type A (FD) '02|214,300|
|Nissan|R33 GT-R V-spec '97|155,200|
|Nissan|SILVIA spec-R Aero (S15) '02|61,100|
|Subaru|Impreza 22B-STi '98|177,300|
|Toyota|MR2 GT-S '97|58,100|
|Toyota|Sprinter Trueno 1600GT APEX (S.Shigeno Version)|97,800|
|Volkswagen|Scirocco R '10|42,000|
