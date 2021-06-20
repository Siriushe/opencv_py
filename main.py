import cv2
import numpy as np

_LABEL_FOR_WHITE = 0
_WHITE_EDGE = 200
_LABEL_INIT = -1;

class pixel:
    gray = 0
    label = _LABEL_INIT
    def __init__(self, t) -> None:
        self.gray = t



_img = cv2.imread('4295.jpg', 0)
_h = _img.shape[0]
_w = _img.shape[1]
_pixels = []
_curLable = _LABEL_FOR_WHITE + 1
_labelRecord= [0]


def updatePixels(curH, curW, label) :
    if curW < 0 or curW >= _w or curH < 0 or curH >= _h :
        return False
    p = _pixels[curH * _w + curW]
    # handle white
    if p.gray >= _WHITE_EDGE:
        p.label = _LABEL_FOR_WHITE
        _labelRecord[_LABEL_FOR_WHITE] = _labelRecord[_LABEL_FOR_WHITE] + 1
        return False

    if p.label != _LABEL_INIT:
        return
    p.label = label
    if len(_labelRecord) <= label:
        _labelRecord.append(1)
    else:
        _labelRecord[label] = _labelRecord[label] + 1

    updatePixels(curH - 1, curW - 1, label)
    updatePixels(curH - 1, curW, label)
    updatePixels(curH - 1 , curW + 1, label)
    updatePixels(curH, curW - 1, label)
    updatePixels(curH, curW + 1, label)
    updatePixels(curH + 1, curW - 1, label)
    updatePixels(curH + 1, curW, label)
    updatePixels(curH + 1, curW + 1, label)
    return True

for i in range(_h):
    for j in range(_w):
        _pixels.append(pixel(_img[i, j]))

for i in range(_h):
    for j in range(_w):
        if _pixels[i * _w + j].label == _LABEL_INIT :
            if updatePixels(i, j, _curLable):
                _curLable += 1
            
        
for i in range(_h):
    for j in range(_w):
        l = _pixels[i * _w + j].label
        if _labelRecord[l] < 100 or l == _LABEL_FOR_WHITE:
            _img[i][j] = 255
            l = 0

cv2.imshow('image',_img)
cv2.waitKey(0)
cv2.destroyAllWindows()