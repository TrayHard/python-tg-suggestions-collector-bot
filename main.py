import os

from bot import init_bot

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
  init_bot()

if __name__ == '__main__':
  main()
