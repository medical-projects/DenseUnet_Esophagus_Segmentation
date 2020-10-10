#after running pr_curve.py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

font = {'family' : 'normal',
        'size'   : 14}
plt.rc('font', **font)

def read_names( tag,test_path):

    gtv_names = [join(test_path, g) for g in [f for f in listdir(test_path ) if ~isfile(join(test_path, f)) ] \
                 if g.endswith(tag) and not g.endswith('all_dice2.xlsx')and not g.endswith('all_dice.xlsx')]
    gtv_names=np.sort(gtv_names)
    return gtv_names


def calculate_precision_recall(xls_files):
    f=True

    for x in xls_files:
        try:
            df = pd.read_excel( x)
            if f:
                f = False
                TP = df['TP']
                TN = df['TN']
                FP = df['FP']
                FN = df['FN']
            else:
                TP = df['TP'] + TP
                TN = df['TN'] + TN
                FP = df['FP'] + FP
                FN = df['FN'] + FN
        except:
            print(x)

    precision =  TP/(TP+FP)
    recall =  TP/(TP+FN)
    print((np.sum(precision)+1)/ (np.size(precision)+1))
    return recall,precision

test_path= ['/exports/lkeb-hpc/syousefi/2-lkeb-17-dl01/syousefi/TestCode/EsophagusProject/Code/Log_2019_09_23/Dataset3/33533_0.75_4-train1-07142020_020/result/',#spatial
            '/exports/lkeb-hpc/syousefi/2-lkeb-17-dl01/syousefi/TestCode/EsophagusProject/Code/Log_2019_09_23/Dataset3/33533_0.75_4-train1-07102020_140/result/',#spatial+channel
            '/exports/lkeb-hpc/syousefi/2-lkeb-17-dl01/syousefi/TestCode/EsophagusProject/Code/Log_2019_09_23/Dataset3/33533_0.75_4-train1-07052020_000/result/',#channel
'/exports/lkeb-hpc/syousefi/2-lkeb-17-dl01/syousefi/TestCode/EsophagusProject/Code/Log_2019_09_23/Dataset3/33533_0.75_4-train1-04172020_140/result/','/exports/lkeb-hpc/syousefi/2-lkeb-17-dl01/syousefi/TestCode/EsophagusProject/Code/Log_2019_09_23/Dataset3/33533_0.75_4-train1-08052020_140/result/'
            ]

print('DDUnet')
xls_files=read_names(tag='.xlsx',test_path=test_path[3])
recall,precision= calculate_precision_recall(xls_files)
precision=precision.to_numpy()
precision=np.insert(precision,-1,1,axis=0)
# print(np.sum(precision3)/np.size(precision3))
recall=recall.to_numpy()
recall = np.insert(recall,-1,0,axis=0)


print('DDSpatialAttUnet')
xls_files=read_names(tag='.xlsx',test_path=test_path[0])
recall1,precision1= calculate_precision_recall(xls_files)
precision1=precision1.to_numpy()
precision1=np.insert(precision1,-1,1,axis=0)
# print(np.sum(precision)/np.size(precision))
recall1=recall1.to_numpy()
recall1 = np.insert(recall1,-1,0,axis=0)



print('DDChannelAttUnet')
xls_files=read_names(tag='.xlsx',test_path=test_path[2])
recall2,precision2= calculate_precision_recall(xls_files)
precision2=precision2.to_numpy()
precision2=np.insert(precision2,-1,1,axis=0)
# print(np.sum(precision2)/np.size(precision2))
recall2=recall2.to_numpy()
recall2 = np.insert(recall2,-1,0,axis=0)



print('DDSpatialChannelAttUnet')
xls_files=read_names(tag='.xlsx',test_path=test_path[1])
recall3,precision3= calculate_precision_recall(xls_files)
precision3=precision3.to_numpy()
precision3=np.insert(precision3,-1,1,axis=0)
# print(np.sum(precision1)/np.size(precision1))
recall3=recall3.to_numpy()
recall3 = np.insert(recall3,-1,0,axis=0)

print('DDSpatialAttUnetBoundryLoss')
xls_files=read_names(tag='.xlsx',test_path=test_path[4])
recall4,precision4= calculate_precision_recall(xls_files)
precision4=precision4.to_numpy()
precision4=np.insert(precision4,-1,1,axis=0)
# print(np.sum(precision4)/np.size(precision4))
recall4=recall4.to_numpy()
recall4 = np.insert(recall4,-1,0,axis=0)


cnn_tags=['DDUnet',
              'DDChannelAttUnet',
              'DDSpatialAttUnet',
              'DDSpatialChannelAttUnet',
              'Skip_att',
              'DDSpatialAttUnetBoundaryLoss',
              # 'FocalLoss',

              ]



# color=['pink', 'lightblue', 'lightgreen','orchid','navy']
color = ['pink', 'lightblue',  'tomato',
         'lightgreen',  'hotpink', 'orchid','cyan']
plt.figure()
line1, = plt.plot(1-recall,precision,linestyle='-',color=color[0])
line2, = plt.plot(1-recall1,precision1,linestyle='-',color=color[1])
line3, =plt.plot(1-recall2,precision2,linestyle='-',color=color[2])
line4, =plt.plot(1-recall3,precision3,linestyle='-',color=color[3])
line5, =plt.plot(1-recall4,precision4,linestyle='-',color=color[4])

plt.legend((line1, line2,line3,line4,line5),('DDUnet','DDSpatialAttUnet',
                                       'DDChannelAttUnet','DDSpatialChannelAttUnet','DDSpatialAttUnetBoundryLoss'))
plt.xlim([0,1])
plt.ylim([0,1])
plt.xlabel('1-Recall')
plt.ylabel('Precision')
plt.title('ROC')
plt.show()
print(3)