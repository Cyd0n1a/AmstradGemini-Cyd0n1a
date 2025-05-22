# Raspberry Pi 5 - Serial to Gemini API Bridge.
#
#          _       _        _          _                  _                _                    _             _        
#        /\ \     /\ \     /\_\       /\ \               /\ \             /\ \     _           /\ \          / /\      
#       /  \ \    \ \ \   / / /      /  \ \____         /  \ \           /  \ \   /\_\         \ \ \        / /  \     
#      / /\ \ \    \ \ \_/ / /      / /\ \_____\       / /\ \ \         / /\ \ \_/ / /         /\ \_\      / / /\ \__  
#     / / /\ \ \    \ \___/ /      / / /\/___  /      / / /\ \ \       / / /\ \___/ /         / /\/_/     / / /\ \___\ 
#    / / /  \ \_\    \ \ \_/      / / /   / / /      / / /  \ \_\     / / /  \/____/         / / /        \ \ \ \/___/ 
#   / / /    \/_/     \ \ \      / / /   / / /      / / /   / / /    / / /    / / /         / / /          \ \ \       
#  / / /               \ \ \    / / /   / / /      / / /   / / /    / / /    / / /         / / /       _    \ \ \      
# / / /________         \ \ \   \ \ \__/ / /      / / /___/ / /    / / /    / / /      ___/ / /__     /_/\__/ / /      
#/ / /_________\         \ \_\   \ \___\/ /      / / /____\/ /    / / /    / / /      /\__\/_/___\    \ \/___/ /       
#\/____________/          \/_/    \/_____/       \/_________/     \/_/     \/_/       \/_________/     \_____\/        
#                                                                                                                      
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BBB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.    @@@@@BBBBB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,.  _@@@@@           "=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                "+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    '4@@@@@@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@B@@@@@@@@@@@@@@@@@@@@@@@@                       "B@@@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@"      9@@@@@@@@B.     'B@@@@@@@ga____.               %@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@         9@@@@@@@.       .@@@@@@@@@@@@@@g__              %@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@         @@@@@@@@.       .@@@@@@@@@@@@@@@@@@@_,            0@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@_    . j@@@@@@@@g_.    _@@@@@@@@@@@@@@@@@@@@@@g_.          '@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@_           @@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           @@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@a          @@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'  _.   %@@@@@@@@@@@@@P'""""`@@@@@@@@g.        .@@@@@@@@@@@
#[@@@@@@@@@@@@@F      B@@@@@@F .+@@@@_.  B@@@@@@@@@@@|      @@@@@@@@@A.         @@@@@@@@@@
#[@@"   \@@@@@         @@@@@@  !@@@@@@;  .@@@T.---- Vg_.   j@'----..B@j         [@@@@@@@@@
#[@@.   ,@@@@@         &@@@@B   B@@@@P   .@@@||      @@|   @@|     [|@@,         @@@@@@@@@
#[@@@@@@@@@@@@@,      j@@@@@@,          .J@@@||      @@|   @@|     [|@@]         @@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@g_       _@@@@@||      --    --      [|@@@         [@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ggggg@@@@@@@||     ___'   ___     [|@@@         [@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||      --.   --,     [|@@@         [@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P"     "%@@@@@||      @@|   @@|     [|@@@         [@@@@@@@@
#[@@@@@@@@@@@@@N     "@@@@@@@F   ...    '@@@@||      @@|   @@|     [|@@@         @@@@@@@@@
#[@@"   \@@@@@"        @@@@@@  .g@@@@_.  .@@@1.===== P.    "@L.====='@@)         @@@@@@@@@
#[@@.    @@@@@         [@@@@B  !@@@@@@!  '@@@@@@@@@@@|      @@@@@@@@@@P         ,@@@@@@@@@
#[@@@ggg@@@@@@B       _@@@@@@   0@@@@f   !@@@@@@@@@@@ggggggg@@@@@@@@@@          @@@@@@@@@@
#[@@@@@@@@@@@@@@@~~~J@@@@@@@@@_         A@@@@@@@@@@@@@@@@@@@@@@@@@@@@"         j@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@g~~~~~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          _@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@N          _@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@W"         .+@@@@@@@@@@@@@
#[@@@@@@@@@@@@@W"'  "4@@@@@@@@@@P"   "4@@@@@@@@@@@@@@@@@@@@@@@P"          .g@@@@@@@@@@@@@@
#[@@@@@@@@@@@@?        @@@@@@@@'       '@@@@@@@@@@@@@@@@@@@@"            ,@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@         [@@@@@@B.       .@@@@@@@@@@@@@@@@P"            ..g@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@B        @@@@@@@@_       J@@@@@@@@@@@=>'               ,g@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@~___~g@@@@@@@@@@g~___~@@@@@                        _@@@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                    ._/@@@@@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 __g@@@@@@@@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P"""9@@@@@           ..__@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.    @@@@@l__-___gg@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@g___g@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#[@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# This script listens for prompts from an Amstrad CPC (or similar retro computer)
# via a serial connection, sends the prompt to the Gemini API,
# and then sends the processed response back to the Amstrad.
#
# Required libraries: pyserial, requests
# Install them with: pip install pyserial requests

