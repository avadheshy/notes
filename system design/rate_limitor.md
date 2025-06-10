# whar is rate limiter
A Rate Limiter limits the number of client requests allowed to be sent over a specified period. If the API request count exceeds the threshold defined by the rate limiter, all the excess calls are blocked.

# Benefits:

A rate limiter prevents DoS attacks, intentional or unintentional, by blocking the excess calls.

Reduces cost where the system is using a 3rd-party API service and is charged on a per-call-basis.

To reduce server load, a rate limiter is used to filter out excess requests caused by bots or users’ misbehaviour.

It mainly depends upon our application, tech stack, tech-team etc, where exactly we want the rate-limiter to be implemented. We have generally 3 places: Client-side, Server-side, or middleware.

The client is an unreliable place to enforce rate limiting because client requests can easily be forged by malicious actors.

Even better than placing it on the server side is to use a rate limiter middleware, which will throttle excess requests even to our server side. So, if you are using a microservice architecture and already using functionalities like authentication middleware, a similar basis you can implement rate limiter middleware alongside it.

# Token Bucket Algorithm
We use the token bucket algorithm to do rate limiting. This algorithm has a centralized bucket host where you take tokens on each request, and slowly drip more tokens into the bucket. If the bucket is empty, reject the request. In our case, every Stripe user has a bucket, and every time they make a request we remove a token from that bucket. We implement our rate limiters using Redis.

# In simple words:

In the Token Bucket algorithm, we process a token from the bucket for every request. New tokens are added to the bucket with rate r. The bucket can hold a maximum of b tokens. If a request comes and the bucket is full it is discarded.

The token bucket algorithm takes two parameters:

Bucket size: the maximum number of tokens allowed in the bucket
Refill rate: number of tokens put into the bucket every second

# Leaky Bucket Algorithm
Leaky Bucket is a simple and intuitive way to implement rate limiting using a queue. It is a simple first-in, first-out queue (FIFO). Incoming requests are appended to the queue and if there is no room for new requests they are discarded (leaked).

When a request arrives, the system checks if the queue is full. If it is not full, the request is added to the queue.
Otherwise, the request is dropped.
Requests are pulled from the queue and processed at regular intervals.

The leaking bucket algorithm takes the following two parameters:

Bucket size: it is equal to the queue size. The queue holds the requests to be processed at a fixed rate.

Outflow rate: it defines how many requests can be processed at a fixed rate, usually in seconds.

# Sliding Window Algorithm
The algorithm keeps track of request timestamps. Timestamp data is usually kept in cache, such as sorted sets of Redis.
When a new request comes in, remove all the outdated timestamps. Outdated timestamps are defined as those older than the start of the current time window.

Add timestamp of the new request to the log.
If the log size is the same or lower than the allowed count, a request is accepted. Otherwise, it is rejected.
