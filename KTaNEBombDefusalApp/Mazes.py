from tkinter import *
from PIL import ImageTk, Image

b11, b12, b13, b14, b15, b16, \
b21, b22, b23, b24, b25, b26, \
b31, b32, b33, b34, b35, b36, \
b41, b42, b43, b44, b45, b46, \
b51, b52, b53, b54, b55, b56, \
b61, b62, b63, b64, b65, b66 = (False for f in range(36))


class Mazes:

    def reset(self, num):
        if num == 0:
            self.mazeWin.destroy()
        elif num == 1:
            self.mazeWin.destroy()
            self.__init__(self.root, self.back, self.manual_font)

    def __init__(self, root, back, font):
        self.root = root
        self.back = back
        self.manual_font = font
        self.mazeWin = Toplevel(self.root)
        self.mazeWin.title("Mazes")
        self.mazeWin.resizable(False, False)
        self.mazeWin.config(bg=back)
        self.lftPos = (self.mazeWin.winfo_screenwidth() - 1000) / 2
        self.topPos = (self.mazeWin.winfo_screenheight() - 700) / 2
        self.mazeWin.geometry("%dx%d+%d+%d" % (1000, 700, self.lftPos, self.topPos))

        self.img = Image.open("Images/MazeSelect.png")
        self.mazeImage = PhotoImage(file="Images/Maze1.png")

        self.width = self.mazeImage.width()
        self.height = self.mazeImage.height()

        self.nameLabel = Label(self.mazeWin, font=("Terminal", 25), fg="white", bg=back,
                               text="ON THE SUBJECT OF MAZES")
        self.selectLabel = Label(self.mazeWin, font=self.manual_font, fg="white", bg=back,
                                 text="PLACE ANY OF THE 2 CIRCLES IN THE MAZE")

        self.canvas = Canvas(self.mazeWin, bg=back, highlightthickness=0, height=self.height + 1,
                             width=self.width + 1)
        self.canvas.create_image(self.width / 2, self.height / 2, image=self.mazeImage)
        self.maze1, self.maze2, self.maze3 = (self.img_crop(i, 0) for i in range(3))
        self.maze4, self.maze5, self.maze6 = (self.img_crop(i, 1) for i in range(3))
        self.maze7, self.maze8, self.maze9 = (self.img_crop(i, 2) for i in range(3))
        mazes = [self.maze1, self.maze2, self.maze3,
                 self.maze4, self.maze5, self.maze6,
                 self.maze7, self.maze8, self.maze9]
        self.maze1img, self.maze2img, self.maze3img, \
            self.maze4img, self.maze5img, self.maze6img, \
            self.maze7img, self.maze8img, self.maze9img = \
            (ImageTk.PhotoImage(mazes[j]) for j in range(len(mazes)))

        self.canvas.bind("<Button-1>", lambda event, click="left": self.callback(event, click))
        self.circles = False
        self.light = False
        self.x_light = 0
        self.y_light = 0
        self.x_triangle = 0
        self.y_triangle = 0
        self.triangle = False
        self.old_x_light = 0
        self.old_y_light = 0
        self.old_x_triangle = 0
        self.old_y_triangle = 0

        self.nameLabel.pack(side=TOP, pady=30)
        self.selectLabel.pack(side=TOP, pady=30)
        self.canvas.pack()

        self.nextButton = Button(self.mazeWin, font=self.manual_font, text="NEXT",
                                 state=DISABLED)
        self.infoLabel = Label(self.mazeWin, font=self.manual_font, fg="white", bg=back,
                                 text="TO PLACE A CIRCLE IN THE MAZE, PRESS LEFT CLICK\n"
                                      "ON ANY EMPTY SPACE.\n"
                                      "TO ERASE A CIRCLE, LEFT CLICK IT AGAIN\n"
                                      "WHEN YOU PLACE A CIRCLE IN ANY POSITION, THE 'NEXT'\n"
                                      "BUTTON WILL BE AVAILABLE")
        self.infoLabel.pack()
        self.nextButton.pack()

        self.backButton = Button(self.mazeWin, text="BACK TO\nMODULE SELECT", font=("Terminal", 20),
                                 command=lambda: self.reset(0))
        self.resetButton = Button(self.mazeWin, text="RESET", font=("Terminal", 20),
                                  command=lambda: self.reset(1))

        self.backButton.pack(side=BOTTOM)

        self.selected = [[b11, b12, b13, b14, b15, b16],
                         [b21, b22, b23, b24, b25, b26],
                         [b31, b32, b33, b34, b35, b36],
                         [b41, b42, b43, b44, b45, b46],
                         [b51, b52, b53, b54, b55, b56],
                         [b61, b62, b63, b64, b65, b66],
                         ]
        self.maze_img = [self.maze1img, self.maze2img, self.maze3img,
                         self.maze4img, self.maze5img, self.maze6img,
                         self.maze7img, self.maze8img, self.maze9img]

    def callback(self, event, click):
        tags = [["b11", "b12", "b13", "b14", "b15", "b16"],
                ["b21", "b22", "b23", "b24", "b25", "b26"],
                ["b31", "b32", "b33", "b34", "b35", "b36"],
                ["b41", "b42", "b43", "b44", "b45", "b46"],
                ["b51", "b52", "b53", "b54", "b55", "b56"],
                ["b61", "b62", "b63", "b64", "b65", "b66"]]
        pos = [[5, 30, 55, 80, 105, 130],
               [20, 45, 70, 95, 120, 145]]
        for i in range(len(pos[0])):
            if event.x in range(pos[0][i], pos[1][i]):
                for j in range(len(pos[0])):
                    if event.y in range(pos[0][j], pos[1][j]):
                        if not self.selected[i][j]:
                            if not self.circles:
                                self.canvas.create_oval(pos[0][i], pos[0][j]
                                                        , pos[1][i], pos[1][j], outline="green", width=3,
                                                        tag=tags[i][j])
                                self.selected[i][j] = True
                            else:
                                if click == "left":
                                    if not self.light:
                                        self.light = True
                                    else:
                                        self.canvas.delete("light")
                                        self.selected[self.old_x_light][self.old_y_light] = False

                                    self.canvas.create_rectangle(pos[0][i] + 5, pos[0][j] + 5
                                                                 , pos[1][i] - 5, pos[1][j] - 5, outline="#182db5",
                                                                 width=2,
                                                                 tag="light", fill="#182db5")
                                    self.selected[i][j] = True
                                    self.old_x_light = i
                                    self.old_y_light = j
                                    self.x_light = pos[0][i]
                                    self.y_light = pos[1][j]

                                else:
                                    if not self.triangle:
                                        self.triangle = True
                                    else:
                                        self.canvas.delete("triangle")
                                        self.selected[self.old_x_triangle][self.old_y_triangle] = False

                                    self.canvas.create_polygon(pos[0][i] + 2, pos[0][j] + 12,
                                                               pos[0][i] + 12, pos[0][j] + 12,
                                                               pos[0][i] + 7, pos[0][j],
                                                               outline="red",
                                                               width=2,
                                                               tag="triangle", fill="red")
                                    self.selected[i][j] = True
                                    self.old_x_triangle = i
                                    self.old_y_triangle = j
                                    self.x_triangle = pos[0][i]
                                    self.y_triangle = pos[1][j]

                            break
                        else:
                            if not self.circles:
                                self.canvas.delete(tags[i][j])
                                self.selected[i][j] = False
                            else:
                                eq_x = False
                                eq_y = False
                                if click == "left":
                                    if self.light:
                                        if pos[0][i] == self.x_triangle:
                                            eq_x = True
                                        if pos[1][j] == self.y_triangle:
                                            eq_y = True
                                        if eq_x and eq_y:
                                            return None
                                        else:
                                            self.canvas.delete("light")
                                            self.light = False
                                            self.x_light = 0
                                            self.y_light = 0
                                            self.selected[i][j] = False
                                else:
                                    if self.triangle:
                                        if pos[0][i] == self.x_light:
                                            eq_x = True
                                        if pos[1][j] == self.y_light:
                                            eq_y = True
                                        if eq_x and eq_y:
                                            return None
                                        else:
                                            self.canvas.delete("triangle")
                                            self.selected[i][j] = False
                                            self.x_triangle = 0
                                            self.y_triangle = 0
                                            self.triangle = False

                            break
                break
        if not self.circles:
            self.activate()

    def img_crop(self, i, j):
        left = i * 150
        right = i * 150 + 150
        upper = j * 150
        lower = j * 150 + 150
        return self.img.crop([left, upper, right, lower])

    def activate(self):
        on = 0
        for i in range(len(self.selected[0])):
            for j in range(len(self.selected[0])):
                if self.selected[i][j]:
                    on = on + 1
        if on == 1:
            self.nextButton.config(state=NORMAL, command=lambda: self.check_maze())
        else:
            self.nextButton.config(state=DISABLED)

    def check_maze(self):
        mazes = [[self.selected[0][1], self.selected[5][2]],
                 [self.selected[1][3], self.selected[4][1]],
                 [self.selected[3][3], self.selected[5][3]],
                 [self.selected[0][0], self.selected[0][3]],
                 [self.selected[3][5], self.selected[4][2]],
                 [self.selected[2][4], self.selected[4][0]],
                 [self.selected[1][0], self.selected[1][5]],
                 [self.selected[2][3], self.selected[3][0]],
                 [self.selected[0][4], self.selected[2][1]]]
        selected_maze = -1
        for i in range(len(mazes)):
            if mazes[i][0] or mazes[i][1]:
                selected_maze = i
                self.canvas.delete("all")
                break
            elif i >= 8:
                self.selectLabel.config(text="PLACE ANY OF THE 2 CIRCLES IN THE MAZE\n"
                                             "MAKE SURE TO PLACE A VALID CIRCLE")
                return None
        self.place_maze(selected_maze)

    def place_maze(self, maze):
        self.resetButton.place(x=0, y=0)
        self.canvas.create_image(self.width / 2, self.height / 2, image=self.maze_img[maze])
        self.nextButton.pack_forget()
        for i in range(len(self.selected[0])):
            for j in range(len(self.selected[0])):
                if self.selected[i][j]:
                    self.selected[i][j] = False
        self.canvas.bind("<Button-3>", lambda event, click="right": self.callback(event, click))
        self.circles = True
        self.selectLabel.config(text="NOW PLACE THE LIGHT AND TRIANGLE\n"
                                     "AND GUIDE THE DEFUSER TO GET THE LIGHT IN\n"
                                     "THE TRIANGLE")
        self.infoLabel.config(text="TO PLACE A LIGHT, LEFT CLICK AN EMPTY SPACE.\n"
                                   "TO REMOVE IT, LEFT CLICK IT AGAIN, OR SELECT ANOTHER\n"
                                   "EMPTY SPACE.\n"
                                   "TO PLACE A TRIANGLE, RIGHT CLICK AN EMPTY SPACE.\n"
                                   "TO REMOVE IT, RIGHT CLICK IT AGAIN, OR SELECT ANOTHER\n"
                                   "EMPTY SPACE.")
