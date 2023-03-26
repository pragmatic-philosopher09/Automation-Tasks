import os
import datetime
import webbrowser
import time

# Path to the file storing the date of the last solved problem
last_solved_file = "last_solved.txt"

# Read the date of the last solved problem from the file
if os.path.exists(last_solved_file):
    with open(last_solved_file, "r") as f:
        last_solved_date = f.read().strip()
else:
    last_solved_date = None

# Get the current date
current_date = str(datetime.date.today())

# Check if a problem has been solved today
if last_solved_date == current_date:
    print("You have already solved a problem today!")
else:
    print("You have not solved a problem today, please solve one before the day is over.")

    # Update the last solved date in the file
    with open(last_solved_file, "w") as f:
        f.write(current_date)
    
    # Open LeetCode in a web browser
    leetcode_url = "https://leetcode.com/"
    webbrowser.open_new_tab(leetcode_url)

    # Wait for 25 minutes to give time to solve a problem
    time.sleep(1500)

    # Refresh the LeetCode page
    webbrowser.reload()

    # Wait for 5 seconds to give time for the page to reload
    time.sleep(5)

    # Close the web browser
    webbrowser.close()