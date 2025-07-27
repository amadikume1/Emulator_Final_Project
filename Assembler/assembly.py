#Assembler
 
import re

 
'''
ALU:
 
 [Mode], [data1] [command] [data2] -> ALU_I, 45 ADD 56
 
'''
 
 
 
modes = {"ALU": '111',"ALU_RI": '100', "ALU_I": '001', "LOD": '010', "STORE": '110', "Branch": '011'}
 
 
 
ALU_OP = {'ADD': '1000', 'SUB':'1100', "MUL": '1110', "DIV":'1111', "MOD":"0001", "POW":"0011", "EQL":"0111", "AND": "1001", "OR": "1011", "FLR": "0010"}  
 
BranchOP = {'10000': "JPI", '11000':'JPR', '11100': 'JPRI', '11110': 'JPII', '11111': 'JPIR', '00001': 'JPRR', '01001': "JMPCIR"}
 
CBOP = {"EQL":"111", "GRAT": "001", "LESS": "011" , "101": "AND", "110": "OR"}
 
StoreOP = {'0': 'R-to-M', '1': 'I-to-M'}
 
LoadOP = {'11': 'LODI', '10': "LODR", '01': "LODI"}
 
 
ChooseOP = {"ALU":  ALU_OP,"ALU_RI": ALU_OP, "ALU_I": ALU_OP, "Load": '010', "Store": '110', "Branch": '011', "RStore": "101"}
 
 
 
 
def isNumber(data):
   
  
    return not(len(data)) == 0 and (data.isdigit() or data[0] == '-' and data[1:].isdigit())
 
def DectoBinary(dec, length):
    
    binary = ''
    
    
    
    if dec >= 2**length or dec <= -2**length:
        
        for i in range(length):
            
            binary += '1'
            
        return binary
    
    
    for i in range(length):
        
        if dec % 2 == 0:
            
            binary += '0'
            
        else:
            
            binary += '1'
            
        dec //= 2   
        
    return binary[::-1]
 
 


def isvalidregister(reg):
    
    
    
    if len(reg) > 1 and len(reg) < 4 and reg[0] == 'R' and int(reg[1:]) < 32 and int(reg[1:]) > 0:
        
        return True
        
    return False
    
    


def islabel(val):
    
    if val[0] == '#':
        
        return True
        
    else:
        
        return False
    
    
 


def getOperation(command, operation):
    
    
    for op in operation:
        
        check = command.split(op)
        
        if len(check) == 2:
            
            return (operation[op], check)
            
            
    return ["Condition_error", command, command]
 


 
def AluData(mode, datalist):
    
    errorList = []
    
   
    
    if mode == 'ALU':
        
        checkR1 = isvalidregister(datalist[0])
        checkR2 = isvalidregister(datalist[1])
        
        if len(datalist) == 2 and checkR1 and checkR2:
            
            
                    return [DectoBinary(int(datalist[0][1:]), 5), DectoBinary(int(datalist[1][1:]), 5)]
    
        if not(checkR1):
            
            return "error"
            
        
        if not(checkR2):
            
             return "error"
            
            
        if  not(len(datalist) == 2):
            
             return "error"
            
            
    elif mode == 'ALU_RI':
        
   
        
        checkV1 = isvalidregister(datalist[0])
        checkV2 = isNumber(datalist[1])
        
        
        checkV3 = isvalidregister(datalist[1])
        checkV4 = isNumber(datalist[0])
        
        
       
        
        if len(datalist) == 2 and (checkV1 and checkV2):
            
            
            
            return [DectoBinary(int(datalist[0][1:]), 5), DectoBinary(int(datalist[1]), 15)]
    
        elif len(datalist) == 2 and (checkV3 and checkV4):
            
         
            
            
            return [DectoBinary(int(datalist[1][1:]), 5), DectoBinary(int(datalist[0]), 15)]
            
            
        else: 
            
            
            
            return "error"
            
            
            
            
    
    elif mode == 'ALU_I':
        
        checkR1 = isNumber(datalist[0])
        checkR2 = isNumber(datalist[1])
        
        
        if len(datalist) == 2 and checkR1 and checkR2:
            
                    
                    return [DectoBinary(int(datalist[0]), 10), DectoBinary(int(datalist[1]), 10)]
    
        if not(checkR1):
            
            return "error"
            
        
        if not(checkR2):
            
            return "error"
            
            
        if  not(len(datalist) == 2):
            
            return "error"
            
               
    
    return "error"
    
    
 
