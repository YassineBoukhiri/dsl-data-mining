# Rename `os.environ` to `env` for nicer code
from os import environ as env

from dotenv import load_dotenv
load_dotenv()

print('API_KEY:  {}'.format(env['APP_NAME1']))

# add variable to .env file
with open('.env', 'a') as f:
    f.write('\nAPP_NAME1=\"App Name 1\"')
