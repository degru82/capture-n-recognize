"""화면을 캡쳐하고 인식하는데 걸리는 시간을 측정
"""
import time
import pyautogui
import pytesseract

# Those values in box variable should be updated
# according to the users' circumstances
box = (880, 430, 985, 470)
time_begin = time.time()

# STEP 1. Capture the full-screen
# i.e. ./full_screenshot.png
# TODO: Search web for capturing screen partially
screenshot = pyautogui.screenshot()
time_captured = time.time()

# STEP 2. Crop the image to focus on index
# i.e. ./croped.png
cropped = screenshot.crop(box)
time_cropped = time.time()

# STEP 3. Pass the cropped image to OCR process
char_recognized = pytesseract.image_to_string(cropped)
time_ocr = time.time()

# STEP 4. Recognized string to floating point number
kospi_index = float(char_recognized.strip('').replace(',', ''))
time_converted = time.time()

# STEP 5. Show the time elapsed between steps
SEC_TO_MILI = 1_000
print(f'''
----------------------------
KOSPI-INDEX = {kospi_index}

total: {(time_converted - time_begin)*SEC_TO_MILI:.3f} ms
    time for screen capture: {(time_captured - time_begin)*SEC_TO_MILI:.3f} ms
    time for cropping: {(time_cropped - time_captured)*SEC_TO_MILI:.3f} ms
    time for character recognition: {(time_ocr - time_cropped)*SEC_TO_MILI:.3f} ms
    time for converting: {(time_converted - time_ocr)*SEC_TO_MILI:.3f} ms
''')
