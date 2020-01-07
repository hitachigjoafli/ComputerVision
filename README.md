# Computer Vision

## Table of Contents

- [Computer Vision](#computer-vision)
  - [Table of Contents](#table-of-contents)
- [OpenCV](#opencv)
  - [Grunder](#grunder)
    - [Kul Bonus Rita med webbkameran](#kul-bonus-rita-med-webbkameran)
  - [Road Recognition](#road-recognition)
  - [YOLO!! You only look once (Object detection)](#yolo-you-only-look-once-object-detection)
    - [Använd yolo!](#anv%c3%a4nd-yolo)
      - [Länkar till vikterna](#l%c3%a4nkar-till-vikterna)
      - [Exempelkod](#exempelkod)
      - [Kommandon](#kommandon)
- [Google Colab](#google-colab)
  - [Träna yolo i molnet med keras](#tr%c3%a4na-yolo-i-molnet-med-keras)
    - [Video där jag går igenom vad som händer i keras på google colab](#video-d%c3%a4r-jag-g%c3%a5r-igenom-vad-som-h%c3%a4nder-i-keras-p%c3%a5-google-colab)
- [Skapa eget yolo-dataset](#skapa-eget-yolo-dataset)
  - [Hitta bilder ](#hitta-bilder)
  - [Train Yolo2 with custom objects](#train-yolo2-with-custom-objects)
    - [För att köra i karas](#f%c3%b6r-att-k%c3%b6ra-i-karas)
      - [Bild endelse](#bild-endelse)
      - [Label konverterare](#label-konverterare)
    - [Ladda upp](#ladda-upp)
      - [Förklaring](#f%c3%b6rklaring)
- [OpenMV](#openmv)
  - [Köra Yolo på MAIX Dock (mikrokontroll)](#k%c3%b6ra-yolo-p%c3%a5-maix-dock-mikrokontroll)
    - [Minnesplats och maixpy version](#minnesplats-och-maixpy-version)
      - [Hur ska man tänka?](#hur-ska-man-t%c3%a4nka)
      - [Om den inte vill ansluta vad kan det vara för fel då?](#om-den-inte-vill-ansluta-vad-kan-det-vara-f%c3%b6r-fel-d%c3%a5)
  - [Road following](#road-following)

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

Filerna guiden pratar om finns i [Githubben Computer Vision](https://github.com/abbjoafli/ComputerVision/tree/master/yolo-openCV-detector/yolo-coco), det kan vara lättare att ladda ner dem därifrån.
#### Länkar till vikterna
Lägg dessa i deras respektive mapp, Coco i yolo-coco osv.
[Coco vikt](https://abbindgym-my.sharepoint.com/:u:/g/personal/joakim_flink_abbindustrigymnasium_se/EVzwihUKtSBEhbz4aMU2Ma0BPY18gIG2lA-_lh_YnvB-fA?e=JroeFG)
[Danger vikt](https://abbindgym-my.sharepoint.com/:u:/g/personal/joakim_flink_abbindustrigymnasium_se/EZZcHUe-l2xHjSj_lGcZ70wB3M0PIetSv7KP111wJpSRnA?e=9ie4Ir)
[Lego vikt](https://abbindgym-my.sharepoint.com/:u:/g/personal/joakim_flink_abbindustrigymnasium_se/EWh3iCUNJZBMp9D7I68OlpIB9VMzScAviDzkZJ3R8QBp3w?e=hivBVs)

Föj guiden, för att starta koden så rekomenderar jag att man gör som på bilden nedan och skriver in följande kod (exempel finns längre ned).
`python kodnamn.py --image images/bild.biltyp --yolo yolomapp`

![Öppna CMD](https://github.com/abbjoafli/ComputerVision/blob/master/images/opencmd.png?raw=true)
####   Exempelkod
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
# Google Colab
## Träna yolo i molnet med keras
I detta avsnitt ska vi testa träna yolo, detta ska vi göra i molnet så sparar vi på vår egna dators datakraft. I vårt fall ska vi använda Google Colabs vilket är ett verktyg som kör pythonkod liknande jupyter notebook på googles servrar. Där får man 12 gb ram och kan använda denna virtuella maskinen i 12 timmar innan den startas om. För att träna saker längre än tolv timmar kan man spara sina vikter mellan varven och starta upp igen när maskinen startats om.

Vi ska följa en [guide](https://www.instructables.com/id/Object-Detection-With-Sipeed-MaiX-BoardsKendryte-K/) som lär oss hur man gör en yolo vikt som kan känna igen tvättbjörnar. Ni följer instruktionerna i guiden men gör fet via google, se länken nedan.

För detta behöver du först skapa ett googlekonto om du inte redan har ett och gå sedan in på länken här([Keras to Kmodel](https://colab.research.google.com/drive/1WHguFsueli-kBhyfcb5dDnZ66urTlFXU)).

Gör det först för racoon datasettet, testa sedan ändra om så du kan göra det för legogubbarna.

### [Video där jag går igenom vad som händer i keras på google colab](https://web.microsoftstream.com/video/eddd21fe-f454-48f0-8c5b-c44d3c07f9e4) 


# Skapa eget yolo-dataset
Det du vill tänka på när du gör ditt eget datasett är att få ut det mesta av det, om du tränar det att se hästar vill du inte bara ha exempel på bruna hästar för då kanske den inte förstår att en vit häst är en häst. Du vill inte heller ha bara bilder på ensamma hästar för då kanske settet inte förstår att det kan vara flera hästar på samma bild. Du vill inte heller ha att alla hästar står från samma håll för då tror AIn att det är enda sättet hästar står på och alla som står annorlunda är då inte hästar. Lego exemplet är bra exempel att titta på, försök se fel i testbilderna som lego-settet missar och fundera varför.

## [Hitta bilder ](https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/)
Söktips
```
site:https://brickset.com/minifigs
site:http://www.collectibleminifigs.com
python download_images.py --urls urls.txt --output images
```
## [Train Yolo2 with custom objects](https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/)
Denna guide lär dig albela ett dataset på NFCA artiklar. Den har redan en färdig bildsamling som du kan använda för att testa köra koden med.

När du ska skapa din egen data så är den här[ yolo annotation tool](https://medium.com/@manivannan_data/yolo-annotation-tool-new-18c7847a2186)  mycket bra så kör med den istället för den som rekomenderas i guiden.

Istället för main.py i artikeln så använd den här, [main.py](https://github.com/abbjoafli/ComputerVision/blob/master/files/main.py) den är omgjord för python 3, se till att ha laddat ner alla bibliotek via pip för att få koden att fungera!
När programmet är öppnat så måste du se till att ha bilderna liggande i en mapp som heter images och inuti en submapp som heter det du vill kalla ditt data set. Exempel images/bilar/volvo1.jpg, images/bilar/volvo2.jpg... Då kan du sedan skriva in bilar i rutan i programmet så kommer den gå igenom alla bilder i mappen.

`python main.py`

![Images example](https://github.com/abbjoafli/ComputerVision/blob/master/images/images.PNG?raw=true)

### För att köra i karas
#### Bild endelse
I karas måste bilderna vara av filtypen .JPEG för att kunna tränas. 
För att göra om bilder till .JPEG istället för jpg eller png. så finns det verktyget rekomenderat i guiden annars finns även ett simpeplt python skript jag har gjort([renamer](https://raw.githubusercontent.com/abbjoafli/Lego-dataset/master/renamer.py   ))
Du väljer bara mappen renamer ska köras i och kör scriptet så byter den endelse på objektet.
**Detta får inte göras innan du labelat bilderna för då visas de inte upp i annotationtool!**. Råkar du dock göra det så är det enkelt att ändra om i koden för renamer så den gör motsatta, det vill säga från JPEG till jpg.

`python renamer.py`

#### Label konverterare
Du måste också konvertera dina labels till voc format, det vill säga xml istället för .txt. Detta gär vi genom att ladda ner pythonscriptet [yolo-voc-converter.py](https://raw.githubusercontent.com/abbjoafli/Lego-dataset/master/yolo-voc-converter.py), ändrar om det så klasstyp och mapp stämmer för dig.
För att få detta och fungera måste bilderna och labels ligga i samma mapp. Du kan till exempel lägga både bilder och labels direkt i label mappen.


`python yolo-voc-converter.py`
![Label](https://github.com/abbjoafli/ComputerVision/blob/master/images/labels.PNG?raw=true)


### Ladda upp
Efter detta så är det bara att antingen ladda upp ditt datasett till en github repo och länka den till keras koden på google colab via github clone eller att ladda upp det via gdrive eller manuellt via ladda upp knappen. Våga vinn!

Mappstrukturen jag rekommenderar är detta.
```
annotations/
annotations_xml/
images/
testing_annotations_xml/
testing_images/
Readme.md
```
#### Förklaring
I mappen
- annotations bör det ligga labels som txt-filer, detta för att man ska kunna träna yolo med darknet om man vill.
- annotations_xml ska det ligga labesl som xml filer, detta för att man ska kunna träna med Keras.
- images, bilderna som ska användas för träning
-  testing_annotations_xml, annotations som xml för validering/testing
-  testing_images, bilderna som ska användas för validering/testing
-  Readme, förklarar vad datasettet är och vad som ligger på de olika platserna.

**Varför finns ingen testing för .txt filerna?**
Jo det finns inte för att i darknet så skickar man in två listor(dessa skapas av process.py i annotation-tool) en för test och en för träning. De kan därför ligga kvar i samma mappar.

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


## Road following
För att kunna hitta vägar eller streck i allmänhet i openMV så gör man lite annorlunda än i OpenCV, tankesättet är detsamma men tillvägagångsättet varierar. [Här](https://raw.githubusercontent.com/abbjoafli/ComputerVision/master/files/findlanes.py) har jag gjort en kodsnutt som hittar ett streck i mitten av skärmen. Det kan man ha som grund när man bygger på och utvecklar det till något som mer liknar resultatet i OpenCV, om det behövs, vill säga.

Här kommer några bra resurser för att kunna göra din egen road recognition eller bara bli bättre på OpenMV överlag. Testa dessa, ändra saker,få inspiration, lek och få det till något bra, våga vinn:
[MaiXPY dokumentation](https://maixpy.sipeed.com/en/libs/machine_vision/image.html)
[MaiXPY openMV demon](https://github.com/AIWintermuteAI/maixpy-openmv-demos)
[Linear Regressions for Line Following w/ the OpenMV Cam](https://www.youtube.com/watch?v=dOd1TZFR480)
[OpenMV robot following lines](https://github.com/zlite/OpenMVrover/blob/master/linefollowing.py)







