import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# The ID and range of a sample spreadsheet.
RANGE_NAME = 'List!A2:C'
SPREADSHEET_ID = '1m9e-T8gkLPmjGv4oJ342Dy6mkQ8c-fW-Lk3FwW5T8t4'

class SpreadsheetReader:
  creds = None
  spreadsheet_id = None

  def __init__(self, spreadsheet_id):
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    self.spreadsheet_id = spreadsheet_id

    if os.path.exists('token.json'):
        self.creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not self.creds or not self.creds.valid:
      if self.creds and self.creds.expired and self.creds.refresh_token:
        self.creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        self.creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open('token.json', 'w') as token:
        token.write(self.creds.to_json())

  def print_from_sheet(self):
    try:
      service = build('sheets', 'v4', credentials=self.creds)

      # Call the Sheets API
      sheet = service.spreadsheets()
      result = sheet.values().get(spreadsheetId=self.spreadsheet_id, range=RANGE_NAME).execute()
      values = result.get('values', [])

      if not values:
        print('No data found.')
        return

      print('Name, Major:')
      for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
      print(err)

spreadsheet_reader = SpreadsheetReader(SPREADSHEET_ID)