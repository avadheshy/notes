In APIs, idempotency is an important concept while implementing a payment system. An idempotent endpoint is one that can be called any number of times while guaranteeing that the side effects will occur only once. In terms of the payment system, it prevents multiple debits from the same account during failures.

The Problem
Let's discuss the problem first. Whenever we have payments in our system, we need to take care of various scenarios such as payment failures, request timeout and catastrophic events.

Let's say Client A is making a payment. Client A will make a request to a server for debit from his account. Now, there will be three scenarios,

Client A request got successful and payment successfully completed.

Client A Request got failed, before completing the transaction.

Client A request got failed, after completing the transaction.

Scenario (1) is also absolutely fine as the payment got successful and the money got debited from the client’s account. The server will give 200 response code and client will show payment successful.

Scenario (2) is absolutely fine as it got failed before the transaction. The server will give back the appropriate error code and message to the client and the client will reinitiate the payment.

Scenario (3) is a problem that we need to address. Here payment has been successfully processed and the money has been debited from the client’s account, But the request got failed after this, due to above mentioned reasons. So, the server will give error code in response to the client, the client will assume that payment got failed, hence will reinitiate the request and server will debit the money from the client’s account twice.

The Solution

In order to ensure a single debit occurs from the client’s account, the Server would need to know a lot about the use-cases of the client and maintain a state of a system on server side, which is not a scalable and appropriate solution. Instead, the client can provide a unique identifier for each unique interaction with the server. For example, if each payment request has a unique id, the Consumer can pass that id along with the payment request. The Server will then make sure it does not serve the same request twice.

In the above problem, let’s say client will make a payment request with an id, server completed the payment successfully and then the request got failed. Now the client will again retry the payment request with the same id, the server will check whether a request with the same id has been successfully completed or not, if it is it will not initiate the payment and if it's not it will complete the payment and send a response to the client appropriately.

The unique id that we send with every request if known as idempotency key.

# Real-World Examples
## 1. HTTP Methods
GET /users/123 → Always returns the same user data; idempotent.

PUT /users/123 → Replaces the user data with what is sent; sending it multiple times has the same result.

POST /users → Not idempotent; it creates a new user every time.

## 2. Bank Transfer System
Transferring ₹100 from A to B is not idempotent unless mechanisms ensure it's done only once.

Marking an order "delivered" is idempotent; even if the status update is retried, the final state is the same.

## 3. Message Queues
A consumer retries processing a message after failure.

If the operation is not idempotent (e.g., sending an SMS), it may duplicate the action.

If it's idempotent (e.g., "set order status to shipped"), retries are safe.

# Why Idempotency Matters
Network retries (timeouts, packet loss)

User refresh or resubmission (double-clicking "Pay")

Retry logic in microservices

Data consistency across replicas

# How to Ensure Idempotency
Use idempotency keys: unique identifiers for a request.

Use deduplication: store hashes or IDs of already-processed messages.

Design operations with overwrites instead of appends.

Use transactions or conditional updates.