import numpy as np
import pdb  # use pdb.set_trace() for debugging

# 구체와 레이의 교차 검사 함수
# ray_origin = viewPoint
# ray_direction = d
# return hit, t
def intersect_ray_sphere(ray_origin, ray_direction, sphere):
    oc = ray_origin - sphere.center     # p
    a = np.dot(ray_direction, ray_direction)    # d dot d
    b = np.dot(oc, ray_direction)               # p dot d
    # pdb.set_trace()
    c = np.dot(oc, oc) - sphere.radius * sphere.radius  # p dot p - r*r
    discriminant = b*b - a*c        # (p dot d)^2 - (d dot d)(p dot p - r*r)
    if discriminant < 0:
        # pdb.set_trace()
        return False, None, None
    else:
        # pdb.set_trace()
        t = ((-b - np.sqrt(discriminant)) / a)
        point = ray_origin + t * ray_direction
        return True, t, point

