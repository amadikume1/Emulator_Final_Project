from cmu_graphics import *

#calibration view


def CalibrationStart(app): 
    
    app.CalLabelX = app.width / 2
    app.CalLabelY = app.height / 2
    app.calcibratetime = 0
    app.callist = []
    app.calibrate = False
    app.timestart = False
    app.timeforkeyPress = 1

    
def CalibrationDraw(app):
    
    drawRect(0, 0, app.width, app.height, fill = 'salmon')
    
    
    drawLabel("Calibrate Typing", app.CalLabelX, app.CalLabelY, size = 70, font= 'monospace')
    
    drawLabel("do you feel like the typing is bad", app.CalLabelX, app.CalLabelY+70, size = 30, font= 'monospace')
    

    drawLabel("Well Fix it your diggity dang self then", app.CalLabelX, app.CalLabelY+120, size = 30, font= 'monospace')
    
    drawLabel("Press any key and start typing at your normal speed", app.CalLabelX, app.CalLabelY+170, size = 30, font= 'monospace')
        
    drawLabel("Once complete, enter either space or click the mouse button to return", app.CalLabelX, app.CalLabelY+220, size = 21, font= 'monospace')
    
    drawLabel(''.join(app.callist), app.CalLabelX, app.CalLabelY+300, size = 21, font= 'monospace')
    
    


def CalibrationMode(app, key):
    

    if key == 'delete':
        
        app.calibrate = False
        app.HelpScreenUp = False
        app.timestart = False
        app.calcibratetime = 1

    if key == 'insert' and not(app.calibrate) and not(app.TurtleRun) and not(app.HelpScreenUp):
   
        app.calibrate = True
        app.calcibratetime = 0
        app.timestart = False
     
    
    elif app.calibrate and not(app.timestart):
        
     
        app.timestart = True
        
        
 
    elif key == 'space' and app.calibrate and app.timestart:
        
        app.calibrate = False
        app.timestart = False
        
        
        
        app.timeforkeyPress = (app.calcibratetime / (len(app.callist)+10)) * 1000
        app.calcibratetime = 0
       

        app.callist =  []
    elif app.calibrate and app.timestart:
        
        app.callist.append(key)
 
    if key == 'pageup':
        
        app.cubemode = not(app.cubemode)

