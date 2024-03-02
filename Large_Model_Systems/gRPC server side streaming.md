
- gRPC Remote Procedure Call
- Uses [[HTTP 2.0]], Protocol Buffers as the interface description language, and provides features such as authentication, load balancing, and more

## Server-side Streaming RPC

**What**
- Client sends a single request to server and receives a stream of responses

**How it works?**
1. **Client Call**: The client initiates the RPC call by sending a single request to the server.

2. **Stream Initialization**: Upon receiving the request, the server starts processing and initializes a stream of responses.
    
3. **Data Streaming**: The server then sends multiple response messages back to the client over the established connection. These messages are sent as soon as they are ready, without waiting for all the responses to be generated. This is particularly useful for real-time data streaming or when the full set of responses is not immediately available.
    
4. **Completion**: Once all the response messages have been sent, the server signals the end of the stream to the client. The client then closes the connection.




