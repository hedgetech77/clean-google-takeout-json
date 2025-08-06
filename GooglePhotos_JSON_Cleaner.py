import os

def delete_json_files(folder):
    count = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    count += 1
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
    print(f"\nTotal JSON files deleted: {count}")

if __name__ == "__main__":
    folder_path = input("Enter the full path to your 'Google Photos' folder: ").strip('"')
    if os.path.isdir(folder_path):
        delete_json_files(folder_path)
    else:
        print("❌ Invalid folder path. Please check and try again.")
