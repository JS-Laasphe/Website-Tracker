# Dieses Programm ermöglicht das Überwachen von Änderungen an einem bestimmten HTML-Element auf einer Webseite.
# Gibt es eine Änderung, wird eine Nachricht per Telegram versendet.
# file_info.txt wird beim erstmaligen Ausführen mit Inhalt gefüllt. Bei der nächsten Ausführung wird der Inhalt
# des HTML-Elements mit dem Inhalt der txt-Datei verglichen.

import requests
from bs4 import BeautifulSoup

url = "<hier url einfügen>"
element_id = "<hier id des div-elements einfügen, z.B. MainArea>"


def save_element_info():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    element = soup.find("div", {"id": element_id})
    element_content = str(element)
    with open("//NAS/Testumgebung/file_info.txt", "w") as f:
        f.write(element_content)


def check_element_change():
    with open("//NAS/Testumgebung/file_info.txt", "r") as f:
        old_element_content = f.read()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    element = soup.find("div", {"id": element_id})
    current_element_content = str(element)
    if current_element_content != old_element_content:
        send_notification()
        with open("//NAS/Testumgebung/file_info.txt", "w") as f:
            f.write(current_element_content)


def send_notification():
    url = "https://api.telegram.org/bot<hier TOKEN einfügen>/sendMessage"
    chat_id = "<hier CHAT_ID einfügen>"
    message = "Bei deinem Lieblingsblog ist ein neuer Artikel aufgetaucht. Jetzt nachsehen auf: <hier url einfügen>"
    payload = {"chat_id": chat_id, "text": message}
    requests.post(url, data=payload)


check_element_change()
