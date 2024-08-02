import numpy as np

'''
Function to calculate the overlap ratio given the ground-truth and predicted bounding boxes.
'''


# Format of label and output is an ndarray with dim ([1], [2])
# I will calculate a distance between predict and labeled data
def overlapScore(output, label):

    avgScore = 0
    scores = []
    xDist =0;
    yDist = 0;

    for i, _ in enumerate(output):

        xDist += abs(output[i][0] - label[i][0])
        yDist += abs(output[i][1] - label[i][1])

    xDist/=len(output)
    yDist/=len(output)

    return xDist, yDist;

'''
def overlapScore(rects1, rects2):

    avgScore = 0
    scores = []

    for i, _ in enumerate(rects1):

        rect1 = rects1[i]
        rect2 = rects2[i]

        left = np.max((rect1[0], rect2[0]))
        right = np.min((rect1[0]+rect1[2], rect2[0]+rect2[2]))

        top = np.max((rect1[1], rect2[1]))
        bottom = np.min((rect1[1]+rect1[3], rect2[1]+rect2[3]))

        # area of intersection
        i = np.max((0, right-left))*np.max((0,bottom-top))

        # combined area of two rectangles
        u = rect1[2]*rect1[3] + rect2[2]*rect2[3] - i

        # return the overlap ratio
        # value is always between 0 and 1
        score = np.clip(i/u, 0, 1)
        avgScore += score
        scores.append(score)

    return avgScore, scores

'''