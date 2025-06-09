import win32gui
import pyautogui
from PIL import Image

# P.S. Rus Не стоит уменьшать время задержки меньше 0.3 т.к. тогда опредление цвета пикселей не будет работать коректно
# P.S. Eng You shouldn't reduce the delay time to less than 0.3 because then the pixel color detection won't work correctly.

pyautogui.PAUSE = 0.3

numbers = {
    0: 1, 
    13: 2, 
    27: 3, 
    40: 4, 
    54: 5, 
    67: 6
    }

hwnd = win32gui.FindWindow(None, "2311DRK48G") 
#Rus Впишите сюда название окна с игрой
#Eng Enter the name of the game window here
if not hwnd:
    raise Exception("Окно не найдено!/Window not found!")

left, top, right, bottom = win32gui.GetWindowRect(hwnd)

left+=30
top+=347
width = 385
height = 435

for _ in range(30): 
    #Rus Количество раз, сколько хотите решить задачу
    #Eng The number of times you want to solve the puzzle

    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    # screenshot.save("screenshot.bmp")
    # Rus Отрегулируйте параметры ширины, высоты и положения так, чтобы кружок вверху касался своей стороной границы, а у кружков слева, справа и снизу был отступ в 1 пиксель, чтобы всё точно работало правильно. Используйте сохранение скриншота и любой редактор для определеия.
    # Eng Adjust the width, height and position parameters so that the circle at the top touches the border with its side, and the circles on the left, right and bottom have an indent of 1 pixel, so that everything works correctly. Use the screenshot save and any editor to determine.

    positions = [(192,4),(245,36),(300,68),(353,103),(138,38),(85,69),(31,103),
                (192,67),(245,100),(300,131),(353,162),(138,102),(85,131),(31,163),
                (192,131),(245,164),(300,195),(353,227),(138,164),(85,197),(31,228),
                (192,200),(245,230),(300,262),(138,230),(85,262),
                (192,259),(245,293),(138,291),
                (192,323)]

    def propagation():
        for x,y in positions:
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            
            color = screenshot.getpixel((x,y))[0]
            
            while color not in numbers:
                screenshot = pyautogui.screenshot(region=(left, top, width, height))
                color = screenshot.getpixel((x,y))[0]
            
            number = numbers[color]
            if number != 1:
                for _ in range(7-number):
                    pyautogui.click((x + left, y + top+61))


    def Encode():
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        
        Bp = (246,354)
        B = numbers[screenshot.getpixel(Bp)[0]]
        Cp = (296,327)
        C = numbers[screenshot.getpixel(Cp)[0]]
        Dp = (348,292)
        D = numbers[screenshot.getpixel(Dp)[0]]
        ap = (192,4)
        bp = (245,36)
        cp = (300,68)
        dp = (353,103)
        
        for _ in range(C-1):
            pyautogui.click((ap[0] + left, ap[1] + top))

        if C!=1:
            for _ in range(7-C):
                pyautogui.click((bp[0] + left, bp[1] + top))
                pyautogui.click((dp[0] + left, dp[1] + top))
        
        if D!=1:
            for _ in range(7-D):
                pyautogui.click((ap[0] + left, ap[1] + top))

        if (B+D)%2==1:
            for _ in range(3):
                pyautogui.click((cp[0] + left, cp[1] + top))
    
    
    propagation()

    Encode()
    
    propagation()

    pyautogui.click((200 + left, 490 + top))