import matplotlib.pyplot as plt
import numpy as np
import cmath
from tkinter import *
from PIL import ImageTk, Image

def julia (constant, x1, x2, y1, y2, scale, d, n):
    target_value = (1 + np.sqrt(1 + 4*abs(constant)))/2
    constant = constant
    x_inches = scale*(x2-x1)
    xpixels = int(d*x_inches)
    xcoords = np.zeros(xpixels)
    for x in range(xpixels):
        xcoords[x] = (x+1)/xpixels*(x2-x1)+x1
    y_inches = scale*(y2-y1)
    ypixels = int(d*y_inches)
    ycoords = np.zeros(ypixels)
    for y in range(ypixels):
        ycoords[y] = (y+1)/ypixels*(y2-y1)+y1
    matrix = np.zeros((ypixels, xpixels))
    def quadratic(number):
        return number**2 + constant
    def iteration(number, n):
        x = quadratic(number)
        if abs(x) > target_value:
            output = 0
        else:
            for num in range(n-1):
                x = quadratic(x)
                if abs(x) > target_value:
                    output = num + 1
                    break
                else:
                    output = 200
        return output
    for yc in range(len(ycoords)):
        for xc in range(len(xcoords)):
            matrix[yc, xc] = iteration((xcoords[xc] - ycoords[yc]*1j), 200)

    plt.figure(figsize=(x_inches, y_inches), dpi=d)
    color_map = plt.imshow(matrix)
    color_map.set_cmap("jet")
    plt.colorbar()
    plt.savefig("images/out.png")

def mandelbrot (x1, x2, y1, y2, scale, d, n):
    x_inches = scale*(x2-x1)
    xpixels = int(d*x_inches)
    xcoords = np.zeros(xpixels)
    for x in range(xpixels):
        xcoords[x] = (x+1)/xpixels*(x2-x1)+x1
    y_inches = scale*(y2-y1)
    ypixels = int(d*y_inches)
    ycoords = np.zeros(ypixels)
    for y in range(ypixels):
        ycoords[y] = (y+1)/ypixels*(y2-y1)+y1
    matrix = np.zeros((ypixels, xpixels))
    def quadratic(number, con):
        return number**2 + con
    def iteration(number, con, n):
        target_value = (1 + np.sqrt(1 + 4*abs(con)))/2
        x = quadratic(number, con)
        if abs(x) > target_value:
            output = 0
        else:
            for num in range(n-1):
                x = quadratic(x, con)
                if abs(x) > target_value:
                    output = num + 1
                    break
                else:
                    output = 200
        return output
    for yc in range(len(ycoords)):
        for xc in range(len(xcoords)):
            matrix[yc, xc] = iteration(0, (xcoords[xc] - ycoords[yc]*1j), 200)

    plt.figure(figsize=(x_inches, y_inches), dpi=d)
    color_map = plt.imshow(matrix)
    color_map.set_cmap("jet")
    plt.colorbar()
    plt.savefig("images/out.png")

def initj ():
    julia(complex(e9.get()), float(e2.get()), float(e3.get()), float(e4.get()), float(e5.get()), float(e6.get()), float(e7.get()), float(e8.get()))
    master.destroy()

def initm ():
    mandelbrot(float(e2.get()), float(e3.get()), float(e4.get()), float(e5.get()), float(e6.get()), float(e7.get()), float(e8.get()))
    master.destroy()

def init ():
    if e1.get() == "Julia":
        initj()
    elif e1.get() == "Mandelbrot":
        initm()
    master2 = Tk()
    im1 = Image.open('images/out.png')
    image1 = ImageTk.PhotoImage(im1)
    Label(master2, image=image1).grid(row=0)
    width, height = master2.winfo_screenwidth(), master2.winfo_screenheight()
    master2.geometry('%dx%d+0+0' % (width,height))
    master2.mainloop()

master = Tk()
Label(master, text="COMPLEX ", font="times 72").grid(row=0, sticky=E)
Label(master, text="ANALYSIS", font="times 72").grid(row=0, column=1, sticky=W)
Label(master, text="Type of set:", font="times 48").grid(row=1, sticky=W)
Label(master, text="Real axis lower bound:", font="times 48").grid(row=2, sticky=W)
Label(master, text="Real axis upper bound:", font="times 48").grid(row=3, sticky=W)
Label(master, text="Imaginary axis lower bound:", font="times 48").grid(row=4, sticky=W)
Label(master, text="Imaginary axis upper bound:", font="times 48").grid(row=5, sticky=W)
Label(master, text="Scale:", font="times 48").grid(row=6, sticky=W)
Label(master, text="DPI:", font="times 48").grid(row=7, sticky=W)
Label(master, text="Maximum mumber of iterations:", font="times 48").grid(row=8, sticky=W)
Label(master, text="Constant (if Julia set):", font="times 48").grid(row=9, sticky=W)

e1 = Entry(master, font="times 48")
e1.grid(row=1, column=1)
e2 = Entry(master, font="times 48")
e2.grid(row=2, column=1)
e3 = Entry(master, font="times 48")
e3.grid(row=3, column=1)
e4 = Entry(master, font="times 48")
e4.grid(row=4, column=1)
e5 = Entry(master, font="times 48")
e5.grid(row=5, column=1)
e6 = Entry(master, font="times 48")
e6.grid(row=6, column=1)
e7 = Entry(master, font="times 48")
e7.grid(row=7, column=1)
e8 = Entry(master, font="times 48")
e8.grid(row=8, column=1)
e9 = Entry(master, font="times 48")
e9.grid(row=9, column=1)

Button(master, text='Enter', font="times 48", command=init).grid(row=10, column=0, pady=4)
Button(master, text='Cancel', font="times 48", command=master.destroy).grid(row=10, column=1, pady=4)

master.mainloop()