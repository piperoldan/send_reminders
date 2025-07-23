Created this repo to learn to debug.

How to use this repo.
The main branch contains the files "As presented in the class". The copy is not exact, but they act as the files in class.

You don't need to setup email server for this to work. It has embedded a fake mail server that is going to "receive the emails in the fake accounts"

For the fake email server, in a separate window run the following and leave it open:
/usr/bin/python3 -m smtpd -n -c DebuggingServer localhost:8025
Do not close while practicing. It will show the emails sent if successful.

Always make all modifications in the branch practice, keep main branch as is, with errors, the idea is to learn how to debug a file.

To play with the scripts, run meeting_reminder.sh and is going to open a calendar window.

Select the date in the calendar, the meeting name and the email of the person it is going to be
sent to.

