#!/bin/bash

# Parse arguments for URL and output path
while getopts u:o: flag
do
    case "${flag}" in
        u) URL=${OPTARG};;
        o) OUTPUT_PATH=${OPTARG};;
    esac
done

# Ensure both arguments are provided
if [ -z "$URL" ] || [ -z "$OUTPUT_PATH" ]; then
    echo "Usage: $0 -u <URL> -o <OUTPUT_PATH>"
    exit 1
fi

# Create the output directory if it doesn't exist
mkdir -p $(dirname "$OUTPUT_PATH")

# Download the file
curl -L "$URL" -o "$OUTPUT_PATH"

# Check if the download was successful
if [ $? -eq 0 ]; then
    echo "File downloaded successfully to $OUTPUT_PATH"
else
    echo "Failed to download the file."
    exit 1
fi
