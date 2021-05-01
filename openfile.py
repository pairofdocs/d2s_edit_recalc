import os
import sys
import wx
from os.path import basename

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
        super(Mywin, self).__init__(parent, title = title, size = (380,420))  
        self.InitUI() 
         
    def InitUI(self):    
        panel = wx.Panel(self) 
        
        # add button to open file
        btn2 = wx.Button(panel, label = "Open File and Run", pos = (45,30)) 
        btn2.Bind(wx.EVT_BUTTON, self.OnOpen) 
        self.Centre() 
        self.Show(True)

        # add text below button
        st = wx.StaticText(panel, label="Select a file and apply the edits from patches.txt", pos = (45+3, 30+30))

        # add image
        png = wx.Image(imglogo, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (45+3+16, 30+30+150), (png.GetWidth(), png.GetHeight()))
    
    def OnOpen(self, event):
        with wx.FileDialog(self, "Open D2S file", wildcard="D2S files |*.d2s",
                        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # load file and run
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as file:
                    # self.doLoadDataOrWhatever(file)
                    wx.MessageBox(f"D2S file {basename(pathname)} edited and saved.", "Result", wx.OK | wx.ICON_INFORMATION) 
            except IOError:
                wx.LogError(f"Cannot open file {newfile}")

		
app  =  wx.App() 
Mywin(None,'D2S Savefile Edit') 
app.MainLoop()