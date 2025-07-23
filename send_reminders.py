#!/usr/bin/env python3

import sys
import email.message
import smtplib
import datetime



def usage():
    print("send_reminders: Send meeting reminders")
    print()
    print("invocation:")
    print("    send_reminders 'date|Meeting Title|Emails' ")
    return 1

def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%m/%d/%Y")
    return dateobj.strftime("%A")

def message_template(date, title):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = f'Meeting reminder: "{title}"'
    message.set_content(f'''
Hi all!

This is a quick mail to remind you all that we have a meeting about:
"{title}"
the {weekday} {date}.

See you there.
''')
    return message

def send_message(message, emails):
    smtp_server = 'localhost'
    smtp_port = 8025 

    smtp = None # Initialize smtp to None
    try:
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        message['From'] = 'noreply@example.com' 

        for email_addr in emails.split(','):
            email_addr = email_addr.strip()
            if not email_addr:
                continue

            current_message = email.message.EmailMessage()
            current_message['Subject'] = message['Subject']
            current_message['From'] = message['From']
            current_message.set_content(message.get_content())

            current_message['To'] = email_addr
            try:
                smtp.send_message(current_message)
                print(f"Attempted to send reminder to: {email_addr} (via fake server)")
            except Exception as e:
                print(f"Failed to send email to {email_addr} (via fake server): {e}", file=sys.stderr)

    except Exception as e:
        print(f"An error occurred during email sending setup: {e}", file=sys.stderr)
    finally: # This 'finally' should be at the same indentation level as 'try' and 'except'
        if smtp: # This 'if' should be indented relative to 'finally'
            smtp.quit() # This 'smtp.quit()' should be indented relative to 'if'
            print("Fake SMTP connection closed.") # This 'print' should be at the same level as 'smtp.quit()'


def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split('|')
        message = message_template(date, title)
        send_message(message, emails)
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        print(f"Failure to send email: {e}", file=sys.stderr)

if __name__ == "__main__":
    sys.exit(main())
