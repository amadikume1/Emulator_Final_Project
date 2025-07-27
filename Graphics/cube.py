import math
from cmu_graphics import *
from Graphics.text import *

#Cube code:

#Used this Video for Theory, No code was taken: https://www.youtube.com/watch?v=ih20l3pJoeU
#Also used ChatGPT to understand some theory, but no code was taken

def MatrixMulti(m1, m2):
    
    output = []
    
    output.append(m1[0] * m2[0][0] + m1[1] * m2[1][0] + m1[2] * m2[2][0] + m2[3][0])
    output.append(m1[0] * m2[0][1] + m1[1] * m2[1][1] + m1[2] * m2[2][1] + m2[3][1])
    output.append(m1[0] * m2[0][2] + m1[1] * m2[1][2] + m1[2] * m2[2][2] + m2[3][2])
    
    x = m1[0] * m2[0][3] + m1[1] * m2[1][3] + m1[2] * m2[2][3] + m2[3][3]
    
    if x != 0:
        
        output[0] = output[0] / x
        output[1] = output[1] / x
        
        output[2] = output[2] / x
        
    
    output[0] += .2
    
    output[2] += .2
    
    return output



def ShapeStart(app):
  
    
    #just AI to get square matrix
    app.Square = [[[0, 0, 0], [0, 1, 0], [1, 1, 0]], [[0, 0, 0], [1, 1, 0], [1, 0, 0]],  
                        
                      [[1, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 0, 0], [1, 1, 1], [1, 0, 1]], 
                      
                      [[1, 0, 1], [1, 1, 1], [0, 1, 1]], [[1, 0, 1], [0, 1, 1], [0, 0, 1]], 
                      
                      [[0, 0, 1], [0, 1, 1],[0, 1, 0]], [[0, 0, 1], [0, 1, 0], [0, 0, 0]],
                      
                      [[0, 1, 0], [0, 1, 1], [1, 1, 1]], [[0, 1, 0], [1, 1, 1], [1, 1, 0]],
                      
                      [[1, 0, 1], [0, 0, 1], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [1, 0, 0]]]
                      
                      
                      
    # matrix of square exists in 3d space, but must be compressed into 2d space
    app.stepsPerSecond = 60
    app.angle = 90 * 0.0174533
    app.hold = False
    
    app.NearPlane = .1
    app.FarPlane = 1000
    app.color = 'grey'
    app.zadd = 3
    
    app.XYProj = (1 / math.tan(app.angle / 2))
    
    
    
    app.Projection = [[(app.width/app.height)*app.XYProj, 0, 0, 0], 
    
                  [0, (app.width/app.height) * app.XYProj, 0, 0], 
                  
                  [0, 0, (app.FarPlane /  (app.FarPlane - app.NearPlane)), 1], 
                  
                  [0, 0, ((-app.NearPlane * app.FarPlane) /  (app.FarPlane - app.NearPlane)), 0]]
    
    app.anglez = 0
    app.anglex = 0
    app.angley = 0
    
    UpdateRotation(app)


def MoveObject(app):
    
   
            
        app.anglez = int(app.CubeMemory.mem[2]) * .1
          
            
      
        app.angley = int(app.CubeMemory.mem[1]) * .1
        
            
        app.anglex = int(app.CubeMemory.mem[0]) * .1
        

def ResetItem(app):
    if app.anglex != 0 and not(app.Hold):
        
        if app.anglex < 0:
            
            app.anglex += .02
            
        else:
            app.anglex -= .02
            
        
        if abs(app.anglex) < .01:
            
            app.anglex = 0
            
        
    if app.angley != 0 and not(app.Hold):
        
        if app.angley < 0:
            
            app.angley += .02
            
        else:
            
            app.angley -= .02
            
        if abs(app.angley) < .01:
            
            app.angley = 0
            
            
   
    if app.anglez != 0 and not(app.Hold):
        
        if app.anglez < 0:
            
            app.anglez += .02
            
        else:
            app.anglez -= .02
        
        
        if abs(app.anglez) < .01:
            
            app.anglez = 0
            
            
    if app.anglez == 0 and app.anglex == 0 and app.angley == 0:
        
        app.reset = False
 
def UpdateRotation(app):
    
    app.rotationz = [[math.cos(app.anglez), -math.sin(app.anglez), 0, 0],
                     [math.sin(app.anglez), math.cos(app.anglez), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]]
                     
                     
    app.rotationx = [[math.cos(app.anglex), -math.sin(app.anglex), 0, 0],
                     [math.sin(app.anglex), math.cos(app.anglex), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]]
                     
                     
    app.rotationy = [
                    [math.cos(app.angley), 0, math.sin(app.angley), 0],
                    [0, 1, 0, 0],
                    [-math.sin(app.angley), 0, math.cos(app.angley), 0],
                    [0, 0, 0, 1]]
    

def DrawObject(app):
    
    for triangle in app.Square:
        
        temp = []
        
        
        
        
        
        for i in range(len(triangle)):
            
            temp.append(MatrixMulti([i - .5 for i in triangle[i]], app.rotationz))
            
            temp[i] = (MatrixMulti(temp[i], app.rotationx))
            
            temp[i] = (MatrixMulti(temp[i], app.rotationy))
            
            temp
            temp[-1][-1] += app.zadd
        
        
       
            
        for i in range(len(temp)):
            
            temp[i] = MatrixMulti(temp[i], app.Projection)
            
            
            
 
        drawPolygon(temp[0][0] * app.width/2 + app.width/2, temp[0][1] * app.height/2 + app.height/2, 
                    temp[1][0] * app.width/2 + app.width/2, temp[1][1] * app.height/2 + app.height/2, 
                    temp[2][0] * app.width/2 + app.width/2, temp[2][1] * app.height/2 + app.height/2, 
                    fill= app.color)

    
        
        
        
        
    