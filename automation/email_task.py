import argparse
import configparser
import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename


def send_email(
    recipients: list, server: str, port: str, from_email: str, password: str
):
    """
        Send an email given...
        recipients (outbound email(s))
        server (smtp server)
        port (smtp server port)
        from_email (Sending email)
        password (password as a string)
    """
    recipients = ",".join(recipients)
    print(f"Sending mail from {from_email} to {recipients}")

    # The message content
    subject = "With love, from ME to YOU"
    text = """This is an example test"""
    msg = EmailMessage()
    msg.set_content(text)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = recipients

    # Open communication and send the email
    server = smtplib.SMTP_SSL(server, int(port))
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()


def send_email_with_attachment(
    recipients: list, server: str, port: str, from_email: str, password: str
):
    """
        Send email with attachments given...
        recipients (The list of the recipients)
        server (The smtp server)
        port (The server port)
        from_email (the email to be the sender)
        password (the sending emails password)
    """
    recipients = ",".join(recipients)

    # Start a multipart email
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = recipients
    msg["Subject"] = "Attaching an image"
    text = MIMEText("Random text", "plain")
    attachment = None

    # open the output file and create an attachment from it
    with open("output", "r") as file:
        attachment = MIMEApplication(file.read(), Name=basename(file))

    # Attach the text and attachment to the email.
    msg.attach(text)
    msg.attach(attachment)

    # Open communication and send the email
    server = smtplib.SMTP_SSL(server, int(port))
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()


if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser()

    # Add the arguments to our application
    parser.add_argument("-e", "--email", type=str, help="destination email")
    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        type=argparse.FileType("r"),
        help="Config file",
        default=None,
    )

    # Parse the arguments
    args = parser.parse_args()

    # Check if the user provided a conf file
    if not args.config:
        print("Error, a config file is required")
        parser.print_help()
        exit(1)

    # Create our config parser
    config = configparser.ConfigParser()
    config.read_file(args.config)

    # Send the email
    send_email(
        [args.email],
        server=config["DEFAULT"]["server"],
        port=config["DEFAULT"]["port"],
        from_email=config["DEFAULT"]["email"],
        password=config["DEFAULT"]["password"],
    )

    # Send the email with an attachment
    send_email_with_attachment(
        [args.email],
        server=config["DEFAULT"]["server"],
        port=config["DEFAULT"]["port"],
        from_email=config["DEFAULT"]["email"],
        password=config["DEFAULT"]["password"],
    )
