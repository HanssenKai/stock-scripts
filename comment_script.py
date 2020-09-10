from pymouse import PyMouse
from pykeyboard import PyKeyboard
import random
import scipy
import time
from scipy import interpolate
import webbrowser

def retrieve_comments():

    url = "https://www.shareville.no/aksjer/mest-kommentert"
    webbrowser.get('chromium').open_new(url)

m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()
# print(x_dim)
# print(y_dim)
# m.move(int(x_dim/2-40),1060)


def movemouse(x, y):    
    """
    Use Bezier line to simulate human mouse movements
    """
    cp = random.randint(3, 6)  # Number of control points. Must be at least 2.
    x1, y1 = m.position()
    x2, y2 = x, y  # Destination
    time.sleep(random.randint(4, 8)+random.random())


    # Distribute control points between start and destination evenly.
    x = scipy.linspace(x1, x2, num=cp, dtype='int')
    y = scipy.linspace(y1, y2, num=cp, dtype='int')
    k.press_key(k.page_down_key)

    # Randomise inner points a bit (+-RND at most).
    RND = 10
    xr = scipy.random.randint(-RND, RND, size=cp)
    yr = scipy.random.randint(-RND, RND, size=cp)
    xr[0] = yr[0] = xr[-1] = yr[-1] = 0
    x += xr
    y += yr

    # Approximate using Bezier spline.
    degree = 3 if cp > 3 else cp - 1  # Degree of b-spline. 3 is recommended.
                                      # Must be less than number of control points.
    tck, u = scipy.interpolate.splprep([x, y], k=degree)
    u = scipy.linspace(0, 1, num=max(x_dim, y_dim))
    points = scipy.interpolate.splev(u, tck)

    # Move mouse.
    duration = random.randint(1, 2)
    timeout = duration / len(points[0])
    for point in zip(*(i.astype(int) for i in points)):
        # pyautogui.platformModule._moveTo(*point)
        m.move(*point)
        time.sleep(timeout)
    time.sleep(random.randint(2,3)+random.random())
    x1,y1 = m.position()
    m.click(x1, y1)


def main():
    ymin = random.randint(675, 680)
    ymax = random.randint(683, 705)
    xmin = random.randint(1010, 1040)
    xmax = random.randint(1046, 1180)
    num = random.randint(20,25)
    i = 0
    while (i<num):
        movemouse(random.randint(xmin, xmax), random.randint(ymin, ymax))
        i+=1
    

if __name__ == '__main__':
    main()