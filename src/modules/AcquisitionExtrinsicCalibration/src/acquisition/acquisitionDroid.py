import cv2


def dropcam():
    thermalCamera = cv2.VideoCapture()
    #thermalCamera.open('http://192.168.1.4:4747/videostream.cgi?.mjpg')
    thermalCamera.open(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = thermalCamera.read()
        #print cap.isOpened(), ret
        if frame is not None:
            # Display the resulting frame
            cv2.imshow('frame',frame)
            # Press q to close the video windows before it ends if you want
            if cv2.waitKey(22) & 0xFF == ord('q'):
                break
        else:
            print("Frame is None")
            break

    # When everything done, release the capture
    thermalCamera.release()
    cv2.destroyAllWindows()
    print("Video stop")


def zoom(image):
    print(image.shape)
    height, width = image.shape[:2]
    crop_img = image[100:height-100, 100:width-100]
    print(crop_img.shape)
    newImage = cv2.resize(
        crop_img, (int(width), int(height)), cv2.INTER_CUBIC)
    print(newImage.shape)
    cv2.imshow('original', image)
    cv2.imshow('newImage', newImage)
    cv2.waitKey(0)
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()


dropcam()
