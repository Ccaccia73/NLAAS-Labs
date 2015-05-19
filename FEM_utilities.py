# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:01:28 2015

@author: claudio
"""

import numpy as np

def Nodes(nx, ny, l, w):
    """
    function to compute nodes and elements coordinates for an horizontal
    cantilever beam fixed at x=0 and loaded with distributed load at x=l
    
    input 
    nx : number of elements in x direction
    ny : number of elements in y direction
    l :  length of plate
    w :  width of plate
    
    output
    - matrix of nodes coordinates
    - matrix of elements (which nodes belongs to each element)
    - matrix of constrained elements
    - matrix of loaded elements
    """
    nodes = np.zeros(( (nx+1)*(ny+1),4 ))
    
    nodes[:,0] = np.arange(1,(nx+1)*(ny+1)+1) 
    nodes[:,1] = np.tile(np.linspace(0,l,nx+1),ny+1)
    nodes[:,2] = np.tile(np.linspace(0,w,ny+1),(nx+1,1)).reshape((nx+1)*(ny+1), order='F') 
    
    # z coordinate is 0    
    
    elements = np.zeros((nx*ny,5))
    
    elements[:,0] = np.arange(1,nx*ny+1)
    elements[:,1] =  np.reshape(np.tile(np.arange(1,nx+1),(ny,1)).T + \
                                np.tile(np.arange(0,nx*ny+(ny-nx)+1,nx+1),(nx,1)), \
                                        (nx*ny),order='F')
    elements[:,2] = elements[:,1] + 1
    elements[:,3] = elements[:,1] + nx + 2
    elements[:,4] = elements[:,1] + nx + 1
    
    constr_nodes = np.arange(1, (nx+1)*(ny+1), nx+1 )
    
    loaded_nodes = np.arange(nx+1, (nx+1)*(ny+1)+1, nx+1)
    
    return nodes, elements, constr_nodes, loaded_nodes
    
    
def NodesLab07(nx, ny, l, w):
    nodes, elements, set_y0, set_yL = Nodes(nx, ny, l, w)
    
    set_x0 = np.arange(1,(nx+1)+1)
    set_xW = np.arange((nx+1)*ny+1, (nx+1)*(ny+1)+1)
    
    return nodes, elements, set_y0, set_yL, set_x0, set_xW
    