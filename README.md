# Computer Vision

# OpenCV
## Grunder
I grunderna finns det två alternativ ([Open CV Python Tut For Beginners](https://www.youtube.com/watch?v=kdLM6AOd2vc&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=1) och [Afshins Open CV tutorial](https://www.youtube.com/watch?v=izN-NLpS5t8&list=PLiHa1s-EL3vjr0Z02ihr6Lcu4Q0rnRvjm&index=3))  både är väldigt bra, kika och se vilken du gillar och vill följa. 

Gör de delar du tycker verkar spännande på videorna och gå sen vidare, ladda ner exempelkod och experimentera runt, nu ska vi lära oss!

[Codebinds hemsida för kodexempel](http://www.codebind.com/category/python/opencv/)
[Afshins github med kodexempel](https://github.com/ashwin-pajankar/Python-OpenCV3)


### Kul Bonus Rita med webbkameran!
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
