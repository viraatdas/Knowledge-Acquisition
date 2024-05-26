Source: https://arxiv.org/pdf/1706.03762

## Attention

### Scaled Dot-Production Attention

**Attention** function is described as mapping a query and a set of key-value pairs to an output. Output is a weighted sum of the values weighting assigned to each values is computated by a compatibility function of the query with the corresponding keys

**Details**:
- **Inputs**: The inputs to the attention mechanism are [[queries (Q), keys (K), and values (V)]]. These are all vectors. In the context of the Transformer, these vectors are usually outputs from the previous layer of the model.
- **Dot Products of Queries and Keys**: The first step in calculating attention is to find the dot products of the query with all keys. This represents a measure of compatibility or similarity, with higher values indicating greater compatibility.
- **Scaling**: Each dot product is scaled by the inverse square root of the dimension of the keys, $\frac{1}{\sqrt{d_k}}$. This scaling factor helps prevent the dot product values from growing too large in magnitude, which can lead to computational instability due to the [[Softmax]] function operating in regions where it has extremely small gradients.
- **Softmax**: Next, a softmax function is applied to the scaled dot products. This step converts the scores into probabilities that sum to one. The softmax essentially picks out the highest scores, magnifying their importance.
- **Output**: The output is computed as a weighted sum of the values V. Each value is weighted by the softmax score, ensuring that values corresponding to more compatible keys contribute more to the result.

**Equation**
$\text{Attention(Q,K,V)} = \text{softmax}(QK^T/\sqrt{d_k})V$

## Practical application in transformer
In the Transformer, this attention mechanism is used in three different ways:

1. **Encoder self-attention**: Each position in the encoder can attend to all positions in the previous layer of the encoder.
2. **Decoder self-attention**: Each position in the decoder can attend to all positions up to and including that position in the decoder, using masking to preserve causality.
3. **Encoder-decoder attention**: Queries from the decoder attend to all positions in the encoder.



