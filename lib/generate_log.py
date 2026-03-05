from datetime import datetime
import os
from fetch_data import fetch_data

# Great hints
def generate_log(data):
    # TODO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list
    if not isinstance(data, list):
        raise ValueError("Log data is not a list.")

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")
    log_file = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")
    with open(log_file, "a") as file:
        for log in data:
            file.write(f"{log}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {log_file}")
    return log_file

# Calling the function
if __name__ == "__main__":
    post = fetch_data()

    log_data = [post.get("title", "No title")]
    generate_log(log_data)

