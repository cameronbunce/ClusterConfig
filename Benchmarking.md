## Cluster Performance

A fantastic way to make sure that we're swimming in the deep end is to run Linpack on our new cluster  [ and for reference, we're using 3 Pi4s with 8 gigs of RAM as compute nodes, and a Pi3 as the controller ]

`Following all the links is not necessary unless you want to read along, downloads are called out`

The Top500 list https://top500.org/project/linpack/ tracks the most powerful supercomputers ( published ) and they use Linpack as their yardstick. 

Netlib.org ( https://www.netlib.org/benchmark/hpl/) has details on how to set up High Performance Linpack for our system, where they tell us that we need to have MPI, BLAS, and VSIPL. We did MPI earlier, but let's see what the rest of the alphabet soup has for us - https://www.netlib.org/benchmark/hpl/links.html

BLAS is Basic Linear Algebra Subprograms
VSIPL is Vector Signal Image Processing Library

# By the book with the big iron?

So let's head on over to the ARM developer site and get their optimized libraries

From - https://developer.arm.com/downloads/-/arm-compiler-for-linux - we're going to download the  `arm-compiler-for-linux_23.04.1_Ubuntu-22.04_aarch64.tar` and hope we don't need to rebuild our cluster with Ubuntu LTS 

I extracted that tarball to the /clusterfs mount ( you went ahead and mounted it from your workstation too, right? ) 

And the installation instructions say ~`run the .sh file as root` so we will

`sudo ./a` + Tab, and fire away.

You have to answer in the affirmative to the EULA

The readme file points us to https://developer.arm.com/documentation/101458/2300/Get-started


which tells us that in order to use this we'll need `module` which lives at https://github.com/cea-hpc/modules

So lets clone that to the /clusterfs - hey, lets make a 'common' folder there while we're at it. This is a resource, not a config or a project. We'll get it straight one day. 

```
cd /clusterfs/
cameron@x86:/clusterfs$ mkdir common
cameron@x86:/clusterfs$ cd common/
cameron@x86:/clusterfs/common$ git clone https://github.com/cea-hpc/modules
```

Now I want to call out here that I'm going to switch to a shell on a node in the cluster. My workstation, as you might infer from the hostname, is not a Raspberry Pi. I want to ensure that the installation of module is configured for the hardware on the cluster. 

And as it turns out, I hadn't installed `make` on all nodes, so I got to do that just now. I found the one without it. And then when I tried to configure I got a failure because it didn't have `tcl`. But `tcl` was installed, so I got the `tcl-dev` package and `configure` was happy with that. 

`sudo apt install make tcl tcl-dev libc6-dev`

that should do it. We bring all nodes up to parity, because why not. 

This all amounts to, as the instructions in the fine README say... 

```
$ ./configure
$ make
$ make install
```

I'm just solving for errors along the way. I had to follow that up with a `sudo !!` because I was not root. 

I then went to the other nodes, navigated to the module folder, and ran `sudo make install` on each. 

When I was younger I used to love to build models, and rockets and things like that. In the instructions, they always told you to read all the way through so that you knew how it was supposed to go together at each step and how that contributed to the final built model. 

I remembered that as I fumbled through figuring out why I couldn't seem to use `module` even though it seemed to have been built correctly. I didn't have the configuration steps in my head when I ran `.configure` so I didn't know where it put its files. 

The default installation is to use `/usr/local/Modules` and now we need to tell bash to use the thing we built.

In /usr/local/Modules/init/profile.sh is a script to tell our shell where to find stuff when we type `module`. We need to put a link to that script in the /etc/profile.d/ folder. On each node we'll run the following commands:

`sudo ln -s /usr/local/Modules/init/profile.sh /etc/profile.d/modules.sh`
`sudo ln -s /usr/local/Modules/init/profile.csh /etc/profile.d/modules.csh`

That will be invoked on your next session, so exit, and ssh back in to verify that now `module` does something.

Oh, it is possible that "sudo apt install environment-modules" would do the same thing, but that's like taking your car in for an oil change. Know what oil filter you use, apt has an older version than what we just compiled. 

Now we tell the module system about our fancy compiler:

`export MODULEPATH=$MODULEPATH:/opt/arm/modulefiles`

and verify

`module avail`

and we should see

```
$ module avail
------------------------------------------------------ /usr/local/Modules/modulefiles ------------------------------------------------------
dot  module-git  module-info  modules  null  use.own  

----------------------------------------------------------- /opt/arm/modulefiles -----------------------------------------------------------
acfl/23.04.1  binutils/12.2.0  gnu/12.2.0  

Key:
modulepath  
```

So let's invoke and use the compiler. First we need a 'hello, world' program

write the following to a file called `hello.c`

```c
#include <stdio.h>

int main() {
    printf("Hello, World!");
    return 0;
}
```

load the module for the Arm compiler

`module load acfl/23.04.1`

and compile 

`armclang -o hello hello.c`

the pattern of that command is as follows

`{armclang|armclang++} -o <binary> <source>.{c|cpp}`

and we now have our `hello` binary which, when run should give the oldest of computer greetings

```
cameron@rp4n0:~$ ./hello 
Hello, World!
```

I got impatient, and found a quick guide to compiling HPL without sweating the optimizations, so lets get a baseline. 


# Or follow some guide for this architecture and tune our way up

I found a very straightforward guide to running Linpack on the Raspberry Pi - https://github.com/jfikar/xhpl-aarch64 - using OpenBLAS instead of going the Arm Performance Libraries direction. Despite completely ignoring the many configuration options for HPL, I saw 16.1 Gflops on the first run on a single node.

Using the dat file copy-pasta from the repo above:

```
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
28000       Ns
20          # of NBs
96 104 112 120 128 136 144 152 160 168 176 184 192 200 208 216 224 232 240 248 NBs
0           PMAP process mapping (0=Row-,1=Column-major)
1           # of process grids (P x Q)
1           Ps
1           Qs
16.0        threshold
1           # of panel fact
1           PFACTs (0=left, 1=Crout, 2=Right)
1           # of recursive stopping criterium
4           NBMINs (>= 1)
1           # of panels in recursion
2           NDIVs
1           # of recursive panel fact.
2           RFACTs (0=left, 1=Crout, 2=Right)
1           # of broadcast
2           BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
1           # of lookahead depth
0           DEPTHs (>=0)
2           SWAP (0=bin-exch,1=long,2=mix)
8           swapping threshold
0           L1 in (0=transposed,1=no-transposed) form
0           U  in (0=transposed,1=no-transposed) form
1           Equilibration (0=no,1=yes)
8           memory alignment in double (> 0)
```


```
./testing/xhpl 
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

N      :   28000 
NB     :      96      104      112      120      128      136      144      152 
             160      168      176      184      192      200      208      216 
             224      232      240      248 
PMAP   : Row-major process mapping
P      :       1 
Q      :       1 
PFACT  :   Crout 
NBMIN  :       4 
NDIV   :       2 
RFACT  :   Right 
BCAST  :   2ring 
DEPTH  :       0 
SWAP   : Mix (threshold = 8)
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
WR02R2C4       28000    96     1     1             908.72             1.6106e+01
HPL_pdgesv() start time Fri Sep  8 14:07:44 2023

HPL_pdgesv() end time   Fri Sep  8 14:22:53 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   4.16418112e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR02R2C4       28000   104     1     1             887.17             1.6497e+01
HPL_pdgesv() start time Fri Sep  8 14:31:52 2023

HPL_pdgesv() end time   Fri Sep  8 14:46:40 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   4.21331888e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR02R2C4       28000   112     1     1             903.95             1.6191e+01
HPL_pdgesv() start time Fri Sep  8 14:55:39 2023

HPL_pdgesv() end time   Fri Sep  8 15:10:43 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   4.30060732e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR02R2C4       28000   120     1     1             888.82             1.6467e+01
HPL_pdgesv() start time Fri Sep  8 15:19:41 2023

HPL_pdgesv() end time   Fri Sep  8 15:34:30 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   4.04103624e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR02R2C4       28000   128     1     1             908.44             1.6111e+01
HPL_pdgesv() start time Fri Sep  8 15:43:29 2023

HPL_pdgesv() end time   Fri Sep  8 15:58:37 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.48716402e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR02R2C4       28000   136     1     1             958.89             1.5263e+01
HPL_pdgesv() start time Fri Sep  8 16:07:35 2023

HPL_pdgesv() end time   Fri Sep  8 16:23:34 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.99129460e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR02R2C4       28000   144     1     1             941.36             1.5547e+01
HPL_pdgesv() start time Fri Sep  8 16:32:32 2023

HPL_pdgesv() end time   Fri Sep  8 16:48:13 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.86139701e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR02R2C4       28000   152     1     1             934.90             1.5655e+01
HPL_pdgesv() start time Fri Sep  8 16:57:11 2023

HPL_pdgesv() end time   Fri Sep  8 17:12:46 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   4.52909216e-03 ...... PASSED
^C

```




On all three nodes, it looks a little weird


```
Master node: rp4n0
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

N      :   28000 
NB     :      96      104      112      120      128      136      144      152 
             160      168      176      184      192      200      208      216 
             224      232      240      248 
PMAP   : Row-major process mapping
P      :       1 
Q      :       1 
PFACT  :   Crout 
NBMIN  :       4 
NDIV   :       2 
RFACT  :   Right 
BCAST  :   2ring 
DEPTH  :       0 
SWAP   : Mix (threshold = 8)
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
WR02R2C4       28000    96     1     1            2879.09             5.0835e+00
HPL_pdgesv() start time Fri Sep  8 17:47:27 2023

HPL_pdgesv() end time   Fri Sep  8 18:35:26 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   4.16418112e-03 ...... PASSED
```

That was because I hadn't updated the HPL.dat to reflect running on multiple nodes. Once I had that updated, I got much better results. Using this site for guidance - https://www.advancedclustering.com/act_kb/tune-hpl-dat-file/ - I now ran it again with the following configuration.

```
HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
20          # of NBs
96 104 112 120 128 136 144 152 160 168 176 184 192 200 208 216 224 232 240 248 NBs
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
```

```
cameron@rp3n0:/clusterfs/common/hpl-2.3$ cat slurm-94.out 
Master node: rp4n0
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
NB     :      96      104      112      120      128      136      144      152 
             160      168      176      184      192      200      208      216 
             224      232      240      248 
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
WR11C2R4       48768    96     3     4            3227.45             2.3959e+01
HPL_pdgesv() start time Fri Sep  8 23:05:34 2023

HPL_pdgesv() end time   Fri Sep  8 23:59:21 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.56848253e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   104     3     4            3241.81             2.3853e+01
HPL_pdgesv() start time Sat Sep  9 00:02:04 2023

HPL_pdgesv() end time   Sat Sep  9 00:56:05 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.43051737e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   112     3     4            3254.16             2.3763e+01
HPL_pdgesv() start time Sat Sep  9 00:58:49 2023

HPL_pdgesv() end time   Sat Sep  9 01:53:03 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.34135088e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   120     3     4            3274.97             2.3612e+01
HPL_pdgesv() start time Sat Sep  9 01:55:47 2023

HPL_pdgesv() end time   Sat Sep  9 02:50:22 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   4.45436890e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   128     3     4            3319.10             2.3298e+01
HPL_pdgesv() start time Sat Sep  9 02:53:07 2023

HPL_pdgesv() end time   Sat Sep  9 03:48:26 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.42739112e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   136     3     4            3356.74             2.3036e+01
HPL_pdgesv() start time Sat Sep  9 03:51:12 2023

HPL_pdgesv() end time   Sat Sep  9 04:47:08 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.48541360e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   144     3     4            3379.16             2.2884e+01
HPL_pdgesv() start time Sat Sep  9 04:49:52 2023

HPL_pdgesv() end time   Sat Sep  9 05:46:12 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.18079104e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   152     3     4            3353.16             2.3061e+01
HPL_pdgesv() start time Sat Sep  9 05:48:56 2023

HPL_pdgesv() end time   Sat Sep  9 06:44:49 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.44086225e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   160     3     4            3368.35             2.2957e+01
HPL_pdgesv() start time Sat Sep  9 06:47:35 2023

HPL_pdgesv() end time   Sat Sep  9 07:43:43 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.14117972e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   168     3     4            3328.35             2.3233e+01
HPL_pdgesv() start time Sat Sep  9 07:46:29 2023

HPL_pdgesv() end time   Sat Sep  9 08:41:57 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.55324320e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   176     3     4            3305.67             2.3392e+01
HPL_pdgesv() start time Sat Sep  9 08:44:42 2023

HPL_pdgesv() end time   Sat Sep  9 09:39:47 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.33240962e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   184     3     4            3278.54             2.3586e+01
HPL_pdgesv() start time Sat Sep  9 09:42:32 2023

HPL_pdgesv() end time   Sat Sep  9 10:37:10 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.14657546e-03 ...... PASSED


```


recompiling with BLIS just as referenced in https://github.com/jfikar/xhpl-aarch64 :

```
wget https://github.com/flame/blis/archive/refs/tags/0.9.0.tar.gz
tar xvf 0.9.0.tar.gz
cd blis-0.9.0
./configure -p ${HOME}/blis --disable-shared -t openmp auto
make -j${nproc}
make check
make install
ln -s ${HOME}/blis/lib/libblis.a ${HOME}/blis/lib/libopenblas.a
LDFLAGS=-L${HOME}/blis/lib CFLAGS="-pthread -fopenmp" ./configure
make -j$(nproc)
```

gave some improvement before I killed it:

```
cameron@rp3n0:/clusterfs/common/hpl-2.3$ cat slurm-95.out 
Master node: rp4n0

HPLinpack benchmark input file
Innovative Computing Laboratory, University of Tennessee
HPL.out     output file name (if any)
6           device out (6=stdout,7=stderr,file)
1           # of problems sizes (N)
48768       Ns
20          # of NBs
96 104 112 120 128 136 144 152 160 168 176 184 192 200 208 216 224 232 240 248 NBs
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

N      :   48768 
NB     :      96      104      112      120      128      136      144      152 
             160      168      176      184      192      200      208      216 
             224      232      240      248 
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
WR11C2R4       48768    96     3     4            3049.57             2.5357e+01
HPL_pdgesv() start time Sat Sep  9 13:09:24 2023

HPL_pdgesv() end time   Sat Sep  9 14:00:14 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.42358129e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   104     3     4            3083.98             2.5074e+01
HPL_pdgesv() start time Sat Sep  9 14:03:01 2023

HPL_pdgesv() end time   Sat Sep  9 14:54:25 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.38448949e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   112     3     4            3120.17             2.4783e+01
HPL_pdgesv() start time Sat Sep  9 14:57:12 2023

HPL_pdgesv() end time   Sat Sep  9 15:49:12 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.11958763e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   120     3     4            3069.91             2.5189e+01
HPL_pdgesv() start time Sat Sep  9 15:51:58 2023

HPL_pdgesv() end time   Sat Sep  9 16:43:08 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.27153433e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   128     3     4            3069.63             2.5191e+01
HPL_pdgesv() start time Sat Sep  9 16:45:54 2023

HPL_pdgesv() end time   Sat Sep  9 17:37:03 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   2.96044964e-03 ...... PASSED
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       48768   136     3     4            3054.20             2.5318e+01
HPL_pdgesv() start time Sat Sep  9 17:39:48 2023

HPL_pdgesv() end time   Sat Sep  9 18:30:42 2023

--------------------------------------------------------------------------------
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   3.22980846e-03 ...... PASSED
mpirun: Forwarding signal 18 to job
slurmstepd-rp4n0: error: *** JOB 95 ON rp4n0 CANCELLED AT 2023-09-09T19:14:22 ***
[rp4n0:57763] oob:tcp: send_msg: write failed: Broken pipe (32) [sd = 23]
[rp4n0:57763] [[4225,0],0]-[[4225,0],2] mca_oob_tcp_peer_send_handler: unable to send message ON SOCKET 23
[rp4n0:57763] oob:tcp: send_msg: write failed: Broken pipe (32) [sd = 22]
[rp4n0:57763] [[4225,0],0]-[[4225,0],1] mca_oob_tcp_peer_send_handler: unable to send message ON SOCKET 22

```

in order to try the difference in configuring the Ns based on the function of nodes having 7630MB of ram as reported, or if 8000MB is better. 

Then I read through the configuration manual for the HPL.dat file and noted that the technical explaination of the BCASTs value is "try all of them" so I templated some 5 NBs files with 0-5 values for BCASTs and let SLURM handle that part. 

namely, my SBATCH file looks similar to this for six jobs:

```
cameron@rp3n0:/clusterfs/common/hpl-2.3$ cat mpihpl0.sh 
#!/bin/bash
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=4

cd $SLURM_SUBMIT_DIR
cp HPL0.dat HPL.dat
echo "Master node: $(hostname)"
echo "Configuration for the results as follows:"
cat HPL.dat


mpirun /clusterfs/common/hpl-2.3/testing/xhpl
```

each with a different value for BCASTs in the HPL#.dat file to copy over the primary one for the run. 

I added a thermal monitoring aspect of my benchmarking to pull in the Raspberry Pi specific temperature, clock and throttling information from each node to the Slurm job output as soon as the main job finishes. In the example files I've included here, mpihpl.sh is the base file I was using to try things out and mpihpl1.sh is the job script that returned the highest performance recorded so far, the output of which is slurm-153.out and the configuration used in it is HPL1.dat 

# To Do 
- Document further comparisons with libraries and compilers:
-- OpenBLAS vs BLIS
-- MPI implementations
-- ARM Performance Libraries
- Clean up notes, distil raw output to charts that better illustrate the comparisons being made, pack away raw output with labels/notes