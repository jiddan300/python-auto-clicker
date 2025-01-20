# Auto-Clicker Program

This is a Python-based auto-clicker program that allows users to configure and automate mouse actions such as clicking and hovering at specific screen positions. Users can save, load, and manage multiple setups for different tasks.

## Requirements

### System Requirements
- Windows operating system

### Python Dependencies
The program requires the following Python libraries:
- `pyautogui`: For controlling mouse and keyboard actions.
- `keyboard`: For detecting keyboard interactions.
- `json`: For saving and loading setup configurations.
- `time`: For managing delays.

### Installation
1. Make sure Python is installed on your system.
2. Install the required libraries using pip:
   ```bash
   pip install pyautogui keyboard
   ```

## How It Works

### Overview
The program provides the following functionality:
1. **Create a New Setup**: Record screen positions, specify actions (click/hover), and set delays between actions.
2. **Run a Saved Setup**: Execute a predefined sequence of actions as per a saved configuration.
3. **Delete a Saved Setup**: Remove unwanted configurations.
4. **Exit the Program**: Close the application.

### Features
- **Failsafe Mechanism**: Move the mouse cursor to the top-left corner of the screen to stop the program.
- **Interactive Input**: Specify actions and delays interactively for each recorded position.
- **Non-blocking Delay**: The program allows for interruptions during delay periods by pressing the `Esc` key.
- **Loop Control**: Option to run setups for a specific number of loops or indefinitely.

### Usage

#### 1. Running the Program
Run the script in your Python environment:
```bash
python auto_clicker.py
```

#### 2. Main Menu
Upon running the program, you'll see the following options:
```
Choose an option:
1: Create a new setup
2: Run a saved setup
3: Delete a saved setup
4: Exit the program
```

#### 3. Creating a New Setup
- Select option `1` from the main menu.
- Follow the instructions to save positions and specify actions (click or hover) and delays.
- Provide a unique name for the setup.

#### 4. Running a Saved Setup
- Select option `2` from the main menu.
- Choose a saved setup by entering its index.
- Specify the number of loops (enter `0` for infinite loops).
- Press `Tab` to start and `Esc` to stop the auto-clicker during execution.

#### 5. Deleting a Setup
- Select option `3` from the main menu.
- Choose a setup to delete by entering its index.

#### 6. Exiting the Program
- Select option `4` from the main menu to exit.

### Key Controls
- `s`: Save the current mouse position during setup creation.
- `q`: Quit the position recording process.
- `Tab`: Start the auto-clicker.
- `Esc`: Stop the auto-clicker or exit during delay.

## Saved Configurations
- All setups are saved in a JSON file named `clicker_setups.txt` in the same directory as the script.
- Each setup includes:
  - `positions`: List of recorded screen positions.
  - `actions`: Actions to perform (click/hover).
  - `delays`: Delays between actions.

## Example Workflow
1. **Create a Setup**:
   - Start the program.
   - Record two positions: (100, 200) and (300, 400).
   - Specify actions: click at (100, 200) and hover at (300, 400).
   - Set delays: 1 second and 2 seconds, respectively.
   - Save the setup as "TestSetup".
2. **Run the Setup**:
   - Select "TestSetup" and set it to run for 5 loops.
   - Press `Tab` to start.
   - Press `Esc` to stop if needed.

## Troubleshooting
- If the script doesn't respond, ensure Python and required libraries are correctly installed.
- Use the `Failsafe` feature by moving the mouse cursor to the top-left corner of the screen to stop the program.
- If the setup file (`clicker_setups.txt`) is missing or corrupted, the program will create a new one.

## Disclaimer
This program is intended for educational and productivity purposes only. Ensure compliance with any applicable terms of use or policies when automating tasks.

