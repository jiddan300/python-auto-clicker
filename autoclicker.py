import pyautogui
import time
import keyboard  # For detecting keyboard interaction
import json  # For saving and loading setups

# Enable pyautogui failsafe
pyautogui.FAILSAFE = True  # Move mouse to top-left corner to stop

# File path for saving setups
SETUP_FILE = "clicker_setups.txt"

def load_all_setups():
    try:
        with open(SETUP_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_all_setups(setups):
    with open(SETUP_FILE, "w") as f:
        json.dump(setups, f, indent=4)
    print("All setups saved successfully.")

def non_blocking_delay(total_delay, check_interval=0.1):
    elapsed = 0
    while elapsed < total_delay:
        if keyboard.is_pressed('esc'):  # Stop on Esc
            print("Stopping during delay...")
            raise KeyboardInterrupt
        time.sleep(check_interval)
        elapsed += check_interval

def get_positions_and_delays():
    positions = []
    actions = []  # To store "click" or "hover"
    delays = []

    print("Set positions for auto-clicking or hovering.")
    print("Hover over a spot and press 's' to save the position. Press 'q' to finish.")

    while True:
        if keyboard.is_pressed('s'):  # Save position
            x, y = pyautogui.position()
            print(f"Position saved: {x}, {y}")

            # Ask if the action is a click (yes/no)
            while True:
                action = input(f"Do you want to click at position ({x}, {y})? (yes/no): ").strip().lower()
                if action in ['yes', 'no']:
                    action = 'click' if action == 'yes' else 'hover'
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            actions.append(action)

            # Get delay
            delay = input(f"Enter delay (in seconds) after action at position ({x}, {y}): ").strip()
            try:
                delay = float(delay)
                if delay < 0:
                    raise ValueError
                delays.append(delay)
            except ValueError:
                print("Invalid delay. Defaulting to 0.5 seconds.")
                delays.append(0.5)

            positions.append((x, y))
            time.sleep(0.5)  # Prevent multiple saves for a single press

        if keyboard.is_pressed('q'):  # Quit position setting
            print("Position recording finished.")
            break

    return positions, actions, delays

def run_clicker(click_positions, actions, click_delays, num_loops):
    print("Press 'Tab' to start and 'Esc' to stop.")
    time.sleep(2)

    try:
        while True:
            if keyboard.is_pressed('tab'):  # Start on Tab
                print("Auto-clicker started. Press 'Esc' to stop or move mouse to the top-left corner.")
                current_loop = 0
                while True:
                    for i, position in enumerate(click_positions):
                        if keyboard.is_pressed('esc'):  # Stop on Esc
                            print("Auto-clicker stopped by user.")
                            raise KeyboardInterrupt

                        if actions[i] == 'click':
                            pyautogui.doubleClick(position)
                        elif actions[i] == 'hover':
                            pyautogui.moveTo(position)

                        non_blocking_delay(click_delays[i])  # Use non-blocking delay

                    current_loop += 1
                    if num_loops != 0 and current_loop >= num_loops:
                        print(f"Completed {num_loops} loops. Exiting.")
                        raise KeyboardInterrupt

            if keyboard.is_pressed('esc'):  # Allow exit before starting
                print("Exiting program.")
                raise KeyboardInterrupt

    except KeyboardInterrupt:
        print("Exiting auto-clicker safely.")
    except pyautogui.FailSafeException:
        print("Fail-safe triggered. Auto-clicker stopped.")

# Main program
while True:
    setups = load_all_setups()

    print("\nChoose an option:")
    print("1: Create a new setup")
    print("2: Run a saved setup")
    print("3: Delete a saved setup")
    print("4: Exit the program")

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == "1":  # New setup
        print("\nSetting up a new configuration...")
        positions, actions, delays = get_positions_and_delays()

        if not positions:
            print("No positions recorded. Exiting.")
            continue

        setup_name = input("Enter a unique name for this setup: ").strip()
        if setup_name in setups:
            print("Setup name already exists. Use a different name.")
            continue

        setups[setup_name] = {
            "positions": positions,
            "actions": actions,
            "delays": delays,
        }

        save_all_setups(setups)
        print(f"Setup '{setup_name}' saved successfully.")

    elif choice == "2":  # Load and run setup
        if not setups:
            print("\nNo saved setups found. Please create a new setup first.")
            continue

        print("\nSaved setups:")
        setup_names = list(setups.keys())
        for i, name in enumerate(setup_names):
            print(f"{i + 1}: {name}")

        try:
            setup_index = int(input("Enter the index of the setup to run: ").strip()) - 1
            if 0 <= setup_index < len(setup_names):
                setup_name = setup_names[setup_index]
                setup = setups[setup_name]

                # Ask for the number of loops
                while True:
                    try:
                        num_loops = int(input("Enter the number of loops (0 for infinite): ").strip())
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                print(f"\nRunning setup '{setup_name}'...")
                run_clicker(setup["positions"], setup["actions"], setup["delays"], num_loops)
            else:
                print("Invalid index. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "3":  # Delete setup
        if not setups:
            print("\nNo saved setups found.")
            continue

        print("\nSaved setups:")
        setup_names = list(setups.keys())
        for i, name in enumerate(setup_names):
            print(f"{i + 1}: {name}")

        try:
            setup_index = int(input("Enter the index of the setup to delete: ").strip()) - 1
            if 0 <= setup_index < len(setup_names):
                setup_name = setup_names[setup_index]
                del setups[setup_name]
                save_all_setups(setups)
                print(f"Setup '{setup_name}' deleted.")
            else:
                print("Invalid index. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "4":  # Exit program
        print("\nExiting program. Goodbye!")
        break

    else:  # Invalid choice
        print("\nInvalid choice. Please enter 1, 2, 3, or 4.")
