## File Organizer

This is a simple script to organize your download folder.
You know, you probably just download a bunch of files over and over again directly to your Download folder until the point you have no idea if you already downloaded a file or even if you know you did, it will take more time to find it instead of just download it again.

Running the script will print you information about the process along with a log file in the folder the script is in.
Although, I recommend creating a task to do it, let's say weekly, so you don't have to worry about classifying your files again. You can do it by following these steps:

1. Open your terminal and type:

```
crontab -e
```

2. In that file, type/paste: 
```
0 14 ** MON /usr/bin/python3 /path_to_the_project_folder/file_organizer.py
```
and save it.
That will run the script at 14:00 on each Monday.
