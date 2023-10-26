import datetime
import sys
from attrs import exceptions
from prettytable import PrettyTable
from moviepy.editor import VideoFileClip
import cv2
from decimal import Decimal
import posemodule as pm
import time




def VideoCheck(Path):
# Open the video file
    #filepath = filedialog.askopenfilename()
   # filepath = 'static/videos/1.mp4'

    file = Path
    clip = VideoFileClip(file)
    duration = clip.duration
    print(duration)
    strt = time.time()
    video = cv2.VideoCapture(Path)
    detector = pm.PoseDetector()
    currentime, currentime2, currentime3, currentime4, currentime5, currentime6, currentime7, currentime8, currentime9, currentime10, currentime11, currentime12, currentime13, currentime14, currentime15, currentime16 = [
        time.time() for _ in range(16)]
    #for i in range(1, 17):
        #globals()["t" + str(i)]

    i, e, w, s, a, b, up1, up2, up3, up4, la1, la2, wr1, wr2, leg1, leg2 = [0.0] * 16

    global t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16
    t1 = 0.0
    t2 = 0.0
    t3 = 0.0
    t4 = 0.0
    t5 = 0.0
    t6 = 0.0
    t7 = 0.0
    t8 = 0.0
    t9 = 0.0
    t10 = 0.0
    t11 = 0.0
    t12 = 0.0
    t13 = 0.0
    t14 = 0.0
    t15 = 0.0
    t16 = 0.0
    cout=0
    while True:
        try:
            cout+=1
            print(cout)
            c = (time.time() - strt)
            x = Decimal(c)
            y = Decimal(duration)
            if y - x <= 0:
                print("stop")
                break
            success, img = video.read()
            pose = video.read()
            img = cv2.resize(img, (400, 600))
            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)
            if len(lmList) != 0:
                neck = detector.findneck(img, 12, 8, 6)
                trunk = detector.findtrunk(img, 24, 12, 24)
                upperarm = detector.upperarm(img, 12, 14, 24)
                lowerarm = detector.lowerarm(img, 14, 18, 22)
                wrist = detector.findwrist(img, 16, 20, 22)
                leg = detector.findleg(img, 24, 28, 26)
                if neck < 20:
                  t1 = time.time() - currentime
                else:
                    if t1 != 0:
                        i += t1
                    t1 = 0
                    currentime = time.time()
                if neck >= 20:
                    t2 = time.time() - currentime2
                else:
                    if t2 != 0:
                        e += t2
                    t2 = 0
                    currentime2 = time.time()
                if trunk == 0:
                    t3 = time.time() - currentime3
                else:
                    if t3 != 0:
                        w += t3
                    t3 = 0
                    currentime3 = time.time()
                if trunk >= 0 and trunk <= 20:
                    t4 = time.time() - currentime4
                else:
                    if t4 != 0:
                        s += t4
                    t4 = 0
                    currentime4 = time.time()
            if trunk >= 20 and trunk <= 60:
                t5 = time.time() - currentime5
            else:
                if t5 != 0:
                    a += t5
                t5 = 0
                currentime5 = time.time()
            if trunk >= 60:
                t6 = time.time() - currentime6
            else:
                if t6 != 0:
                    b += t6
                t6 = 0
                currentime6 = time.time()
            if upperarm <= 20:
                t7 = time.time() - currentime7
            else:
                if t7 != 0:
                    up1 += t7
                t7 = 0
                currentime7 = time.time()
            if upperarm >= 20 and trunk <= 45:
                t8 = time.time() - currentime8
            else:
                if t8 != 0:
                    up2 += t8
                t8 = 0
                currentime8 = time.time()
            if upperarm >= 45 and upperarm <= 90:
                t9 = time.time() - currentime9
            else:
                if t9 != 0:
                    up3 += t9
                t9 = 0
                currentime9 = time.time()
            if upperarm >= 90:
                t10 = time.time() - currentime10
            else:
                if t10 != 0:
                    up4 += t10
                t10 = 0
                currentime10 = time.time()
            if lowerarm >= 60 and lowerarm <= 100:
                t11 = time.time() - currentime11
            else:
                if t11 != 0:
                    la1 += t11
                t11 = 0
                currentime11 = time.time()
            if lowerarm <= 60:
                t12 = time.time() - currentime12
            else:
                if t12 != 0:
                    la2 += t12
                t12 = 0
                currentime12 = time.time()
            if wrist <= 15:
                t13 = time.time() - currentime13
            else:
                if t13 != 0:
                    wr1 += t13
                t13 = 0
                currentime13 = time.time()
            if wrist > 15:
                t14 = time.time() - currentime14
            else:
                if t14 != 0:
                    wr2 += t14
                t14 = 0
                currentime14 = time.time()
            if leg <= 60:
                t15 = time.time() - currentime15
            else:
                if t15 != 0:
                    leg1 += t15
                t15 = 0
                currentime15 = time.time()
            if leg >= 60:
                t16 = time.time() - currentime16
            else:
                if t16 != 0:
                    leg2 += t16
                t16 = 0
                currentime16 = time.time()

        except Exception as x:
            pass
    print(neck)
    print(trunk)
    print(lowerarm)
    print(upperarm)
    print(leg)
    print(wrist)
    table = PrettyTable()
    table.field_names = ["fields", "10 to 20", ">=20 "]
    table.add_row(["neck", i, e])
    #print(table)
    find = PrettyTable()
    find.field_names = ["fields", "0", "0-20", "20-60", ">60"]
    find.add_row(["trunk", w, s, a, b])
    #print(find)
    create = PrettyTable()
    create.field_names = ["fields", "<20", "20-45", "45-90", ">90"]
    create.add_row(["upper_arm", up1, up2, up3, up4])
    #print(create)
    adjust = PrettyTable()
    adjust.field_names = ["fields", "60-100", "<60"]
    adjust.add_row(["lower_arm", la1, la2])
    #print(adjust)
    duck = PrettyTable()
    duck.field_names = ["fields", "<15", ">15"]
    duck.add_row(["wrist", wr1, wr2])
    #print(duck)
    mode = PrettyTable()
    mode.field_names = ["fields", "30-60", ">60"]
    mode.add_row(["leg", leg1, leg2])
    #print(mode)
    caption = 0
    if w > s and w > a and w > b:
        caption = caption + 1
    elif s > w and s > a and s > b:
        caption = caption + 2
    elif a > w and a > s and a > b:
        caption = caption + 3
    elif b > w and b > s and b > a:
        caption = caption + 4
    if caption == 0:
        caption += 2
    tony = 0
    if i > e:
        tony = tony + 1
    if e > i:
        tony = tony + 2
    if tony == 0:
        tony += 1
    hulk = 0
    if la1 > la2:
        hulk = hulk + 1
    elif la2 > la1:
        hulk = hulk + 2
    if hulk == 0:
        hulk += 1
    wanda = 0
    if up1 > up2 and up1 > up3 and up1 > up4:
        wanda = wanda + 1
    elif up2 > up1 and up2 > up3 and up2 > up4:
        wanda = wanda + 2
    elif up3 > up1 and up3 > up2 and up3 > up4:
        wanda = wanda + 3
    elif up4 > up1 and up4 > up2 and up4 > up3:
        wanda = wanda + 4
    if wanda == 0:
        wanda +=2
    panther = 0
    if wr1 > wr2:
        panther = panther + 1
    elif wr2 > wr1:
        panther = panther + 2
    if panther == 0:
        panther += 1
    miller = 0
    if leg1 > leg2:
        miller = miller + 1
    if leg2 > leg1:
        miller = miller + 2
    if miller == 0:
        miller += 1
    m = PrettyTable()
    m.field_names = ["neck", "lowerarm", "upperarm", "wrist", "leg", "trunk"]
    m.add_row([tony, hulk, wanda, panther, miller, caption])
    #print(m)
    lp = 0
    lg = 0

    Source = {
        1: {
            1: {
                1: 1,
                2: 2,
                3: 2,
                4: 3
            },
            2: {
                1: 2,
                2: 3,
                3: 4,
                4: 5
            }
        },
        2: {
            1: {
                1: 1,
                2: 3,
                3: 4,
                4: 5
            },
            2: {
                1: 2,
                2: 4,
                3: 5,
                4: 6
            }
        }
    }

    Source2 = {
        1: {
            1: {
                1: 1,
                2: 1,
                3: 3,
                4: 4
            },
            2: {
                1: 2,
                2: 2,
                3: 4,
                4: 5
            }
        },
        2: {
            1: {
                1: 1,
                2: 2,
                3: 4,
                4: 5
            },
            2: {
                1: 2,
                2: 3,
                3: 5,
                4: 6
            }
        }
    }
    for i in range(1, 3):
        for j in range(1, 3):
            for x in range(1, 5):
                if tony == i and miller == j and caption == x:
                    lp = lp + Source[i][j][x]
                if hulk == i and panther == j and wanda == x:
                    lg = lg + Source2[i][j][x]
    van = PrettyTable()
    van.field_names = ["grade A", "grade B"]
    van.add_row([lp, lg])
    #print(van)
    clr = 0
    cross = {
        1: {
            1: 1,
            2: 1,
            3: 2,
            4: 3,
            5: 4,
            6: 6
        },
        2: {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 4,
            6: 6
        },
        3: {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 4,
            6: 6
        },
        4: {
            1: 2,
            2: 3,
            3: 3,
            4: 4,
            5: 5,
            6: 7
        },
        5: {
            1: 3,
            2: 4,
            3: 4,
            4: 5,
            5: 6,
            6: 8
        },
        6: {
            1: 4,
            2: 5,
            3: 6,
            4: 7,
            5: 8,
            6: 9
        }
    }
    for i in range(1, 7):
        for z in range(1, 7):
            if lg == z and lp == i:
                clr = clr + cross[z][i]
    dunk = PrettyTable()
    dunk.field_names = ["Final score"]
    dunk.add_row([clr])
    #print(dunk)
    redatas= {
        "tony":tony,
        "hulk":hulk,
        "wanda":wanda,
        "panther":panther,
        "miller":miller,
        "caption":caption,
        "lp":lp,
        "lg":lg,
        "clr":clr
    }
    return redatas