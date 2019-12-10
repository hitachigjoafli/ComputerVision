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
Kommer förhoppningsvis snart, tills dess kika på koden i 2.yoloopencamera.py och försök förstå den. Grunden är mycket gjord från 1. men omgjord så det är din webcamera en tittar med.
![Danger](https://github.com/abbjoafli/ComputerVision/blob/master/images/yolo2.PNG?raw=true)

# cmd i mappen
python 1.yoloopencvimage.py --image images/room.png --yolo yolo-coco
python 1.yoloopencvimage.py --image images/danger2.jpg --yolo yolo-danger
python 1.yoloopencvimage.py --image images/dangerbig.jpg --yolo yolo-danger --confidence 0.7

python 1.5.yolotestimage.py  --yolo yolo-legogubbe
python 2.yoloopencamera.py  --yolo yolo-legogubbe

python 1.yoloopencvimage.py --image images/legogang.jpg --yolo yolo-legogubbe