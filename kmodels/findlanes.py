# Untitled - By: joafli - tis dec 10 2019
#find infinite lines
import sensor, image, lcd, time
#import video
enable_lens_corr = True
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames(time = 2000)

#v = video.open("/sd/capture_lines2.avi", record=1, interval=200000, quality=50)
min_degree = 0
max_degree = 179
tim = time.ticks_ms()
roi= (100,100,100,100)

#while(time.ticks_diff(time.ticks_ms(), tim)<30000):# För inspelning en viss tid
while(True):
    img = sensor.snapshot()
    for l in img.find_lines(roi,threshold = 1000, theta_margin = 25, rho_margin = 25):
        if (min_degree <= l.theta()) and (l.theta() <= max_degree):
            img.draw_line(l.line(), color = (255, 0, 0))
            img.draw_rectangle(roi, color = (255, 0, 0), thickness=1, fill=False)
            print(l)
    lcd.display(img)
#    img_len = v.record(img)
print("finish")
#v.record_finish()
lcd.clear()
