## README


# Name: FridgeExpire


## Description
Application for registering food with it`s expiry date and picture. 
Adding/Deleting food options and checking for duplicates in database. 
Table shows foods in order from the shortest to longest expity days left. 
Food that's going to expire soon will be marked with `red` color.

### screenshots:
Screenshots available for better presentation in `screenshots` folder.


## Installation & Requirements
```
Python 3.7, Flask 1.1, WTForms, pillow, sqlalchemy, pyzbar
```
Written on Windows 10


## Usage
To run the app start `main.py` file and open `http://localhost:5000/` in your browser.

To add new product User can take one of two ways:
- take a `picture` of the barcode with the cellphone camera, 
- `type` barcode numbers into the field.

If barcode had been previousply uploaded do database, then product's details will appear in fields 
and there will be only `expiry date` to be added to it.

Main table presents all foods user uploaded in order of days left due to expiry.
Food can be deleted with a `Delete` button.
If `days` are colored `red` then it means food is to be expired in less than 5 days.
After expiry date days will be on minus values.


## Support
Created by paulina.wojno@gmail.com - you can contact me for questions :)


## Authors and acknowledgment
paulina.wojno@gmail.com


## Project status
May be developed further, but in Django framework ;)
