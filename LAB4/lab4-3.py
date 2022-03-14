import cv2

if __name__ == '__main__':
    img0 = cv2.imread('images/book_0.JPG',
                      cv2.IMREAD_GRAYSCALE)
    img1 = cv2.imread('images/book_1.JPG',
                      cv2.IMREAD_GRAYSCALE)

    # TODO: Perform SIFT feature detection and description.

    # TODO: Define FLANN-based matching parameters.

    # TODO: Perform FLANN-based matching.
    matches = []

    # Prepare an empty mask to draw good matches.
    mask_matches = [[0, 0] for i in range(len(matches))]

    # Populate the mask based on David G. Lowe's ratio test.
    for i, (m, n) in enumerate(matches):
        if m.distance < 0.7 * n.distance:
            mask_matches[i] = [1, 0]

    # TODO: Draw the matches that passed the ratio test.
    img_matches = None

    # Show the matches.
    cv2.imshow('lab4-3', img_matches)

    cv2.waitKey()
    cv2.destroyAllWindows()
