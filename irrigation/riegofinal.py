# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 10:22:45 2023

@author: jua-ni-co-x
"""
import Adafruit_BBIO.GPIO as GPIO
import time as t
#outputs
power='P9_22'
bomba='P9_24'
ev1='P9_21'
ev2='P8_7'

GPIO.setup(power,GPIO.OUT)
GPIO.setup(bomba,GPIO.OUT)
GPIO.setup(ev1,GPIO.OUT)
GPIO.setup(ev2,GPIO.OUT)
GPIO.setup('P9_11',GPIO.IN)
GPIO.setup('P9_23',GPIO.IN)
GPIO.setup('P8_10',GPIO.IN)

sa=GPIO.input('P9_11')

#prequisits
for i in [bomba,ev1,ev2]:
    GPIO.output(i,GPIO.HIGH)
GPIO.output(power,GPIO.HIGH)

loctime=t.localtime()
t1=0
t2=0
m=0
auto=0
#seq timepo general
while True:
    loctime=t.localtime()
    ano=loctime[0]
    mes=loctime[1]
    diames=loctime[2]
    hora=loctime[3]
    minuto=loctime[4]
    seg=loctime[5]
    diasem=loctime[6]
    diaano=loctime[7]
    ultriego=[ano,mes,diames]
    
    aguanivel=sa
    if GPIO.input('P9_23')==1 and auto==0:
        m=1
    manual=m
    
    if aguanivel==1:
        for i in [bomba,ev1,ev2]:
            GPIO.output(i,GPIO.HIGH)
        t.sleep(5)
        ultriego=[ano,mes,diames]
    if aguanivel==0 and manual==0:
        if GPIO.input('P8_10')==1:
            for i in [bomba,ev1,ev2]:
                GPIO.output(i,GPIO.HIGH)
            t.sleep(5)
            auto=0
        #seq verano
        if mes==12 or mes==1 or mes==2 or (mes==3 and diames<21):
            if hora==0 and minuto==30 and 1>seg:
                auto=1
                GPIO.output(ev1,GPIO.LOW)
                t.sleep(0.2)#0.5
                GPIO.output(bomba,GPIO.LOW)
            if hora==0 and minuto==45 and 1>seg:    
                GPIO.output(bomba,GPIO.HIGH)
                GPIO.output(ev1,GPIO.HIGH)
            if hora==1 and minuto==15 and 1>seg:
                GPIO.output(ev2,GPIO.LOW)
                t.sleep(0.2)
                GPIO.output(bomba,GPIO.LOW)
            if hora==1 and minuto==30 and 1>seg:
                GPIO.output(bomba,GPIO.HIGH)
                GPIO.output(ev2,GPIO.HIGH)
                
                for i in [bomba,ev1,ev2]:
                    GPIO.output(i,GPIO.HIGH)
                t.sleep(1800)#1800
                auto=0
                ultriego=[ano,mes,diames]
        
        #seq otono
        if (mes==3 and diames>=21) or mes==4:
            if diasem==0 or diasem==2 or diasem==4: 
                if hora==0 and minuto==30 and 1>seg:
                    auto=1
                    GPIO.output(ev1,GPIO.LOW)
                    t.sleep(0.2)
                    GPIO.output(bomba,GPIO.LOW)
                if hora==0 and minuto==45 and 1>seg:    
                    GPIO.output(bomba,GPIO.HIGH)
                    GPIO.output(ev1,GPIO.HIGH)
                if hora==1 and minuto==15 and 1>seg:
                    GPIO.output(ev2,GPIO.LOW)
                    t.sleep(0.2)
                    GPIO.output(bomba,GPIO.LOW)
                if hora==1 and minuto==30 and 1>seg:
                    GPIO.output(bomba,GPIO.HIGH)
                    GPIO.output(ev2,GPIO.HIGH)
                    for i in [bomba,ev1,ev2]:
                        GPIO.output(i,GPIO.HIGH)
                    t.sleep(1800)
                    auto=0
                    ultriego=[ano,mes,diames]
                    
        #seq invierno
        if mes==5 or mes==6 or mes==7 or mes==8:
            if diasem==0 or diasem==3: 
                if hora==22 and minuto==0 and 1>seg:
                    auto=1
                    GPIO.output(ev1,GPIO.LOW)
                    t.sleep(0.2)
                    GPIO.output(bomba,GPIO.LOW)
                if hora==22 and minuto==15 and 1>seg:    
                    GPIO.output(bomba,GPIO.HIGH)
                    GPIO.output(ev1,GPIO.HIGH)
                if hora==22 and minuto==45 and 1>seg:
                    GPIO.output(ev2,GPIO.LOW)
                    t.sleep(0.2)
                    GPIO.output(bomba,GPIO.LOW)
                if hora==23 and minuto==0 and 1>seg:
                    GPIO.output(bomba,GPIO.HIGH)
                    GPIO.output(ev2,GPIO.HIGH)
                    for i in [bomba,ev1,ev2]:
                        GPIO.output(i,GPIO.HIGH)
                    t.sleep(1800)
                    auto=0
                    ultriego=[ano,mes,diames]
                    
        #seq primavera
        if mes==9 or mes==10 or mes==11:
            if diasem==0 or diasem==2 or diasem==4: 
                if hora==0 and minuto==30 and 1>seg:
                    auto=1
                    GPIO.output(ev1,GPIO.LOW)
                    t.sleep(0.2)
                    GPIO.output(bomba,GPIO.LOW)
                if hora==0 and minuto==45 and 1>seg:    
                    GPIO.output(bomba,GPIO.HIGH)
                    GPIO.output(ev1,GPIO.HIGH)
                if hora==1 and minuto==15 and 1>seg:
                    GPIO.output(ev2,GPIO.LOW)
                    t.sleep(0.2)
                    GPIO.output(bomba,GPIO.LOW)
                if hora==1 and minuto==30 and 1>seg:
                    GPIO.output(bomba,GPIO.HIGH)
                    GPIO.output(ev2,GPIO.HIGH)
                    for i in [bomba,ev1,ev2]:
                        GPIO.output(i,GPIO.HIGH)
                    t.sleep(1800)
                    auto=0
                    ultriego=[ano,mes,diames]
    if aguanivel==0 and manual==1 and t1==0:
        auto=1
        GPIO.output(ev1,GPIO.LOW)
        t.sleep(0.2)#0.5
        GPIO.output(bomba,GPIO.LOW)
        while t1<15:#15
            t.sleep(1)
            t1=t1+1/60
            aguanivel=sa
            if GPIO.input('P8_10')==1:
                m=0
            manual=m
            if manual==0:
                GPIO.output(bomba,GPIO.HIGH)
                GPIO.output(ev1,GPIO.HIGH)
                t.sleep(round(120*t1,0))#120
                t1=0
                auto=0
                break
        if t1>=15 or aguanivel==1:
            GPIO.output(bomba,GPIO.HIGH)
            GPIO.output(ev1,GPIO.HIGH)

    if t1>=15 and aguanivel==0 and manual==1 and t2==0:
        t.sleep(1800)#1800
        GPIO.output(ev2,GPIO.LOW)
        t.sleep(0.2)
        GPIO.output(bomba,GPIO.LOW)
        while t2<15:    
            t.sleep(1)
            t2=t2+1/60
            aguanivel=sa
            if GPIO.input('P8_10')==1:
                m=0
            manual=m
            if aguanivel==1:
                GPIO.output(bomba,GPIO.HIGH)
                GPIO.output(ev2,GPIO.HIGH)
                break
            if t2==15 or manual==0:
                GPIO.output(bomba,GPIO.HIGH)
                GPIO.output(ev2,GPIO.HIGH)
                t.sleep(round(120*t2,0))
                t1=0
                t2=0
                m=0
                auto=0
                break
