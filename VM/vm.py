from Assembler.assembly import *
import re
#VM Operations


def GetPushCommands(com):
    backup = com
    com = com.replace(' ', '')
     
    com = re.split(r'[;:,-]', com)
    
    
    
    if len(com) < 2:
        return ['Format_error', backup, backup]
    
    mode = com[0]
    
    
    
    
    VMTemplate = VM[mode]
    
    if mode == 'Push':
        
        data = com[1]
    
        
        
     
            
        if isNumber(data) or isvalidregister(data):
                
                VMTemplate = VMTemplate.replace('y', data)
                
                
                print(VMTemplate, 88)
                
                return VMTemplate
                
                
        return ["Data_error", data, backup]
            
        
                
                
    
    if mode == 'Pop':
        
        
        loc = com[1]
    
        print(com)
        
        if isvalidregister(loc):
            
           
        
                
                VMTemplate = VMTemplate.replace('y', loc)
                
                VMTemplate = VMTemplate.replace('x', 'R30')
                
                VMTemplate = VMTemplate.replace('x', 'R30')
                
                
                
                return VMTemplate
            
            
        elif loc == 'DP':
        
                
                VMTemplate = VMTemplate.replace('x', '0')
                VMTemplate = VMTemplate.replace('y', 'R31')
                
                return VMTemplate
                
                
        else:
            
            return ["Register_error", loc, backup]
                
                
                
                
    
    if mode == "if-true-goto":
        
        data = com[-1]
        
        VMTemplate = VMTemplate.replace('x', data)
        
        return VMTemplate
        
        
 
VM = {'Push': 'ALU_RI, R30- R30 ADD 1 \n STORE, *R30- y', 'Pop': 'LOD, y- *x \n STORE, *x- 0 \nALU_RI, x-x SUB 1', 'if-true-goto': 'LOD, R1- *R30 \n JMP, R1- x', 'add': 'Pop, R1 \n Pop, R2 \n ALU, R3- R1 ADD R2 \n Push, R3'}
    

ErrorList = {"Register_error": "[x] is an Invalid Register", "Data_error": "[x] is not valid Data", "Loc_error": "[x] is not a valid Store location", "Condition_error": "[x] is not a valid JUMP condition", "JMP_error": "[x] is an invalid JUMP command", "Mode_error": "[x] is an Invalid Mode", "Format_error": "[x] is an Invalid Format"}
 

code = ['add']



def GetPushCommands(com):
    backup = com
    com = com.replace(' ', '')
     
    com = re.split(r'[;:,-]', com)
    
    
    
    if len(com) < 2:
        return ['Format_error', backup, backup]
    
    mode = com[0]
    
    
    
    
    VMTemplate = VM[mode]
    
    if mode == 'Push':
        
        data = com[1]
    
        
        
     
            
        if isNumber(data) or isvalidregister(data):
                
                VMTemplate = VMTemplate.replace('y', data)
                
                
                print(VMTemplate, 88)
                
                return VMTemplate
                
                
        return ["Data_error", data, backup]
            
        
                
                
    
    if mode == 'Pop':
        
        
        loc = com[1]
    
        print(com)
        
        if isvalidregister(loc):
            
           
        
                
                VMTemplate = VMTemplate.replace('y', loc)
                
                VMTemplate = VMTemplate.replace('x', 'R30')
                
                VMTemplate = VMTemplate.replace('x', 'R30')
                
                
                
                return VMTemplate
            
            
        elif loc == 'DP':
        
                
                VMTemplate = VMTemplate.replace('x', '0')
                VMTemplate = VMTemplate.replace('y', 'R31')
                
                return VMTemplate
                
                
        else:
            
            return ["Register_error", loc, backup]
                
                
                
                
    
    if mode == "if-true-goto":
        
        data = com[-1]
        
        VMTemplate = VMTemplate.replace('x', data)
        
        return VMTemplate
        
        
        
  



def AssembleCode(code, labels, ErrorList, app):
 
    
    
    
    PreRom = code
    
    
    
    
    
    ROM = []
    
    NewROM = []
    
    index  = 0
    
    
    for command in PreRom:
        
         
        if len(command) == 0:
            
            continue
        
        if command in {'add'}:
            
            
         
            
            ROM += VM[command].replace(' ', '').split('\n')
        
            
        else:
            
                
            ROM += [command]
            
            
        
        index += 1  
        
  
    
    index = 0
        
    for command in ROM:
        
       
        
        if command[:4] == 'Push' or command[:3] == 'Pop' or command[:12] == 'if-true-goto':
            
           
            GetAssembly = GetPushCommands(command)
            
            
            if type(GetAssembly) == list:
                
                return ["Register_error", 'R1', command]
            
            
            
            NewROM += GetPushCommands(command).split('\n')
            
            
        
            
        else:
            
                
           
            
            NewROM += [command]
            
            
        index += 1   
        
    
 
   
    
    ROM = NewROM   
    
    
    index = 0
    
    
    for command in ROM:
      
        
        if command[0] == '#':
            
            labels[command] = index
            
    
        index+=1
        
        
    
    
        
        
    BinaryList = []
    
    
    
    
    
    for instruction in ROM:
        
        
        if instruction[0] != '#':
        
        
            binary = getBinary(instruction, app)
            
           
            if binary[0] in ErrorList:
                
              
                
                
                return binary
        
            BinaryList.append(''.join(binary))
            
           
            
        else:
            
            BinaryList.append(instruction)
    
     
    return BinaryList
    
    
    

#-----------------------------------------------------------------------------------


