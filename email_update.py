# Script to simply return the available items in shops today.

import urllib.request, json, os, sys, ssl, datetime, smtplib, markdown, time
import pandas as pd
from email.message import EmailMessage

def main():

    def str_merge(shop_dataframe):
        nonlocal return_str, md_str
        for _, row in shop_dataframe.iterrows():
            md_str = md_str + "|" + row['manufacturer'] + "|" + row['name'] + "|" + str(row['credits']) + "|\n"
            return_str = return_str + "\n" + row['manufacturer'] + " " + row['name'] + " : " + str(row['credits']) + "cr."

    def today(shop, data, new_data_only):

        nonlocal return_str, md_str

        shop_data = pd.DataFrame.from_dict(data[shop]['cars'])

        shop_data = shop_data[shop_data['state'] != 'soldout']

        if new_data_only:
            shop_data = shop_data[shop_data['new']]
            if len(shop_data) == 0:
                md_str = md_str + "\nNo new items available in " + shop.capitalize() + " shop.\n"
                return_str = return_str + "\nNo new items available in " + shop.capitalize() + " shop.\n"
                return 0
        
        shop_data = shop_data.sort_values(by=['manufacturer', 'name'])

        shop_data['credits'] = shop_data['credits'].apply(lambda x: f'{x:,}')

        if len(shop_data) == 0:
            md_str = md_str + "\nNo items available in " + shop.capitalize() + " shop.\n"
            return_str = return_str + "\nNo items available in " + shop.capitalize() + " shop.\n"
            return 0

        new_shop_data = shop_data[shop_data['new']]
        limited_shop_data = shop_data[shop_data['state'] == 'limited']
        shop_data = shop_data[(~shop_data['new']) & (shop_data['state'] != 'limited')]

        md_str = md_str + "\n\n## " + shop.capitalize() + " shop\n"
        return_str = return_str + "\n\nAvailable in " + shop.capitalize() + " shop:\n"

        if len(new_shop_data) > 0:
            md_str = md_str + "\n### New\n | Manufacturer | Model | Credits |\n | --- | --- | --: |\n"
            return_str = return_str + "\nNew:\n"
            str_merge(new_shop_data)
        if len(limited_shop_data) > 0:
            md_str = md_str + "\n### Leaving Soon\n | Manufacturer | Model | Credits |\n | --- | --- | --: |\n"
            return_str = return_str + "\nLeaving Soon:\n"
            str_merge(limited_shop_data)
        if len(shop_data) > 0:
            md_str = md_str + "\n### Available\n | Manufacturer | Model | Credits |\n | --- | --- | --: |\n"
            return_str = return_str + "\nAvailable:\n" 
            str_merge(shop_data)

        # for _, row in shop_data.iterrows():
        #     if row['state'] == 'limited':
        #         md_str = md_str + "\n" + row['manufacturer'] + " " + row['name'] + " : " + str(row['credits']) + "cr. (Leaving Soon)\n"
        #         return_str = return_str + "\n" + row['manufacturer'] + " " + row['name'] + " : " + str(row['credits']) + "cr. (Leaving Soon)"
        #     elif row['new'] == 'True':
        #         md_str = md_str + "\n" + row['manufacturer'] + " " + row['name'] + " : " + str(row['credits']) + "cr. (New)\n"
        #         return_str = return_str + "\n" + row['manufacturer'] + " " + row['name'] + " : " + str(row['credits']) + "cr. (New)"
        #     else:
        #         md_str = md_str + "\n" + row['manufacturer'] + " " + row['name'] + " : "+ str(row['credits']) + "cr.\n"
        #         return_str = return_str + "\n" + row['manufacturer'] + " " + row['name'] + " : "+ str(row['credits']) + "cr."

    if len(sys.argv) == 1:
        new_data_only = False
    else:
        new_data_only = sys.argv[1] == 'new'
    
    url = urllib.request.urlopen("https://ddm999.github.io/gt7info/data.json")
    data = json.load(url)

    # Time stamp for latest data
    timestamp_date = data['updatetimestamp'][2:10]

    while datetime.datetime.utcnow().date() > datetime.datetime.strptime(timestamp_date, '%y-%m-%d').date():
        time.sleep(30*60)
        new_data = json.load(url)
        timestamp_date = data['updatetimestamp'][2:10]
    
    # Reformat the date
    timestamp_date = datetime.datetime.strptime(timestamp_date, '%y-%m-%d').strftime('%d-%B-%Y')

    # if datetime.datetime.strptime(timestamp_date, date_format).date() < datetime.date.today():
    #     print("\nToday's data is not available yet. The latest data is from", timestamp_date, "\n")
    # else:
    #     print("\nToday's data is available.\n")

    md_str = "# Gran Turismo 7 Shops for " + timestamp_date + "\n\n"

    return_str = "Gran Turismo 7 Shops for " + timestamp_date + "\n\n"

    today('legend', data, new_data_only)
    today('used', data, new_data_only)

    # Step 4: Load secrets from .env
    gmail_address = os.environ.get("GMAIL_ADDRESS")
    gmail_password = os.environ.get("GMAIL_PASSWORD")
    recipients = os.environ.get("RECIPIENTS")

    # Step 5: Create the email
    email = EmailMessage()

    # Subject line of the email
    email["Subject"] = "Gran Turismo 7 Daily Shops Update"
    # Sender of the email
    email["From"] = gmail_address

    # Add plaintext alternative as fallback option
    email.set_content(return_str)
    # Add HTML content to the email
    html = markdown.markdown(md_str, extensions=['tables'])
    email.add_alternative(html, subtype="html")
    
    # email.add_alternative(f"""\
    # <html>
    # <head></head>
    # <body>
    #     <p>Brought to you by <b>Manezki</b></p>
    # </body>
    # </html>
    # """, subtype="html")

    # Step 6: Send the email to the newsletter subscribers
    subscriber_email_addresses = json.loads(recipients)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as smtp_server:
        smtp_server.login(gmail_address, gmail_password)
        for subsciber_email_address in subscriber_email_addresses:
            # Set the recipient for the email
            email["To"] = subsciber_email_address
            smtp_server.send_message(email)
    
    # Specify the path to the existing markdown file
    input_filename = './data/README_baseline.md'

    # Specify the new content to be added
    extra_string = '\n\n' + md_str

    # Specify the filename for the new file to be saved in the root folder
    output_filename = 'README.md'

    # Read the existing markdown content
    with open(input_filename, 'r') as file:
        content = file.read()

    # Append the extra string to the content
    content += extra_string

    # Write the updated content to the new file in the root folder
    with open(output_filename, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    main()
