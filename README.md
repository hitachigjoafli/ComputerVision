# Computer Vision

## Table of Contents

- [OpenCV](#opencv)
    - [Grunder](#grunder)
      - [Kul Bonus Rita med webbkameran](#kul%20bonus%20rita%20med%20webbkameran)

### Example 1 Heading

# OpenCV
## Grunder
I grunderna finns det två alternativ ([Open CV Python Tut For Beginners](https://www.youtube.com/watch?v=kdLM6AOd2vc&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=1) och [Afshins Open CV tutorial](https://www.youtube.com/watch?v=izN-NLpS5t8&list=PLiHa1s-EL3vjr0Z02ihr6Lcu4Q0rnRvjm&index=3))  både är väldigt bra, kika och se vilken du gillar och vill följa. 

Gör de delar du tycker verkar spännande på videorna och gå sen vidare, ladda ner exempelkod och experimentera runt, nu ska vi lära oss!

[Codebinds hemsida för kodexempel](http://www.codebind.com/category/python/opencv/)
[Afshins github med kodexempel](https://github.com/ashwin-pajankar/Python-OpenCV3)


### Kul Bonus Rita med webbkameran
[Webcam Paint Application Using OpenCV](https://towardsdatascience.com/tutorial-webcam-paint-opencv-dbe356ab5d6c?), följ guiden och lär dig göra ett eget paint-program med webbkameran. Titta i files/Webcam_Paint_OpenCV för fungerande exempelkod att ha som referens. Den på hans github, fungerade inte senast jag tittade.
Exempel på delar man kan utveckla:
- Lägga till fler färger
- Ha för valda objekt som skapas
- spara ner som en bild


## Road Recognition
För road recognition har vi också två val (vilken lyx!). 

- Det första alternativet är att man fortsätter med programming Knowledges serie och hoppar till  video 30?(Kan vara redan 28) Värt att veta om denna är att jag inte har kikat på den själv och vet inte kvaliteteten den håller.

- Det andra alternativet är att man följer Self-Driving Car video serien (filväg nedan). Den är mycket bra i min mening, kan rekomenderas starkt!
`Teams\TEBLOCK1X0s\Files\TEBLOCK\Resurser\Videor\Self-Driving Car\5. Computer Vision Finding Lane Lines`

## YOLO!! You only look once (Object detection)
[YOLO](https://pjreddie.com/darknet/yolo/) är en algoritm för att finna objekt på en bild,video eller live-ström. denna bygger på neurala nätverk och fungerar så att den kolla på bilden i helhet och tittar sedan endast på delar som ändras. Detta gör att den är mycket snabbare och än algoritmer som tittar på varje pixel i bilden varje gång.
Det försa vi ska göra är att ladda ner ett förtränat set med yolo object. Dessa kallas Coco och kan identifera 80 olika förbestämda objekt som telefon, flygplan, person osv. Vi ska senare titta på hur vi kan träna egna objekt, samt hur vi kan exportera dem till mikrokontrollen.
### [Använd yolo!](https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/)
Följ guiden i länken ovan, här är [en till bra resurs](https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/) som kan ge extra koll.

Föj guiden, för att starta koden så rekomenderar jag att man gör som på bilden nedan och skriver in följande kod (exempel finns längre ned).
`python kodnamn.py --image images/bild.biltyp --yolo yolomapp`

![Öppna CMD](https://github.com/abbjoafli/ComputerVision/blob/master/images/opencmd.png?raw=true)
####   Exmpelkod
Exmpelkod ligger i submappen yolo-openCV-detector här på github, där finns tre olika typer av yolo set:
- yolo-coco, samma som i exemplet.
- yolo-danger, tränade på att se farliga material skyltar.
- yolo-legogubbe- tränad på att känna igen legogubbar.

Förövrigt finns det en mapp med exempelbilder som man kan testa yolon på.
I settet legogubbar finns flera olika vikter, testa gärna flera av dem genom att byta namn på den man vill testa till yolo.weights, blir det någon skillnad?
Det finns även kod för det han gör i guiden och två fortsättningar:

[1.yoloopencvimage.py](https://github.com/abbjoafli/ComputerVision/blob/master/yolo-openCV-detector/1.yoloopencvimage.py)
[1.5.yolotestimage.py](https://github.com/abbjoafli/ComputerVision/blob/master/yolo-openCV-detector/1.5.yolotestimage.py)
[2.yoloopencamera.py](https://github.com/abbjoafli/ComputerVision/blob/master/yolo-openCV-detector/2.yoloopencamera.py)

Fortsättningarna går jag igenom [här(yolo-openCV-detector/README)](https://github.com/abbjoafli/ComputerVision/blob/master/yolo-openCV-detector/README.md).
![yolo1](https://github.com/abbjoafli/ComputerVision/blob/master/images/yolo1.PNG?raw=true)


#### Kommandon
```cmd
python 1.yoloopencvimage.py --image images/room.png --yolo yolo-coco
python 1.yoloopencvimage.py --image images/danger2.jpg --yolo yolo-danger
python 1.yoloopencvimage.py --image images/dangerbig.jpg --yolo yolo-danger --confidence 0.7
//--yolo yolo-danger --confidence 0.7 Fungerar även för 1,5 och två
python 1.5.yolotestimage.py  --yolo yolo-legogubbe
python 2.yoloopencamera.py  --yolo yolo-legogubbe

python 1.yoloopencvimage.py --image images/legogang.jpg --yolo yolo-legogubbe
```


### Träna eget
#### [Hitta bilder ](https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/)

# OpenMV

## Köra Yolo på MAIX Dock (mikrokontroll)
![MAiX Dock](https://wiki.sipeed.com/assets/dan_dock_1.png)
För att köra Yolo på MAIX Dock så måste man följa följande steg.
1. Ladda ner kflash_gui
`Teams\TEBLOCK1X0s\Files\TEBLOCK\Årskurs 2\Artificel inteligens\Computer Vision\MAIXPY (Sipeed)`
2. Ladda ner och installera senaste versionen av  maixpy-ide-windows(0.2.4 har vi i mappen).
`Teams\TEBLOCK1X0s\Files\TEBLOCK\Årskurs 2\Artificel inteligens\Computer Vision\MAIXPY (Sipeed)\kmodels`
3. Ladda ner och flasha senaste versionen av maixpy (v0.5.0_0_gae433e8 har vi i mappen) genom att öppna Kflash_gui.
![Flash Bin](https://github.com/abbjoafli/ComputerVision/blob/master/images/flash_bin.PNG?raw=true)
4. Ladda ner och flasha din kmodel till rätt plats i mikrokontrollens minne eller till ett sdkort (se lista nedan)
![Flash Kmodel](https://github.com/abbjoafli/ComputerVision/blob/master/images/flash_kmodel.PNG?raw=true)

### Minnesplats och maixpy version

- 20class.kmodel= 0x500000 - vanliga
- racoon.kmodel= 0x600000 - vanliga
- lego.kmodel= 0x600000 - minimum_with_ide_support

#### Hur ska man tänka?
Tänk att dina egenskapade kmodels bör vara på plats 0x600000 och att de ofta bör ha minimum_with_ide_support
 då de är större än de förskapade sakerna.

5. Öppna MAiX IDE och anslut till mikrokontrollern via den gröna knappen i vänstra hörnet (se bild). När den knappen har blivit röd så är du ansluten och kan trycka på playknappen under. När den har blivit ett rött kryss så är koden överförd till mikrokontrollen och den körs. Du kan nu använda din mikrokontroll och glöm inte att kika i serialmonitorn(också med på bilden, längst ner i mitten).
![Anslut](https://github.com/abbjoafli/ComputerVision/blob/master/images/Connect.PNG?raw=true)

#### Om den inte vill ansluta vad kan det vara för fel då?
- Ett fel kan vara att du har bränt det till fel flashdel, t.ex 0x60000 istället för 0x600000 eller 0x500000, titta noga och gör om.
- Man kan ha för stor kmodel och måste använda maixpy_minimum_with_ide_support eller maixpy_minimum istället för vanliga maixpy.




![Legogubbe](https://github.com/abbjoafli/ComputerVision/blob/master/images/legogubbe2.png?raw=true)


## Google Colab
[Keras to Kmodel](https://colab.research.google.com/drive/1WHguFsueli-kBhyfcb5dDnZ66urTlFXU)
