import datetime
import logging
import os
import shutil

# Set up logging 
log_filename = "organizer_log.txt"
log_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), log_filename)
logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",)

try: 
    downloads_path = "/home/chilu/Downloads/"
    print(f"Organizing files in {downloads_path}")
    files = os.listdir(downloads_path)
    print(f"Total {len(files)} files to organize...")

    # Dictionary to store file extensions and their corresponding folders
    extensions = {
        "Documents": [
            ".pdf",
            ".docx",
            ".xlsx",
            ".txt",
            ".pptx",
            ".doc",
            ".ppt",
            ".xls",
            ".odt",
            ".ods",
            ".odp",
            ".odg",
            ".odf",
            ".rtf",
            ".tex",
            ".wpd",
            ".wps",
            ".csv",
            ".epub",
        ],
        "Videos": [
            ".mp4",
            ".mov",
            ".avi",
            ".mkv",
            ".flv",
            ".mpeg",
            ".srt",
        ],
        "Audio": [
            ".mp3",
            ".wav",
            ".flac",
            ".m4a",
            ".ogg",
            ".mp2",
            ".aac",
            ".wma",
            ".aiff",
            ".amr",
            ".m4p",
        ],
        "Compressed": [
            ".zip",
            ".rar",
            ".tar",
            ".gz",
            ".7z",
        ],
        "Images": [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".svg",
            ".webp",
            ".avif",
            ".jfif",
            ".ico",
        ],
        "code": [
            ".py",
            ".java",
            ".c",
            ".cpp",
            ".html",
            ".css",
            ".js",
            ".ts",
            ".php",
            ".sql",
            ".json",
            ".xml",
            ".diff",
        ],
        "keys": [
            ".pem",
            ".pub",
            ".key",
            ".asc",
            ".pgp",
            ".gpg",
        ],
        "databases": [
            ".db",
            ".sqlite",
            ".sqlite3",
            ".sqlitedb",
            ".psql",
            ".psql_history",
            ".psqlrc",
            ".mysql",
            ".mysql_history",
            ".my.cnf",
            ".pgpass",
            ".pg_service.conf",
            ".pgpass.conf",
            ".pg_service.conf",
            ".backup",
        ],
        "drawings": [
            ".svg",
            ".odg",
            ".vdx",
            ".vsdx",
            ".vsd",
            ".vssx",
            ".vss",
            ".vst",
            ".excalidraw",
        ],
    }

    # Create folders if they don't exist
    for folder in extensions:
        extension_folder_path = os.path.join(downloads_path, folder)
        if not os.path.exists(extension_folder_path):
            os.makedirs(extension_folder_path)
            print(f"{folder} folder created! as {extension_folder_path}")


    # Iterate through files in the specified directory
    files_organized = 0
    for filename in files:
        file_extension = os.path.splitext(filename)[1].lower()

        # Move files to corresponding folders based on their extensions
        for category, ext_list in extensions.items():
            print(f"Moving {filename} to {category} folder...")
            if file_extension in ext_list:
                src_path = os.path.join(downloads_path, filename)
                dest_path = os.path.join(downloads_path, category, filename)
                shutil.move(src_path, dest_path)
                print(f"{filename} moved to {category} folder successfully!")
                files_organized += 1
                break

    print("Files have been organized successfully!")
    
    # Add log entry
    with open(log_file_path, "a") as f:
        if files_organized > 0:
            f.write(f"Organized {files_organized} files on {datetime.datetime.now()}\n")
        else:
            f.write(f"No files to organize on {datetime.datetime.now()}\n")

except Exception as e:
    logging.error(e, exc_info=True)
    print("An error occured while organizing files!")
