import os.path as path

import cv2
from numpy.core.fromnumeric import resize

if __name__ == '__main__':
    crazydog = cv2.imread(path.join('images', 'crazydog.jpg'))
    puipui = cv2.imread(path.join('images', 'puipui.jpg'))

    # TODO: merge two images
    puipui=cv2.flip(puipui,1)
    puipui=cv2.resize(puipui,dsize=(160,160))
    crazydog[40:200,235:395,:]=cv2.addWeighted(crazydog[40:200,235:395,:],1,puipui,0.5,0.)
    
    #cv2.imshow('result1',puipui)
    cv2.imshow('result2', crazydog)

    cv2.waitKey()
    cv2.destroyAllWindows()
