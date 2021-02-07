import m5
from m5.objects import *

system = System() # 实例化一个系统

system.clk_domain = SrcClockDomain() # 为系统创建一个时钟域
system.clk_domain.clock = '1GHz' # 设置时钟频率
system.clk_domain.voltage_domain = VoltageDomain() # 设置时钟电压，这里是设置为默认

# 实例化一个512MB大小的内存
system.mem_mode = 'timing' # timing模式是最常用的模式
system.mem_ranges = [AddrRange('512MB')]

# 实例化一个CPU
system.cpu = TimingSimpleCPU()

# 实例化一个内存总线
system.membus = SystemXBar()

# 由于再这个example中没有cache，所以我们直接将CPU的cache端口连接到内存总线上
system.cpu.icache_port = system.membus.slave
system.cpu.dcache_port = system.membus.slave

# 需要系统正常运行，还需要连接几个端口
# 在CPU上创建一个I/O控制器，并将其连接到内存总线
# 需要将系统中的特殊端口连接到内存总线，此端口是functional-only端口，用于允许系统读取和写入内存
# 如果你是X86架构还需要额外连接PIO和中断端口

system.cpu.createInterruptController()

if m5.defines.buildEnv['TARGET_ISA'] == 'x86':
    system.cpu.interrupts[0].pio = system.membus.master
    system.cpu.interrupts[0].int_master = system.membus.slave
    system.cpu.interrupts[0].int_slave = system.membus.master

system.system_port = system.membus.slave

# 创建一个内存控制器，这里创建一个简单的DDR3控制器
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master

# 指定一个可执行文件
process = Process()
process.cmd = ['tests/test-progs/hello/bin/riscv/linux/hello']
system.cpu.workload = process
system.cpu.createThreads()

# 实例化Root对象
root = Root(full_system = False, system = system)
m5.instantiate()

# 开始仿真
print("Beginning simulation!")
exit_event = m5.simulate()

# 在仿真结束后，检查系统状态
print('Exiting @ tick {} because {}'
    .format(m5.curTick(), exit_event.getCause()))

