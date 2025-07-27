from VM.vm import *
from Assembler.assembly import *
#Language



VarLst = []
import re


def GetVarAssembly(command, VarLst):
    
        
        
        Operators = {'+': 'add', '-':'sub'}
    
  
        
        translation = []
        
        
        if not(command[1] in set(VarLst)):
                VarLst.append(command[1])
        
        
        if isNumber(command[-1]):
            
            
                
            
            return [f"Push, {command[-1]}", 'Pop, R1', f"ALU_RI, R2- R31 ADD {VarLst.index(command[1])}", "STORE, *R2-R1"]
            
            
            
        else:
            
            opList = []
            
            for operator in command[-1]:
                
                if operator in Operators:
                    
                    
                    opList.append(Operators[operator])
            
            
            PartsOfOperation = re.split(r'[+-]', command[-1])
            
            for componet in PartsOfOperation:
                
                if not(isNumber(componet)):
                    
                    return ['Data_error', 55]
                    
                    
            for part in PartsOfOperation[::-1]:       
                    
                
                translation.append(f"Push, {part}")
             
            
            
            return translation + opList + ['Pop, R1', f"ALU_RI, R2- R31 ADD {VarLst.index(command[1])}", "STORE, *R31-R1"]
            
            
    





def LanguageToAssembly(command):
    
    returnLst = ['LOD, R31-20']
    
    for i in range(len(command)):
        
        com = re.split(r'[=]', command[i])
                
       
        
        com = com[0].split(' ') + [com[1].replace(' ', '')]
                
        
        
        while '' in com:
            com.remove('')
                
    
        returnLst += GetVarAssembly(com, VarLst)
        
    
         
    return returnLst
         
    
        
        