import pyautogui
import time

pyautogui.FAILSAFE = False


class VirtualMouse:

    def __init__(self):

        self.screen_width, self.screen_height = pyautogui.size()

        self.prev_x = 0
        self.prev_y = 0

        self.smoothening = 7

        # Click cooldown
        self.last_click_time = 0
        self.click_delay = 0.4

    def move(self, x, y, frame_width, frame_height):

        screen_x = int((x / frame_width) * self.screen_width)
        screen_y = int((y / frame_height) * self.screen_height)

        curr_x = self.prev_x + (screen_x - self.prev_x) / self.smoothening
        curr_y = self.prev_y + (screen_y - self.prev_y) / self.smoothening

        pyautogui.moveTo(curr_x, curr_y)

        self.prev_x = curr_x
        self.prev_y = curr_y

    def click(self):

        current_time = time.time()

        if current_time - self.last_click_time > self.click_delay:

            pyautogui.click()

            self.last_click_time = current_time   