# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
I chose the UT Dallas on-campus and nearby off-campus dining options as my domain. This knowledge is valuable because some important information is spread across different websites. These official websites also do not take into account honest student opinions about the food quality, value, or wait times. 
---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source                    | Description                 | URL or location |
|---|---------------------------|----------------------------|-----------------|
| 1 | UTD Campus Dining Services|Main university dining page |https://services.utdallas.edu/dining/ |
| 2 |UTD Student Union           |Student Union food listings |https://union.utdallas.edu/facilities/dining/ |
| 3 |UTD Dining page             | UTD dining page hours     |https://dineoncampus.com/utdallasdining
| 4 |UTD Housing reccomendations |UTD Housing Recommendations |https://housing.utdallas.edu/resources/move-in/lodging-and-restaurants/ |
| 5 |Yelp                       |Student Union Reviews        |https://www.yelp.com/biz/student-union-dining-hall-richardson
| 6 | Reddit                     |Meal plan Thread            |https://www.reddit.com/r/utdallas/search/?q=meal+plan&sort=top
| 7 | Reddit                     |Food recommendations |     https://www.reddit.com/r/utdallas/search/?q=food&sort=top
| 8 | Wanderlog                |Northside Drafthouse reviews|    https://wanderlog.com/place/details/8042138/northside-drafthouse--eatery
| 9 |Facebook                    |UTD Dining Updates      |https://www.facebook.com/UTDallasDining/
| 10 | UTD Dining               |General Information |  https://dineoncampus.com/utdallasdining/general-information

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
400 characters
**Overlap:**
80 characters
**Why these choices fit your documents:**
The documents that I have used is a mix of long pages with multiple paragraphs of information and short reviews of dining options. Because there are long pages, I decided to use bigger chunks in order to take into account the longer pages that would require bigger chunks. The 400 characters seems large enough to chunk a complete thought for a longer document. This would also take into account the smaller reviews completely. The 75 character overlap will make sure that any thought from a longer document is incorporated into the chunk and not seperated into two chunks. 
**Final chunk count:**
56
---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**  all-MiniLM-L6-v2 via sentence-transformers

**Production tradeoff reflection:**
Some tradeoffs that would be considered is the accuracy, multilingual support, and context length. The text-embedding-3-small has seen to be more likely to retrieve more relevant chunks. As for multilingual support, becauase UTD has a large international student population, the multilingual model would help with translating responses to make the information more accessible. The all-MiniLM-L6-v2 can support the 400 characker chunks. 
---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
You are a helpful assistant for UT Dallas students looking for information
about campus dining.
Answer the question using ONLY the information provided in the documents below.
Do not use any outside knowledge. If the documents do not contain enough
information to answer the question, say exactly:
"I don't have enough information in my documents to answer that."
**How source attribution is surfaced in the response:**
Source attribution is handled programmatically, not left to the LLM. In 
query.py, each retrieved chunk carries a "source" metadata field (the original 
.txt filename) stored in ChromaDB. After generation, the code collects the 
unique source filenames from all retrieved chunks and returns them alongside 
the answer. The Gradio UI displays these in a separate "Sources" panel below 
the answer, so users always see which documents the response drew from 
regardless of what the LLM chose to mention in its text.
---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question |                                      Expected answer |                    System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|---------------------------------------------------|------------------------------|-------------------|-------------------|
| 1 |What dining options are  at the Student Union? |Panda Express, Crave, Kalachandji's Express, Chick-fil-A, Firehouse Subs, Halal Shack| The Student Union Food Court includes Panda Express, Crave, Kalachandji’s Express, and Chick-fil-A, as well as the Comet Cafe and Outtakes. Additionally, there is also Moe's and a pizza place.  |  Quality is good. The system response is closely related to the expected answer.  | response is accurate
| 2 | What times are the dining hall open on monday ? |7:30 - 9am, 11am to 2pm, 5pm to 8pm |The dining hall, specifically Dining Hall West, is open on Monday from 7:30a - 9:00a, 11:00a - 2:00p, and 5:00p - 8:00p. | Quality is good. The system response is closely related to the expected answer. | response is accurate
| 3 | Can students use their meal plan at off-campus restaurants? |UT dallas students generally cannot use their meal plan sqipes at off-campus resturants|  I don't have enough information in my documents to answer that. |partially relevant - it was right that it did not have enough information to answer this question. This was because of the lack of information provided in the documents. |Inaccurate — correct refusal but documents should have covered this
| 4 | What do students say about wait times at the UTD Dining options at Student Union ?| Students Union dining options wait times are heavy around noon rush as well as the Starbucks lines can exceed 15 minutes.|  I don't have enough information in my documents to answer that. |partially relevant - it was right that it did not have enough information to answer this question. This was because of the lack of information provided in the documents. | Inaccurate — documents do not contain wait time content
| 5 | What are student opinion on the overall food quality at UTD?|some students find it acceptable, others complain about the lack of variety of options | responded with a paragraph on reviews by students  | Quality is good. The system response is closely related to the expected answer.| response is accurate



**Retrieval quality:** Relevant / **Partially relevant** / Off-target  
**Response accuracy:** Accurate /**Partially accurate** / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**
A question that failed is number 4 about the wait times. 
**What the system returned:**
I don't have enough information in my documents to answer that.
**Root cause (tied to a specific pipeline stage):**
This is because of the document collection stage. There was not enough specific information to answer this question. This ended up with a retrieval with a distance above 0.89 which shows weak matches. 
**What you would change to fix it:**
I would need to research and provide more documents with the necessary information that discusses wait times. 
---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
One way it helped is by helping me plan the implementation before coding it out. It helped me know what I needed to do and how I wanted to organize the information. This way I could give claude clear instructions. 
**One way your implementation diverged from the spec, and why:**
In the planning, I listed a few documents that could have been improved. The choosing of the documents showed a lack in an area of information, which resulted in the response to not have enough information to give the user. These sources had less text than expected
---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:* Chunking Strategy from the planning and asked it to load my documents and chucnk text with the specs I listed. 
- *What it produced:*It produced working code, but it initially used a basic split without using the overlap. 
- *What I changed or overrode:* This made some words cut off, so I asked it to fix the code with the overlap. It was able to correct this

**Instance 2**

- *What I gave the AI:* Retreival Approach and pipeline diagram. I asked it to implement the embedding with the with all-MiniLM-L6-v2 and storage in ChromaDB with 
source metadata.
- *What it produced:* The generated code worked correctly on the first try.
- *What I changed or overrode:* I 
verified it by checking that distance scores were returned alongside chunk 
text and source filenames.
