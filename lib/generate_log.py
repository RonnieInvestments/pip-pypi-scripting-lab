from datetime import datetime
import os


#Implement log generation logic
def generate_log(data):

    # STEP 1: Validate input
    # Check if data is a list
    if not isinstance(data,list):
        raise ValueError("Log data is not a list")


    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Use datetime.now().strftime("%Y%m%d")
    log_file = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")

    if not os.path.exists(log_file):
        with open(log_file,'a') as file:
            for log in data:
                file.write(f"{log}\n")
    
    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {log_file}")

    return log_file

#You can implement a function to generate a list using public API
#First import requests
""" def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
         return response.json()
    else:
         return [] """

#Logic to allow generate_log.py file and its logic to run directly
#If generate_log.py is imported do not run its logic
if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)
