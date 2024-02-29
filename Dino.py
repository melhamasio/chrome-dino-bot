import pyautogui
import time

class Dino:
    def __init__(self) -> None:
        self.dino_x = 773
        self.dino_y = 367

        self.delta_x = 50
        self.delta_y = 30

        self.coord_bg_color = (515, 385)
        self.bg_color = 255
        

    def is_obstacle(self):
        flagObstacle = False

        img = pyautogui.screenshot()

        self.bg_color   = img.getpixel(self.coord_bg_color)[0]
        
        for delta_y in range(self.delta_y):
            pixel_obstacle  = img.getpixel((self.dino_x + self.delta_x, self.dino_y - delta_y))[0]

            if(pixel_obstacle != self.bg_color):
                flagObstacle = True
                print("Jump in", (self.dino_x + self.delta_x, self.dino_y - delta_y))
                break
        
        return flagObstacle


    def jump(self):
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyUp('space')

    def run(self):
        flagObstacle = False

        while True:
            flagObstacle = self.is_obstacle()

            if(flagObstacle):
                self.jump()

dino = Dino()
dino.run()