import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Legislators 2017 copy").sheet1

# list_of_hashes = sheet.get_all_records()
# list_of_hashes = sheet.row_values(2)
# print(list_of_hashes)

sheet.update_cell(2, 2, "I just wrote to a spreadsheet using Python!")
