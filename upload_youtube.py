import os
import pickle

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

VIDEO_FILE = "output/short.mp4"


def get_credentials():

    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json",
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return creds


def upload_video(title, description):

    credentials = get_credentials()

    youtube = build(
        "youtube",
        "v3",
        credentials=credentials
    )

    request = youtube.videos().insert(
        part="snippet,status",

        body={

            "snippet": {

                "title": title,

                "description": description,

                "categoryId": "22"

            },

            "status": {

                "privacyStatus": "public",

                "selfDeclaredMadeForKids": False

            }

        },

        media_body=MediaFileUpload(
            VIDEO_FILE,
            resumable=True
        )

    )

    response = request.execute()

    print("Upload Successful!")

    print("Video ID:", response["id"])