#--------------------------------------------------------------------------------------------------------------------

from cmu_graphics import *
from Graphics.text import *

#User move block game:


def TurtleStart(app): 
    
    app.TurtleLabelX = app.width / 2
    app.TurtleLabelY = app.height / 2
    app.Turtlelist = []
    app.TurtleRun = False
    
def TurtleDraw(app):
    
    drawRect(0, 0, app.width, app.height, fill = 'salmon')
    
    
    drawLabel("Turtle Game", app.CalLabelX, app.CalLabelY, size = 70, font= 'monospace')

        
    drawLabel("use w a s d commands to control a little square, just type out the command path you want and press space when your done", app.CalLabelX, app.CalLabelY+70, size = 21, font= 'monospace')
    
    drawLabel(' / '.join(app.Turtlelist), app.CalLabelX, app.CalLabelY+140, size = 21, font= 'monospace')
    
    

def TurtleMode(app, key):
    
    if key == 'delete':
        
        app.TurtleRun = False
        app.Turtlelist = []
        
        
        
    if key == 'end' and not(app.calibrate) and not(app.TurtleRun) and not(app.HelpScreenUp):
        
        app.TurtleRun = True
    
 
    elif key == 'space' and app.TurtleRun:
        
        
        
        app.TurtleRun = False
        
       

        app.callist =  []
        
    elif app.TurtleRun and key in ('w', 'a', 's', 'd', '+', '-', 'backspace'):
        
        
        if key == 'backspace':
            
           app.Turtlelist = app.Turtlelist[:-1]
        else:
            app.Turtlelist.append(key)

  
def ReplaceCurrentAssemblyTurtle(app, TurtleCode):
    
    SetUpText(app)
    
    
    app.EnableTyping = True  
    
    for command in TurtleCode:
        
        
        for char in list(command):
            
            
            KeyCommand(app, char) 
            
            
            
            
        KeyCommand(app, 'enter') 
        
        
    app.EnableTyping = False
    
    
    
    