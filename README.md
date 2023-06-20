# python-tg-suggestions-collector-bot
Very simple bot for Telegram that just gathers suggestions for posts and write it down into Google Spreadsheet.
Based on aiogram and gspread libraries.

## To launch
1. Install requirements.
2. Create service account in Google Cloud console, get `credentials.json` of that account and put it into project root.
3. Create `.env` file and copy content of `.env.example` there, then add there:
  * your telegram bot key
  * your google spreadsheet document id (don't forget to share permissions with your service account email)
  * list name where this bot should write lines to
4. In terminal: `python main.py`