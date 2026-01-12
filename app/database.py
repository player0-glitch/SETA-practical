#SQLAlchemy enigne and session
import urllib
from sqlalchemy import create_engine
from app.config import appSettings


base_params=urllib.parse.quote_plus( f"DRIVER={appSettings.db_driver};"
             f"SERVER={appSettings.db_server},{appSettings.db_port};"
             f"DATABASE={appSettings.db_name};"
             f"Encrypt={appSettings.db_encrypt};"
             f"TrustServerCertificate={appSettings.db_trust_cert};"
             f"MultipleActiveResultSets={appSettings.db_mars};"
             f"Application Name={appSettings.db_app_name};"
             )

#Different settings for different OS
if appSettings.db_auth=="Windows":
    auth="Trusted_Connection=yes;"
else:
    auth=f"UID={appSettings.db_user};PWD={appSettings.db_password};"

params=urllib.parse.quote_plus(base_params+auth)
DATABASE_URL=f"mssql+pyodbc:///?odbc_connect={params}"

#Start db engine
engine=create_engine(DATABASE_URL,pool_pre_ping=True)
