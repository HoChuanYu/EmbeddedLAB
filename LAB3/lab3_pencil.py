import os.path as path

import cv2


def convert_to_pencil_sketch(rgb_image):
    # TODO: finish this filter
    img_gray = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)
    img_blur=cv2.GaussianBlur(img_gray,(21,21),0,0)
    rgb_image = cv2.divide(img_gray, img_blur, scale=256)


    result = rgb_image
    return result


if __name__ == '__main__':
    img = cv2.imread(path.join('images', 'Lenna.jpg'))
    sketch = convert_to_pencil_sketch(img)

    cv2.imshow("Sketch", sketch)

    cv2.waitKey()
    cv2.destroyAllWindows()
