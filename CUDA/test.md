# Learning CUDA

https://docs.nvidia.com/cuda/cuda-c-programming-guide/

# Definition

- host: the CPU
- device: the GPU
- host memory: the system main memory
- device memory: onboard memory on a GPU card
- kernels: a GPU function launched by the host and executed on the device
- device function: a GPU function executed on the device which can only be called from the device (i.e. from a kernel or another device function)
