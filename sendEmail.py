from google import Create_Service 
import base64
from email.mime.multipart import MIMEMUltipart
from email.mime.ttext import MIMEText

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME,API_VERSION,SCOPES)
