# System Design Interview Questions & Answers

## Table of Contents
1. [URL Shortener (like bit.ly)](#1-url-shortener-like-bitly)
2. [Chat System (like WhatsApp)](#2-chat-system-like-whatsapp)
3. [Social Media Feed (like Twitter)](#3-social-media-feed-like-twitter)
4. [Video Streaming Platform (like YouTube)](#4-video-streaming-platform-like-youtube)
5. [Ride Sharing Service (like Uber)](#5-ride-sharing-service-like-uber)
6. [Search Engine (like Google)](#6-search-engine-like-google)
7. [Notification System](#7-notification-system)
8. [Rate Limiter](#8-rate-limiter)
9. [Distributed Cache](#9-distributed-cache)
10. [Load Balancer Design](#10-load-balancer-design)

---

## 1. URL Shortener (like bit.ly)

### Requirements
- **Functional**: Shorten long URLs, redirect to original URL, custom aliases, expiration
- **Non-functional**: 100:1 read/write ratio, 500M URLs/month, low latency (<100ms)
- **Scale**: 100M users, 50B redirects/month

### High-Level Design
```
Client → Load Balancer → Web Servers → Application Servers → Database
                                    ↘ Cache (Redis)
```

### Detailed Components

#### Database Schema
```sql
-- URLs table
CREATE TABLE urls (
    id BIGINT PRIMARY KEY,
    short_url VARCHAR(7) UNIQUE,
    long_url TEXT NOT NULL,
    user_id BIGINT,
    created_at TIMESTAMP,
    expires_at TIMESTAMP,
    click_count INT DEFAULT 0
);

-- Users table
CREATE TABLE users (
    id BIGINT PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    created_at TIMESTAMP
);
```

#### URL Encoding Algorithm
**Base62 Encoding** (a-z, A-Z, 0-9 = 62 characters)
- 7 characters = 62^7 = ~3.5 trillion combinations
- Use counter-based approach or hash-based approach

#### Implementation Steps
1. **Encode Algorithm**:
   ```python
   def encode(id):
       chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
       result = ""
       while id > 0:
           result = chars[id % 62] + result
           id //= 62
       return result.zfill(7)
   ```

2. **Database Sharding**: Shard by short_url hash
3. **Caching Strategy**: Cache popular URLs in Redis (80/20 rule)
4. **Rate Limiting**: Prevent spam, limit requests per user

#### Scalability Considerations
- **Read Replicas**: For high read traffic
- **CDN**: Cache popular redirects globally
- **Database Partitioning**: Horizontal sharding
- **Analytics**: Separate service for click tracking

---

## 2. Chat System (like WhatsApp)

### Requirements
- **Functional**: Send/receive messages, online status, group chats, message history
- **Non-functional**: Real-time delivery, 50M DAU, 99.9% availability
- **Scale**: 1B messages/day, support 100K concurrent users

### High-Level Architecture
```
Client ← WebSocket → API Gateway → Chat Service → Message Queue → Database
                                        ↓
                                 Notification Service
```

### Detailed Components

#### Database Design
```sql
-- Messages table (partitioned by chat_id)
CREATE TABLE messages (
    id BIGINT PRIMARY KEY,
    chat_id BIGINT,
    sender_id BIGINT,
    content TEXT,
    message_type ENUM('text', 'image', 'file'),
    timestamp TIMESTAMP,
    is_deleted BOOLEAN DEFAULT FALSE
);

-- Chats table
CREATE TABLE chats (
    id BIGINT PRIMARY KEY,
    type ENUM('direct', 'group'),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- Chat participants
CREATE TABLE chat_participants (
    chat_id BIGINT,
    user_id BIGINT,
    joined_at TIMESTAMP,
    role ENUM('admin', 'member'),
    PRIMARY KEY (chat_id, user_id)
);
```

#### Real-time Communication
- **WebSocket Connections**: Maintain persistent connections
- **Connection Management**: Handle connection drops, reconnection
- **Message Delivery**: 
  - Online users: Direct WebSocket delivery
  - Offline users: Push notifications + store in message queue

#### Message Flow
1. User sends message via WebSocket
2. API Gateway validates and routes to Chat Service
3. Chat Service stores message in database
4. Message queued for delivery to recipients
5. Online recipients receive via WebSocket
6. Offline recipients get push notification

#### Scalability Solutions
- **Horizontal Scaling**: Multiple chat service instances
- **Database Sharding**: Partition by chat_id or user_id
- **Message Queue**: Apache Kafka for reliable message delivery
- **Presence Service**: Separate service for online/offline status

---

## 3. Social Media Feed (like Twitter)

### Requirements
- **Functional**: Post tweets, follow users, timeline generation, like/retweet
- **Non-functional**: 300M MAU, 400M tweets/day, timeline load <200ms
- **Scale**: 200M timeline requests/day, heavy read workload

### Architecture Patterns

#### Pull Model (Timeline Generation on Read)
```
User Request → Timeline Service → Follow Graph → Tweet Service → Database
```
**Pros**: Less storage, real-time updates
**Cons**: Slow for users following many people

#### Push Model (Timeline Pre-computation)
```
New Tweet → Fanout Service → Timeline Cache → User Timelines
```
**Pros**: Fast timeline loading
**Cons**: High storage for celebrities with millions of followers

#### Hybrid Approach (Recommended)
- **Push**: For normal users (<1M followers)
- **Pull**: For celebrities (>1M followers)
- **Mixed**: Combine pre-computed + real-time for optimal performance

### Database Schema
```sql
-- Users table
CREATE TABLE users (
    id BIGINT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    follower_count INT DEFAULT 0,
    following_count INT DEFAULT 0
);

-- Tweets table (partitioned by created_at)
CREATE TABLE tweets (
    id BIGINT PRIMARY KEY,
    user_id BIGINT,
    content VARCHAR(280),
    created_at TIMESTAMP,
    like_count INT DEFAULT 0,
    retweet_count INT DEFAULT 0
);

-- Follows table (partitioned by follower_id)
CREATE TABLE follows (
    follower_id BIGINT,
    followee_id BIGINT,
    created_at TIMESTAMP,
    PRIMARY KEY (follower_id, followee_id)
);

-- Timeline cache (Redis)
user:{user_id}:timeline → [tweet_id1, tweet_id2, ...]
```

#### Timeline Generation Algorithm
```python
def generate_timeline(user_id, limit=20):
    # Get users that this user follows
    following = get_following_list(user_id)
    
    # For celebrities, pull latest tweets
    celebrity_tweets = []
    for celebrity in get_celebrities(following):
        celebrity_tweets.extend(get_recent_tweets(celebrity, limit=5))
    
    # Get pre-computed timeline for normal users
    cached_timeline = redis.get(f"user:{user_id}:timeline")
    
    # Merge and sort by timestamp
    timeline = merge_and_sort(cached_timeline, celebrity_tweets)
    return timeline[:limit]
```

---

## 4. Video Streaming Platform (like YouTube)

### Requirements
- **Functional**: Upload videos, stream videos, search, recommendations
- **Non-functional**: 2B hours watched/month, support 4K video, global CDN
- **Scale**: 500 hours uploaded/minute, 1B users

### High-Level Architecture
```
Client → CDN → Load Balancer → API Gateway → Microservices
                                                ↓
Video Storage (AWS S3) ← Video Processing Service → Database
```

### Core Components

#### Video Upload Flow
1. **Upload Service**: Handles large file uploads (chunked)
2. **Video Processing Pipeline**:
   - Transcoding (multiple resolutions: 360p, 720p, 1080p, 4K)
   - Thumbnail generation
   - Metadata extraction
3. **Storage**: Distributed file system (AWS S3, Google Cloud Storage)
4. **CDN Distribution**: Replicate to global edge servers

#### Database Design
```sql
-- Videos table
CREATE TABLE videos (
    id BIGINT PRIMARY KEY,
    user_id BIGINT,
    title VARCHAR(255),
    description TEXT,
    duration INT, -- in seconds
    view_count BIGINT DEFAULT 0,
    upload_date TIMESTAMP,
    video_url VARCHAR(500),
    thumbnail_url VARCHAR(500),
    status ENUM('processing', 'ready', 'failed')
);

-- Video metadata for different resolutions
CREATE TABLE video_files (
    id BIGINT PRIMARY KEY,
    video_id BIGINT,
    resolution ENUM('360p', '720p', '1080p', '4K'),
    file_url VARCHAR(500),
    file_size BIGINT
);
```

#### Video Streaming Optimization
- **Adaptive Bitrate Streaming**: Adjust quality based on network
- **Content Delivery Network**: Global distribution for low latency
- **Video Compression**: H.264/H.265 codecs
- **Preloading**: Load first few seconds immediately

#### Recommendation System
```python
# Collaborative Filtering + Content-Based
def recommend_videos(user_id):
    # User's watch history
    watch_history = get_user_watch_history(user_id)
    
    # Similar users (collaborative filtering)
    similar_users = find_similar_users(user_id)
    
    # Content-based (similar videos)
    content_recommendations = get_similar_videos(watch_history)
    
    # Combine and rank
    recommendations = combine_recommendations(
        collaborative_score * 0.6 + content_score * 0.4
    )
    
    return recommendations
```

---

## 5. Ride Sharing Service (like Uber)

### Requirements
- **Functional**: Request rides, match drivers, real-time tracking, payments
- **Non-functional**: 100M users, 1M drivers, <30s matching time
- **Scale**: Support 1M concurrent rides

### Architecture
```
Mobile Apps → API Gateway → Location Service → Matching Service → Trip Service
                                ↓                    ↓
                         Geospatial DB    →    Notification Service
```

### Core Services

#### Location Service
- **Real-time Tracking**: Drivers send location every 5 seconds
- **Geospatial Database**: PostGIS or Redis with geo-commands
- **Location Storage**:
```sql
-- Driver locations (in-memory for active drivers)
CREATE TABLE driver_locations (
    driver_id BIGINT PRIMARY KEY,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    updated_at TIMESTAMP,
    status ENUM('available', 'busy', 'offline')
);
```

#### Matching Algorithm
```python
def find_nearby_drivers(pickup_lat, pickup_lng, radius_km=5):
    # Use geospatial query
    query = """
    SELECT driver_id, latitude, longitude,
           ST_Distance_Sphere(
               POINT(longitude, latitude),
               POINT(%s, %s)
           ) as distance
    FROM driver_locations 
    WHERE status = 'available'
    AND ST_Distance_Sphere(
        POINT(longitude, latitude),
        POINT(%s, %s)
    ) <= %s * 1000
    ORDER BY distance
    LIMIT 10
    """
    return execute_query(query, pickup_lng, pickup_lat, pickup_lng, pickup_lat, radius_km)

def match_ride(ride_request):
    nearby_drivers = find_nearby_drivers(
        ride_request.pickup_lat, 
        ride_request.pickup_lng
    )
    
    # Send requests to top 5 drivers
    for driver in nearby_drivers[:5]:
        send_ride_request(driver.id, ride_request)
        
    # Wait for acceptance (with timeout)
    return wait_for_driver_acceptance(timeout=30)
```

#### Database Schema
```sql
-- Rides table
CREATE TABLE rides (
    id BIGINT PRIMARY KEY,
    rider_id BIGINT,
    driver_id BIGINT,
    pickup_lat DECIMAL(10, 8),
    pickup_lng DECIMAL(11, 8),
    dropoff_lat DECIMAL(10, 8),
    dropoff_lng DECIMAL(11, 8),
    status ENUM('requested', 'accepted', 'started', 'completed', 'cancelled'),
    fare DECIMAL(10, 2),
    created_at TIMESTAMP
);
```

#### Scalability Considerations
- **Geospatial Partitioning**: Divide by geographic regions
- **Real-time Updates**: WebSocket connections for live tracking
- **Load Balancing**: Route by geographic region
- **Caching**: Cache driver locations in Redis

---

## 6. Search Engine (like Google)

### Requirements
- **Functional**: Web crawling, indexing, search queries, ranking
- **Non-functional**: Index 50B pages, <200ms search response, 40K QPS
- **Scale**: Crawl 20B pages/day, 8.5B searches/day

### Architecture Overview
```
Web Crawler → Document Processor → Indexer → Search Service ← Query Processor
     ↓              ↓                 ↓           ↑
URL Queue → Content Store → Inverted Index → Ranking Service
```

### Core Components

#### Web Crawler
```python
class WebCrawler:
    def __init__(self):
        self.url_queue = Queue()
        self.visited_urls = set()
        self.robots_cache = {}
    
    def crawl(self):
        while not self.url_queue.empty():
            url = self.url_queue.get()
            
            if self.should_crawl(url):
                content = self.fetch_page(url)
                self.process_page(url, content)
                
                # Extract new URLs
                new_urls = self.extract_links(content)
                for new_url in new_urls:
                    if new_url not in self.visited_urls:
                        self.url_queue.put(new_url)
```

#### Inverted Index Structure
```python
# Inverted Index: word → list of documents containing the word
inverted_index = {
    "python": [
        {"doc_id": 1, "tf": 5, "positions": [10, 25, 100, 150, 200]},
        {"doc_id": 15, "tf": 3, "positions": [5, 67, 89]},
        {"doc_id": 23, "tf": 8, "positions": [1, 12, 34, 56, 78, 90, 123, 145]}
    ],
    "programming": [
        {"doc_id": 1, "tf": 2, "positions": [15, 175]},
        {"doc_id": 8, "tf": 4, "positions": [22, 45, 67, 99]}
    ]
}
```

#### Ranking Algorithm (Simplified)
```python
def calculate_relevance_score(query_terms, document):
    score = 0
    
    # TF-IDF Score
    for term in query_terms:
        tf = document.term_frequency(term)
        idf = math.log(total_documents / documents_containing_term(term))
        score += tf * idf
    
    # PageRank Score
    pagerank_score = document.pagerank
    
    # Combined Score
    final_score = (score * 0.7) + (pagerank_score * 0.3)
    
    return final_score
```

#### Database Schema
```sql
-- Documents table
CREATE TABLE documents (
    id BIGINT PRIMARY KEY,
    url VARCHAR(2048) UNIQUE,
    title VARCHAR(512),
    content_hash VARCHAR(64),
    pagerank_score DECIMAL(10, 8),
    last_crawled TIMESTAMP
);

-- Inverted index (distributed across multiple tables/shards)
CREATE TABLE index_terms (
    term VARCHAR(100),
    doc_id BIGINT,
    term_frequency INT,
    positions TEXT, -- JSON array of positions
    PRIMARY KEY (term, doc_id)
);
```

---

## 7. Notification System

### Requirements
- **Functional**: Send push, email, SMS notifications, user preferences
- **Non-functional**: 100M notifications/day, 99.9% delivery rate
- **Scale**: Support multiple platforms (iOS, Android, Web)

### Architecture
```
Trigger Service → Notification Service → Message Queue → Delivery Workers
                        ↓                      ↓              ↓
                 User Preferences    →    Template Service → External APIs
                                                            (APNs, FCM, Twilio)
```

### Component Design

#### Notification Service Core
```python
class NotificationService:
    def send_notification(self, user_id, notification_type, data):
        # Get user preferences
        preferences = self.get_user_preferences(user_id)
        
        # Check if user wants this type of notification
        if not preferences.allows(notification_type):
            return False
            
        # Get delivery channels (push, email, SMS)
        channels = preferences.get_channels(notification_type)
        
        for channel in channels:
            # Create notification message
            message = self.create_message(channel, notification_type, data)
            
            # Queue for delivery
            self.message_queue.enqueue(channel, message)
        
        return True
```

#### Database Schema
```sql
-- Notifications table
CREATE TABLE notifications (
    id BIGINT PRIMARY KEY,
    user_id BIGINT,
    type VARCHAR(50),
    title VARCHAR(255),
    content TEXT,
    channels JSON, -- ['push', 'email', 'sms']
    status ENUM('pending', 'sent', 'delivered', 'failed'),
    created_at TIMESTAMP,
    sent_at TIMESTAMP
);

-- User preferences
CREATE TABLE user_notification_preferences (
    user_id BIGINT,
    notification_type VARCHAR(50),
    push_enabled BOOLEAN DEFAULT TRUE,
    email_enabled BOOLEAN DEFAULT TRUE,
    sms_enabled BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (user_id, notification_type)
);

-- Device tokens for push notifications
CREATE TABLE user_devices (
    id BIGINT PRIMARY KEY,
    user_id BIGINT,
    device_token VARCHAR(255),
    platform ENUM('ios', 'android', 'web'),
    is_active BOOLEAN DEFAULT TRUE
);
```

#### Delivery Strategy
- **Message Queue**: Apache Kafka or Amazon SQS
- **Rate Limiting**: Prevent spam, respect API limits
- **Retry Logic**: Exponential backoff for failed deliveries
- **Analytics**: Track delivery rates, open rates

---

## 8. Rate Limiter

### Requirements
- **Functional**: Limit requests per user/IP, different limits per API
- **Non-functional**: Low latency (<1ms), distributed system
- **Scale**: 1M requests/second, global rate limiting

### Algorithm Comparison

#### 1. Token Bucket
```python
class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.time()
    
    def allow_request(self):
        self.refill()
        if self.tokens > 0:
            self.tokens -= 1
            return True
        return False
    
    def refill(self):
        now = time.time()
        tokens_to_add = (now - self.last_refill) * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill = now
```

#### 2. Sliding Window Log
```python
class SlidingWindowLog:
    def __init__(self, limit, window_size):
        self.limit = limit
        self.window_size = window_size
        self.requests = []
    
    def allow_request(self):
        now = time.time()
        # Remove old requests outside window
        self.requests = [req for req in self.requests if now - req < self.window_size]
        
        if len(self.requests) < self.limit:
            self.requests.append(now)
            return True
        return False
```

#### 3. Sliding Window Counter (Recommended)
```python
class SlidingWindowCounter:
    def __init__(self, limit, window_size, num_buckets=10):
        self.limit = limit
        self.window_size = window_size
        self.num_buckets = num_buckets
        self.bucket_size = window_size / num_buckets
        self.buckets = [0] * num_buckets
        self.last_update = time.time()
    
    def allow_request(self):
        now = time.time()
        self.update_buckets(now)
        
        total_requests = sum(self.buckets)
        if total_requests < self.limit:
            current_bucket = int((now % self.window_size) / self.bucket_size)
            self.buckets[current_bucket] += 1
            return True
        return False
```

### Distributed Rate Limiter Architecture
```
Client → Load Balancer → Rate Limiter Service → Redis Cluster → Backend Service
```

#### Redis-based Implementation
```python
def is_request_allowed(user_id, limit, window):
    key = f"rate_limit:{user_id}"
    current_time = int(time.time())
    
    # Sliding window with Redis sorted sets
    pipeline = redis.pipeline()
    
    # Remove expired entries
    pipeline.zremrangebyscore(key, 0, current_time - window)
    
    # Count current requests
    pipeline.zcard(key)
    
    # Add current request
    pipeline.zadd(key, {str(uuid.uuid4()): current_time})
    
    # Set expiration
    pipeline.expire(key, window)
    
    results = pipeline.execute()
    current_requests = results[1]
    
    return current_requests < limit
```

---

## 9. Distributed Cache

### Requirements
- **Functional**: Get/Set operations, TTL support, cache eviction
- **Non-functional**: <1ms latency, 99.9% availability, auto-scaling
- **Scale**: 1M QPS, TB of data, geographic distribution

### Architecture
```
Client → Consistent Hashing → Cache Nodes (Redis/Memcached) → Database
              ↓
       Replication & Failover
```

### Key Components

#### Consistent Hashing
```python
import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self, nodes=None, replicas=3):
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []
        
        if nodes:
            for node in nodes:
                self.add_node(node)
    
    def add_node(self, node):
        for i in range(self.replicas):
            key = self.hash(f"{node}:{i}")
            self.ring[key] = node
            bisect.insort(self.sorted_keys, key)
    
    def remove_node(self, node):
        for i in range(self.replicas):
            key = self.hash(f"{node}:{i}")
            del self.ring[key]
            self.sorted_keys.remove(key)
    
    def get_node(self, key):
        if not self.ring:
            return None
            
        hash_key = self.hash(key)
        idx = bisect.bisect_right(self.sorted_keys, hash_key)
        
        if idx == len(self.sorted_keys):
            idx = 0
            
        return self.ring[self.sorted_keys[idx]]
    
    def hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)
```

#### Cache Client with Failover
```python
class DistributedCache:
    def __init__(self, nodes):
        self.hash_ring = ConsistentHashRing(nodes)
        self.connections = {node: RedisClient(node) for node in nodes}
    
    def get(self, key):
        node = self.hash_ring.get_node(key)
        try:
            return self.connections[node].get(key)
        except Exception:
            # Fallback to next node
            return self.get_with_fallback(key, excluded=[node])
    
    def set(self, key, value, ttl=None):
        node = self.hash_ring.get_node(key)
        try:
            # Write to primary node
            self.connections[node].set(key, value, ttl)
            
            # Async replication to backup nodes
            self.replicate_async(key, value, ttl, exclude=node)
            
        except Exception:
            # Try next available node
            self.set_with_fallback(key, value, ttl, excluded=[node])
```

#### Cache Eviction Policies
```python
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.access_order = OrderedDict()
    
    def get(self, key):
        if key in self.cache:
            # Move to end (most recently used)
            self.access_order.move_to_end(key)
            return self.cache[key]
        return None
    
    def set(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.access_order.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # Remove least recently used
                oldest_key = next(iter(self.access_order))
                del self.cache[oldest_key]
                del self.access_order[oldest_key]
            
            self.cache[key] = value
            self.access_order[key] = True
```

---

## 10. Load Balancer Design

### Requirements
- **Functional**: Distribute requests, health checks, SSL termination
- **Non-functional**: Handle 1M RPS, <1ms latency overhead
- **Scale**: Support thousands of backend servers

### Load Balancing Algorithms

#### 1. Round Robin
```python
class RoundRobinBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current = 0
    
    def get_server(self):
        server = self.servers[self.current]
        self.current = (self.current + 1) % len(self.servers)
        return server
```

#### 2. Weighted Round Robin
```python
class WeightedRoundRobinBalancer:
    def __init__(self, servers_with_weights):
        self.servers = []
        for server, weight in servers_with_weights:
            self.servers.extend([server] * weight)
        self.current = 0
    
    def get_server(self):
        server = self.servers[self.current]
        self.current = (self.current + 1) % len(self.servers)
        return server
```

#### 3. Least Connections
```python
class LeastConnectionsBalancer:
    def __init__(self, servers):
        self.servers = {server: 0 for server in servers}
    
    def get_server(self):
        return min(self.servers, key=self.servers.get)
    
    def on_request_start(self, server):
        self.servers[server] += 1
    
    def on_request_end(self, server):
        self.servers[server] -= 1
```

#### 4. Consistent Hashing (for sticky sessions)
```python
class ConsistentHashBalancer:
    def __init__(self, servers):
        self.hash_ring = ConsistentHashRing(servers)
    
    def get_server(self, client_id):
        return self.hash_ring.get_node(client_id)
```

### Health Check Implementation
```python
class HealthChecker:
    def __init__(self, servers, check_interval=30):
        self.servers = servers
        self.healthy_servers = set(servers)
        self.check_interval = check_interval
        self.start_health_checks()
    
    def start_health_checks(self):
        def check_health():
            for server in self.servers:
                if self.is_healthy(server):
                    self.healthy_servers.add(server)
                else:
                    self.healthy_servers.discard(server)
        
        # Run health checks periodically
        threading.Timer(self.check_interval, check_health).start()
    
    def is_healthy(self, server):
        try:
            response = requests.get(f"http://{server}/health", timeout=5)
            return response.status_code == 200
        except:
            return False
```

### Layer 7 Load Balancer
```python
class ApplicationLoadBalancer:
    def __init__(self):
        self.routes = {}
        self.default_balancer = None
    
    def add_route(self, path_pattern, balancer):
        self.routes[path_pattern] = balancer
    
    def route_request(self, request):
        for pattern, balancer in self.routes.items():
            if re.match(pattern, request.path):
                return balancer.get_server()
        
        return self.default_balancer.get_server() if self.default_balancer else None
```

## Key System Design Principles

### 1. Scalability Patterns
- **Horizontal Scaling**: Add more servers
- **Database Sharding**: Partition data across multiple databases
- **Microservices**: Break monolith into smaller services
- **Caching**: Multiple levels (browser, CDN, application, database)

### 2. Reliability Patterns
- **Replication**: Master-slave, master-master
- **Circuit Breaker**: Prevent cascade failures
- **Bulkhead**: Isolate critical resources
- **Graceful Degradation**: Maintain partial functionality

### 3. Performance Optimization
- **CDN**: Global content distribution
- **Database Indexing**: Optimize query performance
- **Connection Pooling**: Reuse database connections
- **Async Processing**: Non-blocking operations

### 4. Monitoring and Observability
- **Logging**: Structured logging with correlation IDs
- **Metrics**: Business and technical metrics
- **Distributed Tracing**: Track requests across services
- **Health Checks**: Automated failure detection

## Interview Tips

1. **Start with Requirements**: Always clarify functional and non-functional requirements
2. **Estimate Scale**: Back-of-envelope calculations for QPS, storage, bandwidth
3. **High-level Design First**: Draw the big picture before diving into details
4. **Justify Decisions**: Explain trade-offs and why you chose specific technologies
5. **Think About Edge Cases**: Handle failures, peak traffic, data consistency
6. **Iterate and Improve**: Start simple, then add complexity and optimizations

## Additional Important System Design Concepts

### CAP Theorem
- **Consistency**: All nodes see the same data simultaneously
- **Availability**: System remains operational
- **Partition Tolerance**: System continues despite network failures
- **Trade-off**: Can only guarantee 2 out of 3 in distributed systems

### Database Concepts

#### ACID Properties
- **Atomicity**: Transactions are all-or-nothing
- **Consistency**: Database remains in valid state
- **Isolation**: Concurrent transactions don't interfere
- **Durability**: Committed data persists

#### NoSQL Database Types
- **Document**: MongoDB, CouchDB (flexible schema)
- **Key-Value**: Redis, DynamoDB (simple operations)
- **Column-Family**: Cassandra, HBase (wide columns)
- **Graph**: Neo4j, Amazon Neptune (relationships)

### Message Queue Patterns

#### Publisher-Subscriber
```python
# Publisher
def publish_event(topic, message):
    message_queue.publish(topic, message)

# Subscriber
def subscribe_to_events(topic, callback):
    message_queue.subscribe(topic, callback)
```

#### Work Queue
```python
# Producer
def add_task(task):
    work_queue.enqueue(task)

# Consumer
def process_tasks():
    while True:
        task = work_queue.dequeue()
        process_task(task)
```

### Caching Strategies

#### Cache-Aside (Lazy Loading)
```python
def get_user(user_id):
    # Try cache first
    user = cache.get(f"user:{user_id}")
    if user is None:
        # Cache miss - fetch from database
        user = database.get_user(user_id)
        cache.set(f"user:{user_id}", user, ttl=3600)
    return user
```

#### Write-Through
```python
def update_user(user_id, data):
    # Update database first
    database.update_user(user_id, data)
    # Then update cache
    cache.set(f"user:{user_id}", data, ttl=3600)
```

#### Write-Behind (Write-Back)
```python
def update_user(user_id, data):
    # Update cache immediately
    cache.set(f"user:{user_id}", data, ttl=3600)
    # Asynchronously update database
    async_queue.enqueue('update_user_db', user_id, data)
```

### Security Considerations

#### Authentication & Authorization
- **JWT Tokens**: Stateless authentication
- **OAuth 2.0**: Third-party authentication
- **Rate Limiting**: Prevent abuse
- **Input Validation**: Prevent injection attacks

#### Data Protection
- **Encryption at Rest**: Database encryption
- **Encryption in Transit**: HTTPS/TLS
- **PII Handling**: Data anonymization
- **Compliance**: GDPR, CCPA requirements

### Performance Metrics

#### Key Metrics to Monitor
- **Latency**: P50, P95, P99 response times
- **Throughput**: Requests per second (RPS)
- **Error Rate**: 4xx/5xx error percentage
- **Availability**: Uptime percentage (99.9%, 99.99%)

#### SLA/SLO Examples
```
Service Level Objectives (SLOs):
- 99.9% availability (8.77 hours downtime/year)
- P95 latency < 200ms
- Error rate < 0.1%
- Recovery time < 1 minute
```

### Common Bottlenecks & Solutions

#### Database Bottlenecks
- **Problem**: Slow queries
- **Solutions**: Indexing, query optimization, read replicas

#### Memory Bottlenecks
- **Problem**: High memory usage
- **Solutions**: Caching optimization, memory profiling

#### CPU Bottlenecks
- **Problem**: High CPU utilization
- **Solutions**: Load balancing, code optimization, auto-scaling

#### Network Bottlenecks
- **Problem**: Network latency/bandwidth
- **Solutions**: CDN, compression, regional deployment

### Disaster Recovery

#### Backup Strategies
- **Full Backup**: Complete data copy
- **Incremental Backup**: Changes since last backup
- **Differential Backup**: Changes since last full backup

#### Recovery Objectives
- **RTO (Recovery Time Objective)**: Maximum downtime
- **RPO (Recovery Point Objective)**: Maximum data loss

### Interview Framework: SNAKE Method

#### S - Scope
- Clarify requirements (functional & non-functional)
- Define success metrics
- Identify constraints

#### N - Napkin Math
- Estimate scale (users, requests, storage)
- Calculate bandwidth requirements
- Determine hardware needs

#### A - Abstract Design
- Draw high-level architecture
- Identify major components
- Show data flow

#### K - Key Components
- Design core services in detail
- Define APIs and data models
- Address scalability concerns

#### E - Evolve & Extend
- Handle edge cases and failures
- Add monitoring and logging
- Discuss future improvements

### Sample Interview Questions by Company

#### Google/Meta/Amazon
- Design a URL shortener
- Design a chat system
- Design a news feed
- Design a video streaming service

#### Netflix/Spotify
- Design a recommendation system
- Design a content delivery network
- Design a real-time analytics system

#### Uber/Lyft
- Design a ride-sharing service
- Design a location-based service
- Design a payment system

#### Twitter/Reddit
- Design a social media platform
- Design a trending topics system
- Design a voting system

### Common Mistakes to Avoid

1. **Not asking clarifying questions**
2. **Jumping into implementation details too early**
3. **Ignoring non-functional requirements**
4. **Not considering failure scenarios**
5. **Over-engineering the initial design**
6. **Not explaining trade-offs**
7. **Forgetting about monitoring and logging**

### Best Practices Summary

#### Design Principles
- **Start simple, then scale**
- **Favor horizontal over vertical scaling**
- **Design for failure**
- **Keep it stateless when possible**
- **Cache everything (that makes sense)**

#### Communication Tips
- **Think out loud**
- **Draw diagrams**
- **Explain your reasoning**
- **Ask for feedback**
- **Acknowledge limitations**

---

*This comprehensive guide covers the most frequently asked system design questions in technical interviews. Practice drawing these architectures, explaining trade-offs, and discussing how to handle scale and failures. Remember: there's no single "correct" answer - focus on demonstrating your thought process and engineering judgment.*