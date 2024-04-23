import os
import signal
import time
import re

# Function to monitor log file
def monitor_log(log_file):
    try:
        with open(log_file, 'r') as file:
            file.seek(0, os.SEEK_END)  # Go to the end of file
            while True:
                line = file.readline()
                if line:
                    print(line.strip())  # Print new log entry
                else:
                    time.sleep(0.1)  # Sleep briefly to avoid high CPU usage
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
    except FileNotFoundError:
        print("Log file not found.")
    except Exception as e:
        print("An error occurred:", e)

# Function to analyze log file
def analyze_log(log_file, keyword):
    try:
        with open(log_file, 'r') as file:
            log_content = file.read()
            occurrences = len(re.findall(keyword, log_content))
            print(f"Number of occurrences of '{keyword}': {occurrences}")
    except FileNotFoundError:
        print("Log file not found.")
    except Exception as e:
        print("An error occurred:", e)

# Main function
def main():
    log_file = "sample.log"  # Change this to your log file path
    keyword = "ERROR"  # Change this to the keyword you want to search for

    print("Starting log monitoring...")
    monitor_log(log_file)

    print("\nAnalyzing log...")
    analyze_log(log_file, keyword)

if __name__ == "__main__":
    main()
