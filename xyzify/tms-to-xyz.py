# -*- coding: utf-8 -*-
# -+-+-+-+-+-+-+-+-+-+-+-+
''' ---------------------------------------
https://github.com/barbosaale/tms-to-xyz
barbosa.ale@gmail.com
--------------------------------------- '''
import sys
import os


def Main():
    pasta = sys.argv[1] + '/'
    ConvertTms(pasta)


def ConvertTms(pasta):
    cwd = os.getcwd() + '/'
    contentz = os.listdir(cwd + pasta)
    print (contentz)
    for z in contentz:

    
        if os.path.isdir(pasta + z):
            # print 'Z: ' + z
            nz = float(z)

            contentx = os.listdir(cwd + pasta + z + '/')
            print(contentx)
            for x in contentx:
                
                if os.path.isdir(cwd + pasta + z + "/" + x):
                    # print 'X: ' + x
                    
                    pngs = os.listdir(cwd + pasta + z + '/' + x )
                    
                    for png in pngs:
                        ny = float(png.split('.')[0])
                        
                        ny_new = int( (2 ** nz) - ny - 1 )
                        print(ny_new)
                        
                        os.rename(cwd + pasta + z + '/' + x + '/' + png, cwd + pasta + z + '/' + x + '/' + str(ny_new) + ".png" )
                        

        
    print('Tiles successfully converted ...!')
    
    
    
if __name__ == "__main__":
    Main()