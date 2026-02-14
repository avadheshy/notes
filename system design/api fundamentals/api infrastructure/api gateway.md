# API Gateways ?
APIs, or Application Programming Interfaces, are a set of rules and protocols that allows two software applications or services to communicate with each other.

An API Gateway acts as a central server that sits between clients (e.g., browsers, mobile apps) and backend services.

Instead of clients interacting with multiple microservices directly, they send their requests to the API Gateway. The gateway processes these requests, enforces security, and forwards them to the appropriate microservices.

# 1. Why Do We Need an API Gateway?
Modern applications, especially those built using microservices architecture, have multiple backend services managing different functionalities.

**Without an API Gateway:**
Clients would need to know the location and details of all backend services.

Developers would need to manage authentication, rate limiting, and security for each service individually.

**With an API Gateway:**
Clients send all requests to one place – the API Gateway.

The API Gateway takes care of routing, authentication, security, and other operational tasks, simplifying both client interactions and backend management.

# 2. Core Features of an API Gateway
1. Authentication and Authorization
API Gateway secures the backend systems by ensuring only authorized users and clients can access backend services.

It handles tasks like:

Authentication: Verifying the identity of the client using tokens (e.g., OAuth, JWT), API keys, or certificates.
Authorization: Checking the client’s permissions to access specific services or resources.
By centralizing these tasks, the API gateway eliminates the need for individual services to handle authentication, reducing redundancy and ensuring consistent access control across the system.

2. Rate Limiting
To prevent abuse and ensure fair usage of resources, most API Gateways implement rate limiting.

This feature:

Controls the frequency of requests a client can make within a given timeframe.
Protects backend services from being overwhelmed by excessive traffic or potential denial-of-service (DoS) attacks.
For example, a public API might allow a maximum of 100 requests per minute per user. If a client exceeds this limit, the API Gateway will block additional requests until the rate resets.

3. Load Balancing
High-traffic applications rely on load balancing to distribute incoming requests evenly across multiple instances of a service.

The API Gateway can:

Redirect requests to healthy service instances while avoiding ones that are down or overloaded.
Use algorithms like round-robin, least connections, or weighted distribution to manage traffic intelligently.
4. Caching
To improve response times and reduce the strain on backend services, most API Gateways provide caching.

They temporarily store frequently requested data, such as:

Responses to commonly accessed endpoints (e.g., product catalogs or weather data).
Static resources like images or metadata.
Caching helps in reducing latency and enhancing user experience while lowering the operational cost of backend services.

5. Request Transformation
In systems with diverse clients and backend services, request transformation is essential for compatibility.

An API Gateway can:

Modify the structure or format of incoming requests to match the backend service requirements.
Transform responses before sending them back to the client, ensuring they meet the client’s expectations.
For instance, it might convert XML responses from a legacy service into JSON for modern frontend applications.

6. Service Discovery
Modern systems often involve microservices that scale dynamically.

The service discovery feature of an API Gateway dynamically identifies the appropriate backend service instance to handle each request.

This ensures seamless request routing even in environments where services frequently scale up or down.

7. Circuit Breaking
Circuit breaking is a mechanism that temporarily stops sending requests to a backend service when it detects persistent failures, such as:

Slow responses or timeouts.
Server errors (e.g., HTTP 500 status codes).
High latency or unavailability of a service.
The API Gateway continuously monitors the health and performance of backend services and uses circuit breaking to block requests to a failing service.

8. Logging and Monitoring
API Gateways provide robust monitoring and logging capabilities to track and analyze system behavior.

These capabilities include:

Logging detailed information about each request, such as source, destination, and response time.
Collecting metrics like request rates, error rates, and latency.
This data helps system administrators detect anomalies, troubleshoot issues, and optimize the system’s performance. Many API Gateways also integrate with monitoring tools like Prometheus, Grafana, or AWS CloudWatch.

# 3. How Does an API Gateway Work?
Imagine you're using a food delivery app to order dinner. When you tap "Place Order" your phone makes an API request. But instead of talking directly to various backend services, it communicates with an API Gateway first.

## Step 1: Request Reception
When you tap "Place Order," the app sends a request to the API Gateway, asking it to process your order.

This request includes things like:

- Your user ID
- Selected restaurant and menu items
- Delivery address
- Payment method
- Authentication tokens

The API Gateway receives the request as the single entry point to the backend system.

## Step 2: Request Validation
Before forwarding the request, the API Gateway validates it to ensure:

- The required parameters or headers are present.
- The data is in the correct format (e.g., JSON).
- The request conforms to the expected structure or schema.
# Step 3: Authentication & Authorization
The gateway now verifies your identity and permissions to ensures only legitimate users can place orders:

It forwards your authentication token (e.g., OAuth or JWT) to an identity provider to confirm your identity.
It checks your permissions to ensure you’re authorized to use the app for placing an order.

## Step 4: Rate Limiting
To prevent abuse, the API Gateway checks how many requests you’ve made recently. For example:

If you’ve made 10 "Place Order" requests in the last minute (maybe by accident), the gateway might block additional requests temporarily and return 429 Too Many Requests response.

## Step 5: Request Transformation (if needed)
If any of these backend services require specific data formats or additional details, the API Gateway transforms the request.

## Step 6: Request Routing
The API Gateway now needs to coordinate several backend services to process your order.

Using service discovery, it identifies:

Order Service: To create a new order record.

Inventory Service: To check if the restaurant has your selected items available.

Payment Service: To process your payment.

Delivery Service: To assign a delivery driver to your order.

The gateway dynamically routes the request to these services using a load balancing algorithm, ensuring it connects to available and healthy service instances.


# Step 7: Response Handling
Once the API Gateway receives the response(s) from the backend service(s), it performs the following tasks:

Transformation: Adjusts the response format or structure to match the client’s requirements.
Caching (Optional): Stores the response temporarily for frequently accessed data, reducing future latency.

Finally, the API Gateway sends the processed response back to the client in a format they can easily understand.

## Step 8: Logging & Monitoring
Throughout this process, the gateway records important metrics to track each request: