from libraries import *

def firstGraph():
    # 100 linearly spaced numbers
    x = np.linspace(-5,5,100)
    # the function, which is y = x^2 here
    y = x**2
    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('#000000')
    ax.spines['top'].set_color('#000000')
    ax.spines['left'].set_color('#000000')
    ax.spines['bottom'].set_color('#000000')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    # plot the function
    plt.plot(x,y, 'b')
    # show the plot
    plt.show()