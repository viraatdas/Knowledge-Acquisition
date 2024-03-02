resource: [[Gemini.pdf]]


## Model Architecture
- build on top of Transformer decoders
- Visual encoding was done based on the work of [[Flamingo]], [[Coca]], [[PaLI]]

- [[Video understanding]] is accomplished by encoding the video as a sequence of frames in the large context window. 
	- They can be interleaved naturally with text or audio as part of the model input
- Can also ingest audio signals at 16kHz from [[Universal Speech Model (USM)]]

## Training Infrastructure
- trained on [[TPUv5e]] and [[TPUv4]]

**TPUv4**
TPUv4 accelerators are deployed in "SuperPPods" of [[4096 chips]], each connected to a dedicated [[optical switch]], which can dynamically reconfogire `4x4x4` chip cubes into arbitrary 3d torus topologies in around 10 seconds. 


TPU acclerators communicate over high spped inter-chip-interconnect, but at Gemini ultra scale, we combine SuperPods in multiple datacenters using Google's intra-cluster and inter-cluster network. 