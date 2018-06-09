#! /usr/bin/env python

# from ROOT import RooFit as rf
# from ROOT import *
import ROOT as r
import sys
import os
# import glob
import math
# import datetime
import numpy as np
# from array import array
# import re
# import matplotlib as ml
# import matplotlib.pyplot as plt
# from PIL import Image
import random

# R.gSystem.Load('libRooFit')


def main():
    c1 = r.TCanvas('c1', 'c1', 700, 700)
    c1.SetGrid()
    nx, ny = 400, 400
    h1 = r.TH2D('h1', 'h1', nx, -50, 50, ny, -50, 50)
    h2 = r.TH2D('h2', 'h2', 100, -3.15, 3.15, 100, 0, .1)
    init = [[60., 60., 0.], [70., 0., 70.]]
    for ini in init:
        R = ini[0]
        x0, y0 = ini[1], ini[2]
        R2 = R**2
        dl = .2
        nphi = int(2*math.pi*R / dl)
        dphi = 2*math.pi/nphi
        for i in xrange(nphi):
            x = x0 + R * math.cos(i*dphi) + random.gauss(0., .5)
            y = y0 + R * math.sin(i*dphi) + random.gauss(0., .5)
            ibin = h1.FindBin(x, y)
            bc = h1.GetBinContent(ibin)
            h1.SetBinContent(ibin, bc+1.)
        xbc, ybc = [], []
        for i in xrange(1, nx+1):
            for j in xrange(1, ny+1):
                if h1.GetBinContent(i, j) > 0.:
                    '''
                    xbc.append( h1.GetXaxis().GetBinCenter(i) )
                    ybc.append( h1.GetYaxis().GetBinCenter(j) )
                    '''
                    xbc = h1.GetXaxis().GetBinCenter(i)
                    ybc = h1.GetYaxis().GetBinCenter(j)
                    phi = math.atan2(ybc, xbc)
                    rho = (xbc**2+ybc**2)**.5
                    h2.Fill(phi, 1/rho)
    '''
    nbc = len(xbc)
    for
    for i in xrange(nbc):
        xbc[i]
    '''
    h1.Draw('colz')
    c1.Update()
    c2 = r.TCanvas('c2', 'c2', 700, 700)
    c2.SetGrid()
    h2.Draw('colz')
    c2.Update()
    raw_input()


if __name__ == '__main__':
    main()
