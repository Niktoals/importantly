import pyautogui as pa
import keyboard
import time
import pyperclip

def paste(text: str):
    pyperclip.copy(text)
    keyboard.press_and_release('ctrl + v')


def main():
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('d'):
            text=pa.prompt(text='Please enter text or code of emoji', title='Input Data', default='')
            print(text)
            if len(text)!=0:
                time.sleep(5)
                while True:
                    paste(text)
                    pa.press('enter')
                    if keyboard.is_pressed('esc'):
                        break
                    #pa.click()

if __name__=="__main__":
    main()


                



            
        

