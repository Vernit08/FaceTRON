import cv2
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

# vid = cv2.VideoCapture(0)
# while(True):
#     ret,frame = vid.read()
#     cv2.imshow('Capture Your Photo',frame)
#     if cv2.waitKey(15) & 0xFF == ord('q'):
#         s = time.time()
#         cv2.imwrite("G:/My Drive/Attendance/Pic%s.jpg" %s,frame)
#         break
# vid.release()
# cv2.destroyAllWindows()