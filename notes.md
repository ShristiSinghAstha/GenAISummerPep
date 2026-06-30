RAG -- (Retrieval Augmented Generation)
Document loadr
text splitter(chunking)
database
retrivers -- when data embedded -> loaded -> retrieve data stored inside vector


Text splitter --
character based chunking
token based chunking
semantic/meaning-based splitting


Vector Store--A vector store is a database optimized for storing and searching vector embeddings—numerical representations of data such as text, images, audio, or code.
Use Approximate Nearest neighbours algorithms like-  HNSW, IVF, PQ


-------------SYSTEM DESIGN-----------------
System Design is the process of defining the architecture, components, data flow, and infrastructure of a software system to meet functional and non-functional requirements.


----30 Important Topics to cover in System Design----
1.Client-Server Architecture
2.IP Address
3.DNS
4.Proxy/Reverse Proxy
5.Latency
6.HTTP/HTTPS
7.APIs
8.Rest APIs
9.GraphQL
10.Databases
11.SQL vs NoSQL
12.Vertical Scaling
13.Horizontal Scaling
14.Load Balancers
15.Database Indexing
16.Replication
17.Shrading
18.Vertical Partitioning
19.Caching
20.Denormalization
21.CAP Theorem
22.Blob Storage
23.CDN
24.WebSockets
25.Webhooks
26.MicroServices
27.Message Queues
28.Rate Limiting
29.API Gateways
30.Idemmpotency


--Functional Requirements:(eg online exam portal)
User registration
User login/logout
Create exams
Add questions
Attempt exams
Submit answers

--Non-functional requirements: Availability, Functionality, Scalibility, Reliability

(1)Monolithic and MicroService Architecture

Monolithic---
single code base -> we will build + run + test + deploy together
Disadvantages: 
-- (Issue1) --Single point of failure (if one file will crash , everything will crash)
-- (Issue2) --Deployment Bottleneck: A Deployment Bottleneck occurs when releasing new changes to production becomes slow, risky, or difficult because the application's deployment process is tightly coupled.
-- (Issue3) --Scaling: Scaling is the ability of a system to handle increased workload, traffic, or data without degrading performance.

MicroService Architecture---
Every module is loosely coupled -> test+run+deploy all can done individually -> Not too much dependent on each other
Every service can have their own database and server too.


-------CONVERTING MONOLITHIC TO MICROSERVICES-----
-We don't migrate our whole project at once to the micro.

(1)Build/Understand API Contracts
An API Contract is an agreement between the client and server that defines:

-What endpoints are available
-What request data should be sent
-What response data will be returned
-Error codes and formats

(2) Setup Communication 
If not setup-> System will be slow 
-Sync
-Async

Canary Method-----------
While shifting from mono to micro -> We don't shift  whole traffic directly -> We use Traffic canary method.
--By using it, we shift a small set of user first and check if its working, then we shift the rest.

Strangler Design Pattern----------
We graduaaly replace a legacy system with new one-> without shifting everything down at once.
--Untill 100% traffic is not transferred, it will not demolish the old architecture.

The Strangler Design Pattern is a migration strategy used to gradually replace a legacy (old) system with a new system without shutting down or rewriting everything at once.
The name comes from the Strangler Fig tree, which grows around an existing tree and slowly replaces it over time.

Saga Design Pattern ------------
It handles transactions across multiple micro services without using single global database transaction.
Core Idea: Instead of core big transaction, u break it into small local transaction.
If something fails -> undo previous steps (compensation).

#Transaction: SAGA : the design pattern hanles transactions across multiple microservices without using single global DB transaction
Core idea: instead of core big transaction, u break it into small local transaction If something fails:-> u undo previous step(compensation)

2 types of SAGA:=> 
(i) Choreography(event-based):- services talk via events (no central controller),
                                    flow->order created->payment listens->payment success->inventory listens
(ii) Orchestration(central control):- one service controls the flow(saga orchestration)
                                        flow-> orchestratior->call order->then payment->then inventory

# Data Consistancy (Outbox) :=> ex: 
when a user place order, u need to do 2 things:- (i) save the order in database (ii) send the event -> "order created"(so that payment service can act)
Problem(without outbox): what if:- 
*order saved
*event sending fails
-> now ur system is broken(order is about no payment )


with outbox pattern:-
trusted of sending the event directly 
step 1: save both in one db transaction, 
        -> order -> order table
        -> event -> outbox table
{
    "event": "order created",
    "orderID": "123"
}  


Part 2: API Gateway vs load balancer
# API gateway:- "API gateway is a single entry point for all the clients reqs in a system with multiple backend services."
User => GATEWAY :- 
    a. User
    b. payment
    c. order
what does api gateway do? 
=> a. routes req to the correct serivce
b. handles auth and authorization
c. perform rate Limitingow.

#Load Balancer:- "A load balancer is a device or software that distributes incoming network traffic across multiple servers to improve availability, performance, and reliability."

if it's about region--> API gateway comes first, then load balancer
if it's  about locality--> Load balancer comes first.
