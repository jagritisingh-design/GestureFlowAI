class GestureRecognizer:

    def __init__(self):
        pass

    def recognize(self, fingers):

        if fingers == [0,0,0,0,0]:
            return "FIST"

        elif fingers == [1,1,1,1,1]:
            return "OPEN HAND"

        elif fingers == [0,1,0,0,0]:
            return "INDEX"

        elif fingers == [0,1,1,0,0]:
            return "PEACE"

        elif fingers == [1,0,0,0,0]:
            return "THUMBS UP"

        return "UNKNOWN" 