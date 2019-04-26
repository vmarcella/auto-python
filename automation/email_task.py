import argparse
import configparser
import smtplib
from email.message import EmailMessage


def send_email(to_email: str, server: str, port: str, from_email: str, password: str):
    print(f"With love, from {from_email} to {to_email}")

    subject = "With love, from ME to YOU"
    text = """This is an example test"""
    msg = EmailMessage()
    msg.set_content(text)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    # Open communication and send

    print(from_email)
    server = smtplib.SMTP_SSL(server, int(port))
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email", type=str, help="destination email")
    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        type=argparse.FileType("r"),
        help="Config file",
        default=None,
    )

    args = parser.parse_args()
    if not args.config:
        print("Error, a config file is required")
        parser.print_help()
        exit(1)

    config = configparser.ConfigParser()
    config.read_file(args.config)

    send_email(
        args.email,
        server=config["DEFAULT"]["server"],
        port=config["DEFAULT"]["port"],
        from_email=config["DEFAULT"]["email"],
        password=config["DEFAULT"]["password"],
    )
