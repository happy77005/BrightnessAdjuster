import cv2
import numpy as np
import screen_brightness_control as sbc

# Function to capture light intensity from the webcam
def capture_light_intensity():
    cap = cv2.VideoCapture(0)  # Use 0 for inbuilt webcam
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    ret, frame = cap.read()
    if ret:
        # Convert frame to grayscale to measure intensity
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        light_intensity = np.mean(gray_frame)  # Average intensity
    else:
        light_intensity = None
    
    cap.release()
    cv2.destroyAllWindows()
    return light_intensity

# Function to determine brightness level based on light intensity
def classify_brightness(light_intensity):
    if light_intensity is None:
        return None
    elif light_intensity < 70:
        return 30
    elif light_intensity < 100:
        return 40
    elif light_intensity < 111:
        return 40
    elif light_intensity < 121:
        return 40
    elif light_intensity < 131:
        return 50
    elif light_intensity < 141:
        return 60
    elif light_intensity < 151:
        return 70
    elif light_intensity < 161:
        return 80
    elif light_intensity < 171:
        return 90
    else:
        return 92

# Function to adjust screen brightness
def adjust_brightness(brightness_level):
    if 0 <= brightness_level <= 100:
        sbc.set_brightness(int(brightness_level))  # Adjust system brightness
    else:
        print("Brightness level should be between 0 and 100")

# Function to automatically adjust brightness based on light intensity
def auto_adjust_brightness():
    light_intensity = capture_light_intensity()
    if light_intensity is not None:
        suggested_brightness = classify_brightness(light_intensity)
        if suggested_brightness is not None:
            adjust_brightness(suggested_brightness)
            print(f"Light Intensity: {light_intensity} → Adjusted Brightness: {suggested_brightness}")

# Main function to interactively adjust brightness
def run_brightness_adjuster():
    while True:
        current_brightness = sbc.get_brightness(display=0)[0]  # Get current brightness
        print(f"Current brightness: {current_brightness}")
        user_input = input("Enter 'a' for auto-adjust, + or - to manually adjust brightness, or 'e' to exit: ")
        
        if user_input.lower() == 'e':
            print("Exiting brightness adjuster.")
            break
        elif user_input == 'a':
            auto_adjust_brightness()
        elif user_input == '+':
            new_brightness = min(100, current_brightness + 10)
            adjust_brightness(new_brightness)
            print(f"Brightness adjusted to {new_brightness}")
        elif user_input == '-':
            new_brightness = max(0, current_brightness - 10)
            adjust_brightness(new_brightness)
            print(f"Brightness adjusted to {new_brightness}")
        else:
            print("Invalid input. Please enter 'a', +, -, or 'e' to exit.")
            continue

if __name__ == "__main__":
    run_brightness_adjuster()
