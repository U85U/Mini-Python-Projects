import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

try:
    user = sys.argv[1].strip()
except:
    sys.stderr.write("Eksik argüman girişi!")
    sys.stderr.flush()
    sys.exit()

if sys.argv[1] != "?":

    url = "https://github.com/" + user + "?tab=repositories"
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")

    mesaj = MIMEMultipart()

    mesaj["From"] = "89D5C9@gmail.com"
    mesaj["To"] = "utkuaraal1@gmail.com"
    mesaj["Subject"] = user + " kullanıcısına ait repo isimleri."
    yazi = ""

    for i in soup.find_all("a", {"itemprop": "name codeRepository"}):
        yazi += i.text + "\n"

    mesaj_govdesi = MIMEText(yazi, "plain")
    mesaj.attach(mesaj_govdesi)

    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login("89D5C9@gmail.com", "***")
        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        print("Mail Başarıyla Gönderildi.")
        mail.close()
    except:
        sys.stderr.write("Bir sorun oluştu!")
        sys.stderr.flush()
else:
    print("Bu uygulamayı kullanmak için argüman olarak github kullanıcı adı girmelisiniz.")


