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

Functional Requirements:(eg online exam portal)
User registration
User login/logout
Create exams
Add questions
Attempt exams
Submit answers

Non-functional requirements: Availability, Functionality, Scalibility, Reliability

(1)Monolithic and MicroService Architecture

Monolithic---
single code based -> we will build + run + test + deploy together
Disadvantages: 
--Single point of failure (if one file will crash , everything will crash)
--Deployment Bottleneck: A Deployment Bottleneck occurs when releasing new changes to production becomes slow,      risky, or difficult because the application's deployment process is tightly coupled.
--Scaling: Scaling is the ability of a system to handle increased workload, traffic, or data without degrading performance.

MicroService Architecture---
Everything is loosely coupled -> test+run+deploy all can done individually -> Not dependent o each other
Every service can have their own database and server too.


-------CONVERTING MONOLITHIC TO MICROSERVICES-----
-We don't migrate our whole traffic at once to the micro.

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



