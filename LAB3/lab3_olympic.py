import cv2
import numpy as np

if __name__ == '__main__':
    symbol = np.zeros((400, 700, 3), dtype=np.uint8)

    # TODO: change to white background and draw circles in symbol

    symbol[:,:,:]=255
    
    cv2.circle(symbol, (350, 160), 70, (0, 0, 0), thickness=3)
    cv2.circle(symbol, (210, 160), 70, (255, 0, 0), thickness=3)
    cv2.circle(symbol, (490, 160), 70, (0, 0, 255), thickness=3)
    cv2.circle(symbol, (420, 230), 70, (0, 255, 0), thickness=3)
    cv2.circle(symbol, (280, 230), 70, (0, 255, 255), thickness=3)

    cv2.imshow('olympic symbol', symbol)

    cv2.waitKey()
    cv2.destroyAllWindows()
