import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread("images/star.jpg")
    #cv2.imshow("original", img)
    img_h = img.shape[0]
    img_w = img.shape[1]
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY ) [1]

    # TODO: DO the image processing, clean up unwanted background
    #gray_img = cv2.Canny(gray_img, 200, 200)
    clean = gray_img

    # Extract contours
    contours, hierarchy = cv2.findContours(clean, cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    # TODO: Extract the contours from stat shape, contours is a list of np.ndarray
    for cnt in contours:
        if cv2.contourArea(cnt) > 10000 and cv2.contourArea(cnt)<20000:
            star = cnt
            
    img = cv2.drawContours(img, [star], -1, (0, 0, 255), 2)  # The contour argument must be a list
  
    cv2.imshow("lab4-1", img)

    cv2.waitKey()
    cv2.destroyAllWindows()
