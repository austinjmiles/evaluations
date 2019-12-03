import numpy as np
from matplotlib import pyplot as plt

def StatisticalAnalysis(in_data): #$data[questions][responses] prints mean and stddev of each question and prints histogram
#Returns a list of lists where the inner list is [mean, stddev, $OutputOfPlt.Hist()]

    data = np.array(in_data)#Just in case, cause np arrays are nice :^)

    return_list = [0,]*len(in_data) #Return list is the length of the number of questions
    return_line = []
    for i in range(len(in_data)):
        return_line.append(np.mean(data[i]))
        #print(np.mean(data[i]))
        return_line.append(np.std(data[i]))
        #print(np.std(data[i]))
        return_line.append(plt.hist(data[i], bins=[0,1,2,3,4,5,6], align='left', rwidth=.5))
        return_list[i] = return_line
        return_line = []

    return return_list