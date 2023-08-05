import os
from datetime import datetime, timedelta

def delete_previous_day_file(path):
    # Get yesterday's date
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    # Construct the full file path
    file_path = os.path.join(path, yesterday)
    
    # Check if the file exists
    if os.path.exists(file_path):
        # Delete the file
        os.remove(file_path)
        print(f"Deleted file: {file_path}")
    else:
        print(f"File not found: {file_path}")

# Example usage
delete_previous_day_file("/workspaces/WEDDING")

