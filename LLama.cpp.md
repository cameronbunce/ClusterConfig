cd /clusterfs
mkdir Projects
cd Projects/
git clone https://github.com/ggerganov/llama.cpp

cameron@rp4n1:~$ cd /clusterfs/Projects/llama.cpp/
cameron@rp4n1:/clusterfs/Projects/llama.cpp$ make CC=mpicc CXX=mpicxx LLAMA_MPI=1



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