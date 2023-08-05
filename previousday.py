from datetime import datetime, timedelta
import os

def create_yesterday_date_file(path: str):
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    file_name = f"{yesterday}"
    file_path = os.path.join(path, file_name)
    with open(file_path, 'w') as f:
        f.write(f"File created on {yesterday}")
    print(f"File created at {file_path}")

# Example usage
create_yesterday_date_file('/workspaces/WEDDING')
