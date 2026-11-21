SPEC = dict(left=1150, top=70, k=1.08)
B = 14
def toC(x, y, spec=SPEC):
    return (spec['left'] + B + x*spec['k'], spec['top'] + B + y*spec['k'])
def F(s, P, T):
    return dict(s=s, P=P, T=T)
def under(f, x, y):
    """canvas point of screen point (x,y) under focus f (identity if f None)"""
    cx, cy = toC(x, y)
    if f is None: return (cx, cy)
    px, py = toC(*f['P'])
    return (f['T'][0] + f['s']*(cx-px), f['T'][1] + f['s']*(cy-py))
def box(f, b):
    x0, y0 = under(f, b[0], b[1]); x1, y1 = under(f, b[0]+b[2], b[1]+b[3])
    return (round(x0,1), round(y0,1), round(x1,1), round(y1,1))
def vis(f):
    # visible screen y-range and screen x-range on canvas
    px, py = toC(*f['P'])
    y_top = (py + (0 - f['T'][1])/f['s'] - (SPEC['top']+B))/SPEC['k']
    y_bot = (py + (1080 - f['T'][1])/f['s'] - (SPEC['top']+B))/SPEC['k']
    xl = under(f, 0, 0)[0]; xr = under(f, 390, 0)[0]
    return dict(screen_y=(round(y_top,1), round(y_bot,1)), canvas_x=(round(xl,1), round(xr,1)))
def rig(f):
    px, py = toC(*f['P'])
    return dict(scale=f['s'], x=round(f['T'][0]-f['s']*px,2), y=round(f['T'][1]-f['s']*py,2))
FOC = {
 'F1':      F(1.4, [195, 236], [1420, 200]),
 'Fcreate': F(1.4, [195, 734], [1420, 700]),
 'Fconf':   F(1.8, [195, 575], [1500, 528]),
 'Ftotals': F(1.5, [195, 560], [1440, 520]),
 'Fcard':   F(1.4, [195, 142], [1420, 300]),
 'Fhand':   F(1.7, [195, 532], [1480, 500]),
}
if __name__ == '__main__':
    for k, f in FOC.items():
        print(k, f, 'rig', rig(f), vis(f), 'P canvas', tuple(round(v,1) for v in toC(*f['P'])))
