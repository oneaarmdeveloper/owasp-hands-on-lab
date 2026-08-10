
#Loads secrets from environment variables instead of hardcoding them.

import os
from dotenv import load_dotenv

load_dotenv()


# SECURE : load directly from environmental  variable
DB_PASSWORD = os.environ.get("DB_PASSWORD")
STRIPE_KEY  = os.environ.get("STRIPE_API_KEY")

if not DB_PASSWORD:
    raise SystemExit("FATAL: DB_PASSWORD is missing from environment!")

print("Config loaded securely!")
print(f"DB password length : {len(DB_PASSWORD)} characters")
print(f"Stripe key prefix  : {STRIPE_KEY[:7]}...")

