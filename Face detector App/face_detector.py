import cv2
"""
The three steps involved:
1. Grab a bunch of image data
2. Make them all black and white
3. Train your model
"""
# Step 1:
trained_face_data = cv2.CascadeClassifier('data.xml')

img =cv2.imread('group.png')
# cv2.imshow('Ronald Face detector', img)
# cv2.waitKey()

# step 2:
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Ronald Face detector', grayscaled_img)
# cv2.waitKey()

# step 3:
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
# cv2.rectangle(img, (340, 102), (550, 300), (0, 255, 0), 2)

for i in range(len(face_coordinates)):
    (x, y, w, h) = face_coordinates[i]
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255 , 0), 2)
print(face_coordinates)
cv2.imshow('Ronald Face detector', img)
cv2.waitKey()
print("Code completed") 