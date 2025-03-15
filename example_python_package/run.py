import datetime
import os

if __name__ == "__main__":
    print("Hello, World!")

    
    # Get the current timestamp in ISO format
    timestamp = datetime.datetime.now().isoformat()
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create a file with the timestamp
    timestamp_file_path = os.path.join(current_dir, "main_invocation_timestamp.txt")
    with open(timestamp_file_path, "w") as f:
        f.write(f"Main was invoked at: {timestamp}")
    
    print(f"Timestamp written to {timestamp_file_path}")