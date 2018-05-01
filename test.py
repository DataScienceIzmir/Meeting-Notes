import numpy  
import cv2

fotograf = cv2.imread('C:/Users/ado3iz/documents/ip/peakup.jpg')
fotografGri = cv2.cvtColor(fotograf, cv2.COLOR_BGR2GRAY)
cv2.imwrite("C:/Users/ado3iz/documents/ip/peakupGri.jpg",fotografGri)


ret,fotografBW = cv2.threshold(fotografGri,110,240,cv2.THRESH_BINARY) 
cv2.imshow('Binary Fotograf', fotografBW)

cv2.imshow('Orijinal Fotograf', fotograf)
cv2.imshow('Gri tonlarina cevrilmis fotograf', fotografGri)
cv2.imwrite("C:/Users/ado3iz/documents/ip/peakup01.jpg",fotografBW)
cv2.destroyAllWindows()