import numpy as np
import pyproj

from pyproj import CRS, Transformer, transform
from math import sin, cos, atan2, pi, sqrt

gps_coords_epsg="epsg:4326"
ecef_coords_epsg="epsg:4978"

def conv_enu(llh,ecef_ref,ecef_target):
    """Converts a vector (equalling ecef_target-ecef_ref) in ECEF coordinates into ENU coordinates. Can be used to convert ECEF coordinates into ENU coordinates

    :param llh: (lat,lon,height) reference point coordinates in LLH
    :type llh: ndarray
    :param ecef_ref: (x,y,z) reference point coordinates in ECEF
    :type ecef_ref: ndarray
    :param ecef_target: (x,y,z) target location coordinates in ECEF
    :type ecef_target: ndarray
    :return: (x,y,z) vector from reference to target location in ENU coordinates
    :rtype: ndarray
    """
    mat = generate_enu_matrix(llh)
    enu = mat.dot(np.array(ecef_target)-np.array(ecef_ref))
    return enu

def conv_llh_enu(llh):
    ecef = llh_to_ecef(llh)
    mat = generate_enu_matrix(llh)
    enu = mat.dot(np.array(ecef))
    return enu

def conv_ecef_enu(ecef):
    llh = ecef_to_llh(ecef)
    mat = generate_enu_matrix(llh)
    enu = mat.dot(np.array(ecef))
    return enu

def llh_to_ecef(llh_coords):
    """Convert ECEF coordinates to LLH

    :param ecef: (lat,lon,height) reference point coordinates in LLH
    :type ecef: ndarray
    :return: (x,y,z) reference point coordinates in ECEF
    :rtype: ndarray
    """
    trans = Transformer.from_crs(gps_coords_epsg,ecef_coords_epsg)
    return np.array(trans.transform(*llh_coords))

def ecef_to_llh(ecef_coords):
    """Convert ECEF coordinates to LLH

    :param ecef: (x,y,z) reference point coordinates in ECEF
    :type ecef: ndarray
    :return: (lat,lon,height) reference point coordinates in LLH
    :rtype: ndarray
    """
    trans = Transformer.from_crs(ecef_coords_epsg,gps_coords_epsg)
    return np.array(trans.transform(*ecef_coords))

def enu_cart_to_enu_sphere(enu):
    """Convert ENU cartesian coordinates to ENU spherical.

    :param ecef: (x,y,z) reference point coordinates in ENU cartesian
    :type ecef: ndarray
    :return: (theta,phi,rho) reference point coordinates in ENU spherical
    :rtype: ndarray
    """
    (x, y, z) = enu
    rho = np.sqrt(x*x+y*y+z*z)
    theta = np.arctan2(y,x)
    phi = np.arccos(z/rho)
    return (theta,phi,rho)

def generate_enu_matrix(llh):
    """Generates coordinate transform matrix (from LLH to ENU)

    :param llh: (lat,lon,height) reference point coordinates in LLH
    :type llh: ndarray
    :return: A rotation (coordinate transform) matrix in ENU coordinates
    :rtype: ndarray
    """
    (theta, phi, h) = llh
    return np.array([
        [-sin(theta),cos(theta),0],
        [-sin(phi)*cos(theta),-sin(phi)*sin(theta),cos(phi)],
        [cos(phi)*cos(theta),cos(phi)*sin(theta),sin(phi)]
    ])

if(__name__=="__main__"):
    llh = np.array([0,0,0])
    ecef = llh_to_ecef(llh)
    ecef2 = llh_to_ecef(llh+np.array([0,1,0]))
    print("ECEF coordinates: ")
    print(ecef)
    print(ecef2)
    test_enu = conv_enu(llh,ecef,ecef2)
    print(test_enu)
    print(enu_cart_to_enu_sphere(test_enu))
    # coords = llh_to_ecef(llh)
    # print(coords)
    # print(ecef_to_llh(ecef))
    # print(atan2(coords[1],coords[0])*180/pi)
    # print(generate_enu_matrix(llh))
    # print(conv_enu(np.array([90,0,0]),llh_to_ecef(np.array([90,0,0]))))
    # print(conv_llh_enu(llh))
    # print(conv_ecef_enu(ecef))
    # print(conv_enu(llh,ecef,ecef2))
    # conv_enu(llh,ecef,ecef2)
    # print(llh_to_ecef(np.array([90,0,0])))
