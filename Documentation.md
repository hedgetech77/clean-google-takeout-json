---

### 📄 `DOCUMENTATION.md`

```markdown
# Documentation: Google Photos JSON Cleanup Script

## Purpose

Google Takeout exports include metadata `.json` files with every photo and video. These files are often unnecessary for most users. This script provides a safe and fast way to remove all `.json` files from a Google Photos export folder.

## How It Works

The script uses `os.walk()` to recursively visit all subdirectories and checks each file for the `.json` extension. If found, it attempts to delete the file using `os.remove()`.

## Function: `delete_json_files(folder)`

- **Parameters:** `folder` (string) – The root directory from which to begin deletion.
- **Returns:** None
- **Prints:** A message for each deleted file and a summary count at the end.

## Usage

Run the script from the terminal and enter the full path to the Google Photos folder.

### Input Example

"C:\Users\YourName\Downloads\Takeout\Google Photos"

### Output Example

Deleted: C:\Path\To\File\example.json
Total JSON files deleted: 35

## Error Handling

If a file cannot be deleted (due to permissions or locks), an error message will be printed, and the script will continue processing the remaining files.

## Compatibility

- Python 3.6+
- Works on Windows, macOS, and Linux

## Support

This script is provided as-is. If you find it useful, feel free to share or contribute improvements via GitHub.
```
