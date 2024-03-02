resource: https://pytorch.org/serve/large_model_inference.html
## How it works?

- `TorchServe` sets distributed environment
- Uses round-rzobin to assign GPUs to a worker on a host
  - in case of large inference, we can specify based on `model_config.yaml`
- `CUDA_VISIBLE_DEVICES` is based on this number

_ex:_

```
For instance, suppose there are eight GPUs on a node and one worker needs 4 GPUs (ie, nproc-per-node=4) on a node. In this case, TorchServe would assign CUDA_VISIBLE_DEVICES=”0,1,2,3” to worker1 and CUDA_VISIBLE_DEVICES=”4,5,6,7” to worker2.
```


Ways of running Torchserve:
- [[PiPPy integration]]
- [[Deepspeed]]
- [[gRPC server side streaming]]



