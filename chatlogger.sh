#!/bin/bash

# Get the current timestamp in the format YYYY-MM-DD HH:MM:SS
timestamp=$(date +"%Y-%m-%d %H:%M:%S")

# Get the current username from the environment
username=$USER

# Define the custom message
custom_message="Script executed successfully"

# Append the log entry to user_activity.log
echo "[$timestamp] User: $username" >> user_activity.log
echo "" >> user_activity.log
echo "    Log entry: $custom_message" >> user_activity.log