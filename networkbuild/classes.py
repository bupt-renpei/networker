# -*- coding: utf-8 -*-

import osr
import networkx as nx

"""
Module for GeoGraph extension to networkx Graph class
"""

class GeoObject(object):

    """ Base class for Geo objects 
    
    Attributes:
        srs:  spatial reference system for the coords
            In proj4 string format (http://trac.osgeo.org/proj/)
        coords:  The coordinates of this object 
            This may be a vector or a vector of vectors depending
            on the object type
    
    """

    def __init__(self, srs, coords):
        self.srs = srs
        self.coords = coords

    def is_geographic(self):
        """ Returns whether the coords are geocentric, based on proj4 """
        
        sr = osr.SpatialReference()
        sr.ImportFromProj4(self.srs)
        return bool(sr.IsGeographic())


class GeoGraph(GeoObject, nx.Graph):

    """ class representing networkx Graph with Geo components 
    
    Attributes:
        inherited from GeoObject and nx.Graph
        coords:  coords array associated with node ids by ix
    
    See Also
    --------

    GeoObject
    networkx.Graph
    
    """

    def __init__(self, srs, coords, data=None, **attr):
        """ initialize via both parent classes """

        GeoObject.__init__(self, srs, coords)
        nx.Graph.__init__(self, data, **attr)

    def is_valid(self):
        """
        Test whether this GeoGraph is valid

        Useful in case you have a GeoGraph that has its coords/nodes modified
        """

        assert sorted(self.nodes()) == \
            [i for i, coord in enumerate(self.coords)], \
            "GeoGraph nodes and coords not aligned"

        return True
