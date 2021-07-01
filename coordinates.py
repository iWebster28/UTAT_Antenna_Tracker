import numpy as np
import pyproj

from pyproj import CRS, Transformer, transform
from math import sin, cos, atan2, pi

def conv_enu(llh,ecef):
    mat = generate_enu_matrix(llh)
    enu = mat.dot(np.array(ecef))
    return enu

def llh_to_ecef(llh_coords):
    trans = Transformer.from_crs("epsg:4326","epsg:4978")
    print(*llh_coords)
    return np.array(trans.transform(*llh_coords))

def ecef_to_llh(ecef_coords):
    trans = Transformer.from_crs("epsg:4978","epsg:4326")
    return np.array(trans.transform(*ecef_coords))

def generate_enu_matrix(llh):
    (theta, phi, h) = llh
    return np.array([
        [-sin(theta),cos(theta),0],
        [-sin(phi)*cos(theta),-sin(phi)*sin(theta),cos(phi)],
        [cos(phi)*cos(theta),cos(phi)*sin(theta),sin(phi)]
    ])

if(__name__=="__main__"):
    llh = np.array([43.6690207,-79.3916043,0])
    ecef = np.array([850.695*1000,-4541.966*1000,4381.564*1000])
    coords = llh_to_ecef(llh)
    print(coords)
    print(ecef_to_llh(ecef))
    print(atan2(coords[1],coords[0])*180/pi)
    print(generate_enu_matrix(llh))
    print(conv_enu(np.array([90,0,0]),llh_to_ecef(np.array([90,0,0]))))
    print(llh_to_ecef(np.array([90,0,0])))
