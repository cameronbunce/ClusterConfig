# Running Llama.cpp on the cluster we have made

I'm not paving any particularly new ground here, just recording my path, standing on the shoulders of giants - thanks to https://github.com/ggerganov and https://github.com/theycallmeloki for paving the way.


```
cd /clusterfs
mkdir Projects
cd Projects/
git clone https://github.com/ggerganov/llama.cpp
```

Since writing all the README steps, I've enlisted a RPi 3B+ as a scheduler node to free up one of my Pi4s for compute. There's one more entry in the hostfile, one more node in the slurm.conf, but otherwise it's the same. I still have one node on wifi still. 

This is to build the llama.cpp main executable with MPI enabled, dependencies for this are satisfied with the instructions in Part 3 of Garret Mills' instructions (https://glmdev.medium.com/building-a-raspberry-pi-cluster-f5f2446702e8):

`srun --nodes=3 apt install openmpi-bin openmpi-common libopenmpi3 libopenmpi-dev -y`

```
cameron@rp4n1:~$ cd /clusterfs/Projects/llama.cpp/
cameron@rp4n1:/clusterfs/Projects/llama.cpp$ make CC=mpicc CXX=mpicxx LLAMA_MPI=1
```

I'm not redistributing these files, just tracking back for reproducibility, the model files I used were from TheBloke, the q4_0 version of each

- 13b https://huggingface.co/TheBloke/LLaMa-13B-GGML 
- 65B - https://huggingface.co/TheBloke/llama-65B-GGML


# 13B

SLurm job :

```
#!/bin/bash
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=4

cd $SLURM_SUBMIT_DIR

echo "Master node: $(hostname)"

mpirun -hostfile /clusterfs/Projects/llama.cpp/hostfile -n 3 /clusterfs/Projects/llama.cpp/main -m /home/cameron/models/llama-13b.ggmlv3.q4_0.bin -p "Raspberry Pi computers are " -n 128
```

slurm output:

```
cat slurm-21.out 
Master node: rp4n0
main: build = 975 (9ca4abe)
main: seed  = 1692035168
main: build = 975 (9ca4abe)
main: seed  = 1692035168
main: build = 975 (9ca4abe)
main: seed  = 1692035168
llama.cpp: loading model from /home/cameron/models/llama-13b.ggmlv3.q4_0.bin
llama.cpp: loading model from /home/cameron/models/llama-13b.ggmlv3.q4_0.bin
llama.cpp: loading model from /home/cameron/models/llama-13b.ggmlv3.q4_0.bin
llama_model_load_internal: format     = ggjt v3 (latest)
llama_model_load_internal: n_vocab    = 32000
llama_model_load_internal: n_ctx      = 512
llama_model_load_internal: n_embd     = 5120
llama_model_load_internal: n_mult     = 256
llama_model_load_internal: n_head     = 40
llama_model_load_internal: n_head_kv  = 40
llama_model_load_internal: n_layer    = 40
llama_model_load_internal: n_rot      = 128
llama_model_load_internal: n_gqa      = 1
llama_model_load_internal: rnorm_eps  = 5.0e-06
llama_model_load_internal: n_ff       = 13824
llama_model_load_internal: freq_base  = 10000.0
llama_model_load_internal: freq_scale = 1
llama_model_load_internal: ftype      = 2 (mostly Q4_0)
llama_model_load_internal: model size = 13B
llama_model_load_internal: ggml ctx size =    0.11 MB
llama_model_load_internal: mem required  = 6983.72 MB (+  400.00 MB per state)
llama_model_load_internal: format     = ggjt v3 (latest)
llama_model_load_internal: n_vocab    = 32000
llama_model_load_internal: n_ctx      = 512
llama_model_load_internal: n_embd     = 5120
llama_model_load_internal: n_mult     = 256
llama_model_load_internal: n_head     = 40
llama_model_load_internal: n_head_kv  = 40
llama_model_load_internal: n_layer    = 40
llama_model_load_internal: n_rot      = 128
llama_model_load_internal: n_gqa      = 1
llama_model_load_internal: rnorm_eps  = 5.0e-06
llama_model_load_internal: n_ff       = 13824
llama_model_load_internal: freq_base  = 10000.0
llama_model_load_internal: freq_scale = 1
llama_model_load_internal: ftype      = 2 (mostly Q4_0)
llama_model_load_internal: model size = 13B
llama_model_load_internal: ggml ctx size =    0.11 MB
llama_model_load_internal: mem required  = 6983.72 MB (+  400.00 MB per state)
llama_model_load_internal: format     = ggjt v3 (latest)
llama_model_load_internal: n_vocab    = 32000
llama_model_load_internal: n_ctx      = 512
llama_model_load_internal: n_embd     = 5120
llama_model_load_internal: n_mult     = 256
llama_model_load_internal: n_head     = 40
llama_model_load_internal: n_head_kv  = 40
llama_model_load_internal: n_layer    = 40
llama_model_load_internal: n_rot      = 128
llama_model_load_internal: n_gqa      = 1
llama_model_load_internal: rnorm_eps  = 5.0e-06
llama_model_load_internal: n_ff       = 13824
llama_model_load_internal: freq_base  = 10000.0
llama_model_load_internal: freq_scale = 1
llama_model_load_internal: ftype      = 2 (mostly Q4_0)
llama_model_load_internal: model size = 13B
llama_model_load_internal: ggml ctx size =    0.11 MB
llama_model_load_internal: mem required  = 6983.72 MB (+  400.00 MB per state)
llama_new_context_with_model: kv self size  =  400.00 MB
llama_new_context_with_model: compute buffer total size =   75.35 MB
llama_new_context_with_model: kv self size  =  400.00 MB
llama_new_context_with_model: compute buffer total size =   75.35 MB
llama_new_context_with_model: kv self size  =  400.00 MB
llama_new_context_with_model: compute buffer total size =   75.35 MB

system_info: n_threads = 4 / 4 | AVX = 0 | AVX2 = 0 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | FMA = 0 | NEON = 1 | ARM_FMA = 1 | F16C = 0 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 0 | SSE3 = 0 | VSX = 0 | 
sampling: repeat_last_n = 64, repeat_penalty = 1.100000, presence_penalty = 0.000000, frequency_penalty = 0.000000, top_k = 40, tfs_z = 1.000000, top_p = 0.950000, typical_p = 1.000000, temp = 0.800000, mirostat = 0, mirostat_lr = 0.100000, mirostat_ent = 5.000000
generate: n_ctx = 512, n_batch = 512, n_predict = 128, n_keep = 0


 Raspberry Pi computers are 21st century classics
Raspberry Pi has become a classic in the world of computing, as it was one of the first single-board computers to make waves when it came out back in 2012. In fact, you can say that if Steve Jobs were alive today, he would probably buy hundreds of thousands of Raspberry Pi computers and give them out to people who are considered to be "at risk". The idea is that you'd use the computer for everything from social media to playing Minecraft.
This type of computing is known as “educational computing”, as it was
llama_print_timings:        load time = 17766.29 ms
llama_print_timings:      sample time =   264.42 ms /   128 runs   (    2.07 ms per token,   484.07 tokens per second)
llama_print_timings: prompt eval time = 10146.71 ms /     8 tokens ( 1268.34 ms per token,     0.79 tokens per second)
llama_print_timings:        eval time = 287157.12 ms /   127 runs   ( 2261.08 ms per token,     0.44 tokens per second)
llama_print_timings:       total time = 297598.22 ms
```

