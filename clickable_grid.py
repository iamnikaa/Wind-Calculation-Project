import matplotlib.pyplot as plt

f = plt.figure(figsize=(8, 8))
ax = f.add_subplot()

# initialize your grid
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.xaxis.set_major_locator(plt.FixedLocator(range(10)))
ax.yaxis.set_major_locator(plt.FixedLocator(range(10)))
ax.grid()


# print some info text
t1 = ax.text(.5, .5,
"""LEFT-click to draw a line
RIGHT-click to remove the last point
MIDDLE-click to toggle 'snap-to-grid'""",
bbox=dict(facecolor='w',
          edgecolor='black',
          boxstyle='round, pad=1, rounding_size=1', pad=0))

t2 = ax.text(7, .5,
"""'snap-to-grid active!'""",
bbox=dict(facecolor='w',
          edgecolor='red',
          boxstyle='round, pad=1, rounding_size=1', pad=0))
t2.set_visible(False)


# draw initial lines that will be updated later
l, = ax.plot([], [], lw=2, marker='o', c='k')
p, = ax.plot([], [], lw=0, marker='.', c='r', alpha=0.25)
p_round, = ax.plot([], [], lw=0, marker='o', c='r')


# get a dict to store the values you need to change during runtime
retdict = dict(points=[],
               round_to_int=False)

# define what to do when a mouse-click event is happening
def on_click(event):
    if event.inaxes != ax:
        return
    if event.button == 1:  # (e.g. left-click)
        if retdict['round_to_int']:
            retdict['points'] += [[round(event.xdata), round(event.ydata)]]
        else:
            retdict['points'] += [[event.xdata, event.ydata]]
    elif event.button == 3:  # (e.g. right-click)
        if len(retdict['points']) >= 1:
            retdict['points'] = retdict['points'][:-1]
            plt.draw()

    elif event.button == 2:  # (e.g. middle-click)
        retdict['round_to_int'] = not retdict['round_to_int']
        if retdict['round_to_int']:
            t2.set_visible(True)
        else:
            t2.set_visible(False)
        plt.draw()

    if len(retdict['points']) > 0:
        l.set_visible(True)
        l.set_data(list(zip(*retdict['points'])))

        plt.draw()
    else:
        l.set_visible(False)


# define what to do when a motion-event is detected
def on_move(event):
    if event.inaxes != ax:
        return

    p.set_data(event.xdata, event.ydata)

    if retdict['round_to_int']:
        p_round.set_data(round(event.xdata), round(event.ydata))

    plt.draw()

# connect the callbacks to the figure
f.canvas.mpl_connect('button_press_event', on_click)
f.canvas.mpl_connect('motion_notify_event', on_move)