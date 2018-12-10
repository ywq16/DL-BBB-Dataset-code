import re,csv
import numpy as np

def get_datasets(): 
    
    sourcefile = open('train-5-fold-dataset.csv') # source file
    lines = sourcefile.readlines() 
    lastLine = lines[-1]
    outfile = open('0323-Sideffects_CNS_in_line_sorted.tsv','w')
    entire_dataset = []
    current_event = np.zeros(43)
    print 'Reading data file'

    for line in lines:
        Category_effects = [0]*43
        infoList = line.strip().split(',')
        currentCID = infoList[0] 
        if infoList[3] != 'NONE': 
            currentSideEffectMatch = infoList[2:]
            length = len(currentSideEffectMatch)
            if length > 42:
               length = 42
            #print length
            for i in range(0,length,1):
               # index=int(currentSideEffectMatch[i])  
                Category_effects[i] = int(currentSideEffectMatch[i])  
                #print index
               # current_event[i/2]=index
            #print  Category_effects
           # current_event[0] = string(currentCID)
            Category_effects[-1] = int(currentSideEffectMatch[-1]) 
            entire_dataset.append(Category_effects)
            current_event = np.zeros(43)

        else:
      
            entire_dataset.append(current_event)
            #current_event = np.zeros(43)
    entire_dataset = np.array(entire_dataset, dtype=np.int)
    #print train
    
    sourcefile.close()
    outfile.close()
    return entire_dataset[:250]

def get_datasets1(): 
    
    sourcefile = open('test.csv') # source file
    lines = sourcefile.readlines() 
    lastLine = lines[-1]
    outfile = open('0323-Sideffects_CNS_in_line_sorted.tsv','w')
    entire_dataset = []
    current_event = np.zeros(43)
    print 'Reading data file'

    for line in lines:
        Category_effects = [0]*43
        infoList = line.strip().split(',')
        currentCID = infoList[0] 
        if infoList[3] != 'NONE': 
            currentSideEffectMatch = infoList[2:]
            length = len(currentSideEffectMatch)
            if length > 42:
               length = 42
            #print length
            for i in range(0,length,1):
               # index=int(currentSideEffectMatch[i])  
                Category_effects[i] = int(currentSideEffectMatch[i])  
                #print index
               # current_event[i/2]=index
            #print  Category_effects
           # current_event[0] = string(currentCID)
            Category_effects[-1] = int(currentSideEffectMatch[-1]) 
            entire_dataset.append(Category_effects)
            current_event = np.zeros(43)

        else:
      
            entire_dataset.append(current_event)
            #current_event = np.zeros(43)
    entire_dataset = np.array(entire_dataset, dtype=np.int)

    
    sourcefile.close()
    outfile.close()
    return entire_dataset[:250]
