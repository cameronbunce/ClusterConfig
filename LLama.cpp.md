cd /clusterfs
mkdir Projects
cd Projects/
git clone https://github.com/ggerganov/llama.cpp

cameron@rp4n1:~$ cd /clusterfs/Projects/llama.cpp/
cameron@rp4n1:/clusterfs/Projects/llama.cpp$ make CC=mpicc CXX=mpicxx LLAMA_MPI=1

# 13B

#!/bin/bash
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=4

cd $SLURM_SUBMIT_DIR

echo "Master node: $(hostname)"

mpirun -hostfile /clusterfs/Projects/llama.cpp/hostfile -n 3 /clusterfs/Projects/llama.cpp/main -m /home/cameron/models/llama-13b.ggmlv3.q4_0.bin -p "Raspberry Pi computers are " -n 128


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


# 65B

sub_65b.sh 
#!/bin/bash
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=4

cd $SLURM_SUBMIT_DIR

echo "Master node: $(hostname)"

mpirun -hostfile /clusterfs/Projects/llama.cpp/hostfile -n 3 /clusterfs/Projects/llama.cpp/main -m /home/cameron/models/llama-65b.ggmlv3.q4_0.bin -p "Why do we have to sleep?" -n 128


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
 Why do we have to sleep? That’s something that researchers are still trying to figure out. What they do know