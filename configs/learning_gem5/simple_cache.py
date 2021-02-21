import m5
from m5.objects import *

system = System()
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

system.cpu = TimingSimpleCPU()

system.membus = SystemXBar()

system.cache = SimpleCache(size='1kB')


system.cpu.icache_port = system.cache.cpu_side
system.cpu.dcache_port = system.cache.cpu_side

system.cache.mem_side = system.membus.slave

system.cpu.createInterruptController()

if m5.defines.buildEnv['TARGET_ISA'] == 'x86':
    system.cpu.interrupts[0].pio = system.membus.master
    system.cpu.interrupts[0].int_master = system.membus.slave
    system.cpu.interrupts[0].int_slave = system.membus.master

system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.master

system.system_port = system.membus.slave

process = Process()
if m5.defines.buildEnv['TARGET_ISA'] == 'x86':
    process.cmd = ['tests/test-progs/hello/bin/x86/linux/hello']
else:
    process.cmd = ['tests/test-progs/hello/bin/riscv/linux/hello']
system.cpu.workload = process
system.cpu.createThreads()

root = Root(full_system = False, system = system)
m5.instantiate()

print("Begining simulation!")
exit_event = m5.simulate()
print('Exiting @ tick %i because %s' % (m5.curTick(), exit_event.getCause()))

