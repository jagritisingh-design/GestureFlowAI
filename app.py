import cv2
import math

from hand_detector import HandTracker
from gesture_recognizer import GestureRecognizer
from virtual_mouse import VirtualMouse


cap = cv2.VideoCapture(0)

tracker = HandTracker()
recognizer = GestureRecognizer()
mouse = VirtualMouse()


while True:

    success, img = cap.read()

    if not success:
        break

    hands, img = tracker.findHands(img)

    gesture = "NO HAND"

    if hands:

        hand = hands[0]

        lmList = hand["lmList"]

        fingers = tracker.fingersUp(hand)

        gesture = recognizer.recognize(fingers)

        # Index Finger Tip
        x, y, z = lmList[8]

        # Thumb Tip
        thumb_x, thumb_y, _ = lmList[4]

        frame_height, frame_width, _ = img.shape

        # Move Mouse
        if gesture == "INDEX":
            mouse.move(x, y, frame_width, frame_height)

        # Pinch Distance
        distance = math.hypot(
            x - thumb_x,
            y - thumb_y
        )

        # Left Click
        if gesture == "INDEX" and distance < 35:

             mouse.click()

             cv2.putText(
                 img,
                 "LEFT CLICK",
                 (20, 140),
                 cv2.FONT_HERSHEY_SIMPLEX,
                 1,
                 (0, 0, 255),
                 3
        )

        # Draw Index Finger
        cv2.circle(
            img,
            (x, y),
            12,
            (255, 0, 255),
            cv2.FILLED
        )

        # Draw Thumb
        cv2.circle(
            img,
            (thumb_x, thumb_y),
            12,
            (0, 255, 255),
            cv2.FILLED
        )

        # Draw Line Between Thumb & Index
        cv2.line(
            img,
            (x, y),
            (thumb_x, thumb_y),
            (255, 255, 0),
            3
        )

        # Show Distance
        cv2.putText(
            img,
            f"Distance: {int(distance)}",
            (20, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

    # Display Gesture
    cv2.putText(
        img,
        f"Gesture: {gesture}",
        (20, 45),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("GestureFlow AI", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows() 