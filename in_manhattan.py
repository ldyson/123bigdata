# determine if a point is inside a given polygon or not
# Polygon is a list of (x,y) pairs. http://www.ariel.com.au/a/python-point-int-poly.html
# coordinates from https://gist.github.com/baygross/5430626
# use Python 2.7
# use: 

from planar import Polygon

poly_Manhattan = Polygon([
        (40.700292, -74.010773),
        (40.707580, -73.999271),
        (40.710443, -73.978758),
        (40.721762, -73.971977),
        (40.729568, -73.971291),
        (40.733503, -73.973994),
        (40.746834, -73.968072),
        (40.775114, -73.941936),
        (40.778884, -73.942580),
        (40.781906, -73.943589),
        (40.785351, -73.939362),
        (40.789640, -73.936272),
        (40.793149, -73.932238),
        (40.795228, -73.929491),
        (40.801141, -73.928976),
        (40.804877, -73.930907),
        (40.810496, -73.934298),
        (40.834074, -73.934383),
        (40.855371, -73.922281),
        (40.870690, -73.908892),
        (40.878348, -73.928289),
        (40.851151, -73.947258),
        (40.844074, -73.947086),
        (40.828229, -73.955498),
        (40.754019, -74.008713),
        (40.719941, -74.013863),
        (40.718575, -74.013605),
        (40.718802, -74.017038),
        (40.704977, -74.020042),
        (40.700553, -74.016438)
        ])

def point_in_Manhattan(x, y, poly = poly_Manhattan):

    n = len(poly)
    inside = False

    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y)*(p2x - p1x)/(p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside