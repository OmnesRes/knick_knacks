import pylab as plt
import numpy as np
'''This script will plot cdf curves. You only need to provide a sorted list of values.  To make the curve smoother you can increase
the number of bins by adjusting the interval variable'''



def cdf(sorted_list):
    new_y_values=[]
    cumulative=0
    newindex=0
    for i in bins:
        number=0
        for j in sorted_list[newindex:]:
            if j<i:
                number+=1
            else:
                break
        newindex+=number
        cumulative+=100*number/float(len(sorted_list))
        new_y_values.append(cumulative)
    return new_y_values



#example cdf

##choose the start and end of your distribution and interval
start=-150
end=150
interval=1

#this makes the bins
bins=np.arange(start,end,interval)

##this is an example list, load your data here
example=np.random.normal(0,50,100000)
#you need to sort your values
example.sort()
cdf_example=cdf(example)


##this plots your cdf
##fig = plt.figure()
##ax = fig.add_subplot(111)
##ax.plot(bins,cdf_example,'--',lw=6)
##ax.tick_params(axis='x',length=15,width=3,direction='out',labelsize=30)
##ax.tick_params(axis='y',length=15,width=3,direction='out',labelsize=30)
##ax.spines['bottom'].set_position(['outward',10])
##ax.spines['left'].set_position(['outward',10])
##ax.spines['top'].set_visible(False)
##ax.spines['right'].set_visible(False)
##ax.spines['left'].set_linewidth(3)
##ax.spines['bottom'].set_linewidth(3)
##ax.spines['left'].set_bounds(0,100)
##ax.xaxis.set_ticks_position('bottom')
##ax.yaxis.set_ticks_position('left')
##plt.ylim(-1,101)
##plt.show()

########################################################################

##bonus code
##plot with more than one curve, with labels

##first curve
##first=np.random.normal(0,50,100000)
##first.sort()
##cdf_first=cdf(first)
###second curve
##second=np.random.normal(-20,50,100000)
##second.sort()
##cdf_second=cdf(second)
##
##fig = plt.figure()
##ax = fig.add_subplot(111)
##ax.plot(bins,cdf_first,'--',lw=6,color='b')
##ax.plot(bins,cdf_second,'--',lw=6,color='r')
##ax.tick_params(axis='x',length=15,width=3,direction='out',labelsize=30)
##ax.tick_params(axis='y',length=15,width=3,direction='out',labelsize=30)
##ax.spines['bottom'].set_position(['outward',10])
##ax.spines['left'].set_position(['outward',10])
##ax.spines['top'].set_visible(False)
##ax.spines['right'].set_visible(False)
##ax.spines['left'].set_linewidth(3)
##ax.spines['bottom'].set_linewidth(3)
##ax.spines['left'].set_bounds(0,100)
##ax.xaxis.set_ticks_position('bottom')
##ax.yaxis.set_ticks_position('left')
##ax.legend(('1','2'),frameon=False,loc=2,fontsize=20)
##plt.ylim(-1,101)
##plt.show()
##
##
##
##
##





