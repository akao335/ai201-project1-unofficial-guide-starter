# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
I chose the UT Dallas on-campus and nearby off-campus dining options as my domain. This knowledge is valuable because some important information is spread across different websites. These official websites also do not take into account honest student opinions about the food quality, value, or wait times. 
---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source                    | Description                 | URL or location |
|---|---------------------------|----------------------------|-----------------|
| 1 | UTD Campus Dining Services|Main university dining page |https://services.utdallas.edu/dining/ |
| 2 |UTD Student Union           |Student Union food listings |https://union.utdallas.edu/facilities/dining/ |
| 3 |UTD DIning page             | UTD dining page hours    |https://dineoncampus.com/utdallasdining
| 4 |UTD Housing reccomendations |UTD Housing Recommendations |https://housing.utdallas.edu/resources/move-in/lodging-and-restaurants/ |
| 5 |Yelp                      |Student Union Reviews        |https://www.yelp.com/biz/student-union-dining-hall-richardson
| 6 | Reddit                     |Meal plan Thread            |https://www.reddit.com/r/utdallas/search/?q=meal+plan&sort=top
| 7 | Reddit                     |Food recommendations |     https://www.reddit.com/r/utdallas/search/?q=food&sort=top
| 8 | Wanderlog                  |Northside Drafthouse |    https://wanderlog.com/place/details/8042138/northside-drafthouse--eatery
| 9 |Facebook                   |UTD Dining Updates      |https://www.facebook.com/UTDallasDining/
| 10 | UTD Dining              |General Information |  https://dineoncampus.com/utdallasdining/general-information

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
400 Characters
**Overlap:**
75 characters
**Reasoning:**
The documents that I have used is a mix of long pages with multiple paragraphs of information and short reviews of dining options. Because there are long pages, I decided to use bigger chunks in order to take into account the longer pages that would require bigger chunks. The 400 characters seems large enough to chunk a complete thought for a longer document. This would also take into account the smaller reviews completely. The 75 character overlap will make sure that any thought from a longer document is incorporated into the chunk and not seperated into two chunks. 
---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
all-MiniLM-L6-v2 via sentence-transformers
**Top-k:**
5 chunks per query
**Production tradeoff reflection:**
Some tradeoffs that would be considered is the accuracy, multilingual support, and context length. The text-embedding-3-small has seen to be more likely to retrieve more relevant chunks. As for multilingual support, becauase UTD has a large international student population, the multilingual model would help with translating responses to make the information more accessible. The all-MiniLM-L6-v2 can support the 400 characker chunks. 
---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question |                                     Expected answer |
|---|----------|--------------------------------------------------|
| 1 | What dining options are  at the Student Union? |Panda Express, Crave, Kalachandji's Express, Chick-fil-A, Firehouse Subs, Halal Shack
| 2 |What times are the dining hall open on monday ? |7:30 - 9am, 11am to 2pm, 5pm to 8pm
| 3 |Can students use their meal plan at off-campus restaurants? |UT dallas students generally cannot use their meal plan sqipes at off-campus resturants
| 4 |What do students say about wait times at the UTD Dining options at Student Union ? | Students Union dining options wait times are heavy around noon rush as well as the Starbucks lines can exceed 15 minutes. 
| 5 | What are student opinion on the overall food quality at UTD?|some students find it acceptable, others complain about the lack of variety of options |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Noisy inconsistent documents - The pages such as Yelp, Facebook, Reddit can contain lots of text that is not directly related to the domain. This might pollute the retrieval results if the extra text is used out of context. 

2.Chuncks that split key information across boundaries - Information like the dining option hours will change depending on how you chunk the information. If the chunks are a few characters off, it can result in the timings being incorrect when displaying the information to the user. 

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->
[.txt files in /documents]
|
v
[Ingestion + Cleaning] — os, re
|
v
[Chunking] — custom chunk_text(), 400 chars, 80 overlap
|
v
[Embedding + Vector Store] — all-MiniLM-L6-v2, ChromaDB
|
v
[Retrieval] — ChromaDB query(), top-5
|
v
[Generation] — Groq llama-3.3-70b-versatile
|
v
[Gradio UI] — http://localhost:7860
---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**
- AI tool: Claude
- Input provided: Documents section (file names) + Chunking Strategy section 
  (400 chars, 80 overlap) + list of noise to remove (HTML, URLs, Reddit vote 
  counts, boilerplate nav lines)
- Expected output: ingest.py with load_documents() and chunk_text() functions
- Verified by: printing 5 sample chunks and confirming each was readable, 
  self-contained, and free of HTML or nav artifacts

**Milestone 4 — Embedding and retrieval:**
- AI tool: Claude
- Input provided: Retrieval Approach section (all-MiniLM-L6-v2, top-k=5, 
  ChromaDB) + pipeline diagram + chunk format from ingest.py
- Expected output: embed.py with build_vector_store() and retrieve() functions
- Verified by: running 3 test queries and checking that returned chunks 
  visibly related to each query and distance scores were below 0.5

**Milestone 5 — Generation and interface:**
- AI tool: Claude
- Input provided: grounding requirement (answer from retrieved context only) + 
  desired output format (answer + source list) + Gradio skeleton from project spec
- Expected output: query.py with grounded prompt template + app.py with 
  working Gradio UI
- Verified by: asking a question not covered by documents and confirming the 
  system returned "I don't have enough information" rather than hallucinating