# 65B

Slurm job:

```
sub_65b.sh 
#!/bin/bash
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=4

cd $SLURM_SUBMIT_DIR

echo "Master node: $(hostname)"

mpirun -hostfile /clusterfs/Projects/llama.cpp/hostfile -n 3 /clusterfs/Projects/llama.cpp/main -m /home/cameron/models/llama-65b.ggmlv3.q4_0.bin -p "Why do we have to sleep?" -n 128
```

running and output ( 16 Aug 10:20 ):

```
cameron@rp3n0:/clusterfs/Projects$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
rp4*         up   infinite      3  alloc rp4n[0-2]
cameron@rp3n0:/clusterfs/Projects$ cat slurm-22.out 
Master node: rp4n0
main: build = 975 (9ca4abe)
main: seed  = 1692118354
main: build = 975 (9ca4abe)
main: seed  = 1692118354
main: build = 975 (9ca4abe)
main: seed  = 1692118354
llama.cpp: loading model from /home/cameron/models/llama-65b.ggmlv3.q4_0.bin
llama.cpp: loading model from /home/cameron/models/llama-65b.ggmlv3.q4_0.bin
llama.cpp: loading model from /home/cameron/models/llama-65b.ggmlv3.q4_0.bin
llama_model_load_internal: format     = ggjt v3 (latest)
llama_model_load_internal: n_vocab    = 32000
llama_model_load_internal: n_ctx      = 512
llama_model_load_internal: n_embd     = 8192
llama_model_load_internal: n_mult     = 256
llama_model_load_internal: n_head     = 64
llama_model_load_internal: n_head_kv  = 64
llama_model_load_internal: n_layer    = 80
llama_model_load_internal: n_rot      = 128
llama_model_load_internal: n_gqa      = 1
llama_model_load_internal: rnorm_eps  = 5.0e-06
llama_model_load_internal: n_ff       = 22016
llama_model_load_internal: freq_base  = 10000.0
llama_model_load_internal: freq_scale = 1
llama_model_load_internal: ftype      = 2 (mostly Q4_0)
llama_model_load_internal: model size = 65B
llama_model_load_internal: ggml ctx size =    0.21 MB
llama_model_load_internal: mem required  = 35026.50 MB (+ 1280.00 MB per state)
llama_model_load_internal: format     = ggjt v3 (latest)
llama_model_load_internal: n_vocab    = 32000
llama_model_load_internal: n_ctx      = 512
llama_model_load_internal: n_embd     = 8192
llama_model_load_internal: n_mult     = 256
llama_model_load_internal: n_head     = 64
llama_model_load_internal: n_head_kv  = 64
llama_model_load_internal: n_layer    = 80
llama_model_load_internal: n_rot      = 128
llama_model_load_internal: n_gqa      = 1
llama_model_load_internal: rnorm_eps  = 5.0e-06
llama_model_load_internal: n_ff       = 22016
llama_model_load_internal: freq_base  = 10000.0
llama_model_load_internal: freq_scale = 1
llama_model_load_internal: ftype      = 2 (mostly Q4_0)
llama_model_load_internal: model size = 65B
llama_model_load_internal: ggml ctx size =    0.21 MB
llama_model_load_internal: mem required  = 35026.50 MB (+ 1280.00 MB per state)
llama_model_load_internal: format     = ggjt v3 (latest)
llama_model_load_internal: n_vocab    = 32000
llama_model_load_internal: n_ctx      = 512
llama_model_load_internal: n_embd     = 8192
llama_model_load_internal: n_mult     = 256
llama_model_load_internal: n_head     = 64
llama_model_load_internal: n_head_kv  = 64
llama_model_load_internal: n_layer    = 80
llama_model_load_internal: n_rot      = 128
llama_model_load_internal: n_gqa      = 1
llama_model_load_internal: rnorm_eps  = 5.0e-06
llama_model_load_internal: n_ff       = 22016
llama_model_load_internal: freq_base  = 10000.0
llama_model_load_internal: freq_scale = 1
llama_model_load_internal: ftype      = 2 (mostly Q4_0)
llama_model_load_internal: model size = 65B
llama_model_load_internal: ggml ctx size =    0.21 MB
llama_model_load_internal: mem required  = 35026.50 MB (+ 1280.00 MB per state)
llama_new_context_with_model: kv self size  = 1280.00 MB
llama_new_context_with_model: compute buffer total size =  119.35 MB

system_info: n_threads = 4 / 4 | AVX = 0 | AVX2 = 0 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | FMA = 0 | NEON = 1 | ARM_FMA = 1 | F16C = 0 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 0 | SSE3 = 0 | VSX = 0 | 
sampling: repeat_last_n = 64, repeat_penalty = 1.100000, presence_penalty = 0.000000, frequency_penalty = 0.000000, top_k = 40, tfs_z = 1.000000, top_p = 0.950000, typical_p = 1.000000, temp = 0.800000, mirostat = 0, mirostat_lr = 0.100000, mirostat_ent = 5.000000
generate: n_ctx = 512, n_batch = 512, n_predict = 128, n_keep = 0


llama_new_context_with_model: kv self size  = 1280.00 MB
llama_new_context_with_model: compute buffer total size =  119.35 MB
llama_new_context_with_model: kv self size  = 1280.00 MB
llama_new_context_with_model: compute buffer total size =  119.35 MB
 Why do we have to sleep? That’s something that researchers are still trying to figure out. What they do know, however, is how a lack of quality sleep can affect your health and well-being. This includes more than just feeling tired the next day!
Without enough sleep, you may be at greater risk for heart disease and type 2 diabetes, as well as obesity. And while most people associate being drowsy with safety concerns such as driving while fatigued (see below), a new study has found that sleep deprivation may even put nurses’ patients in jeopardy!
The
llama_print_timings:        load time = 1446192.69 ms
llama_print_timings:      sample time =   281.36 ms /   128 runs   (    2.20 ms per token,   454.93 tokens per second)
llama_print_timings: prompt eval time = 592147.39 ms /     8 tokens (74018.42 ms per token,     0.01 tokens per second)
llama_print_timings:        eval time = 74540213.30 ms /   127 runs   (586930.81 ms per token,     0.00 tokens per second)
llama_print_timings:       total time = 75132679.76 ms

```

To Do:
- [x] Move all nodes to 1Gbit network
- [ ] Add Jetson Nano and VIM3 nodes, requires some version mindfulness:

- Jetson Nano base OS images are still on 18.04, but https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image 
- VIM3 images are on 20.04
- I could build from source on both, or rebase the Pis to 20.04 and only build the Nano from source, but I'd rather keep it uniform. ( scheduler has to be on the same version, so I can't run the weirdies as a partition unto themselves controlled by the same controller as the others, I tried )