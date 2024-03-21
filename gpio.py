#coding=utf-8
import RPi.GPIO as GPIO
import time

IN1 = 17
IN2 = 22
PWM_12 = 7

GPIO.setmode(GPIO.BCM)

GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)

GPIO.setup(PWM_12,GPIO.OUT)

GPIO.output(IN1,GPIO.LOW)
GPIO.output(IN2,GPIO.LOW)
GPIO.output(PWM_12,GPIO.LOW)

GPIO.output(IN1,GPIO.HIGH)
GPIO.output(PWM_12,GPIO.HIGH)


GPIO.output(IN1,GPIO.LOW)





