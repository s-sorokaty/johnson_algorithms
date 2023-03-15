import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime as dt

def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)

def plot(df:pd.DataFrame, order:pd.Series):
    #plt.style.use('dark_background')
    fig, gnt = plt.subplots()
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Время')
    gnt.set_ylabel('Станки')

    # Setting ticks on y-axis
    y_labels = df.iloc[:, 0].to_list()
    y_labels.reverse()
    y_ticks = [i*5+1 for i in range(1, len(y_labels)+1)]
    gnt.set_yticks(y_ticks)
    y_ticks.reverse()
    # Labelling tickes of y-axis
    gnt.set_yticklabels(y_labels)
    delays =  [0 for i in range(1, len(y_labels)+1)]
    gnt.grid(True)
    colors = ['red', 'blue', 'black', 'green', 'orange']
    cmap = get_cmap(10)
    detail = 0
    for index in order.index:
        data = df[index]
        workspace = 0
        next_delay = 0

        for val in data:
            if detail == 0:
                gnt.broken_barh([(next_delay, val)], (y_ticks[workspace], 2), facecolors=cmap(detail), label=data.name)
                next_delay += val
                delays[workspace] += next_delay
            else:
                if workspace > 1 and delays[workspace] - delays[workspace-1]<0:
                    
                    gnt.broken_barh([(-(delays[workspace] - delays[workspace-1])+delays[workspace], val)], (y_ticks[workspace], 2), facecolors=cmap(detail), label=data.name)
                    delays[workspace] += -(delays[workspace] - delays[workspace-1])+val
                else:
                    gnt.broken_barh([(delays[workspace], val)], (y_ticks[workspace], 2), facecolors=cmap(detail), label=data.name)
                    delays[workspace] += val

            workspace += 1
        detail +=1

    
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    gnt.legend(by_label.values(), by_label.keys())
    
    plt.savefig("gantt1.png")
    plt.show()
#plot(pd.read_csv('test.csv'), pd.DataFrame([]))