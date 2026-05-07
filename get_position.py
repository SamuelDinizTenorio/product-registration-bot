import pyautogui
import time

def get_mouse_position():
    print("Point the mouse at the desired location...")
    print("Starting countdown: 5", end="...", flush=True)
    time.sleep(1)
    print("4", end="...", flush=True)
    time.sleep(1)
    print("3", end="...", flush=True)
    time.sleep(1)
    print("2", end="...", flush=True)
    time.sleep(1)
    print("1", end="...", flush=True)
    time.sleep(1)
    
    # Get coordinates
    x, y = pyautogui.position()
    
    print(f"\n\n✅ Position captured!")
    print(f"X: {x} | Y: {y}")
    print("-" * 25)
    print(f"Update your .py file with: pyautogui.click(x={x}, y={y})")

if __name__ == "__main__":
    get_mouse_position()