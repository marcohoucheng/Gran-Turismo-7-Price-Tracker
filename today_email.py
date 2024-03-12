# Script to simply return the available items in shops today.

import urllib.request, json, os, sys, ssl, datetime, smtplib, markdown
import pandas as pd
from dotenv import load_dotenv
from email.message import EmailMessage


def main():

    def today(shop, data, new_data_only):

        nonlocal return_str, md_str

        shop_data = pd.DataFrame.from_dict(data[shop]['cars'])

        if new_data_only:
            shop_data = shop_data[shop_data['new'] == 'True']
        
        shop_data = shop_data.sort_values(by=['manufacturer', 'name'])

        if len(shop_data) == 0:
            md_str = md_str + "\nNo new items available in " + shop + " shop.\n"
            return_str = return_str + "\nNo new items available in " + shop + " shop.\n"
            return 0

        md_str = md_str + "\n\n## " + shop + " shop:\n"
        return_str = return_str + "\n\nAvailable in " + shop + " shop:\n"

        for _, row in shop_data.iterrows():
            if row['state'] == 'soldout':
                continue
            elif row['state'] == 'limited':
                md_str = md_str + "\n" + row['manufacturer'] + " " + row['name'] + " : " + str(row['credits']) + "cr. (Leaving Soon)"
                return_str = return_str + "\n" + row['manufacturer'] + " " + row['name'] + " : " + str(row['credits']) + "cr. (Leaving Soon)"
            elif row['new'] == 'True':
                md_str = md_str + "\n" + row['manufacturer'] + " " + row['name'] + " : " + str(row['credits']) + "cr. (New)"
                return_str = return_str + "\n" + row['manufacturer'] + " " + row['name'] + " : " + str(row['credits']) + "cr. (New)"
            else:
                md_str = md_str + "\n" + row['manufacturer'] + " " + row['name'] + " : "+ str(row['credits']) + "cr."
                return_str = return_str + "\n" + row['manufacturer'] + " " + row['name'] + " : "+ str(row['credits']) + "cr."

    if len(sys.argv) == 1:
        new_data_only = False
    else:
        new_data_only = sys.argv[1] == 'new'
    
    # date_format = '%y-%m-%d'

    url = urllib.request.urlopen("https://ddm999.github.io/gt7info/data.json")
    data = json.load(url)

    # Time stamp for latest data
    timestamp_date = data['updatetimestamp'][2:10]

    # if datetime.datetime.strptime(timestamp_date, date_format).date() < datetime.date.today():
    #     print("\nToday's data is not available yet. The latest data is from", timestamp_date, "\n")
    # else:
    #     print("\nToday's data is available.\n")

    md_str = "# Gran Turismo 7 shops for " + timestamp_date + "\n\n"

    return_str = "Gran Turismo 7 shops for " + timestamp_date + "\n\n"

    today('legend', data, new_data_only)
    today('used', data, new_data_only)

    # Step 4: Load secrets from .env
    gmail_address = os.environ.get("GMAIL_ADDRESS")
    gmail_password = os.environ.get("GMAIL_PASSWORD")
    recipients = os.environ.get("RECIPIENTS")

    # Step 5: Create the email
    email = EmailMessage()

    # Subject line of the email
    email["Subject"] = "Gran Turismo 7 shops update"
    # Sender of the email
    email["From"] = gmail_address

    email.set_content(return_str)
    # Add HTML content to the email
    html = markdown.markdown(md_str)
    email.add_alternative(html, subtype="html")
    
    # email.add_alternative(f"""\
    # <html>
    # <head></head>
    # <body>
    #     <p>Brought to you by <b>Manezki</b></p>
    # </body>
    # </html>
    # """, subtype="html")

    # Add plaintext alternative as fallback option
    # email.set_content(return_str)

    # Step 6: Send the email to the newsletter subscribers
    subscriber_email_addresses = json.loads(recipients)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as smtp_server:
        smtp_server.login(gmail_address, gmail_password)
        for subsciber_email_address in subscriber_email_addresses:
            # Set the recipient for the email
            email["To"] = subsciber_email_address
            smtp_server.send_message(email)

if __name__ == "__main__":
    main()

    # pip3 install python-dotenv
