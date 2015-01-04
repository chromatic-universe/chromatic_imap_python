'''
Created on Dec 31, 2012

@author: wiljoh
'''
import sys 
import traceback 
import Ice
import chromatic
from ice_python_utils import ostream , endl


status = 0
ic = None
try:
    ic = Ice.initialize( sys.argv )
    
    cout = ostream()
    cout << "ice_python_client...Internet Communication Engine....2012" << endl

    base = ic.stringToProxy( "SimplePrinter:default -p 10000" )
    printer = chromatic.printerPrx.checkedCast( base )
    if not printer:
        raise RuntimeError( "Invalid proxy" )

    printer.printString( "The Original Corny Snaps!" )
    
except:
    traceback.print_exc()
    status = 1
    
if ic:
    #clean up
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)

