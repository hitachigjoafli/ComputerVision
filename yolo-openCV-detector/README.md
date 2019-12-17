# 1.5.yolotestimage.py
Skillnaderna från denna fil och den ni gjorde genom guiden(1.yoloopencvimage.py) är inte stora. Ska man vara krass så det vi gör är att vi loopar igenom hela bild mappen istället för att välja ut en specifik bild och att vi sparar bilden med labeln i en egen mapp (out).
## Rad 19 - Välj output path
Lägg till följande efter rad 19. Vad en gör är att den väljer var vi ska spara våra outputbilder.
```python
ap.add_argument(
    '-o',
    '--output_path',
    help='path to output test images, defaults to images/out',
    default='images/out')
```
## Rad 41 - Skapa outputpath loopa igenom bilder
Vi skapar nu på rad 41 vår output mapp om den inte finns. Efter det så ändrar vi image_path så den tar varje bild i bilder. Efter det så tittar vi om det är en .jpg bild, man kan om man vill lägga till stöd för .png .JPEG och annat eller ta bort ifsatsen helt. sen läser vi in bilden.
```python

#skapar outputpath
output_path = os.path.expanduser(args["output_path"])
if not os.path.exists(output_path):
        print('Creating output path {}'.format(output_path))
        os.mkdir(output_path)

#Loopar igenom bilder 
image_path = os.path.expanduser(args["image"])

for image_file in os.listdir(image_path):
    if image_file[-4:]==".jpg":
        print(image_path+"/"+image_file)
        
                # load our input image and grab its spatial dimensions
        image = cv2.imread(image_path+"/"+image_file)
```

Det man kan göra efter det här är att markera hela resterande koden och tabba in två nivåer, då följer allt med ifsatsen och körs för varje object i mappen.

## Rad 124 - Spara bild
Här skriver vi ut den nya bilden med ruta, label och allt och visar sedan  upp den


 ```python
ap.add_argument(
                cv2.imwrite(os.path.join(output_path, image_file), image)
                cv2.imshow("Image", image)
```


Voila! nu ska koden köras på alla bilder i din valda bild mapp och spara dem i en output mapp, kul!
![Legogubbe](https://github.com/abbjoafli/ComputerVision/blob/master/images/yolo1.5.PNG?raw=true)

# 2.yoloopencamera.py
Grunden är mycket lik 1. men omgjord så det är din webkamera du använder istället.

## Ladda in
Vi börjar med att importera de bibliotek vi ska använda och skapar seda nen argparser där vi begär in yolomappen, confidence och threshold. Standard värden sätts på de två sistnämnda och den första är required att skickas in.
Efter detta så sätts en input width och höjd på kameran. 
```python
import cv2 as cv
import numpy as np
import argparse
import os


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-y", "--yolo", required=True,
	help="base path to YOLO directory")
ap.add_argument("-c", "--confidence", type=float, default=0.25,
	help="minimum probability to filter weak detections")
ap.add_argument("-t", "--threshold", type=float, default=0.40,
	help="threshold when applying non-maxima suppression")
args = vars(ap.parse_args())
#Write down conf, nms thresholds,inp width/height
confThreshold = args["confidence"]
nmsThreshold = args["threshold"]
inpWidth = 416
inpHeight = 416

#Väljer mapp att ta yolo data ifrån
folder= args["yolo"]

```

Efter detta så hämtar vi classfilen(yolo.names) från yolomappen och sedan config-filen (yolo.cfg) och yolo.weights (vikten). 

```python
#Load names of classes and turn that into a list
classesFile = os.path.sep.join([folder, "yolo.names"]) 
classes = None

with open(classesFile,'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

#Model configuration
modelConf =  os.path.sep.join([folder, "yolo.cfg"]) 
modelWeights =  os.path.sep.join([folder, "yolo.weights"])  
```

## Hitta objektet
Om du tittar på rad 64-101 i 1.yoloopencvimage.py så ser du att den ser nästan identisk ut med metoden nedan bara med mindre skillnader. Om du vill kan du med några få ändringar använda den istället för koden jag har nedan då de gör samma sak fast på olika sätt.

```python
def postprocess(frame, outs):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]

    classIDs = []
    confidences = []
    boxes = []


    

    for out in outs:
        for detection in out:
            
            scores = detection [5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            if confidence > confThreshold:
                centerX = int(detection[0] * frameWidth)
                centerY = int(detection[1] * frameHeight)

                width = int(detection[2]* frameWidth)
                height = int(detection[3]*frameHeight )

                left = int(centerX - width/2)
                top = int(centerY - height/2)

                classIDs.append(classID)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    indices = cv.dnn.NMSBoxes (boxes,confidences, confThreshold, nmsThreshold )

    indices = cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    for i in indices:
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        
        drawPred(classIDs[i], confidences[i], left, top, left + width, top + height)

```
## Rita ut fyrkant och label
Denna metod ritar ut fyrkanten med labeln. Denna gör samma sak som rad 120-124 på lite annat sätt.
```python
def drawPred(classId, conf, left, top, right, bottom):
    # Draw a bounding box.
    cv.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)

    label = '%.2f' % conf

    # Get the label for the class name and its confidence
    if classes:
        assert (classId < len(classes))
        label = '%s:%s' % (classes[classId], label)

    #A fancier display of the label from learnopencv.com 
    # Display the label at the top of the bounding box
    #labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    #top = max(top, labelSize[1])
    #cv.rectangle(frame, (left, top - round(1.5 * labelSize[1])), (left + round(1.5 * labelSize[0]), top + baseLine),
                 #(255, 255, 255), cv.FILLED)
    # cv.rectangle(frame, (left,top),(right,bottom), (255,255,255), 1 )
    #cv.putText(frame, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 1)
    cv.putText(frame, label, (left,top), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
```

## Hämta labeln
Denna tar fram vilken label det är som ska visas, den får fram det från sista layeret i det neurala nätverk.
```python
def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
   
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
```
## Skapar fönster
Denna skapar fönsteret som ska visa webkameran.
```python
#Set up the net

net = cv.dnn.readNetFromDarknet(modelConf, modelWeights)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)


#Process inputs
winName = 'OpenCV'
cv.namedWindow(winName, cv.WINDOW_NORMAL)
cv.resizeWindow(winName, 1000,1000)
```
## Starta inspeling
Startar inspelning och börjar leta efter objekt i kameran.
```python
cap = cv.VideoCapture(0)

while cv.waitKey(1) < 0:

    #get frame from video
    hasFrame, frame = cap.read()

    #Create a 4D blob from a frame
    
    blob = cv.dnn.blobFromImage(frame, 1/255, (inpWidth, inpHeight), [0,0,0], 1, crop = False)

    #Set the input the the net
    net.setInput(blob)
    outs = net.forward (getOutputsNames(net))


    postprocess (frame, outs)

    #show the image
    cv.imshow(winName, frame)
```


![Danger](https://github.com/abbjoafli/ComputerVision/blob/master/images/yolo2.PNG?raw=true)

# cmd i mappen
python 1.yoloopencvimage.py --image images/room.png --yolo yolo-coco
python 1.yoloopencvimage.py --image images/danger2.jpg --yolo yolo-danger
python 1.yoloopencvimage.py --image images/dangerbig.jpg --yolo yolo-danger --confidence 0.7

python 1.5.yolotestimage.py  --yolo yolo-legogubbe
python 2.yoloopencamera.py  --yolo yolo-legogubbe

python 1.yoloopencvimage.py --image images/legogang.jpg --yolo yolo-legogubbe