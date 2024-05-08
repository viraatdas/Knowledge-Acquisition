

Core reference: https://github.com/viraatdas/llm.c/blob/master/train_gpt2.c 

1. **Header inclusion and Definitions**
```C
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdint.h>
#include <assert.h>
#include <math.h>
#include <time.h>
#include <string.h>
#include <unistd.h>
#ifdef OMP
#include <omp.h>
#endif
```

2. **Core Functions (Forward and Backward Passes)**

`encoder_forward` Function

```C
void encoder_forward(float* out,
                     int* inp, float* wte, float* wpe,
                     int B, int T, int C) {
    for (int b = 0; b < B; b++) {
        for (int t = 0; t < T; t++) {
            float* out_bt = out + b * T * C + t * C;
            int ix = inp[b * T + t];
            float* wte_ix = wte + ix * C;
            float* wpe_t = wpe + t * C;
            for (int i = 0; i < C; i++) {
                out_bt[i] = wte_ix[i] + wpe_t[i];
            }
        }
    }
}
```
#### Parameters:

- **out**: Output array where the embeddings will be stored.
- **inp**: Input array containing token indices.
- **wte**: [[Token embeddings matrix]]
	- each row corresponds to a unique token (word or subword) in the models vocabulary
- **wpe**: [[Positional embeddings matrix]]
- **B, T, C**: Dimensions representing Batch size, Sequence length, and Number of Channels (embedding dimension), respectively.