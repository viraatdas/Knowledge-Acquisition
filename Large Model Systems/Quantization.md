Converting a model from using FP (like 32-bit floats) to using lower-precision formats (like 8-bit integers). 

## How does quantization work?
1. [[Post-Training Static quantization]]: Entire model including weights and activations are converted to lower precision. Model is calibrated using a small calibration dataset to minimize the impact on accuracy. May not always have best accuracy. 
2. [[Dynamic Quantization]]: Weights quantized statically, but activations are quantized dynamocally at runtime. Method is often used for models wehre activation ranges can vary significantly depending on the input data. 
3. Quantization-Aware Training (QAT):