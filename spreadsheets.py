import os

import gspread
from dotenv import load_dotenv
load_dotenv()

SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
LIST_NAME = os.getenv('SPREADSHEET_LIST_NAME')

class SpreadsheetManager:

  worksheet = None

  def __init__(self, spreadsheet_id, worksheet_name):
    service_account = gspread.service_account(filename='credentials.json')
    spreadsheet = service_account.open_by_key(spreadsheet_id)
    self.worksheet = spreadsheet.worksheet(worksheet_name)

  def append_row(self, data):
    self.worksheet.append_row(data)

spreadsheet_manager = SpreadsheetManager(SPREADSHEET_ID, LIST_NAME)