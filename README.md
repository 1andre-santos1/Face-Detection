Face Detection
===

<p align="center">
<img src="https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg?w=1260&h=750&auto=compress&cs=tinysrgb" width="120" height="100" /><img src="https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?w=1260&h=750&auto=compress&cs=tinysrgb" width="120" height="100" /><img src="https://images.pexels.com/photos/428341/pexels-photo-428341.jpeg?w=1260&h=750&auto=compress&cs=tinysrgb" width="120" height="100" /><img src="https://images.pexels.com/photos/542282/pexels-photo-542282.jpeg?w=1260&h=750&auto=compress&cs=tinysrgb"  width="120" height="100" />
</p>
<p align="center">
<img src="https://images.pexels.com/photos/428331/pexels-photo-428331.jpeg?w=1260&h=750&auto=compress&cs=tinysrgb" width="110" height="90" /><img src="https://images.pexels.com/photos/355164/pexels-photo-355164.jpeg?w=1260&h=750&auto=compress&cs=tinysrgb" width="110" height="90" /><img src="https://images.pexels.com/photos/762020/pexels-photo-762020.jpeg?w=1260&h=750&auto=compress&cs=tinysrgb" width="110" height="90" /><img src="https://images.pexels.com/photos/831993/pexels-photo-831993.jpeg?w=1260&h=750&auto=compress&cs=tinysrgb" width="110" height="90" />
</p>

# Algorithm - Steps #
`This explanation is just an abstract introduction to the algorithm. If you want more information see the See More section below.`

## Get An Image ##
<p align="center">
  <img src="https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg?w=1260&h=750&auto=compress&cs=tinysrgb" width="200" height="180" />
</p>
<p align="left">
 <b><i>This step is pretty straightforward. 
   Here in this application however, the image will be every frame recorded by the webcam.</i></b>

## Convert The Colored Image Into Grayscale ##
<p align="center">
  <img src="https://image.ibb.co/h0YYOS/68747470733a2f2f696d616765732e706578656c732e636f6d2f70686f746f732f3631343831302f706578656c732d70686f746f2d3631343831302e6a7065673f773d3132363026683d373530266175746f3d636f6d70726573732663733d74696e7973726762.jpg" width="200" height="180" />
</p>
<p align="left">
 <b><i>Given the fact that our search for face features will be based on the black and white contrast between the pixels, we need to convert the original colored image into a gray one.</i></b>
</p>

## Shrink The Image ##
<p align="center">
  <img src="https://image.ibb.co/h0YYOS/68747470733a2f2f696d616765732e706578656c732e636f6d2f70686f746f732f3631343831302f706578656c732d70686f746f2d3631343831302e6a7065673f773d3132363026683d373530266175746f3d636f6d70726573732663733d74696e7973726762.jpg" width="100" height="90" />
</p>
<p align="left">
 <b><i>With a smaller image we can search efficiently, at a faster rate, the pixels for the face features. Based on the fact that we will be taking on real time the frames from the webcam, we will need to be sure to take time has an useful resource.</i></b>
</p>

## Detect The Face ##
<p align="center">
  <img src="https://image.ibb.co/c7qzV7/68747470733a2f2f696d616765732e706578656c732e636f6d2f70686f746f732f3631343831302f706578656c732d70686f746f2d3631343831302e6a7065673f773d3132363026683d373530266175746f3d636f6d70726573732663733d74696e7973726762.jpg" width="100" height="90" />
</p>
<p align="left">
 <b><i>In this step the search for the face features will begin on the frame and in some way it will be used. In this application, when a face is encountered in a frame, a box will be drawn indicating it's presence.</i></b>
</p>

## See More ##
`If you want to learn in depth all the processes behind this you can take a look at the papers below.`

[Rapid Object Detection Using a Boosted Cascade of Simple
Features](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf)

[A General Framework For Object Detection](http://ieeexplore.ieee.org/document/710772/)

[Boosting Image Retrieval](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.136.2419&rep=rep1&type=pdf)

# Using This App #
`In this section I will explain how to use this application and how do you run it.`

## Files ##

### [face_detection.py](https://github.com/1andre-santos1/Face-Detection/blob/master/face_detection.py) ### 
`This python script contains all the logic for the application.`

### [haarcascade_frontalface_default.xml](https://github.com/1andre-santos1/Face-Detection/blob/master/haarcascade_frontalface_default.xml) ###
`This xml file contains all the information needed to identify a frontal face. The file was not created by me, you can see the repository where the original file resides here:`
[haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

### [app.rar](https://github.com/1andre-santos1/Face-Detection/blob/master/app.rar) ###
`This rar file contains the application. It was made with pyinstaller from the face_detection script. Download, extract and run the executable inside the folder, and you can start having fun detecting faces!`

### [README.md](https://github.com/1andre-santos1/Face-Detection/blob/master/README.md) ###
`Used to show you this text.`

## Instructions ##

! ` When you run the executable a window will pop up accessing your webcam and your face should be detected by the app. `

! ` Press the 'e' key on your keyboard to exit the application `

! ` If you're having problems detecting your face try lighten up the scene around you or assume a more frontal position towards the webcam `

