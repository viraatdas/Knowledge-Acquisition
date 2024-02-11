# Learning CUDA

https://docs.nvidia.com/cuda/cuda-c-programming-guide/

# Definition

- host: the CPU
- device: the GPU
- host memory: the system main memory
- device memory: onboard memory on a GPU card
- kernels: a GPU function launched by the host and executed on the device
- device function: a GPU function executed on the device which can only be called from the device (i.e. from a kernel or another device function)

## 1. Introduction

- **GPU Application**
  https://www.nvidia.com/en-us/gpu-accelerated-applications/
- FPGAs also energy efficient but don’t offer much programming flexibility

- GPU design for highly parallel computation. More transistors are devote to data processing.
  ![alt text](image.png)

## 2. CUDA: General Purpose Parallel Computing Platform and Programming Model

CUDA comes with a software environment that can use C++.
Also available are FORTRAN, DirectCompute, OpenACC.

![alt text](image-1.png)

## 3. Scalable Programming Model

- CUDA parallel programming is design to overcome parallelism problems for GPUs
- Three key abstractions:

  1. hierarchy of thread groups
  2. shared memories
  3. barrier synchronization

- Automatic scalability
  ![alt text](image-2.png)

- GPU is built around an array of [Streaming Multiprocessors (SMs)](#hardware-implementation)

## 4. Document Structure

_just describes document structure_

## 5. Programming Model

Full code for the [vector addition example](#vectorAdd-CUDA-sample)

### Kernels

CUDA C++ extends C++ by allowing programmer to define C++ functions called _kernels_, that when called, are executed N times in parallel by N different _CUDA threads_. This is opposed to only once like regular C++ functions.

- Kernel is defined using `__global__` declaration specifier and the number of CUDA threads that kernel for a given kernel call is specified using a new `<<<...>>> execution configuration` syntax.
- Each thread that executes the kernel is given a unique thread ID that is accessible within the kernel through built-in variables

_ex._
As an illustration, the following sample code, using the built-in variable threadIdx, adds two vectors A and B of size N and stores the result into vector C:

```cpp
∕∕ Kernel definition
__global__ void VecAdd(float* A, float* B, float* C) {

  int i = threadIdx.x;

  C[i] = A[i] + B[i];
}

int main() { ...

∕∕ Kernel invocation with N threads VecAdd<<<1, N>>>(A, B, C); ...

}
```

Here, each of the _N_ threads that execute `VecAdd(0` performs one pair-wise addition

### Thread Hierarchy

- A "thread block" refers to a group of threads that are executed
  simultaneously on the same processor or core. In parallel computing,
  threads are organized into blocks based on their access patterns and
  spatial locality. For example, in a vector processing algorithm, threads
  might be grouped into blocks based on the index of the vector element they
  are operating on.

- The relationship between a thread's index and its thread ID is
  straightforward:

  - For a one-dimensional block, the thread ID is simply the same as the
    thread index.
  - For a two-dimensional block of size (Dx, Dy), the thread ID of a thread
    of index (x, y) is (x + y Dx).
  - For a three-dimensional block of size (Dx, Dy, Dz), the thread ID of a
    thread of index (x, y, z) is (x + y Dx + z Dx Dy).

- In each case, the thread ID is calculated by adding the component of the
  index that corresponds to the dimension of the block in which the thread
  is executing. This allows threads to be addressed and communicated with
  within a block, as well as across blocks.

**What does it mean for a block to be a one-dimensional block?**
In the context of parallel computing, a "one-dimensional block" refers to
a block of threads where all threads are executed in a single dimension. In other words, all
threads within the block have the same index in that dimension.

For example, consider a vector processing algorithm that operates on vectors of length N. In
this case, each thread can be assigned an index from 0 to N-1, and all threads within a
block will have the same index in the same dimension (i.e., all threads within the block are
executing the same operation on the same position of the vector).

In this scenario, the thread ID calculation would be simple: for any thread within the
block, its thread ID is simply its index within the block. So, for example, if a thread with
index 2 is within a one-dimensional block of size 5, then its thread ID is 2.

One-dimensional blocks are useful when the access pattern and spatial locality of the
threads are well-defined in a single dimension. This allows for efficient parallelization
and coordination within the block, as all threads can be addressed and communicated with
using a simple index.

### `threadIdx`

3-component vector that represent the thread index within a block. Makes it natural to represent a vector, matrix, and volume (?).

In the CUDA programming model, `threadIdx` is a 3-component vector that represents the thread index within a block. The
three components are:

- `threadIdx.x`: The index of the thread in the one-dimensional dimension of the block. For a one-dimensional block,
  this is the same as the thread ID.
- `threadIdx.y`: The index of the thread in the two-dimensional dimension of the block (if the block size is greater
  than 1).
- `threadIdx.z`: The index of the thread in the three-dimensional dimension of the block (if the block size is greater
  than 2).

The relationship between `threadIdx` and the thread ID is straightforward: For a one-dimensional block, `threadIdx` and
`threadID` are the same; for a two-dimensional block of size `(Dx, Dy)`, `threadIdx.y` represents the thread ID of a
thread of index `(x, y)` as `(x + y * Dx)`. For a three-dimensional block of size `(Dx, Dy, Dz)`, `threadIdx.z`
represents the thread ID of a thread of index `(x, y, z)` as `(x + y * Dx + z * Dx * Dy)`.

The `threadIdx` vector is used to identify threads within a block, and it is used in conjunction with the `blockDim`
vector to access threads within a block. The `blockDim` vector represents the size of the block in each dimension, and
it is used to calculate the index of a thread within the block.

The limit on the number of threads per block is due to the fact that all threads within a block must share the limited
memory resources of the same streaming multiprocessor core. On current GPUs, a thread block may contain up to 1024
threads. However, multiple equally-shaped thread blocks can be executed simultaneously, allowing the total number of
threads to be equal to the number of threads per block in each dimension.

Cooperative groups are used to enable efficient cooperation among threads within a block. Shared memory is expected to
be a low-latency memory near each processor core (much like an L1 cache), and `__syncthreads()` is expected to be
lightweight. Cooperative groups provide a rich set of thread-synchronization primitives that can be used to coordinate
memory accesses among threads within a block.

**Streaming multiprocessor core**

### Thread block clusters

## Programming Interface

### Compilation with nvcc

- Kernels can be written using the CUDA instruction set architecture called `PTX`.
- More effective to use high-level programming language such as C++
- Both cases, kernels must be compiled into binary code by `nvcc` to execute on device

### nvcc

- compiler drive to simplify process of compiling C++ or PTX code

Link `nvcc` user manual (?)

**Compilation workflow**

1. **Offline compilation**

- nvcc basic workflow consists of separate GPU code from CPU code and then:
  1. Compiling GPU code into PTX code and/or binary form (`cubin` (?) object)
  2. modifying host code by replacing the `<<<...>>>` by necessary CUDA runtime function calls to load and launch each compiled kernel from the `PTX` code and/or `cubin` object

The modified host code is output either as C++ code that is left to be compiled using another tool or as object code directly by letting nvcc invoke the host compiler during the last compilation stage (NOTE: can this be made efficient? (?))

Applications can then:

- either link to the compiled host code (this is the most common use case)
- Or ignore the modified host code (if any) and use the [CUDA driver API](#driver-api) to load and execute the PTX code or cubin object

2. **Just-in-Time Compilation**
