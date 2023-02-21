import requests
import time

# Configuration
url_file = "congif.txt"  # File containing list of URLs to monitor
check_interval = 5  # Interval in seconds between checks
text_to_find = "login"  # String that should be present in the web page

# Read URLs from file
with open(url_file, "r") as f:
    urls = [line.strip() for line in f]

# Start monitoring loop
while True:
    # Loop through URLs and check availability
    for url in urls:
        try:
            # Send HTTP request and measure response time
            start_time = time.time()
            response = requests.get(url)
            response_time = time.time() - start_time

            # Verify content requirement
            if text_to_find in response.text:
                status = "OK"
            else:
                status = "Error: login text not found"

        except requests.exceptions.RequestException as e:
            # Request failed
            response_time = None
            status = f"Error: {str(e)}"

        # Write log entry
        log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {url} - {status} - Response time: {response_time}\n"
        with open("monitoring.log", "a") as f:
            f.write(log_entry)

    # Wait for next check interval
    time.sleep(check_interval)
