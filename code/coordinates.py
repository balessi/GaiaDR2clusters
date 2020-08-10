    
import math

def ra_to_degrees(ra):
    """Convert Right Ascencion in format 'hh mm ss.s' to degrees"""
    _ra = ra.strip()
    if ' ' in _ra:
        comps = _ra.split()
        h = int(comps[0])
        m = int(comps[1])
        s = float(comps[2])
        return 15 * (h + m/60 + s/3600)
    #If there is not spaces assume its already in degrees
    return float(_ra)
    
def de_to_degrees(de):
    """Convert Declination in format '+/-dd mm ss' to degrees"""
    _de = de.strip()
    if ' ' in _de:
        comps = _de.split()
        sign = 1
        d = comps[0]
        if d[0] == "-":
            sign = -1
        d = math.fabs(int(d))
        m = int(comps[1])
        s = float(comps[2])
        return math.copysign(d + m/60 + s/3600, sign)
    #If there is not spaces assume its already in degrees
    return float(_de)