import serial
import requests
import json
import time
import os

# --- Configuration ---
# Serial Port Configuration (Adjust as needed)
# For Raspberry Pi 5, the primary UART is often /dev/ttyAMA0 if enabled via raspi-config,
# or /dev/serial0 (which is a symlink).
# If using a USB-to-Serial adapter, it might be /dev/ttyUSB0 or /dev/ttyACM0.
SERIAL_PORT = "/dev/ttyAMA0"  # Or "/dev/ttyUSB0", "/dev/serial0" etc.
BAUD_RATE = 4800  # Match this with Amstrad's serial interface configuration.
                  # Slower rates like 4800, 2400, or even 1200 might be more reliable
                  # for older hardware and long cable runs. Max for CPC RS232 is often 19200.
                  # The BASIC program doesn't set this; it's assumed to be pre-configured.

# Gemini API Configuration
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"  # !!! REPLACE WITH YOUR ACTUAL API KEY !!!
# IMPORTANT: For security, consider loading the API key from an environment variable
# or a configuration file not checked into version control.
# Example for environment variable: GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

# Response Processing
MAX_RESPONSE_LINES = 15  # Max number of lines to send back to Amstrad
MAX_LINE_LENGTH = 38     # Max characters per line (for Amstrad MODE 1 is 40 chars, leave some margin)
END_OF_RESPONSE_MARKER = "ENDOFRSP" # Marker to signal end of full response to Amstrad

# --- Helper Functions ---

def send_to_gemini(prompt_text):
    """
    Sends the prompt to the Gemini API and returns the response.
    """
    if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        print("ERROR: Gemini API Key not configured. Please set it in the script.")
        return None

    headers = {
        "Content-Type": "application/json",
    }
    # Construct the payload as per Gemini API documentation
    # Using a simple text-only prompt here
    payload = {
        "contents": [{
            "parts": [{
                "text": prompt_text
            }]
        }],
        # Optional: Add generationConfig for more control if needed
        # "generationConfig": {
        #   "temperature": 0.7,
        #   "maxOutputTokens": 200, # Limit output tokens from API side
        # }
    }

    print(f"Sending to Gemini API: {prompt_text[:50]}...")
    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=payload, timeout=60) # 60s timeout
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        
        response_json = response.json()
        
        # Extract text from the response (structure may vary slightly based on model/version)
        # This parsing assumes the standard successful response structure.
        if (response_json.get("candidates") and
            response_json["candidates"][0].get("content") and
            response_json["candidates"][0]["content"].get("parts") and
            response_json["candidates"][0]["content"]["parts"][0].get("text")):
            
            generated_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
            print("Gemini API Response (raw):", generated_text[:100] + "...")
            return generated_text
        else:
            print("Error: Could not parse text from Gemini response.")
            print("Full API Response:", response_json)
            return "Error: Could not parse API response."

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Gemini API: {e}")
        return f"Error: API connection failed ({e})"
    except json.JSONDecodeError:
        print("Error: Could not decode JSON response from Gemini API.")
        return "Error: Invalid API response format."
    except Exception as e:
        print(f"An unexpected error occurred during API call: {e}")
        return f"Error: Unexpected API issue ({e})"


def process_response_for_amstrad(text_response):
    """
    Processes the Gemini response to fit Amstrad's display limitations.
    Splits into lines, truncates lines, and limits total lines.
    """
    processed_lines = []
    if not text_response:
        return ["No response or error."]

    # Split the response into lines based on newline characters
    raw_lines = text_response.splitlines()

    for line in raw_lines:
        if len(processed_lines) >= MAX_RESPONSE_LINES:
            break
        # Further split long lines if necessary, or just truncate
        start = 0
        while start < len(line):
            if len(processed_lines) >= MAX_RESPONSE_LINES:
                break
            chunk = line[start:start + MAX_LINE_LENGTH]
            processed_lines.append(chunk)
            start += MAX_LINE_LENGTH
        if not line.strip() and len(processed_lines) < MAX_RESPONSE_LINES : # Preserve empty lines if not exceeding max
            if not processed_lines or processed_lines[-1].strip(): # Avoid multiple consecutive empty lines unless intended
                 processed_lines.append("")


    # If no lines were generated (e.g. empty response), provide a default
    if not processed_lines:
        processed_lines.append("Received empty response.")

    # Ensure we don't exceed MAX_RESPONSE_LINES even after splitting
    return processed_lines[:MAX_RESPONSE_LINES]

