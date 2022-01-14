import secrets
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SETTINGS = dict(
        template_path=BASE_DIR / 'templates',
        static_path=BASE_DIR / 'static',
        cookie_secret=secrets.token_bytes(),
        )