def StoreData(mode, datalist):
    
    
    if mode == 'StoreI':
        
        checkV1 = isvalidregister(datalist[0])
        checkV2 = isNumber(datalist[1])
        
        
        if len(datalist) == 2 and (checkV1 and checkV2):
            
            
            return [DectoBinary(int(datalist[0][1:]), 5), DectoBinary(int(datalist[1]), 22)]
            
            
        else:
            
            return "error"
            
    
    if mode == 'LODR':
        
        checkR1 = isvalidregister(datalist[0])
        checkR2 = isvalidregister(datalist[1])
        
        if len(datalist) == 2 and checkR1 and checkR2:
            
                    return [DectoBinary(int(datalist[0][1:]), 5), DectoBinary(int(datalist[1][1:]), 5)]   
                    
        else:
            
            return "error"
            
    return "error"    
 



 
def LodData(mode, datalist):
    
    
    if mode == 'LODI' or mode == 'LODM':
        
        checkV1 = isvalidregister(datalist[0])
        checkV2 = isNumber(datalist[1])
        
        
        if len(datalist) == 2 and (checkV1 and checkV2):
            
            
            return [DectoBinary(int(datalist[0][1:]), 5), DectoBinary(int(datalist[1]), 22)]
            
        else:
            
            return "error"
            
    
    if mode == 'LODR':
        
        checkR1 = isvalidregister(datalist[0])
        checkR2 = isvalidregister(datalist[1])
        
        if len(datalist) == 2 and checkR1 and checkR2:
            
                    return [DectoBinary(int(datalist[0][1:]), 5), DectoBinary(int(datalist[1][1:]), 5)]   
                    
        else:
            
            return "error"
            
    return "error"
    
 


