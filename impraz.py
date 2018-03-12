import cv2
import numpy

WHITE = 'WHITE'
BLUE = 'BLUE'
RED = 'RED'
YELLOW = 'YELLOW'
GREEN = 'GREEN'
ORANGE = 'ORANGE'

NIR_DICT = {WHITE: 'U',
            BLUE: 'R',
            RED: 'F',
            YELLOW: 'D',
            GREEN: 'L',
            ORANGE: 'B'}

recColors = {WHITE: (255, 255, 255),
             BLUE: (255, 0, 0),
             RED: (0, 0, 255),
             YELLOW: (0, 255, 255),
             GREEN: (0, 255, 0),
             ORANGE: (0, 125, 255)
             }

RANGES = {'H': {'red': (0, 0),
                'green': (0, 0),
                'blue': (0, 0),
                'orange': (0, 0),
                'yellow': (0, 0),
                'white': (90, 120)},
          'S': {'red': (0, 0),
                'green': (0, 0),
                'blue': (0, 0),
                'orange': (0, 0),
                'yellow': (0, 0),
                'white': (0, 0)},
          'V': {'red': (0, 0),
                'green': (0, 0),
                'blue': (0, 0),
                'orange': (0, 0),
                'yellow': (0, 0),
                'white': (0, 0)}}

imgHeight = 480/2
imgWidth = 640/2
recSize = 35
recPos = [((int(imgWidth - recSize * 2.5 - recSize / 2), int(imgHeight - recSize * 2.5 - recSize / 2)), (int(imgWidth - recSize * 2.5 + recSize / 2), int(imgHeight - recSize * 2.5 + recSize / 2))),
          ((int(imgWidth - recSize / 2), int(imgHeight - recSize * 2.5 - recSize / 2)), (int(imgWidth + recSize / 2), int(imgHeight - recSize * 2.5 + recSize / 2))),
          ((int(imgWidth + recSize * 2.5 - recSize / 2), int(imgHeight - recSize * 2.5 - recSize / 2)), (int(imgWidth + recSize * 2.5 + recSize / 2), int(imgHeight - recSize * 2.5 + recSize / 2))),
          ((int(imgWidth - recSize * 2.5 - recSize / 2), int(imgHeight - recSize / 2)), (int(imgWidth - recSize * 2.5 + recSize / 2), int(imgHeight + recSize / 2))),
          ((int(imgWidth - recSize / 2), int(imgHeight - recSize / 2)), (int(imgWidth + recSize / 2), int(imgHeight + recSize / 2))),
          ((int(imgWidth + recSize * 2.5 - recSize / 2), int(imgHeight - recSize / 2)), (int(imgWidth + recSize * 2.5 + recSize / 2), int(imgHeight + recSize / 2))),
          ((int(imgWidth - recSize * 2.5 - recSize / 2), int(imgHeight + recSize * 2.5 - recSize / 2)), (int(imgWidth - recSize * 2.5 + recSize / 2), int(imgHeight + recSize * 2.5 + recSize / 2))),
          ((int(imgWidth - recSize / 2), int(imgHeight + recSize * 2.5 - recSize / 2)), (int(imgWidth + recSize / 2), int(imgHeight + recSize * 2.5 + recSize / 2))),
          ((int(imgWidth + recSize * 2.5 - recSize / 2), int(imgHeight + recSize * 2.5 - recSize / 2)), (int(imgWidth + recSize * 2.5 + recSize / 2), int(imgHeight + recSize * 2.5 + recSize / 2)))]

def getColor(h, s, v):
    if s in range(0, 90):
        return WHITE
    else:
        if h in range(20, 47):
            return YELLOW
        elif h in range(47, 85):
            return GREEN
        elif h in range(85, 155):
            return BLUE
        else:
            if v in range(215, 255):
                return ORANGE
            else:
                return RED

def drawRec(img, pos, color, fill=False):
    thickness = 3
    if fill:
        thickness = -1
    line = cv2.rectangle(frame, pos[0], pos[1], color, thickness)  # BGR
    return line

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.cvtColor(frame, cv2.COLOR_BGR2HSV, frame)
    cube_frame = frame[0:200, 0:200].reshape(40000, 3).T
    h = numpy.median(cube_frame[0])
    s = numpy.median(cube_frame[1])
    v = numpy.median(cube_frame[2])
    for p in recPos:
        drawRec(frame, p, recColors[getColor(h, s, v)])
    cv2.imshow('cyber', frame)

    print(getColor(h, s, v))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()