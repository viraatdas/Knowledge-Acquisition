resource: [[Gemini.pdf]]


## Model Architecture
- build on top of Transformer decoders
- Visual encoding was done based on the work of [[Flamingo]], [[Coca]], [[PaLI]]

- [[Video understanding]] is accomplished by encoding the video as a sequence of frames in the large context window. 
	- They can be interleaved naturally with text or audio as part of the model input
- Can also ingest audio signals at 16kHz from [[Universal Speech Model (USM)]]

## Training Infrastructure