def getBinary(com, app):
    
   
    command = com
    
    com = com.replace(' ', '')
    
    backup = com
     
    com = re.split(r'[;:,-]', com)
    
    com = backup[:backup.find('-')].split(',') + [backup[backup.find('-') + 1:]]
    
    
    
    while '' in com:
        
        com.remove('')
        
        
    if len(com) == 0:
        
        com = [['']]
        
    
    
    if not(com) == [['']] and (((len(com) != 3 and (com[0] == "JMP" and len(com) != 2)) or (backup.count('-') < 1) or backup.count(',') != 1 or (backup.find(',') > backup.find('-')))):
        
       
        return ["Format_error", backup, command]
    
    mode = com[0]
    
    
    if mode == ['']:
        
        return ['']
    
    
    
    elif mode in {'ALU_I', 'ALU_RI', 'ALU'}:
        
        
        data = com[-1]
    
        loc = com[1]
        
        
        if isvalidregister(loc):
            
            for op in ALU_OP:
                
                if len(data.split(op)) == 2:
                    
                    
                    break
            
            
            if AluData(mode, data.split(op)) == 'error':
                
                return ["Data_error", data, command]
                
                
        
            return [modes[mode]] + [ALU_OP[op]] + [DectoBinary(int(loc[1:]), 5)]  + AluData(mode, data.split(op))
            
        else:
            
            return ["Register_error", loc, command]
            
            
    elif mode == 'LOD':
        
        data = com[-1]
    
        loc = com[1]
        
        
        if isvalidregister(loc):
            
            
            if isvalidregister(data):
                
                return [modes[mode]] + ['10'] + [DectoBinary(int(loc[1:]), 5)] + [DectoBinary(int(data[1:]), 5)]
            
            
            elif isNumber(data):
                
                
                return [modes[mode]] + ['11'] + [DectoBinary(int(loc[1:]), 5)] + [DectoBinary(int(data), 21)]
                
                
        
            elif data[0] == '*' and isNumber(data[1:]):
            
                 return [modes[mode]] + ['01'] + [DectoBinary(int(loc[1:]), 5)] + [DectoBinary(int(data[1:]), 21)]
             
                 
                 
            elif data[0] == '*' and isvalidregister(data[1:]):
            
                 return [modes[mode]] + ['00'] + [DectoBinary(int(loc[1:]), 5)] + [DectoBinary(int(data[2:]), 5)]
                 
                 
            else:
                
                return ["Data_error", data, command]
                
        else:
            
            return ["Register_error", loc, command]
                 
                 
                 
    
    
                 
    elif mode == 'STORE':
        
        data = com[-1]
        
        loc = com[1]
        
  
        
        if loc[0] == '*' and isNumber(loc[1:]):
            
            if isNumber(data):
            
                return ['110'] + ['0'] + [DectoBinary(int(loc[1:]), 13)] + [DectoBinary(int(data), 15)]
                
            
            elif isvalidregister(data):
                
                
                return ['110'] + ['1'] + [DectoBinary(int(loc[1:]), 13)] + [DectoBinary(int(data[1:]), 5)]
                
            
            else:
                
                return ["Data_error", data, command]
                
                
        elif loc[0] == '*' and isvalidregister(loc[1:]):
            
            
            if isNumber(data):
            
                return ['101'] + ['0'] + [DectoBinary(int(loc[2:]), 5)] + [DectoBinary(int(data), 22)]
                
            
            elif isvalidregister(data):
                
                
                
                return ['101'] + ['1'] + [DectoBinary(int(loc[2:]), 5)] + [DectoBinary(int(data[1:]), 5)]
                
                
            else:
                
                return ["Data_error", data, command]
                
                
        else:
                
                return ["Loc_error", loc, command]
            
            
            
                
   
    elif mode == 'JMP':
      
        Jmpcondition = com[1]
        
 
        
        if len(com) == 2:
            data = com[-1]
        
            loc = com[1]
        
            
            if isNumber(data):
                
               
            
                return ['011'] + ['10000'] + [DectoBinary(int(data), 24)]
                
                
            elif islabel(data) and data in app.labels:
                
                
                
                return ['011'] + ['10000'] + [DectoBinary(int(app.labels[data]), 24)]
                
                
            elif isvalidregister(data):
                
                return ['011'] + ['11000'] + [DectoBinary(int(data[1:]), 5)]
                
                
            
            else:
                
                return ["Data_error", data, command]
                
                
        elif len(com) == 3 and isvalidregister(Jmpcondition):
            
          
            data = com[-1]
        
            Jmpcondition = com[1]
            
            if isvalidregister(Jmpcondition):
                
                
                if isNumber(data):
                    
                    return ['011'] + ['11100'] + [DectoBinary(int(Jmpcondition[1:]), 5)] + [DectoBinary(int(data), 19)]
                    
                    
                elif islabel(data) and data in app.labels:
                
                    return ['011'] + ['11100'] + [DectoBinary(int(Jmpcondition[1:]), 5)] + [DectoBinary(int(app.labels[data]), 19)]
                
                    
                elif isvalidregister(data):
                    
                    return  ['011'] + ['00001'] + [DectoBinary(int(Jmpcondition[1:]), 5)] +  [DectoBinary(int(data[1:]), 5)]
                    
                    
                else:
                
                    return ["Data_error", data, command]
                
            else:
                
                return ["Condition_error", data, command]
                    
                
        
        elif len(com) == 3:
            op = getOperation(Jmpcondition, CBOP)
 
            if op[0] == "Condition_error":
                
                return op
            
            RegOne = op[1][0]
            RegTwo = op[1][1]
            data = com[-1]
            
            if isvalidregister(RegOne) and  isvalidregister(RegTwo):
                
                if isNumber(data):
                    
                    return ['011'] + ['01001'] + [op[0]] + [DectoBinary(int(RegOne[1:]), 5)] + [DectoBinary(int(RegTwo[1:]), 5)] + [DectoBinary(int(data), 11)]
                    
                elif islabel(data) and data in app.labels:
                    
                    return ['011'] + ['01001'] + [op[0]] + [DectoBinary(int(RegOne[1:]), 5)] + [DectoBinary(int(RegTwo[1:]), 5)] + [DectoBinary(int(app.labels[data]), 11)]
                
                
                elif isvalidregister(data):
                    
                    
                   
                    return ['011'] + ['01101'] + [op[0]] + [DectoBinary(int(RegOne[1:]), 5)] + [DectoBinary(int(RegTwo[1:]), 5)] + [DectoBinary(int(data[1:]), 5)] 
                    
                    
                else:
                
                    return ["Data_error", data, command]
                    
            
                    
            else:
                
                return ["Register_error", f"{RegOne} or {RegTwo}", command]
                
        
        else:
            
           return ["JMP_error", data, command]
        
    return ["Mode_error", mode, command]
 
