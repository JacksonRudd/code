## Basic Chat App

This is a very basic chat application that can be used for reference.

## Lessons Learned

### 0.0.0.0 vs 127.0.0.1

We have to use 0.0.0.0 instead of 127.0.0.1 now that we are on the docker image.

Listening to 127.0.0.1 (localhost) on the server means the server only listens to requests originating from itself. Since the server is now separated from the client (since the client is not running on the same docker image), it won't be listening for the clients requests.

We fix this issue by getting the server to listen on 0.0.0.0 which means it accepts requests from all IPs.
