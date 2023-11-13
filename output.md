mpirun --hostfile hostfile ./testing/xhpl
================================================================================
HPLinpack 2.3  --  High-Performance Linpack benchmark  --   December 2, 2018
Written by A. Petitet and R. Clint Whaley,  Innovative Computing Laboratory, UTK
Modified by Piotr Luszczek, Innovative Computing Laboratory, UTK
Modified by Julien Langou, University of Colorado Denver
================================================================================

An explanation of the input/output parameters follows:
T/V    : Wall time / encoded variant.
N      : The order of the coefficient matrix A.
NB     : The partitioning blocking factor.
P      : The number of process rows.
Q      : The number of process columns.
Time   : Time in seconds to solve the linear system.
Gflops : Rate of execution for solving the linear system.

The following parameter values will be used:

N      :   48768 
NB     :      96      112      128      184      200 
PMAP   : Row-major process mapping
P      :       3 
Q      :       4 
PFACT  :   Right 
NBMIN  :       4 
NDIV   :       2 
RFACT  :   Crout 
BCAST  :  1ringM 
DEPTH  :       1 
SWAP   : Mix (threshold = 64)
L1     : transposed form
U      : transposed form
EQUIL  : yes
ALIGN  : 8 double precision words

--------------------------------------------------------------------------------

- The matrix A is randomly generated for each test.
- The following scaled residual check will be computed:
      ||Ax-b||_oo / ( eps * ( || x ||_oo * || A ||_oo + || b ||_oo ) * N )
- The relative machine precision (eps) is taken to be               1.110223e-16
- Computational tests pass if scaled residuals are less than                16.0

================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768    96     3     4            2902.62             2.6641e+01
HPL_pdgesv() start time Thu Nov  9 09:29:43 2023

HPL_pdgesv() end time   Thu Nov  9 10:18:05 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.49390825e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   112     3     4            2906.87             2.6602e+01
HPL_pdgesv() start time Thu Nov  9 10:20:40 2023

HPL_pdgesv() end time   Thu Nov  9 11:09:07 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.11958763e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   128     3     4            2910.01             2.6573e+01
HPL_pdgesv() start time Thu Nov  9 11:11:43 2023

HPL_pdgesv() end time   Thu Nov  9 12:00:13 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.04458497e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   184     3     4            2883.63             2.6816e+01
HPL_pdgesv() start time Thu Nov  9 12:02:50 2023

HPL_pdgesv() end time   Thu Nov  9 12:50:53 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.02852534e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   200     3     4            2901.08             2.6655e+01
HPL_pdgesv() start time Thu Nov  9 12:53:28 2023

HPL_pdgesv() end time   Thu Nov  9 13:41:49 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.05286087e-03 ...... PASSED
================================================================================

Finished      5 tests with the following results:
              5 tests completed and passed residual checks,
              0 tests completed and failed residual checks,
              0 tests skipped because of illegal input values.
--------------------------------------------------------------------------------

End of Tests.
================================================================================
cameron@rp3n0:/clusterfs/common/hpl-2.3$ nano HPL.dat 
cameron@rp3n0:/clusterfs/common/hpl-2.3$ mpirun --hostfile hostfile ./testing/xhpl
================================================================================
HPLinpack 2.3  --  High-Performance Linpack benchmark  --   December 2, 2018
Written by A. Petitet and R. Clint Whaley,  Innovative Computing Laboratory, UTK
Modified by Piotr Luszczek, Innovative Computing Laboratory, UTK
Modified by Julien Langou, University of Colorado Denver
================================================================================

An explanation of the input/output parameters follows:
T/V    : Wall time / encoded variant.
N      : The order of the coefficient matrix A.
NB     : The partitioning blocking factor.
P      : The number of process rows.
Q      : The number of process columns.
Time   : Time in seconds to solve the linear system.
Gflops : Rate of execution for solving the linear system.

The following parameter values will be used:

N      :   48768 
NB     :     184 
PMAP   : Row-major process mapping
P      :       3 
Q      :       4 
PFACT  :   Right 
NBMIN  :       4 
NDIV   :       2 
RFACT  :   Crout 
BCAST  :   1ring 
DEPTH  :       1 
SWAP   : Mix (threshold = 64)
L1     : transposed form
U      : transposed form
EQUIL  : yes
ALIGN  : 8 double precision words

--------------------------------------------------------------------------------

- The matrix A is randomly generated for each test.
- The following scaled residual check will be computed:
      ||Ax-b||_oo / ( eps * ( || x ||_oo * || A ||_oo + || b ||_oo ) * N )
- The relative machine precision (eps) is taken to be               1.110223e-16
- Computational tests pass if scaled residuals are less than                16.0

================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768   184     3     4            2745.54             2.8165e+01
HPL_pdgesv() start time Thu Nov  9 14:20:15 2023

HPL_pdgesv() end time   Thu Nov  9 15:06:01 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.02852534e-03 ...... PASSED
================================================================================

Finished      1 tests with the following results:
              1 tests completed and passed residual checks,
              0 tests completed and failed residual checks,
              0 tests skipped because of illegal input values.
--------------------------------------------------------------------------------

