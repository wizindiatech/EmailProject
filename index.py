import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "cp.smaket@gmail.com"
you = "hyperfeelings@gmail.com,confuzkid@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Leave Application."
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "https://www.smaketsolutions.com"
html = """\
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Application</title>
</head>
<style>
    * {
        margin: 0;
        padding: 0;
    }
    span{
        color: red;
    }
</style>

<body style="background-color: rgb(202, 175, 252);">
    <div class="first" style="padding: 10px 20px 10px 20px; font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif; font-style: oblique;">
        <div style=" align-items: center; justify-content: center; display: flex;">
            <h2 style="color: green; padding: 10px 10px 30px;">Leave Application</h2>
        </div>
        <div>
            <P>26th March 2023</P><br><br>

            <p style="color: green;">Barsharani Mohanty</p>
            <p style="color: green;">HR</p>
            <p>Smaket Solutions</p>
            <p>Bhubaneswar</p><br><br>

            <p>Sub : Grant of leave.</p><br><br>

            <p></p>Mam<br>
            <p>With due respect I am writing this application to request you for approving 4 days leave for my semester
                examination as will be held from 28th March to 11st April.<br><br></p>

            <p>I am sure that our team will manage the work in my absence. Kindly consider on it and grant me leave on
                <span>28</span> March, <span>03</span>, <span>06</span>, and <span>11</span> April.</p><br><br>

            <p>Thank You.</p>
            <p>Yours Sincerely,</p>
            <p style="color: red;">Chinmaya Pradhan.</p>
        </div>
</body>

</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('cp.smaket@gmail.com', 'pkyvowjnxmzrcbwk')
mail.sendmail(me, you.split(","), msg.as_string())
mail.quit()
print("Email Send Successfully..")



