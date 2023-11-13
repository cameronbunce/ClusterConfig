from vcgencmd import Vcgencmd
from mpi4py import MPI
import socket

comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
vcgm = Vcgencmd()

hostname = socket.gethostname()
my_temp = vcgm.measure_temp()
output = f"{hostname} temperature is {my_temp}"
print(output)
output = f"{hostname} clock is {vcgm.measure_clock('arm')}"
print(output)
output = f"{hostname} throttled info is {vcgm.get_throttled()}"
print(output)
