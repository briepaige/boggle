# Contributors: Brie Sloves and Sophie Quinn

import random
import numpy
import tkinter
import turtle
import datetime
from pygame import mixer

class Game(tkinter.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.buildWindow()

    def buildWindow(self):
        self.root.title('Boggle')
        self.pack()

        self.width = 510
        self.height = 510
        self.canvas = tkinter.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack(side = 'left')

        sideBar = tkinter.Frame(self, padx = 10, pady = 10)
        sideBar.pack(side = 'right', fill = 'y')


        self.artist = turtle.RawTurtle(self.canvas)
        self.screen = self.artist.getscreen()
        self.screen.setworldcoordinates(0, self.height, self.width, 0)

        self.startButton4 = tkinter.Button(sideBar, text = 'New 4x4 Game', command = self.startNewGame4x4)
        self.startButton4.pack()

        self.startButton5 = tkinter.Button(sideBar, text = 'New 5x5 Game', command = self.startNewGame5x5)
        self.startButton5.pack()

        self.timer = tkinter.Label(sideBar, text = 'Time Remaining')
        self.timer.pack()

        self.elapsedTime = tkinter.StringVar()
        self.elapsedTime.set('3:00')
        self.elapsedTimeLabel = tkinter.Label(sideBar, textvariable = self.elapsedTime)
        self.elapsedTimeLabel.pack()

        self.endButton = tkinter.Button(sideBar, text = 'Quit Game', command = self.root.destroy)
        self.endButton.pack()

        self.screen.bgcolor("dark blue")

        self.screen.update()

    def countdown(self):
        currTime = datetime.datetime.now()
        elapsedTime = currTime - self.startTime
        elapsedSeconds = elapsedTime.seconds
        totalSecondsRemaining = 180 - elapsedSeconds
        minutesRemaining = totalSecondsRemaining // 60
        secondsRemaining = totalSecondsRemaining % 60
        secondsRemainingStr = str(secondsRemaining)
        if len(secondsRemainingStr) == 1:
            secondsRemainingStr = '0' + secondsRemainingStr
        timeStr = str(minutesRemaining) + ":" + secondsRemainingStr
        self.elapsedTime.set(timeStr)
        if totalSecondsRemaining == 0:

            mixer.init()
            sound=mixer.Sound("bell.mp3")
            sound.play()

            self.root.after(1000, self.gameOver)
        else:
            self.root.after(1000, self.countdown)

    def startNewGame5x5(self):

        #initialize tiles
        tile0 = Tile(['A', 'A', 'A', 'F', 'R', 'S'], self)
        tile1 = Tile(['A', 'A', 'E', 'E', 'E', 'E'], self)
        tile2 = Tile(['A', 'A', 'F', 'I', 'R', 'S'], self)
        tile3 = Tile(['A', 'D', 'E', 'N', 'N', 'N'], self)
        tile4 = Tile(['A', 'E', 'E', 'E', 'E', 'M'], self)
        tile5 = Tile(['A', 'E', 'E', 'G', 'M', 'U'], self)
        tile6 = Tile(['A', 'E', 'G', 'M', 'N', 'N'], self)
        tile7 = Tile(['A', 'F', 'I', 'R', 'S', 'Y'], self)
        tile8 = Tile(['B', 'J', 'K', 'Qu', 'X', 'Z'], self)
        tile9 = Tile(['C', 'C', 'E', 'N', 'S', 'T'], self)
        tile10 = Tile(['C', 'E', 'I', 'I', 'L', 'T'], self)
        tile11 = Tile(['C', 'E', 'I', 'L', 'P', 'T'], self)
        tile12 = Tile(['C', 'E', 'I', 'P', 'S', 'T'], self)
        tile13 = Tile(['D', 'D', 'H', 'N', 'O', 'T'], self)
        tile14 = Tile(['D', 'H', 'H', 'L', 'O', 'R'], self)
        tile15 = Tile(['D', 'H', 'L', 'N', 'O', 'R'], self)
        tile16 = Tile(['D', 'H', 'L', 'N', 'O', 'R'], self)
        tile17 = Tile(['E', 'I', 'I', 'I', 'T', 'T'], self)
        tile18 = Tile(['E', 'M', 'O', 'T', 'T', 'T'], self)
        tile19 = Tile(['E', 'N', 'S', 'S', 'S', 'U'], self)
        tile20 = Tile(['F', 'I', 'P', 'S', 'R', 'Y'], self)
        tile21 = Tile(['G', 'O', 'R', 'R', 'V', 'W'], self)
        tile22 = Tile(['I', 'P', 'R', 'R', 'R', 'Y'], self)
        tile23 = Tile(['N', 'O', 'O', 'T', 'U', 'W'], self)
        tile24 = Tile(['O', 'O', 'O', 'T', 'T', 'U'], self)

        #randomize placement on board
        board = [tile0, tile1, tile2, tile3, tile4, tile5, tile6, tile7,
        tile8, tile9, tile10, tile11, tile12, tile13, tile14, tile15,
        tile16, tile17, tile18, tile19, tile20, tile21, tile22, tile23, tile24]

        random.shuffle(board)

        letters = []

        #randomly select letters for each tile
        for tile in board:
            letter = tile.roll()
            letters.append(letter)

        self.drawTiles(5, letters)



    def startNewGame4x4(self):

        #initialize tiles
        tile0 = Tile(['R', 'I', 'F', 'O', 'B', 'X'], self)
        tile1 = Tile(['I', 'F', 'E', 'H', 'E', 'Y'], self)
        tile2 = Tile(['D', 'E', 'N', 'O', 'W', 'S'], self)
        tile3 = Tile(['U', 'T', 'O', 'K', 'N', 'D'], self)
        tile4 = Tile(['H', 'M', 'S', 'R', 'A', 'O'], self)
        tile5 = Tile(['L', 'U', 'P', 'E', 'T', 'S'], self)
        tile6 = Tile(['A', 'C', 'I', 'T', 'O', 'A'], self)
        tile7 = Tile(['Y', 'L', 'G', 'K', 'U', 'E'], self)
        tile8 = Tile(['Qu', 'B', 'M', 'J', 'O', 'A'], self)
        tile9 = Tile(['E', 'H', 'I', 'S', 'P', 'N'], self)
        tile10 = Tile(['V', 'E', 'T', 'I', 'G', 'N'], self)
        tile11 = Tile(['B', 'A', 'L', 'I', 'Y', 'T'], self)
        tile12 = Tile(['E', 'Z', 'A', 'V', 'N', 'D'], self)
        tile13 = Tile(['R', 'A', 'L', 'E', 'S', 'C'], self)
        tile14 = Tile(['U', 'W', 'I', 'L', 'R', 'G'], self)
        tile15 = Tile(['P', 'A', 'C', 'E', 'M', 'D'], self)

        #randomize placement on board
        board = [tile0, tile1, tile2, tile3, tile4, tile5, tile6, tile7,
        tile8, tile9, tile10, tile11, tile12, tile13, tile14, tile15]

        random.shuffle(board)

        letters = []

        #randomly select letters for each tile
        for tile in board:
            letter = tile.roll()
            letters.append(letter)

        self.drawTiles(4, letters)


    def drawTiles(self, size, letters):


        self.screen.clear()
        self.screen.bgcolor("dark blue")
        self.screen.tracer(0)

        self.artist.color("black", "white")
        style = ('Times', 50, 'bold')
        self.artist.ht()
        self.artist.up()

        for i in range(size**2):
            if i % size == 0:
                self.artist.goto(10, ((self.height - 10)/size)* (i/size)+10)
            self.artist.down()
            self.artist.begin_fill()
            for j in range(4):
                self.artist.forward((self.width-50)/size)
                self.artist.left(90)
            self.artist.end_fill()
            self.artist.up()
            self.artist.left(90)
            self.artist.forward((self.height-50)/(size*1.25))
            self.artist.right(90)
            self.artist.forward((self.width-50)/(size * 2))
            self.artist.write(letters[i], font=style, align = 'center')
            self.artist.left(180)
            self.artist.forward((self.width-50)/(size * 2))
            self.artist.left(90)
            self.artist.forward((self.height-50)/(size * 1.25))
            self.artist.left(90)
            self.artist.forward((self.width-10)/size)
        self.screen.update()

        self.startTime = datetime.datetime.now()
        self.root.after(1000, self.countdown)

        self.screen.update()

    def gameOver(self):
        gameOverStr = '''Time is up!\n4 letters : 1 point     \n5 letters  : 2 points
        6 letters  : 3 points\n7 letters  : 5 points\n8+ letters : 11 points'''
        tkinter.messagebox.showinfo(message = gameOverStr, title = gameOverStr)



class Tile(turtle.RawTurtle):

    def __init__(self, letters, game):
        self.letters = letters
        super().__init__(game.canvas)

    def roll(self):
        self.side = random.randrange(6)
        return self.letters[self.side]

def main():
    root = tkinter.Tk()
    game = Game(root)
    game.mainloop()

if __name__ == "__main__":
    main()
