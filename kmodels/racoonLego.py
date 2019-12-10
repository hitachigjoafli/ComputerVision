import sensor,image,lcd
import KPU as kpu

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.set_vflip(0)
sensor.run(1)
classes = ["Legogubbe"]
#classes = ["Racoon"]
#kpu.memtest()
task = kpu.load(0x600000)
#task = kpu.load("racoon.kmodel")
anchor = (0.57273, 0.677385, 1.87446, 2.06253, 3.33843, 5.47434, 7.88282, 3.52778, 9.77052, 9.16828)
a = kpu.init_yolo2(task, 0.3, 0.3, 5, anchor)

while(True):
    img = sensor.snapshot()
    #.rotation_corr(z_rotation=90.0)
    #a = img.pix_to_ai()
    code = kpu.run_yolo2(task, img)
    if code:
        for i in code:
            a=img.draw_rectangle(i.rect(),color = (0, 255, 0))
            a = img.draw_string(i.x(),i.y(), classes[i.classid()], color=(255,0,0), scale=3)
            print("NAME= " + classes[i.classid()])
        a = lcd.display(img)
    else:
        a = lcd.display(img)
a = kpu.deinit(task)
