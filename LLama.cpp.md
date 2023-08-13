cd /clusterfs
mkdir Projects
cd Projects/
git clone https://github.com/ggerganov/llama.cpp

cameron@rp4n1:~$ cd /clusterfs/Projects/llama.cpp/
cameron@rp4n1:/clusterfs/Projects/llama.cpp$ make CC=mpicc CXX=mpicxx LLAMA_MPI=1
