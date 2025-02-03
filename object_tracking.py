import cv2


cap = cv2.VideoCapture('video.mp4')

tracker = cv2.TrackerCSRT_create()


ret, frame = cap.read()
roi = cv2.selectROI("Tracking", frame, fromCenter=False, showCrosshair=True)


tracker.init(frame, roi)

while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    
    success, roi = tracker.update(frame)
    
    if success:
        
        x, y, w, h = [int(i) for i in roi]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Tracking failed", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Object Tracking", frame)

    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
