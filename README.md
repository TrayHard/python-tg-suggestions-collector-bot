# tg-bot-suggestions-gatherer
Very simple bot for Telegram that just gathers suggestions for posts and write it down into Google Spreadsheet.
Based on aiogram and gspread libraries.

## To launch
1. Install requirements.
2. Create `.env` file and copy content of `.env.example` there, then add your telegram bot key there
3. Generate `credentials.json` in Google Cloud console and put it into project root
4. In terminal: `python main.py`