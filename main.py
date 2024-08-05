import keyboard
import pyautogui

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.025


def toggle_running():
    global running
    running = not running
    print(f"Bot {'running' if running else 'stopped'}")


if __name__ == '__main__':
    running = False

    keyboard.add_hotkey('space', toggle_running)
    print("Press <SPACE> key for run/stop")

    while not keyboard.is_pressed('esc'):
        if running:
            pyautogui.click()
