import pyautogui
import keyboard
import threading
import time

clicking = False
click_thread = None

def click_thread_function():
    global clicking
    while clicking:
        pyautogui.click()
        time.sleep(0.2)  # Intervalo entre cliques

def  main():
    global clicking, click_thread
    print("Pressione F7 para iniciar e F6 para parar os cliques.")
    while True:
        if keyboard.is_pressed("F7"):
            if not clicking:
                clicking = True
                click_thread = threading.Thread(target=click_thread_function)
                click_thread.start()
        elif keyboard.is_pressed("F6"):
            clicking = False
            click_thread.join()

if __name__ == "__main__":
    main()

