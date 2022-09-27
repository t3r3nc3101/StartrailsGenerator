import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import cv2 
import os 
import numpy
from fnmatch import fnmatch
from datetime import datetime, timedelta
import random

srcDirName = ""
outputDirName = ""

class App:
    def __init__(self, root):
        #setting title
        root.title("Star Trails Generator")
        #setting window size
        width=512
        height=512
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_941=tk.Button(root)
        GButton_941["bg"] = "#d0d0d0"
        GButton_941["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=12)
        GButton_941["font"] = ft
        GButton_941["fg"] = "#000000"
        GButton_941["justify"] = "center"
        GButton_941["text"] = "Select Folder"
        GButton_941.place(x=300,y=30,width=130,height=30)
        GButton_941["command"] = self.GButton_941_command

        GLabel_345=tk.Label(root)
        GLabel_345["anchor"] = "s"
        GLabel_345["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_345["font"] = ft
        GLabel_345["fg"] = "#8f8f8f"
        GLabel_345["justify"] = "center"
        GLabel_345["text"] = "T3 Star Trails Generator | v0.1 | 27/09/22"
        GLabel_345["relief"] = "flat"
        GLabel_345.place(x=270,y=480,width=252,height=30)

        self.GMessage_678=tk.Message(root)
        self.GMessage_678["anchor"] = "w"
        self.GMessage_678["bg"] = "#c6c6c6"
        self.GMessage_678["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=11)
        self.GMessage_678["font"] = ft
        self.GMessage_678["fg"] = "#333333"
        self.GMessage_678["justify"] = "left"
        self.GMessage_678["text"] = ""
        self.GMessage_678["relief"] = "sunken"
        self.GMessage_678.configure(width=450)
        self.GMessage_678.place(x=10,y=410,width=490,height=73)
        
        new_text = "Ready!\nSelect a source directory to begin..."
        self.GMessage_678["text"] = new_text

        GLabel_730=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_730["font"] = ft
        GLabel_730["fg"] = "#333333"
        GLabel_730["justify"] = "center"
        GLabel_730["text"] = "1) Select folder with images:"
        GLabel_730.place(x=20,y=30,width=212,height=31)

        GLabel_117=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_117["font"] = ft
        GLabel_117["fg"] = "#333333"
        GLabel_117["justify"] = "center"
        GLabel_117["text"] = "2) Customize settings:"
        GLabel_117.place(x=0,y=80,width=213,height=34)

       # def setCloudThreshold(self):
        #    gotText = GLabel_302.config(text= GLabel_302.get(), font= ('Helvetica 13'))
      #      print(gotText)

        
        GLineEdit_753=tk.Entry(root)
        GLineEdit_753["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_753["font"] = ft
        GLineEdit_753["fg"] = "#333333"
        GLineEdit_753["justify"] = "center"
        GLineEdit_753["text"] = ""
        GLineEdit_753['state'] = 'disabled'
        GLineEdit_753.place(x=300,y=160,width=131,height=30)
        #GLineEdit_753["show"] = "undefined"
        #GLineEdit_753["invalidcommand"] = "undefined"
        #GLineEdit_753["validatecommand"] = "undefined"  #setCloudThreshold
        #GLineEdit_753.bind("<Return>", setCloudThreshold) 

        GLabel_302=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_302["font"] = ft
        GLabel_302["fg"] = "#333333"
        GLabel_302["justify"] = "center"
        GLabel_302["text"] = "• Cloud filter threshold:"
        GLabel_302.place(x=10,y=160,width=228,height=30)

        GLabel_285=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_285["font"] = ft
        GLabel_285["fg"] = "#333333"
        GLabel_285["justify"] = "center"
        GLabel_285["text"] = "• Ignore cloudy images:"
        GLabel_285.place(x=30,y=120,width=190,height=30)

        GCheckBox_40=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=12)
        GCheckBox_40["font"] = ft
        GCheckBox_40["fg"] = "#333333"
        GCheckBox_40["justify"] = "center"
        GCheckBox_40["text"] = " Cloud Filter"
        GCheckBox_40.place(x=290,y=120,width=143,height=30)
        GCheckBox_40["offvalue"] = "0"
        GCheckBox_40["onvalue"] = "1"
        GCheckBox_40["command"] = self.GCheckBox_40_command
        GCheckBox_40['state'] = 'disabled'

        GLabel_289=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_289["font"] = ft
        GLabel_289["fg"] = "#333333"
        GLabel_289["justify"] = "center"
        GLabel_289["text"] = "3) Select output folder:"
        GLabel_289.place(x=10,y=240,width=200,height=30)

        GButton_996=tk.Button(root)
        GButton_996["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Times',size=12)
        GButton_996["font"] = ft
        GButton_996["fg"] = "#000000"
        GButton_996["justify"] = "center"
        GButton_996["text"] = "Select Folder"
        GButton_996.place(x=300,y=240,width=130,height=30)
        GButton_996["command"] = self.GButton_996_command

        GButton_661=tk.Button(root)
        GButton_661["bg"] = "#a1cd96"
        ft = tkFont.Font(family='Times',size=14)
        GButton_661["font"] = ft
        GButton_661["fg"] = "#000000"
        GButton_661["justify"] = "center"
        GButton_661["text"] = "Generate Startrails"
        GButton_661.place(x=140,y=320,width=232,height=48)
        GButton_661["command"] = self.GButton_661_command

        self.GLabel_312=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_312["font"] = ft
        self.GLabel_312["fg"] = "darkgreen"
        self.GLabel_312["justify"] = "center"
        self.GLabel_312["text"] = ""
        self.GLabel_312.place(x=300,y=60,width=130,height=30)
        
        
    def GButton_941_command(self):
        global srcDirName
        srcDirName = filedialog.askdirectory()
        srcDirName = srcDirName + "/"
        print(srcDirName)
        
        imagefiles = [name for name in os.listdir(srcDirName) if fnmatch(name, '*.jpeg')]
        fileCount = 0
        for imagefile in imagefiles:
            fileCount  += 1
        new_text = "Source directory choosen: " + srcDirName
        self.GMessage_678["text"] = new_text
        self.GLabel_312.config(text = str(fileCount) + " images found")

    def undefined(self):
        print("command")
    def undefined(self):
        print("command")


    def GCheckBox_40_command(self):
        print("command")
        


    def GButton_996_command(self):
        global outputDirName
        outputDirName = filedialog.askdirectory()
        print(outputDirName)
        new_text = "Output directory choosen: " + outputDirName
        self.GMessage_678["text"] = new_text


    def GButton_661_command(self):
        print("command")
        
        basepath = srcDirName
        print(basepath)
        imagefiles = [name for name in os.listdir(basepath) if fnmatch(name, '*.jpeg')]
        #imagefiles = sorted(imagefiles)
        #print(imagefiles)
        height, width = numpy.shape(cv2.imread(f'{basepath}{imagefiles[0]}'))[0:2]

        stack   = numpy.zeros((height, width, 3), dtype = float)
        keo = numpy.zeros((height, len(imagefiles), 3), dtype = float)
        counter = 0
        filter_threshold = 45  #45

        for imagefile in imagefiles:

            image_new = cv2.imread(f'{basepath}{imagefile}')
            keo[:, counter]   = image_new[:, int(width / 2)]
            counter  += 1
            if numpy.average(image_new) >  filter_threshold:
                continue 
            stack     = numpy.maximum(stack, image_new)

        stack = numpy.array(numpy.round(stack), dtype = numpy.uint8)
        star_trails = stack #cv2.cvtColor(stack) #, cv2.COLOR_RGB2BGR

        #filename = basepath + "generatedStatrails.jpeg"
        #rand = str(random.randint(0, 10000))
        #dateANDtime = str(datetime.now().strftime("%m_%d-%I:%M"))
        filename = outputDirName + "/Startrails_" + str(counter) + ".jpeg"
        print(filename)
        cv2.imwrite(filename, star_trails)
        ##cv2.imwrite(f'/dev/shm/keogram.jpg', flippedKeogram)
        print("generated!")
        new_text = "-- SUCCESSFUL! -- Startrails saved: " + filename
        self.GMessage_678["text"] = new_text

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
