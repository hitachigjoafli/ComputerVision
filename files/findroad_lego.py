# Untitled - By: joafli - tis dec 10 2019
#find infinite lines
import sensor, image, lcd, time
import KPU as kpu
enable_lens_corr = True
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.set_vflip(0)
sensor.run(1)
sensor.skip_frames(time = 2000)

classes = ["Legogubbe"]
task = kpu.load(0x600000)
anchor = (0.57273, 0.677385, 1.87446, 2.06253, 3.33843, 5.47434, 7.88282, 3.52778, 9.77052, 9.16828)
a = kpu.init_yolo2(task, 0.3, 0.3, 5, anchor)

min_degree = 0
max_degree = 179
tim = time.ticks_ms()
roi= (100,100,100,100)
while(True):
    img = sensor.snapshot()
    code = kpu.run_yolo2(task, img)
    if code:
        for i in code:
            a=img.draw_rectangle(i.rect(),color = (0, 255, 0))
            a = img.draw_string(i.x(),i.y(), classes[i.classid()], color=(255,0,0), scale=3)
            print("NAME= " + classes[i.classid()])
    for l in img.find_lines(roi,threshold = 1000, theta_margin = 25, rho_margin = 25):
        if (min_degree <= l.theta()) and (l.theta() <= max_degree):
            img.draw_line(l.line(), color = (255, 0, 0))
            img.draw_rectangle(roi, color = (255, 0, 0), thickness=1, fill=False)
            print(l)
    lcd.display(img)
