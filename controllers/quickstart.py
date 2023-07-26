from __future__ import print_function
import os.path
import base64
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ['https://www.googleapis.com/auth/gmail.modify']



def extract_links(text):
    pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.findall(pattern, text)


def extract_links_data(link):
    pattern = r'/users/password-reset/(?P<uidb64>[^/]+)/(?P<token>[^/]+)/'
    match = re.search(pattern, link)
    if match:
        uidb64 = match.group('uidb64')
        token = match.group('token')
        return uidb64, token
    else:
        return None, None


def get_credentials():
    creds = None
    # Check if the token file exists
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds


def process_messages():
    uidb64_token_pairs = []

    # Get credentials
    creds = get_credentials()

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        query = 'is:unread from:feedabaza@gmail.com'
        messages = service.users().messages().list(userId='me', q=query).execute()

        if 'messages' not in messages:
            print('No unread messages from "feedabaza@gmail.com".')
            return uidb64_token_pairs

        unread_messages = messages['messages']

        for message in unread_messages:
            message_id = message['id']

            full_message = service.users().messages().get(userId='me', id=message_id, format='full').execute()

            if 'payload' in full_message and 'parts' in full_message['payload']:
                parts = full_message['payload']['parts']
                for part in parts:
                    part_data = part['body']['data']
                    part_data_decoded = base64.urlsafe_b64decode(part_data.encode('ASCII')).decode('utf-8')

                    if part['mimeType'] == 'text/plain':
                        links = extract_links(part_data_decoded)
                        for link in links:
                            uidb64, token = extract_links_data(link)
                            if uidb64 and token:
                                uidb64_token_pairs.append((uidb64, token))

            else:
                part_data = full_message['payload']['body']['data']
                part_data_decoded = base64.urlsafe_b64decode(part_data.encode('ASCII')).decode('utf-8')

                if full_message['payload']['mimeType'] == 'text/plain':
                    links = extract_links(part_data_decoded)
                    for link in links:
                        uidb64, token = extract_links_data(link)
                        if uidb64 and token:
                            uidb64_token_pairs.append((uidb64, token))


            service.users().messages().delete(userId='me', id=message_id).execute()

    except HttpError as error:
        print(f'An error occurred: {error}')

    return uidb64_token_pairs


def main():
    pairs = process_messages()
    for uidb64, token in pairs:
        print('UIDB64:', uidb64)
        print('Token:', token)
    print(pairs)


if __name__ == '__main__':
    main()


# Стара версія
# from __future__ import print_function
# import os.path
# import base64
# import re
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
#
# # If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
#
#
# def extract_links(text):
#     pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
#     return re.findall(pattern, text)
#
#
# def extract_links_data(link):
#     pattern = r'/users/password-reset/(?P<uidb64>[^/]+)/(?P<token>[^/]+)/'
#     match = re.search(pattern, link)
#     if match:
#         uidb64 = match.group('uidb64')
#         token = match.group('token')
#         return uidb64, token
#     else:
#         return None, None
#
#
# def get_link():
#     """Shows basic usage of the Gmail API.
#     Lists the user's Gmail labels.
#     """
#     uidb64_token_pairs = []  # Створюємо список для збереження пар 'uidb64' і 'token'
#
#     creds = None
#     # Ваші імпорти та інші частини функції залишаються без змін...
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#         # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())
#
#     try:
#         # Call the Gmail API
#         service = build('gmail', 'v1', credentials=creds)
#         query = 'is:unread from:feedabaza@gmail.com'
#         messages = service.users().messages().list(userId='me', q=query).execute()
#
#         if 'messages' not in messages:
#             print('No unread messages from "feedabaza@gmail.com".')
#             return uidb64_token_pairs  # Повертаємо порожній список, якщо немає повідомлень
#
#         unread_messages = messages['messages']
#         for message in unread_messages:
#             message_id = message['id']
#             full_message = service.users().messages().get(userId='me', id=message_id, format='full').execute()
#
#             if 'payload' in full_message and 'parts' in full_message['payload']:
#                 parts = full_message['payload']['parts']
#                 for part in parts:
#                     part_data = part['body']['data']
#                     part_data_decoded = base64.urlsafe_b64decode(part_data.encode('ASCII')).decode('utf-8')
#
#                     if part['mimeType'] == 'text/plain':
#                         links = extract_links(part_data_decoded)
#                         for link in links:
#                             uidb64, token = extract_links_data(link)
#                             if uidb64 and token:
#                                 uidb64_token_pairs.append((uidb64, token))  # Додаємо пару у список
#
#             else:
#                 part_data = full_message['payload']['body']['data']
#                 part_data_decoded = base64.urlsafe_b64decode(part_data.encode('ASCII')).decode('utf-8')
#
#                 if full_message['payload']['mimeType'] == 'text/plain':
#                     links = extract_links(part_data_decoded)
#                     for link in links:
#                         uidb64, token = extract_links_data(link)
#                         if uidb64 and token:
#                             uidb64_token_pairs.append((uidb64, token))  # Додаємо пару у список
#
#     except HttpError as error:
#         # Обробка помилок, як і раніше...
#         print(f'An error occurred: {error}')
#
#     return uidb64_token_pairs  # Повертаємо список пар 'uidb64' і 'token' після обробки всіх повідомлень
#
#
# def main():
#     pairs = get_link()  # Викликаємо функцію та отримуємо список пар 'uidb64' і 'token'
#     for uidb64, token in pairs:
#         print('UIDB64:', uidb64)
#         print('Token:', token)
#     print(pairs)
#
#
# if __name__ == '__main__':
#     main()