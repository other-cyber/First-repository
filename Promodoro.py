import time
import pygame
import plyer
import threading
import keyboard

stop_event = threading.Event()


def format_time(seconds):
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes}:{secs:02d}"


def timer(seconds):
    while seconds > 0 and not stop_event.is_set():
        if keyboard.is_pressed("space"):
            stop_event.set()
        if stop_event.is_set():
            print("Таймер остановлен")
        time.sleep(1)
        print(format_time(seconds))
        seconds -= 1


def countdown(num_cycles, seconds=1500):
    for i in range(num_cycles):
        if i == num_cycles - 1:
            timer(seconds)
            notice("Таймер", "Время закончилось")
        else:
            timer(seconds)
            notice("Перерыв", "Время началось")
            timer(300)
            notice("Перерыв", "Время закончилось")


def notice(name, message):
    print(name, message.lower())
    pygame.mixer.music.load("C:/Users/Никита/Downloads/undertaker-bell-repeat.mp3")
    pygame.mixer.music.play()
    plyer.notification.notify(
        title=name,
        message=message,
        app_name="Таймер",
        timeout=10,
    )


def main():
    pygame.mixer.init()

    while True:
        try:
            num_cycles = int(input("Введите сколько циклов: "))
            seconds = int(input("Введите сколько секунд: "))
        except ValueError:
            print("Вы ввели не число")
            continue
        t = threading.Thread(target=countdown, args=(seconds, num_cycles))
        if seconds > 0:
            t.start()
            return
        else:
            print("Число отрицательное")
            continue


main()
