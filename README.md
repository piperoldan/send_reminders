#Created this repo to learn to debug.<br>
##**Do not submit push requests please.**<br>

Please read these instructions carefully, the idea is to keep the original file untouched to be able to practice debug.<br>

##How to use this repo.<br>
The main branch contains the files "As presented in the class". The copy is not exact, but they act as the files in class.<br>

You don't need to setup email server for this to work. It has embedded a fake mail server that is going to "receive the emails in the fake accounts"<br>

For the fake email server, in a separate command prompt window run the following and leave it open:<br>
>>/usr/bin/python3 -m smtpd -n -c DebuggingServer localhost:8025<br>
**Do not close while practicing. It is going to look like doing nothing but don't be fooled, its doing its job. At the end, it will show the emails sent if successful.**<br>

Before making any changes run: git checkout -b practice
to create a new branch named practice.<br>

Always make all modifications in the branch practice, keep main branch as is, with errors, the idea is to learn how to debug a file.<br>

To play with the scripts, run meeting_reminder.sh and is going to open a calendar window.<br>

Select the date in the calendar, the meeting name and the email of the person it is going to be sent to.<br>

At the end of the practice, make sure to delete the branch created using:<br>
>>git checkout main<br>
>>M	meeting_reminder.sh<br>
>>M	send_reminders.py<br>
>>Switched to branch 'main'<br>
>>Your branch is up to date with 'origin/main'.<br>

>>git branch -D practice<br>
>>Deleted branch practice (was 570b450).<br>

And make sure to reverse all the changes made.