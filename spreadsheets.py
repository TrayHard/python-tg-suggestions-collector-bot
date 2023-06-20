import gspread

SPREADSHEET_ID = '1m9e-T8gkLPmjGv4oJ342Dy6mkQ8c-fW-Lk3FwW5T8t4'
LIST_NAME="List"

class SpreadsheetManager:

  worksheet = None

  def __init__(self, spreadsheet_id, worksheet_name):
    service_account = gspread.service_account(filename='credentials.json')
    spreadsheet = service_account.open_by_key(spreadsheet_id)
    self.worksheet = spreadsheet.worksheet(worksheet_name)

  def append_row(self, data):
    self.worksheet.append_row(data)

spreadsheet_manager = SpreadsheetManager(SPREADSHEET_ID, LIST_NAME)