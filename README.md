# Google Photos JSON Cleanup Script

This is a simple Python script to help you clean up unwanted `.json` files from a Google Photos export folder. When you use Google Takeout to export your photos, it includes metadata `.json` files alongside the media files. This script recursively deletes all `.json` files from a specified folder and its subfolders.

## 🔧 Features

- Recursively traverses folders
- Deletes all `.json` files
- Provides a summary of deleted files
- Simple and safe to use

## 🚀 How to Use

1. Make sure you have Python installed (version 3+).
2. Download or clone this repository.
3. Open a terminal or command prompt.
4. Run the script:

```bash
python delete_google_json.py
```

## 📂 Example

```bash
Enter the full path to your 'Google Photos' folder: "C:\Users\YourName\Downloads\Takeout\Google Photos"
Deleted: C:\Users\YourName\Downloads\Takeout\Google Photos\Album\IMG_1234.json
...
Total JSON files deleted: 237
```

## ⚠️ Warning

This script permanently deletes .json files. Make sure to back up your data if needed before proceeding.

## 📄 License

This project is licensed under the MIT License. See LICENSE.txt for details.
