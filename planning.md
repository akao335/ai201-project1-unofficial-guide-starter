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
| 3 |UTD DIning page             | UTD dining page hours|     |https://dineoncampus.com/utdallasdining
| 4 |UTD Housing reccomendations |UTD Housing Recommendations |https://housing.utdallas.edu/resources/move-in/lodging-and-restaurants/ |
| 5 |Yelp |                      |Student Union Reviews        |https://www.yelp.com/biz/student-union-dining-hall-richardson
| 6 | Reddit |                    |Meal plan Thread            |https://www.reddit.com/r/utdallas/search/?q=meal+plan&sort=top
| 7 | Reddit |                     |Food recommendations |     https://www.reddit.com/r/utdallas/search/?q=food&sort=top
| 8 | Wanderlog|                   |Northside Drafthouse |    https://wanderlog.com/place/details/8042138/northside-drafthouse--eatery
| 9 |Facebook |                    |UTD Dining Updates      |https://www.facebook.com/UTDallasDining/
| 10 | UTD Dining|                 |General Information |  https://dineoncampus.com/utdallasdining/general-information

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**

**Overlap:**

**Reasoning:**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

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

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
