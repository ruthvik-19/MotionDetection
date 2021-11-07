
# all of the imports for required packages
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2

# parses arrguments
par = argparse.ArgumentParser()
par.add_argument("-v", "--video", help ="to video file")
args = vars(par.parse_args())

# condition for reading from webcame when args is None
if args.get("video", None) is None:
    stream = VideoStream(src=0).start()
    time.sleep(5.0)
else
    stream = cv2.VideoCapture(args["video"])


frameOne = None #first frame of the stream

# while loop used to 
while True:

    frame = vs.read()
    frame = frame if  args.get("video", None) is None
    
    else 
        frame[1]


    if frame is None
        break

    if frameOne is None:
		frameOne = gray
		continue    

    cv2.putText(frame, " Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    cv2.imshow("Feed", frame)
	cv2.imshow("Thresh", thresh)
	key = cv2.waitKey(1) & 0xFF    

    if key == ord("q"):
		break

    # close windows and exit software   
    vs.stop() if args.get("video", None) is None else vs.release()
    cv2.destroyAllWindows()        