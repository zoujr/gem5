from m5.params import *
# from MemObject import MemObject
from m5.SimObject import SimObject

class SimpleMemobj(SimObject):
    type = 'SimpleMemobj'
    cxx_header = "learning_gem5/simple_memobj.hh"

    inst_port = SlavePort("CPU side port, receives requests")
    data_port = SlavePort("CPU side port, receives requests")
    mem_side = MasterPort("Memory side port, sends requests")
