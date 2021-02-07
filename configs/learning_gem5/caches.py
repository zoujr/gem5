from m5.objects import Cache

class L1Cache(Cache):
    assoc = 2 # 2路组相联？
    tag_latency = 2 # Tag查找延迟
    data_latency = 2 # 数据访问延迟
    response_latency = 2 # miss时返回路径延迟
    mshrs = 4
    tgts_per_mshr = 20 # 每个MSHR最大访问次数

    def connectCPU(self, cpu):
        # need to define this in a base class!
        raise NotImplementedError

    def connectBUS(self, bus):
        self.mem_side = bus.cpu_side_ports

    def __init__ (self, options=None):
        super(L1Cache, self).__init__()
        pass

class L1ICache(L1Cache):
        size = '16kB'

    def connectCPU(self, cpu):
        self.cpu_side = cpu.icache_port


    def __init__ (self, options=None):
        super(L1ICache, self).__init__(options)
        if not options or not options.l1i_size:
            return
        self.size = options.l1i_size

class L1DCache(L1Cache):
    size = '64kB'

    def connectCPU(self, cpu):
        self.cpu_side = cpu.dcache_port

    def __init__ (self, options=None):
        super(L1DCache, self).__init__(options)
        if not options or not options.l1d_size:
            return
        self.size = options.l1d_size

class L2Cache(Cache):
    size = '256kB'
    assoc = 8
    tag_latency = 20
    data_latency = 20
    response_latency = 20
    mshrs = 20
    tgts_per_mshr = 12

    def connectCPUSideBUS(self, bus):
        self.cpu_side = bus.mem_side_ports

    def connectMemSideBUS(self, bus):
        self.mem_side = bus.cpu_side_ports

    def __init__ (self, options=None):
        super(L2Cache, self).__init__()
        if not options or not options.l2_size:
            return
        self.size = options.l2_size
