import os
import argparse
from dotenv import load_dotenv

load_dotenv()

db_string_dev = os.getenv('DB_STRING_DEV')
db_string_test = os.getenv('DB_STRING_TEST')
db_string_local = os.getenv('DB_STRING_LOCAL')

migration_command = f"migra --unsafe --schema sr {db_string_dev} {db_string_local} > sr_main-migra-sr.sql"
print(migration_command)
os.system(migration_command)
