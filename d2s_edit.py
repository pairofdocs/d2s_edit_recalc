import os
import sys
import wx

from edit_and_recalc import open_and_edit

# refs 
# https://wxpython.org/Phoenix/docs/html/wx.FileDialog.html
# https://www.tutorialspoint.com/wxpython/wx_dialog_class.htm
# https://stackoverflow.com/questions/55698056/minimal-wx-filedialog-example-freezes-program


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

imglogo = resource_path("d2logo_sm.png")


class Mywin(wx.Frame): 
    def __init__(self, parent, title): 
        super(Mywin, self).__init__(parent, title = title, size = (380,460))  
        self.InitUI() 
         
    def InitUI(self):    
        panel = wx.Panel(self) 
        
        # add button to open file
        btn2 = wx.Button(panel, label = "Open File and Run", pos = (15,3)) 
        btn2.Bind(wx.EVT_BUTTON, self.OnOpen) 
        self.Centre() 
        self.Show(True)

        # add text below button
        st = wx.StaticText(panel, label="Select a file and apply these edits from patches.txt:", pos=(15+3, 1+30))

        # display uncommented patches
        with open('patches.txt') as f:
            lines = f.readlines()
            uncommented = ""
            for i in range(1,len(lines)):
                if lines[i].strip() and lines[i][0] != '#':
                    uncommented += lines[i-1] + lines[i] + "\n"
        text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL, pos=(3, 8+30+20), size=(358,200))
        text.WriteText(uncommented)

        # add image
        png = wx.Image(imglogo, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (45+3+16, 30+30+40+185), (png.GetWidth(), png.GetHeight()))
    
    def OnOpen(self, event):
        with wx.FileDialog(self, "Open D2S file", wildcard="D2S files |*.d2s",
                        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            # load file and run
            pathname = fileDialog.GetPath()
            try:
                open_and_edit(pathname)
                wx.MessageBox(f"D2S file {os.path.basename(pathname)} edited and saved.", "Result", wx.OK | wx.ICON_INFORMATION) 
            except Exception as e:
                wx.LogError(f"Error: {e}")

		
app  =  wx.App() 
Mywin(None,'D2S Savefile Edit') 
app.MainLoop()