End of Tests.
================================================================================
cameron@rp3n0:/clusterfs/common/hpl-2.3$ python3
Python 3.11.4 (main, Jun  9 2023, 07:59:55) [GCC 12.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 24*.7
16.799999999999997
>>> sqrt((24*.7)/8)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined
>>> import numpy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
>>> exit()
cameron@rp3n0:/clusterfs/common/hpl-2.3$ nano HPL.dat 
cameron@rp3n0:/clusterfs/common/hpl-2.3$ mpirun --hostfile hostfile ./testing/xhpl
================================================================================
HPLinpack 2.3  --  High-Performance Linpack benchmark  --   December 2, 2018
Written by A. Petitet and R. Clint Whaley,  Innovative Computing Laboratory, UTK
Modified by Piotr Luszczek, Innovative Computing Laboratory, UTK
Modified by Julien Langou, University of Colorado Denver
================================================================================

An explanation of the input/output parameters follows:
T/V    : Wall time / encoded variant.
N      : The order of the coefficient matrix A.
NB     : The partitioning blocking factor.
P      : The number of process rows.
Q      : The number of process columns.
Time   : Time in seconds to solve the linear system.
Gflops : Rate of execution for solving the linear system.

The following parameter values will be used:

N      :   47485 
NB     :     184 
PMAP   : Row-major process mapping
P      :       3 
Q      :       4 
PFACT  :   Right 
NBMIN  :       4 
NDIV   :       2 
RFACT  :   Crout 
BCAST  :   1ring 
DEPTH  :       1 
SWAP   : Mix (threshold = 64)
L1     : transposed form
U      : transposed form
EQUIL  : yes
ALIGN  : 8 double precision words

--------------------------------------------------------------------------------

- The matrix A is randomly generated for each test.
- The following scaled residual check will be computed:
      ||Ax-b||_oo / ( eps * ( || x ||_oo * || A ||_oo + || b ||_oo ) * N )
- The relative machine precision (eps) is taken to be               1.110223e-16
- Computational tests pass if scaled residuals are less than                16.0

================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       47485   184     3     4            2617.76             2.7269e+01
HPL_pdgesv() start time Thu Nov  9 15:13:07 2023

HPL_pdgesv() end time   Thu Nov  9 15:56:45 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.23278291e-03 ...... PASSED
================================================================================

Finished      1 tests with the following results:
              1 tests completed and passed residual checks,
              0 tests completed and failed residual checks,
              0 tests skipped because of illegal input values.
--------------------------------------------------------------------------------

End of Tests.
================================================================================
cameron@rp3n0:/clusterfs/common/hpl-2.3$ nano HPL.dat 
cameron@rp3n0:/clusterfs/common/hpl-2.3$ mpirun --hostfile hostfile ./testing/xhpl
================================================================================
HPLinpack 2.3  --  High-Performance Linpack benchmark  --   December 2, 2018
Written by A. Petitet and R. Clint Whaley,  Innovative Computing Laboratory, UTK
Modified by Piotr Luszczek, Innovative Computing Laboratory, UTK
Modified by Julien Langou, University of Colorado Denver
================================================================================

An explanation of the input/output parameters follows:
T/V    : Wall time / encoded variant.
N      : The order of the coefficient matrix A.
NB     : The partitioning blocking factor.
P      : The number of process rows.
Q      : The number of process columns.
Time   : Time in seconds to solve the linear system.
Gflops : Rate of execution for solving the linear system.

The following parameter values will be used:

N      :   48768 
NB     :     184 
PMAP   : Row-major process mapping
P      :       3 
Q      :       4 
PFACT  :   Right 
NBMIN  :       4 
NDIV   :       2 
RFACT  :   Crout 
BCAST  :   2ring 
DEPTH  :       1 
SWAP   : Mix (threshold = 64)
L1     : transposed form
U      : transposed form
EQUIL  : yes
ALIGN  : 8 double precision words

--------------------------------------------------------------------------------

- The matrix A is randomly generated for each test.
- The following scaled residual check will be computed:
      ||Ax-b||_oo / ( eps * ( || x ||_oo * || A ||_oo + || b ||_oo ) * N )
- The relative machine precision (eps) is taken to be               1.110223e-16
- Computational tests pass if scaled residuals are less than                16.0

 ================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR12C2R4       48768   184     3     4            2897.22             2.6690e+01
HPL_pdgesv() start time Thu Nov  9 16:00:45 2023

HPL_pdgesv() end time   Thu Nov  9 16:49:02 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.02852534e-03 ...... PASSED
================================================================================

Finished      1 tests with the following results:
              1 tests completed and passed residual checks,
              0 tests completed and failed residual checks,
              0 tests skipped because of illegal input values.
--------------------------------------------------------------------------------

End of Tests.
===============================================================================






cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-138.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
================================================================================
HPLinpack 2.3  --  High-Performance Linpack benchmark  --   December 2, 2018
Written by A. Petitet and R. Clint Whaley,  Innovative Computing Laboratory, UTK
Modified by Piotr Luszczek, Innovative Computing Laboratory, UTK
Modified by Julien Langou, University of Colorado Denver
================================================================================

An explanation of the input/output parameters follows:
T/V    : Wall time / encoded variant.
N      : The order of the coefficient matrix A.
NB     : The partitioning blocking factor.
P      : The number of process rows.
Q      : The number of process columns.
Time   : Time in seconds to solve the linear system.
Gflops : Rate of execution for solving the linear system.

The following parameter values will be used:

N      :   48768 
NB     :      96      184      224      232      248 
PMAP   : Row-major process mapping
P      :       3 
Q      :       4 
PFACT  :   Right 
NBMIN  :       4 
NDIV   :       2 
RFACT  :   Crout 
BCAST  :   1ring 
DEPTH  :       1 
SWAP   : Mix (threshold = 64)
L1     : transposed form
U      : transposed form
EQUIL  : yes
ALIGN  : 8 double precision words

--------------------------------------------------------------------------------

- The matrix A is randomly generated for each test.
- The following scaled residual check will be computed:
      ||Ax-b||_oo / ( eps * ( || x ||_oo * || A ||_oo + || b ||_oo ) * N )
- The relative machine precision (eps) is taken to be               1.110223e-16
- Computational tests pass if scaled residuals are less than                16.0

================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768    96     3     4            2456.48             3.1479e+01
HPL_pdgesv() start time Sat Nov 11 13:13:38 2023

HPL_pdgesv() end time   Sat Nov 11 13:54:34 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   2.97247158e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768   184     3     4            2360.44             3.2760e+01
HPL_pdgesv() start time Sat Nov 11 13:57:01 2023

HPL_pdgesv() end time   Sat Nov 11 14:36:22 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.02852534e-03 ...... PASSED
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-138.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
================================================================================
HPLinpack 2.3  --  High-Performance Linpack benchmark  --   December 2, 2018
Written by A. Petitet and R. Clint Whaley,  Innovative Computing Laboratory, UTK
Modified by Piotr Luszczek, Innovative Computing Laboratory, UTK
Modified by Julien Langou, University of Colorado Denver
================================================================================

An explanation of the input/output parameters follows:
T/V    : Wall time / encoded variant.
N      : The order of the coefficient matrix A.
NB     : The partitioning blocking factor.
P      : The number of process rows.
Q      : The number of process columns.
Time   : Time in seconds to solve the linear system.
Gflops : Rate of execution for solving the linear system.

The following parameter values will be used:

N      :   48768 
NB     :      96      184      224      232      248 
PMAP   : Row-major process mapping
P      :       3 
Q      :       4 
PFACT  :   Right 
NBMIN  :       4 
NDIV   :       2 
RFACT  :   Crout 
BCAST  :   1ring 
DEPTH  :       1 
SWAP   : Mix (threshold = 64)
L1     : transposed form
U      : transposed form
EQUIL  : yes
ALIGN  : 8 double precision words

--------------------------------------------------------------------------------

- The matrix A is randomly generated for each test.
- The following scaled residual check will be computed:
      ||Ax-b||_oo / ( eps * ( || x ||_oo * || A ||_oo + || b ||_oo ) * N )
- The relative machine precision (eps) is taken to be               1.110223e-16
- Computational tests pass if scaled residuals are less than                16.0

================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768    96     3     4            2456.48             3.1479e+01
HPL_pdgesv() start time Sat Nov 11 13:13:38 2023

HPL_pdgesv() end time   Sat Nov 11 13:54:34 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   2.97247158e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768   184     3     4            2360.44             3.2760e+01
HPL_pdgesv() start time Sat Nov 11 13:57:01 2023

HPL_pdgesv() end time   Sat Nov 11 14:36:22 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.02852534e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768   224     3     4            2568.30             3.0108e+01
HPL_pdgesv() start time Sat Nov 11 14:38:49 2023

HPL_pdgesv() end time   Sat Nov 11 15:21:37 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.18208529e-03 ...... PASSED
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-138.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
================================================================================
HPLinpack 2.3  --  High-Performance Linpack benchmark  --   December 2, 2018
Written by A. Petitet and R. Clint Whaley,  Innovative Computing Laboratory, UTK
Modified by Piotr Luszczek, Innovative Computing Laboratory, UTK
Modified by Julien Langou, University of Colorado Denver
================================================================================

An explanation of the input/output parameters follows:
T/V    : Wall time / encoded variant.
N      : The order of the coefficient matrix A.
NB     : The partitioning blocking factor.
P      : The number of process rows.
Q      : The number of process columns.
Time   : Time in seconds to solve the linear system.
Gflops : Rate of execution for solving the linear system.

The following parameter values will be used:

N      :   48768 
NB     :      96      184      224      232      248 
PMAP   : Row-major process mapping
P      :       3 
Q      :       4 
PFACT  :   Right 
NBMIN  :       4 
NDIV   :       2 
RFACT  :   Crout 
BCAST  :   1ring 
DEPTH  :       1 
SWAP   : Mix (threshold = 64)
L1     : transposed form
U      : transposed form
EQUIL  : yes
ALIGN  : 8 double precision words

--------------------------------------------------------------------------------

- The matrix A is randomly generated for each test.
- The following scaled residual check will be computed:
      ||Ax-b||_oo / ( eps * ( || x ||_oo * || A ||_oo + || b ||_oo ) * N )
- The relative machine precision (eps) is taken to be               1.110223e-16
- Computational tests pass if scaled residuals are less than                16.0

================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768    96     3     4            2456.48             3.1479e+01
HPL_pdgesv() start time Sat Nov 11 13:13:38 2023

HPL_pdgesv() end time   Sat Nov 11 13:54:34 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   2.97247158e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768   184     3     4            2360.44             3.2760e+01
HPL_pdgesv() start time Sat Nov 11 13:57:01 2023

HPL_pdgesv() end time   Sat Nov 11 14:36:22 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.02852534e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768   224     3     4            2568.30             3.0108e+01
HPL_pdgesv() start time Sat Nov 11 14:38:49 2023

HPL_pdgesv() end time   Sat Nov 11 15:21:37 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.18208529e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768   232     3     4            2612.18             2.9603e+01
HPL_pdgesv() start time Sat Nov 11 15:24:03 2023

HPL_pdgesv() end time   Sat Nov 11 16:07:36 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.68941738e-03 ...... PASSED
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-138.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
================================================================================
HPLinpack 2.3  --  High-Performance Linpack benchmark  --   December 2, 2018
Written by A. Petitet and R. Clint Whaley,  Innovative Computing Laboratory, UTK
Modified by Piotr Luszczek, Innovative Computing Laboratory, UTK
Modified by Julien Langou, University of Colorado Denver
================================================================================

An explanation of the input/output parameters follows:
T/V    : Wall time / encoded variant.
N      : The order of the coefficient matrix A.
NB     : The partitioning blocking factor.
P      : The number of process rows.
Q      : The number of process columns.
Time   : Time in seconds to solve the linear system.
Gflops : Rate of execution for solving the linear system.

The following parameter values will be used:

N      :   48768 
NB     :      96      184      224      232      248 
PMAP   : Row-major process mapping
P      :       3 
Q      :       4 
PFACT  :   Right 
NBMIN  :       4 
NDIV   :       2 
RFACT  :   Crout 
BCAST  :   1ring 
DEPTH  :       1 
SWAP   : Mix (threshold = 64)
L1     : transposed form
U      : transposed form
EQUIL  : yes
ALIGN  : 8 double precision words

--------------------------------------------------------------------------------

- The matrix A is randomly generated for each test.
- The following scaled residual check will be computed:
      ||Ax-b||_oo / ( eps * ( || x ||_oo * || A ||_oo + || b ||_oo ) * N )
- The relative machine precision (eps) is taken to be               1.110223e-16
- Computational tests pass if scaled residuals are less than                16.0

================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768    96     3     4            2456.48             3.1479e+01
HPL_pdgesv() start time Sat Nov 11 13:13:38 2023

HPL_pdgesv() end time   Sat Nov 11 13:54:34 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   2.97247158e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768   184     3     4            2360.44             3.2760e+01
HPL_pdgesv() start time Sat Nov 11 13:57:01 2023

HPL_pdgesv() end time   Sat Nov 11 14:36:22 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.02852534e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768   224     3     4            2568.30             3.0108e+01
HPL_pdgesv() start time Sat Nov 11 14:38:49 2023

HPL_pdgesv() end time   Sat Nov 11 15:21:37 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.18208529e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768   232     3     4            2612.18             2.9603e+01
HPL_pdgesv() start time Sat Nov 11 15:24:03 2023

HPL_pdgesv() end time   Sat Nov 11 16:07:36 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.68941738e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       48768   248     3     4            2809.88             2.7520e+01
HPL_pdgesv() start time Sat Nov 11 16:10:02 2023

HPL_pdgesv() end time   Sat Nov 11 16:56:51 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.27270098e-03 ...... PASSED
================================================================================

Finished      5 tests with the following results:
              5 tests completed and passed residual checks,
              0 tests completed and failed residual checks,
              0 tests skipped because of illegal input values.
--------------------------------------------------------------------------------

End of Tests.
================================================================================
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ ls
HPL.dat   HPL4.dat    mpihpl2.sh     slurm-101.out  slurm-110.out  slurm-120.out  slurm-129.out  slurm-90.out  slurm-95.out
HPL0.dat  HPL5.dat    mpihpl3.sh     slurm-102.out  slurm-111.out  slurm-121.out  slurm-138.out  slurm-91.out  slurm-96.out
HPL1.dat  mpihpl.sh   mpihpl4.sh     slurm-107.out  slurm-117.out  slurm-122.out  slurm-86.out   slurm-92.out  slurm-97.out
HPL2.dat  mpihpl0.sh  mpihpl5.sh     slurm-108.out  slurm-118.out  slurm-123.out  slurm-87.out   slurm-93.out  slurm-98.out
HPL3.dat  mpihpl1.sh  slurm-100.out  slurm-109.out  slurm-119.out  slurm-128.out  slurm-88.out   slurm-94.out  slurm-99.out
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl0.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl0.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano HPL0.dat 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl0.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cp mpihpl0.sh mpitemp.sh
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpitemp.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ /clusterfs/usr/bin/pip3 install vcgencmd
^CTraceback (most recent call last):
  File "/clusterfs/usr/bin/pip3", line 5, in <module>
    from pip._internal.cli.main import main
  File "/clusterfs/usr/lib/python3.11/site-packages/pip/_internal/cli/main.py", line 10, in <module>
    from pip._internal.cli.autocompletion import autocomplete
  File "/clusterfs/usr/lib/python3.11/site-packages/pip/_internal/cli/autocompletion.py", line 10, in <module>
    from pip._internal.cli.main_parser import create_main_parser
  File "/clusterfs/usr/lib/python3.11/site-packages/pip/_internal/cli/main_parser.py", line 9, in <module>
    from pip._internal.build_env import get_runnable_pip
  File "/clusterfs/usr/lib/python3.11/site-packages/pip/_internal/build_env.py", line 19, in <module>
    from pip._internal.cli.spinners import open_spinner
  File "/clusterfs/usr/lib/python3.11/site-packages/pip/_internal/cli/spinners.py", line 9, in <module>
    from pip._internal.utils.logging import get_indentation
  File "/clusterfs/usr/lib/python3.11/site-packages/pip/_internal/utils/logging.py", line 4, in <module>
    import logging.handlers
  File "/clusterfs/usr/lib/python3.11/logging/handlers.py", line 26, in <module>
    import io, logging, socket, os, pickle, struct, time, re
KeyboardInterrupt

cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cd ../..
cameron@rp3n0:/clusterfs$ cd common/
cameron@rp3n0:/clusterfs/common$ ls
0.9.0.tar.gz  OpenBLAS-0.3.23                    arm-compiler-for-linux_23.04.1_Ubuntu-22.04  hpl-2.3  v0.3.23.tar.gz
MagPiPrime    Raspberry-Pi-OS-64-Bit-Benchmarks  blis-0.9.0                                   modules  vcgencmd-0.1.1
cameron@rp3n0:/clusterfs/common$ cd vcgencmd-0.1.1/
cameron@rp3n0:/clusterfs/common/vcgencmd-0.1.1$ ls
PKG-INFO  README.md  setup.cfg  setup.py  vcgencmd  vcgencmd.egg-info
cameron@rp3n0:/clusterfs/common/vcgencmd-0.1.1$ /clusterfs/usr/bin/pip3 install -e .
Defaulting to user installation because normal site-packages is not writeable
Obtaining file:///clusterfs/common/vcgencmd-0.1.1
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Building wheels for collected packages: vcgencmd
  Building editable for vcgencmd (pyproject.toml) ... done
  Created wheel for vcgencmd: filename=vcgencmd-0.1.1-0.editable-py3-none-any.whl size=5558 sha256=2868f77c11483642ccbde778e82cff9ef611942829bdc5eeb33bd069a81e4b10
  Stored in directory: /tmp/pip-ephem-wheel-cache-gupacdvt/wheels/f3/83/a5/9c08e072b5943c85e842a822b9efcb97dae7f86a9a67c51180
Successfully built vcgencmd
Installing collected packages: vcgencmd
Successfully installed vcgencmd-0.1.1

[notice] A new release of pip is available: 23.1.2 -> 23.3.1
[notice] To update, run: /clusterfs/usr/bin/python3.11 -m pip install --upgrade pip
cameron@rp3n0:/clusterfs/common/vcgencmd-0.1.1$ cd ../..
cameron@rp3n0:/clusterfs$ cd usr/bin/
cameron@rp3n0:/clusterfs/usr/bin$ ./python3
Python 3.11.4 (main, Aug  9 2023, 22:16:22) [GCC 12.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import vcgencmd
>>> vcgm = vcgencmd.Vcgencmd()
>>> output = vcgm.get_throttled()
>>> output
{'raw_data': '0x50000', 'binary': '01010000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': True, '17': False, '18': True, '19': False}}
>>> output = vcgm.measure_temp()
>>> output
38.1
>>> output = vcgm.measure_clock(
... arm)
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'arm' is not defined
>>> output = vcgm.measure_clock(arm)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'arm' is not defined
>>> output = vcgm.measure_clock("arm")
>>> output
1400148000
>>> exit()
cameron@rp3n0:/clusterfs/usr/bin$ cd ../..
cameron@rp3n0:/clusterfs$ ls
Projects  benchmarks  common  configs  lost+found  python  usr
cameron@rp3n0:/clusterfs$ cd benchmarks/
cameron@rp3n0:/clusterfs/benchmarks$ ls 
BLIS
cameron@rp3n0:/clusterfs/benchmarks$ d BLIS/
ls
d: command not found
cameron@rp3n0:/clusterfs/benchmarks$ ls
BLIS
cameron@rp3n0:/clusterfs/benchmarks$ cd BLIS/
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ ls
HPL.dat   HPL4.dat    mpihpl2.sh  slurm-100.out  slurm-109.out  slurm-119.out  slurm-128.out  slurm-88.out  slurm-94.out  slurm-99.out
HPL0.dat  HPL5.dat    mpihpl3.sh  slurm-101.out  slurm-110.out  slurm-120.out  slurm-129.out  slurm-90.out  slurm-95.out
HPL1.dat  mpihpl.sh   mpihpl4.sh  slurm-102.out  slurm-111.out  slurm-121.out  slurm-138.out  slurm-91.out  slurm-96.out
HPL2.dat  mpihpl0.sh  mpihpl5.sh  slurm-107.out  slurm-117.out  slurm-122.out  slurm-86.out   slurm-92.out  slurm-97.out
HPL3.dat  mpihpl1.sh  mpitemp.sh  slurm-108.out  slurm-118.out  slurm-123.out  slurm-87.out   slurm-93.out  slurm-98.out
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano temp.py
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl.sh 
Submitted batch job 139
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-139.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
  File "/clusterfs/benchmarks/BLIS/temp.py", line 8
    output = f"My rank is {my_rank} and my temperature is {vcgm.measure_temp('arm')"
                                                                                    ^
SyntaxError: f-string: expecting '}'
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano temp.py
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl.sh 
Submitted batch job 140
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-140.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 1, in <module>
    from vcgencmd import Vcgencmd
ModuleNotFoundError: No module named 'vcgencmd'
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ srun --nodes=3 "/clusterfs/usr/bin/pip3 install -e /clusterfs/common/vcgencmd-0.1.1" 
slurmstepd-rp4n0: error: execve(): /clusterfs/usr/bin/pip3 install -e /clusterfs/common/vcgencmd-0.1.1: No such file or directory
slurmstepd-rp4n1: error: execve(): /clusterfs/usr/bin/pip3 install -e /clusterfs/common/vcgencmd-0.1.1: No such file or directory
slurmstepd-rp4n2: error: execve(): /clusterfs/usr/bin/pip3 install -e /clusterfs/common/vcgencmd-0.1.1: No such file or directory
srun: error: rp4n1: task 1: Exited with exit code 2
srun: error: rp4n0: task 0: Exited with exit code 2
srun: error: rp4n2: task 2: Exited with exit code 2
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cd ../..
cameron@rp3n0:/clusterfs$ ls
Projects  benchmarks  common  configs  lost+found  python  usr
cameron@rp3n0:/clusterfs$ cd usr/bin/
cameron@rp3n0:/clusterfs/usr/bin$ ls
2to3       f2py   f2py3.11  idle3.11  pip3.11  pydoc3.11  python3-config  python3.11-config
2to3-3.11  f2py3  idle3     pip3      pydoc3   python3    python3.11
cameron@rp3n0:/clusterfs/usr/bin$ srun --nodes=3 "./pip3 install -e /clusterfs/common/vcgencmd-0.1.1" 
srun: job 142 queued and waiting for resources
srun: job 142 has been allocated resources
slurmstepd-rp4n0: error: execve(): /clusterfs/usr/bin/./pip3 install -e /clusterfs/common/vcgencmd-0.1.1: No such file or directory
slurmstepd-rp4n1: error: execve(): /clusterfs/usr/bin/./pip3 install -e /clusterfs/common/vcgencmd-0.1.1: No such file or directory
slurmstepd-rp4n2: error: execve(): /clusterfs/usr/bin/./pip3 install -e /clusterfs/common/vcgencmd-0.1.1: No such file or directory
srun: error: rp4n1: task 1: Exited with exit code 2
srun: error: rp4n0: task 0: Exited with exit code 2
srun: error: rp4n2: task 2: Exited with exit code 2
cameron@rp3n0:/clusterfs/usr/bin$ cd ../..
cameron@rp3n0:/clusterfs$ ls
Projects  benchmarks  common  configs  lost+found  python  usr
cameron@rp3n0:/clusterfs$ cd Projects/
cameron@rp3n0:/clusterfs/Projects$ ls
LearningSlurm  llama.cpp     slurm-11.out  slurm-13.out  slurm-15.out  slurm-19.out  slurm-21.out  slurm-23.out  sub_65b.sh
generator      slurm-10.out  slurm-12.out  slurm-14.out  slurm-18.out  slurm-20.out  slurm-22.out  slurm-78.out  sub_llama.sh
cameron@rp3n0:/clusterfs/Projects$ cd LearningSlurm/
cameron@rp3n0:/clusterfs/Projects/LearningSlurm$ ls
a.out       hello_mpi.c     normal         slurm-102.out  slurm-105.out  slurm-15.out  slurm-72.out  slurm-94.out  slurm-97.out
calc-pi     helloworld.sh   slurm-100.out  slurm-103.out  slurm-106.out  slurm-6.out   slurm-73.out  slurm-95.out  slurm-99.out
fix_ssh.sh  helloworld.txt  slurm-101.out  slurm-104.out  slurm-107.out  slurm-70.out  slurm-93.out  slurm-96.out  sub_mpi.sh
cameron@rp3n0:/clusterfs/Projects/LearningSlurm$ cd ..
cameron@rp3n0:/clusterfs/Projects$ ls
LearningSlurm  llama.cpp     slurm-11.out  slurm-13.out  slurm-15.out  slurm-19.out  slurm-21.out  slurm-23.out  sub_65b.sh
generator      slurm-10.out  slurm-12.out  slurm-14.out  slurm-18.out  slurm-20.out  slurm-22.out  slurm-78.out  sub_llama.sh
cameron@rp3n0:/clusterfs/Projects$ cd ..
cameron@rp3n0:/clusterfs$ ls
Projects  benchmarks  common  configs  lost+found  python  usr
cameron@rp3n0:/clusterfs$ cd benchmarks/BLIS/
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ ls
HPL.dat   HPL4.dat    mpihpl2.sh  slurm-100.out  slurm-109.out  slurm-119.out  slurm-128.out  slurm-86.out  slurm-92.out  slurm-97.out
HPL0.dat  HPL5.dat    mpihpl3.sh  slurm-101.out  slurm-110.out  slurm-120.out  slurm-129.out  slurm-87.out  slurm-93.out  slurm-98.out
HPL1.dat  mpihpl.sh   mpihpl4.sh  slurm-102.out  slurm-111.out  slurm-121.out  slurm-138.out  slurm-88.out  slurm-94.out  slurm-99.out
HPL2.dat  mpihpl0.sh  mpihpl5.sh  slurm-107.out  slurm-117.out  slurm-122.out  slurm-139.out  slurm-90.out  slurm-95.out  temp.py
HPL3.dat  mpihpl1.sh  mpitemp.sh  slurm-108.out  slurm-118.out  slurm-123.out  slurm-140.out  slurm-91.out  slurm-96.out
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl.sh 
Submitted batch job 143
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-143.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 2, in <module>
    from mpi4pi import MPI
ModuleNotFoundError: No module named 'mpi4pi'
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-144.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 2, in <module>
    from mpi4pi import MPI
ModuleNotFoundError: No module named 'mpi4pi'
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl.sh 
Submitted batch job 145
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-145.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 2, in <module>
    from mpi4pi import MPI
ModuleNotFoundError: No module named 'mpi4pi'
--------------------------------------------------------------------------
Primary job  terminated normally, but 1 process returned
a non-zero exit code. Per user-direction, the job has been aborted.
--------------------------------------------------------------------------
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 2, in <module>
    from mpi4pi import MPI
ModuleNotFoundError: No module named 'mpi4pi'
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 2, in <module>
    from mpi4pi import MPI
ModuleNotFoundError: No module named 'mpi4pi'
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 2, in <module>
    from mpi4pi import MPI
ModuleNotFoundError: No module named 'mpi4pi'
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 2, in <module>
    from mpi4pi import MPI
ModuleNotFoundError: No module named 'mpi4pi'
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 2, in <module>
    from mpi4pi import MPI
ModuleNotFoundError: No module named 'mpi4pi'
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 2, in <module>
    from mpi4pi import MPI
ModuleNotFoundError: No module named 'mpi4pi'
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 2, in <module>
    from mpi4pi import MPI
ModuleNotFoundError: No module named 'mpi4pi'
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 2, in <module>
    from mpi4pi import MPI
ModuleNotFoundError: No module named 'mpi4pi'
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 2, in <module>
    from mpi4pi import MPI
ModuleNotFoundError: No module named 'mpi4pi'
--------------------------------------------------------------------------
mpiexec detected that one or more processes exited with non-zero status, thus causing
the job to be terminated. The first process to do so was:

  Process name: [[63214,1],1]
  Exit code:    1
--------------------------------------------------------------------------
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano temp.py 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl.sh 
Submitted batch job 146
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-146.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 8, in <module>
Traceback (most recent call last):
    output = f"My rank is {my_rank} and my temperature is {vcgm.measure_temp('arm')}"
  File "/clusterfs/benchmarks/BLIS/temp.py", line 8, in <module>
    output = f"My rank is {my_rank} and my temperature is {vcgm.measure_temp('arm')}"
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Vcgencmd.measure_temp() takes 1 positional argument but 2 were given
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 8, in <module>
TypeError: Vcgencmd.measure_temp() takes 1 positional argument but 2 were given
    output = f"My rank is {my_rank} and my temperature is {vcgm.measure_temp('arm')}"
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Vcgencmd.measure_temp() takes 1 positional argument but 2 were given
Traceback (most recent call last):
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 8, in <module>
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 8, in <module>
    output = f"My rank is {my_rank} and my temperature is {vcgm.measure_temp('arm')}"
    output = f"My rank is {my_rank} and my temperature is {vcgm.measure_temp('arm')}"
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Vcgencmd.measure_temp() takes 1 positional argument but 2 were given
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Vcgencmd.measure_temp() takes 1 positional argument but 2 were given
  File "/clusterfs/benchmarks/BLIS/temp.py", line 8, in <module>
    output = f"My rank is {my_rank} and my temperature is {vcgm.measure_temp('arm')}"
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Vcgencmd.measure_temp() takes 1 positional argument but 2 were given
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 8, in <module>
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 8, in <module>
    output = f"My rank is {my_rank} and my temperature is {vcgm.measure_temp('arm')}"
Traceback (most recent call last):
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^
    output = f"My rank is {my_rank} and my temperature is {vcgm.measure_temp('arm')}"
TypeError: Vcgencmd.measure_temp() takes 1 positional argument but 2 were given
  File "/clusterfs/benchmarks/BLIS/temp.py", line 8, in <module>
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Vcgencmd.measure_temp() takes 1 positional argument but 2 were given
    output = f"My rank is {my_rank} and my temperature is {vcgm.measure_temp('arm')}"
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Vcgencmd.measure_temp() takes 1 positional argument but 2 were given
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 8, in <module>
    output = f"My rank is {my_rank} and my temperature is {vcgm.measure_temp('arm')}"
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 8, in <module>
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Vcgencmd.measure_temp() takes 1 positional argument but 2 were given
    output = f"My rank is {my_rank} and my temperature is {vcgm.measure_temp('arm')}"
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Vcgencmd.measure_temp() takes 1 positional argument but 2 were given
Traceback (most recent call last):
  File "/clusterfs/benchmarks/BLIS/temp.py", line 8, in <module>
    output = f"My rank is {my_rank} and my temperature is {vcgm.measure_temp('arm')}"
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Vcgencmd.measure_temp() takes 1 positional argument but 2 were given
--------------------------------------------------------------------------
Primary job  terminated normally, but 1 process returned
a non-zero exit code. Per user-direction, the job has been aborted.
--------------------------------------------------------------------------
--------------------------------------------------------------------------
mpiexec detected that one or more processes exited with non-zero status, thus causing
the job to be terminated. The first process to do so was:

  Process name: [[63185,1],0]
  Exit code:    1
--------------------------------------------------------------------------
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano temp.py 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl.sh 
Submitted batch job 147
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-147.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-147.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
rp4*         up   infinite      3  alloc rp4n[0-2]
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-147.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-147.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-147.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-147.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-147.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ scancel 147
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano temp.py 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl.sh 
Submitted batch job 148
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-148.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
My rank is 2 and my temperature is 43.3
My rank is 3 and my temperature is 43.3
My rank is 0 and my temperature is 43.3
My rank is 4 and my temperature is 28.7
My rank is 6 and my temperature is 28.7
My rank is 7 and my temperature is 28.7
My rank is 1 and my temperature is 43.3
My rank is 5 and my temperature is 28.7
My rank is 9 and my temperature is 28.2
My rank is 10 and my temperature is 28.2
My rank is 11 and my temperature is 28.2
My rank is 8 and my temperature is 28.2
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl.sh 
Submitted batch job 149
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-149.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
----------------------------------------------------------------------------
Open MPI has detected that a parameter given to a command line
option does not match the expected format:

  Option: n
  Param:  /clusterfs/usr/bin/python3

This is frequently caused by omitting to provide the parameter
to an option that requires one. Please check the command line and try again.
----------------------------------------------------------------------------
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl.sh 
Submitted batch job 150
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-150.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
My rank is 1 and my temperature is 42.8
My rank is 0 and my temperature is 42.8
My rank is 2 and my temperature is 42.8
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano temp.py 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl.sh 
Submitted batch job 151
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-151.out 
Master node: rp4n0
Configuration for the HPL.dat as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
rp4n0 temperature is 43.8
rp4n0 temperature is 43.8
rp4n0 temperature is 43.8
rp4n0 temperature is 43.8
rp4n0 clock is 1800457088
rp4n0 clock is 1800457088
rp4n1 temperature is 30.1
rp4n1 temperature is 30.1
rp4n1 temperature is 30.1
rp4n1 temperature is 30.1
rp4n0 clock is 1800457088
rp4n2 temperature is 28.7
rp4n2 temperature is 28.7
rp4n2 temperature is 28.7
rp4n2 temperature is 28.7
rp4n0 clock is 1800404352
rp4n0 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n0 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n1 clock is 1800457088
rp4n1 clock is 1800457088
rp4n1 clock is 1800457088
rp4n1 clock is 1800457088
rp4n2 clock is 1800404352
rp4n2 clock is 1800457088
rp4n0 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n2 clock is 1800457088
rp4n2 clock is 1700419968
rp4n1 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n1 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n1 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n0 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n2 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n2 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n1 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n2 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n2 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ ls
HPL.dat   HPL5.dat    mpihpl4.sh     slurm-107.out  slurm-118.out  slurm-128.out  slurm-144.out  slurm-150.out  slurm-91.out  slurm-97.out
HPL0.dat  mpihpl.sh   mpihpl5.sh     slurm-108.out  slurm-119.out  slurm-129.out  slurm-145.out  slurm-151.out  slurm-92.out  slurm-98.out
HPL1.dat  mpihpl0.sh  mpitemp.sh     slurm-109.out  slurm-120.out  slurm-138.out  slurm-146.out  slurm-86.out   slurm-93.out  slurm-99.out
HPL2.dat  mpihpl1.sh  slurm-100.out  slurm-110.out  slurm-121.out  slurm-139.out  slurm-147.out  slurm-87.out   slurm-94.out  temp.py
HPL3.dat  mpihpl2.sh  slurm-101.out  slurm-111.out  slurm-122.out  slurm-140.out  slurm-148.out  slurm-88.out   slurm-95.out
HPL4.dat  mpihpl3.sh  slurm-102.out  slurm-117.out  slurm-123.out  slurm-143.out  slurm-149.out  slurm-90.out   slurm-96.out
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat HPL0.dat 
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
49920       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat HPL1.dat 
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
49920       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
1           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ ls
HPL.dat   HPL5.dat    mpihpl4.sh     slurm-107.out  slurm-118.out  slurm-128.out  slurm-144.out  slurm-150.out  slurm-91.out  slurm-97.out
HPL0.dat  mpihpl.sh   mpihpl5.sh     slurm-108.out  slurm-119.out  slurm-129.out  slurm-145.out  slurm-151.out  slurm-92.out  slurm-98.out
HPL1.dat  mpihpl0.sh  mpitemp.sh     slurm-109.out  slurm-120.out  slurm-138.out  slurm-146.out  slurm-86.out   slurm-93.out  slurm-99.out
HPL2.dat  mpihpl1.sh  slurm-100.out  slurm-110.out  slurm-121.out  slurm-139.out  slurm-147.out  slurm-87.out   slurm-94.out  temp.py
HPL3.dat  mpihpl2.sh  slurm-101.out  slurm-111.out  slurm-122.out  slurm-140.out  slurm-148.out  slurm-88.out   slurm-95.out
HPL4.dat  mpihpl3.sh  slurm-102.out  slurm-117.out  slurm-123.out  slurm-143.out  slurm-149.out  slurm-90.out   slurm-96.out
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl0.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl1.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl2.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl3.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl4.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl5.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl0.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl1.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl2.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl3.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl4.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ nano mpihpl5.sh 
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl0.sh 
Submitted batch job 152
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl1.sh 
Submitted batch job 153
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl2.sh 
Submitted batch job 154
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl3.sh 
Submitted batch job 155
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl4.sh 
Submitted batch job 156
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ sbatch mpihpl5.sh 
Submitted batch job 157
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
               153       rp4 mpihpl1.  cameron PD       0:00      3 (Resources)
               154       rp4 mpihpl2.  cameron PD       0:00      3 (Priority)
               155       rp4 mpihpl3.  cameron PD       0:00      3 (Priority)
               156       rp4 mpihpl4.  cameron PD       0:00      3 (Priority)
               157       rp4 mpihpl5.  cameron PD       0:00      3 (Priority)
               152       rp4 mpihpl0.  cameron  R       0:32      3 rp4n[0-2]
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
               153       rp4 mpihpl1.  cameron PD       0:00      3 (Resources)
               154       rp4 mpihpl2.  cameron PD       0:00      3 (Priority)
               155       rp4 mpihpl3.  cameron PD       0:00      3 (Priority)
               156       rp4 mpihpl4.  cameron PD       0:00      3 (Priority)
               157       rp4 mpihpl5.  cameron PD       0:00      3 (Priority)
               152       rp4 mpihpl0.  cameron  R      54:00      3 rp4n[0-2]
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-152.out 
Master node: rp4n0
Configuration for the results as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
49920       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
0           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
================================================================================
HPLinpack 2.3  --  High-Performance Linpack benchmark  --   December 2, 2018
Written by A. Petitet and R. Clint Whaley,  Innovative Computing Laboratory, UTK
Modified by Piotr Luszczek, Innovative Computing Laboratory, UTK
Modified by Julien Langou, University of Colorado Denver
================================================================================

An explanation of the input/output parameters follows:
T/V    : Wall time / encoded variant.
N      : The order of the coefficient matrix A.
NB     : The partitioning blocking factor.
P      : The number of process rows.
Q      : The number of process columns.
Time   : Time in seconds to solve the linear system.
Gflops : Rate of execution for solving the linear system.

The following parameter values will be used:

N      :   49920 
NB     :      96      184      224      232      248 
PMAP   : Row-major process mapping
P      :       3 
Q      :       4 
PFACT  :   Right 
NBMIN  :       4 
NDIV   :       2 
RFACT  :   Crout 
BCAST  :   1ring 
DEPTH  :       1 
SWAP   : Mix (threshold = 64)
L1     : transposed form
U      : transposed form
EQUIL  : yes
ALIGN  : 8 double precision words

--------------------------------------------------------------------------------

- The matrix A is randomly generated for each test.
- The following scaled residual check will be computed:
      ||Ax-b||_oo / ( eps * ( || x ||_oo * || A ||_oo + || b ||_oo ) * N )
- The relative machine precision (eps) is taken to be               1.110223e-16
- Computational tests pass if scaled residuals are less than                16.0

================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR10C2R4       49920    96     3     4            2617.46             3.1686e+01
HPL_pdgesv() start time Sat Nov 11 19:03:54 2023

HPL_pdgesv() end time   Sat Nov 11 19:47:32 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.12586362e-03 ...... PASSED
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ client_loop: send disconnect: Broken pipe
cameron@x86:~$ ssh rp3n0
Welcome to Ubuntu 23.04 (GNU/Linux 6.2.0-1016-raspi aarch64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Nov 12 08:03:52 EST 2023

  System load:  0.08               Temperature:           39.2 C
  Usage of /:   14.5% of 28.96GB   Processes:             143
  Memory usage: 27%                Users logged in:       0
  Swap usage:   0%                 IPv4 address for eth0: 192.168.1.52

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

0 updates can be applied immediately.

New release '23.10' available.
Run 'do-release-upgrade' to upgrade to it.


Last login: Sat Nov 11 13:08:22 2023 from 192.168.1.183
cameron@rp3n0:~$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
rp4*         up   infinite      3  alloc rp4n[0-2]
cameron@rp3n0:~$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
               156       rp4 mpihpl4.  cameron PD       0:00      3 (Resources)
               157       rp4 mpihpl5.  cameron PD       0:00      3 (Priority)
               155       rp4 mpihpl3.  cameron  R    1:00:29      3 rp4n[0-2]
cameron@rp3n0:~$ cd /clusterfs/benchmarks/BLIS/
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-154.out 
Master node: rp4n0
Configuration for the results as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
49920       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
2           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
================================================================================
HPLinpack 2.3  --  High-Performance Linpack benchmark  --   December 2, 2018
Written by A. Petitet and R. Clint Whaley,  Innovative Computing Laboratory, UTK
Modified by Piotr Luszczek, Innovative Computing Laboratory, UTK
Modified by Julien Langou, University of Colorado Denver
================================================================================

An explanation of the input/output parameters follows:
T/V    : Wall time / encoded variant.
N      : The order of the coefficient matrix A.
NB     : The partitioning blocking factor.
P      : The number of process rows.
Q      : The number of process columns.
Time   : Time in seconds to solve the linear system.
Gflops : Rate of execution for solving the linear system.

The following parameter values will be used:

N      :   49920 
NB     :      96      184      224      232      248 
PMAP   : Row-major process mapping
P      :       3 
Q      :       4 
PFACT  :   Right 
NBMIN  :       4 
NDIV   :       2 
RFACT  :   Crout 
BCAST  :   2ring 
DEPTH  :       1 
SWAP   : Mix (threshold = 64)
L1     : transposed form
U      : transposed form
EQUIL  : yes
ALIGN  : 8 double precision words

--------------------------------------------------------------------------------

- The matrix A is randomly generated for each test.
- The following scaled residual check will be computed:
      ||Ax-b||_oo / ( eps * ( || x ||_oo * || A ||_oo + || b ||_oo ) * N )
- The relative machine precision (eps) is taken to be               1.110223e-16
- Computational tests pass if scaled residuals are less than                16.0

================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR12C2R4       49920    96     3     4            2585.22             3.2082e+01
HPL_pdgesv() start time Sun Nov 12 03:06:05 2023

HPL_pdgesv() end time   Sun Nov 12 03:49:10 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   2.94361502e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR12C2R4       49920   184     3     4            2477.00             3.3483e+01
HPL_pdgesv() start time Sun Nov 12 03:51:43 2023

HPL_pdgesv() end time   Sun Nov 12 04:33:00 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.22737008e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR12C2R4       49920   224     3     4            2701.99             3.0695e+01
HPL_pdgesv() start time Sun Nov 12 04:35:33 2023

HPL_pdgesv() end time   Sun Nov 12 05:20:35 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.14309729e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR12C2R4       49920   232     3     4            2735.80             3.0316e+01
HPL_pdgesv() start time Sun Nov 12 05:23:08 2023

HPL_pdgesv() end time   Sun Nov 12 06:08:44 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   2.85187576e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR12C2R4       49920   248     3     4            3058.20             2.7120e+01
HPL_pdgesv() start time Sun Nov 12 06:11:17 2023

HPL_pdgesv() end time   Sun Nov 12 07:02:15 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.19462466e-03 ...... PASSED
================================================================================

Finished      5 tests with the following results:
              5 tests completed and passed residual checks,
              0 tests completed and failed residual checks,
              0 tests skipped because of illegal input values.
--------------------------------------------------------------------------------

End of Tests.
================================================================================
rp4n0 temperature is 52.1
rp4n0 temperature is 52.5
rp4n0 temperature is 52.5
rp4n0 clock is 1800404352
rp4n0 temperature is 52.5
rp4n0 clock is 1800457088
rp4n0 clock is 1800457088
rp4n1 temperature is 43.3
rp4n1 temperature is 43.3
rp4n1 temperature is 43.3
rp4n1 temperature is 43.3
rp4n2 temperature is 38.9
rp4n0 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n2 temperature is 38.9
rp4n2 temperature is 38.9
rp4n2 temperature is 38.9
rp4n0 clock is 1800457088
rp4n0 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n1 clock is 1800404352
rp4n1 clock is 1800404352
rp4n0 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n1 clock is 1800457088
rp4n1 clock is 1800457088
rp4n2 clock is 1800457088
rp4n2 clock is 1800457088
rp4n2 clock is 1800457088
rp4n2 clock is 1800457088
rp4n1 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n1 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n1 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n1 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n2 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n2 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n0 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n2 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n2 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ cat slurm-153.out 
Master node: rp4n0
Configuration for the results as follows:
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
49920       Ns
5          # of NBs
96 184 224 232 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
3           Ps
4           Qs
16.0        threshold
1           # of panel fact
2           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
1           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
1           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
1           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
64           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
================================================================================
HPLinpack 2.3  --  High-Performance Linpack benchmark  --   December 2, 2018
Written by A. Petitet and R. Clint Whaley,  Innovative Computing Laboratory, UTK
Modified by Piotr Luszczek, Innovative Computing Laboratory, UTK
Modified by Julien Langou, University of Colorado Denver
================================================================================

An explanation of the input/output parameters follows:
T/V    : Wall time / encoded variant.
N      : The order of the coefficient matrix A.
NB     : The partitioning blocking factor.
P      : The number of process rows.
Q      : The number of process columns.
Time   : Time in seconds to solve the linear system.
Gflops : Rate of execution for solving the linear system.

The following parameter values will be used:

N      :   49920 
NB     :      96      184      224      232      248 
PMAP   : Row-major process mapping
P      :       3 
Q      :       4 
PFACT  :   Right 
NBMIN  :       4 
NDIV   :       2 
RFACT  :   Crout 
BCAST  :  1ringM 
DEPTH  :       1 
SWAP   : Mix (threshold = 64)
L1     : transposed form
U      : transposed form
EQUIL  : yes
ALIGN  : 8 double precision words

--------------------------------------------------------------------------------

- The matrix A is randomly generated for each test.
- The following scaled residual check will be computed:
      ||Ax-b||_oo / ( eps * ( || x ||_oo * || A ||_oo + || b ||_oo ) * N )
- The relative machine precision (eps) is taken to be               1.110223e-16
- Computational tests pass if scaled residuals are less than                16.0

================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       49920    96     3     4            2635.22             3.1473e+01
HPL_pdgesv() start time Sat Nov 11 23:05:23 2023

HPL_pdgesv() end time   Sat Nov 11 23:49:18 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   2.98900715e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       49920   184     3     4            2475.63             3.3502e+01
HPL_pdgesv() start time Sat Nov 11 23:51:51 2023

HPL_pdgesv() end time   Sun Nov 12 00:33:06 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.22737008e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       49920   224     3     4            2661.01             3.1168e+01
HPL_pdgesv() start time Sun Nov 12 00:35:40 2023

HPL_pdgesv() end time   Sun Nov 12 01:20:01 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.14309729e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       49920   232     3     4            2691.05             3.0820e+01
HPL_pdgesv() start time Sun Nov 12 01:22:34 2023

HPL_pdgesv() end time   Sun Nov 12 02:07:25 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   2.85187576e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       49920   248     3     4            3207.26             2.5859e+01
HPL_pdgesv() start time Sun Nov 12 02:09:59 2023

HPL_pdgesv() end time   Sun Nov 12 03:03:26 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.19462466e-03 ...... PASSED
================================================================================

Finished      5 tests with the following results:
              5 tests completed and passed residual checks,
              0 tests completed and failed residual checks,
              0 tests skipped because of illegal input values.
--------------------------------------------------------------------------------

End of Tests.
================================================================================
--------------------------------------------------------------------------
A system call failed during shared memory initialization that should
not have.  It is likely that your MPI job will now either abort or
experience performance degradation.

  Local host:  rp4n1
  System call: unlink(2) /dev/shm/vader_segment.rp4n1.1000.fb1a0001.3
  Error:       No such file or directory (errno 2)
--------------------------------------------------------------------------
[rp4n0:02616] 3 more processes have sent help message help-opal-shmem-mmap.txt / sys call fail
[rp4n0:02616] Set MCA parameter "orte_base_help_aggregate" to 0 to see all help / error messages
rp4n0 temperature is 53.0
rp4n0 temperature is 53.0
rp4n0 temperature is 52.1
rp4n0 clock is 1800457088
rp4n0 clock is 1800457088
rp4n0 clock is 1800457088
rp4n0 temperature is 53.0
rp4n0 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n0 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n1 temperature is 41.8
rp4n1 temperature is 41.8
rp4n1 temperature is 41.8
rp4n1 temperature is 41.8
rp4n2 temperature is 39.4
rp4n2 temperature is 39.4
rp4n2 temperature is 39.4
rp4n2 temperature is 39.4
rp4n0 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n0 clock is 1800457088
rp4n1 clock is 1800457088
rp4n1 clock is 1800457088
rp4n1 clock is 1800457088
rp4n1 clock is 1800404352
rp4n2 clock is 1800404352
rp4n2 clock is 1800457088
rp4n2 clock is 1800457088
rp4n2 clock is 1800457088
rp4n1 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n1 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n1 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n0 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n2 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n1 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n2 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n2 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
rp4n2 throttled info is {'raw_data': '0x0', 'binary': '00000000000000000000', 'breakdown': {'0': False, '1': False, '2': False, '3': False, '16': False, '17': False, '18': False, '19': False}}
cameron@rp3n0:/clusterfs/benchmarks/BLIS$ 