def send_line_to_amstrad(serial_conn, line):
    """
    Sends a single line of text to the Amstrad, followed by CR+LF.
    """
    try:
        print(f"Sending to Amstrad: {line}")
        serial_conn.write(line.encode('ascii', 'replace') + b'\r\n') # Amstrad expects CR LF
        serial_conn.flush() # Ensure data is sent immediately
        # Short delay might be needed if Amstrad BASIC is slow to process
        # However, LINE INPUT # should handle waiting.
        # time.sleep(0.05) # Experiment if issues occur
    except serial.SerialException as e:
        print(f"Serial write error: {e}")
    except Exception as e:
        print(f"Error sending line to Amstrad: {e}")

# --- Main Program ---
if __name__ == "__main__":
    print("Raspberry Pi - Amstrad CPC to Gemini API Bridge")
    print(f"Attempting to open serial port: {SERIAL_PORT} at {BAUD_RATE} baud.")

    # Attempt to load API key from environment variable if not hardcoded
    if GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE" and os.getenv("GEMINI_API_KEY"):
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
        print("Loaded Gemini API Key from environment variable.")
    elif GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        print("CRITICAL: GEMINI_API_KEY is not set. Please edit the script and add your key.")
        exit(1)


    ser = None # Initialize ser to None
    try:
        # Initialize serial connection
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=10) # 10-second read timeout
        print(f"Serial port {SERIAL_PORT} opened successfully.")
        print("Waiting for prompt from Amstrad...")

        while True:
            if ser.in_waiting > 0:
                try:
                    # Read a line from Amstrad (expects prompt terminated by CR or CR+LF)
                    # The Amstrad BASIC program uses PRINT #, which sends CR+LF
                    amstrad_prompt_bytes = ser.readline()
                    amstrad_prompt = amstrad_prompt_bytes.decode('ascii', 'replace').strip()
                    
                    if amstrad_prompt: # Proceed if prompt is not empty
                        print(f"\nReceived from Amstrad: '{amstrad_prompt}'")

                        # 1. Send prompt to Gemini API
                        gemini_response_text = send_to_gemini(amstrad_prompt)

                        # 2. Process the response for Amstrad
                        if gemini_response_text:
                            amstrad_lines = process_response_for_amstrad(gemini_response_text)
                        else:
                            amstrad_lines = ["Error: No response from API."]

                        # 3. Send processed lines back to Amstrad
                        print(f"\nSending {len(amstrad_lines)} lines to Amstrad...")
                        for line_to_send in amstrad_lines:
                            send_line_to_amstrad(ser, line_to_send)
                            time.sleep(0.1) # Small delay between lines, helps Amstrad BASIC keep up

                        # 4. Send the end-of-response marker
                        print(f"Sending end-of-response marker: '{END_OF_RESPONSE_MARKER}'")
                        send_line_to_amstrad(ser, END_OF_RESPONSE_MARKER)
                        
                        print("\nTransaction complete. Waiting for next prompt...")

                except UnicodeDecodeError as ude:
                    print(f"Serial read decode error: {ude}. Ensure Amstrad is sending ASCII.")
                except serial.SerialTimeoutException:
                    print("Serial readline timed out. No data from Amstrad.")
                    # This is normal if Amstrad is idle, loop will continue
                except Exception as e:
                    print(f"An error occurred in the main loop: {e}")
                    # Attempt to send an error message back to Amstrad if possible
                    try:
                        send_line_to_amstrad(ser, "PI:ERR IN LOOP")
                        send_line_to_amstrad(ser, END_OF_RESPONSE_MARKER)
                    except:
                        pass # Ignore errors during error reporting
                    time.sleep(1) # Brief pause before retrying

            time.sleep(0.1) # Main loop polling delay

    except serial.SerialException as e:
        print(f"CRITICAL Serial Error: {e}")
        print("Please check:")
        print(f"1. Is the serial device '{SERIAL_PORT}' correct and connected?")
        print(f"2. Does the user running this script (e.g., 'pi') have permission? (Try 'sudo usermod -a -G dialout pi')")
        print(f"3. Is the correct baud rate ({BAUD_RATE}) set on both devices?")
    except KeyboardInterrupt:
        print("\nExiting program (Ctrl+C pressed).")
    finally:
        if ser and ser.is_open:
            print("Closing serial port.")
            ser.close()