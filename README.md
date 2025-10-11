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


# Gran Turismo 7 Shops for 11-October-2025



## Legend shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Mercedes-Benz|190 E 2.5-16 Evolution II '91|300,000|
|Porsche|911 GT1 Strassenversion '97|10,000,000|
|Toyota|Land Cruiser FJ40V '74|44,100|
|Toyota|Land Cruiser FJ40V '74|44,100|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Dodge|Charger R/T 426 Hemi '68|147,000|
|Ferrari|250 GT Berlinetta passo corto '61|6,850,000|
|Honda|NSX GT500 '00|1,650,000|
|McLaren|McLaren F1 GTR - BMW '95|17,000,000|
|Mercedes-Benz|300 SL Coupe '54|1,650,000|
|Mercedes-Benz|S Barker Tourer '29|13,000,000|
|NISMO|400R '95|1,600,000|
|Nissan|Skyline 2000GT-R (KPGC110) '73|537,000|
|Nissan|Skyline Hard Top 2000GT-R (KPGC10) '70|194,000|
|Porsche|Spyder type 550/1500RS '55|4,950,000|


## Used shop

### Leaving Soon
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Abarth|Abarth 595 SS '70|53,100|
|Alfa Romeo|MiTo '09|22,700|
|BMW|3.0 CSL '71|141,800|
|BMW|3.0 CSL '73|205,200|
|Ferrari|Dino 246 GT '71|400,000|
|Ferrari|Dino 246 GT '71|400,000|
|Lancia|Stratos '73|539,800|
|Toyota|Celica GT-Four (ST205) '94|65,500|

### Available
 | Manufacturer | Model | Credits |
 | --- | --- | --: |
|Audi|TT Coupe 3.2 quattro '03|43,300|
|Audi|TTS Coupe '09|58,300|
|BMW|M3 '07|77,600|
|Citroen|BX 19 TRS '87|22,700|
|DMC|DeLorean S2 '04|462,400|
|De Tomaso|Pantera '71|166,500|
|Ferrari|308 GTB '75|176,100|
|Ferrari|430 Scuderia '07|378,100|
|Ferrari|512 BB '76|299,300|
|Ford|Ford GT '06|397,100|
|Honda|NSX Type R '02|432,900|
|MINI|MINI Cooper S '05|23,600|
|Nissan|180SX Type X '96|57,400|
|Nissan|Fairlady Z (Z34) '08|37,100|
|Nissan|Fairlady Z 300ZX TT 2seater '89|56,200|
|Nissan|Fairlady Z Version S (Z33) '07|26,800|
|Nissan|GT-R NISMO (R32) '90|400,000|
|Nissan|R32 GT-R V-spec II '94|200,000|
|Nissan|R33 GT-R V-spec '97|180,000|
|Nissan|Silvia Q's (S13) '88|31,500|
|Renault|Kangoo 1.4 '01|14,200|
|Renault|R5 Turbo '80|161,400|
|Toyota|Prius G '09|19,400|
