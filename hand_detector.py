from cvzone.HandTrackingModule import HandDetector


class HandTracker:

    def __init__(self):

        self.detector = HandDetector(
            staticMode=False,
            maxHands=1,
            detectionCon=0.7,
            minTrackCon=0.7
        )

    def findHands(self, img):

        hands, img = self.detector.findHands(img)

        return hands, img

    def fingersUp(self, hand):

        return self.detector.fingersUp(hand) 