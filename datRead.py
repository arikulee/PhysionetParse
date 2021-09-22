from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import shutil
import posixpath
import wfdb_paths
import wfdb


'''
# DICTIONARY KEYS FOR REF

dict_keys(['record_name', 'extension', 'sample', 'symbol', 'subtype', 
           'chan', 'num', 'aux_note', 'fs', 'label_store', 'description', 
           'custom_labels', 'contained_labels', 'ann_len'])
'''

# LOOPS THROUGH LIST TO CONVERT SIGNAL TO CSV FILES

def csv_export(db):
    
    if db == 'MIT-BIHArr':
        
        data = ['100','101','102','103','104','105','106','107','108','109','111','112','113','114',
               '115','116','117','118','119','121','122','123','124','200','201','202','203','205',
               '207','208','209','210','212','213','214','215','217','219','220','221','222','223',
               '228','230','231','232','233','234']
        
    else:
            
         data = ['04015','04043','04048','04126','04746','04908','04936','05091',
        '05121','05261','06426','06453','06995','07162','07859','07879','07910','08215',
        '08219','08378','08405','08434','08455']
    
    for i in (data):
        
        print('Processing ', i)
        
        record = wfdb.rdrecord(str(db)+'/'+i)
        annotation = wfdb.rdann(str(db)+'/'+i, 'atr')
        
        sam = annotation.sample
        sam = np.reshape(sam, (len(sam),1))
        sym = annotation.symbol
        sym = np.reshape(sym, (len(sym),1))
        lab = annotation.aux_note
        lab = np.reshape(lab, (len(lab),1))
    
        arr = np.concatenate((sam,sym,lab), axis = 1)
        
        # SAVES SIGNAL CSV
        sig = record.p_signal
        out = wfdb_paths.outputpath+str(db)+'/'
        arrOut = wfdb_paths.atr_outputpath+str(db)+'/annotation/'
        
        if not os.path.exists(wfdb_paths.outputpath):
            os.mkdir(wfdb_paths.outputpath)
            
        if not os.path.exists(wfdb_paths.atr_outputpath):
            os.mkdir(wfdb_paths.atr_outputpath)
        
        if not os.path.exists(out):
            os.mkdir(out)
        
        if not os.path.exists(arrOut):
            os.mkdir(arrOut)
            
        np.savetxt(out+str(i)+'.csv', sig, delimiter=',')
        
        # SAVES SIGNAL ANNOTATION
        arr = pd.DataFrame(arr)
        arr.to_csv(arrOut+str(i)+'.csv')

    return
