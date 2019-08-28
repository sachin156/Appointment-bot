# Appointment-bot



main folder for the process is bot and events.py is used for the add,fetch calendar events..

Pickle file is generate using below code...

from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
scopes=['https://www.googleapis.com/auth/calendar']

flow=InstalledAppFlow.from_client_secrets_file("client_secret.json",scopes=scopes)
credentials=flow.run_console()
import pickle
pickle.dump(credentials,open('token.pkl','wb'))
