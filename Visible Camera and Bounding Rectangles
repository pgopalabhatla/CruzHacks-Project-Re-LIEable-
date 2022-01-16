import cv2 

cv2.namedWindow("preview")
vc = cv2. VideoCapture(O)

if vc.isOpened(): 
  rval, frame = vc.read
else:
  rival = False


  while rval:
    cv2.imshow("preview",frame)
    rval, frame = vc.read()

 cv2.destoryWindow("preview")
    vc.release()
setup(
    name='lie_to_me',
    packages=['lie_to_me'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)

im = cv2.imread(whateverthedatais)
somecolor= cv2. cvtColor (im,cv2.Color_whatevercoloryouwant)
contours, hierarchy = cv2.findContours(somecolor,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2:]
idx =0 
for cnt in contours:
    idx += 1
    x,y,w,h = cv2.boundingRect(cnt)
    roi=im[y:y+h,x:x+w]


   cv2.imwrite(str(idx) + 'data', roi)
    #cv2.rectangle(im,(x,y),(x+w,y+h),(200,0,0),2)
cv2.imshow('whaterverdata',im)
cv2.waitKey(0)
