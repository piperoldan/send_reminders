#!/usr/bin/env python3

import sys
import email  # was email.message
import smtplib
import datetime



def usage():
    print("send_reminders: Send meeting reminders")
    print()
    print("invocation:")
    print("    send_reminders 'date|Meeting Title|Emails' ")
    return 1

def dow(date):
    dateobj = datetime.datetime.striptime(date, r"%d/%m/%Y")
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
    # Change these to point to your fake server
    smtp_server = 'localhost'
    smtp_port = 8025 

    smtp = None # Initialize smtp to None so finally block doesn't error if con>
    try:
        # No need for starttls() or login() with DebuggingServer as it doesn't >
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        # You might want to enable debug level for more output from smtplib
        # smtp.set_debuglevel(1) 

        # The 'From' address will still be part of the email content
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
                # Corrected: Ensure 'file=sys.stderr' is complete
                print(f"Failed to send email to {email_addr} (via fake server)")

    except Exception as e:
        # Catch connection errors here, or other unexpected errors during setup
        print(f"An error occurred during email sending setup: {e}, <file=sys.st>")
    finally:
        if smtp: # Check if smtp object was successfully created
            smtp.quit()
            print("Fake SMTP connection closed.")

def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split('|')
        message = message_template(date, title)
        send_message(message, emails)
        print(f"Successfully sent reminders to:", emails)
    except Exception as e:
        return usage()

    except Exception as e:
        print("Failure to send email", file=sys.stderr)

if __name__ == "__main__":
    sys.exit(main())
