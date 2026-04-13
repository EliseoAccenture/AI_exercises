# AI Team Exercises 
Track: OCR Exploration + Agent Development with Microsoft Agent Framework Stack: Python or C# · VS Code · Ollama (local models) Reference: Microsoft Agent Framework Docs.
These exercises are meant to be explored, not just executed. Read the linked documentation, experiment, break things, and be ready to explain your choices. 
## Exercise 1:  OCR Model Exploration 
_Status: 🟡 In Progress_

Context You have been provided with a set of images of varying complexity (clean scans, handwritten notes, low-contrast photos, mixed layouts). Your goal is to explore different AI-based OCR approaches and find the most efficient one depending on the difficulty of the input. 

What you need to do Pick at least 3 different OCR models or approaches (e.g. Tesseract, EasyOCR, TrOCR, PaddleOCR, or a vision-capable LLM via Ollama, etc.) and run them against the provided images. For each image, evaluate which approach gives the best extraction quality and why. Document your findings and justify your final choice per image category. 

Deliverable A small, clean GitHub repository containing your scripts, a /results folder with extracted outputs per model, and a short README.md that summarizes your findings in a table (model vs. image difficulty vs. accuracy/quality assessment). 

What we'll evaluate:
* Did you try meaningfully different approaches, not just variations of the same tool? 
* Is your repo organized and readable by someone who wasn't in the room? 
* Can you defend why a given model works better on a given image type? 

## Exercise 2 - Your First Agent (Hello Agentino) 
_Status: 🔜 Up Next_

Context This is your entry point into the Microsoft Agent Framework. The goal is simple: get an agent running locally using Ollama, with no cloud dependencies. 

What you need to do Install the framework (pip install agent-framework --pre for Python, or the NuGet packages for C#). Read the Get Started guide and spin up a minimal agent backed by a local Ollama model of your choice. Give the agent a custom personality through its instructions parameter and ask it at least 3 different questions. Observe and note how the instructions shape the responses. 

Deliverable A single runnable script (hello_agent.py or HelloAgent.cs) with a short comment block at the top explaining which Ollama model you chose and why. 

What we'll evaluate:
* Does it run cleanly end-to-end with a local model? 
* Did you actually read the docs or just copy-paste the snippet?
* Can you explain what instructions does under the hood? 

## Exercise 3 - Agent with Tools 
_Status: 🔜 Up Next_ 

Context A raw LLM call is not an agent - what makes it an agent is its ability to decide when and how to use tools. In this exercise, you will give your agent real capabilities. 

What you need to do Read the Tools documentation and add at least 2 custom tools to your agent. Tools should be functions you write yourself - for example a get_weather(city: str) that returns mocked data, a calculate_discount(price: float, pct: float) function, or a simple file reader. Then craft prompts that force the agent to reason about which tool to use and when. Try a prompt where neither tool is needed and observe the behavior. 

Deliverable A script agent_with_tools.py (or .cs) and a short written note (in the README or inline comments) describing one case where the agent surprised you - either by calling the right tool unexpectedly well, or by failing in an interesting way. 

What we'll evaluate 
* Are your tools non-trivial and actually useful in context? 
* Does the agent correctly decide when not to use a tool? 
* Did you handle the case where a tool call fails or returns unexpected data? 

## Exercise 4 - Stateful Conversations with Session Management 
_Status: 🔜 Up Next_ 

Context Stateless agents forget everything between calls. Real assistants remember context. This exercise is about giving your agent memory within a conversation. 

What you need to do Read the Session documentation and build a small interactive CLI loop using Python's input() (or a console loop in C#) where the user can have a back-and-forth conversation with the agent. The agent must demonstrate memory across turns. Test it with a sequence like: tell the agent your name and a preference → ask an unrelated question → then ask it to recall what you told it earlier. 

Deliverable A runnable script stateful_agent.py (or .cs) and a small transcript (copy-pasted into your README) showing at least 6 turns of conversation that prove the agent is maintaining state correctly. 

What we'll evaluate:
* Is state actually being managed by the framework, or did you hack it manually? 
* Does the conversation feel coherent across turns? 
* What happens if you start a brand new session - does it correctly forget? 

## Exercise 5 - Middleware: Observability and Guardrails 
_Status: 🔜 Up Next_ 

Context Production agents need more than just LLM calls ; they need logging, safety checks, and the ability to intercept what's happening under the hood. This is what middleware is for. 

What you need to do Read the Middleware documentation and implement two middleware components on your agent. The first should be an observability middleware that logs every tool call the agent makes (tool name, input, output) to the console or a file. The second should be a guardrail middleware that inspects incoming user messages and blocks any message containing sensitive keywords of your choice (e.g. "password", "secret", "token"), responding with a safe refusal message instead of forwarding to the LLM. 

Deliverable A script agent_with_middleware.py (or .cs) and a brief explanation in the README of how your middleware is ordered in the pipeline and why order matters. 

What we'll evaluate:
* Are both middleware components clearly separated and reusable? 
* Does the guardrail actually prevent the message from reaching the model? 
* Can you explain the middleware execution order and what would break if you reversed it?

## Exercise 6 - Your First Workflow (Multi-Step Orchestration)
_Status: 🔜 Up Next_

Context Sometimes a single agent is not enough. Workflows let you chain agents and functions in explicit, controlled sequences. This is the final and most complex exercise. 

What you need to do Read the Workflows documentation and design a small but complete sequential workflow with at least 2 steps. A suggested scenario: Step 1 - an agent takes a raw paragraph of text and produces a structured summary (bullet points, key facts). Step 2 - a second agent takes that summary and translates it into another language of your choice. Both agents should run on local Ollama models. The output of Step 1 must be the input of Step 2 - wiring this correctly is the core challenge. 

Feel free to design your own scenario if you have a better idea - but it must involve at least two distinct agents with a clear data handoff between them. 

Deliverable A script mini_workflow.py (or .cs), a diagram (even hand-drawn and photographed) showing your workflow graph, and a README section explaining when you would choose a Workflow over a single Agent with tools (hint: re-read the overview comparison table). 

What we'll evaluate:
* Is the data handoff between steps clean and explicit? 
* Does each agent have a focused, single responsibility? 
* Can you articulate the architectural difference between this and Exercise 3? 

## General Rules for All Exercises 
No magic boxes. If you use a library or class, be ready to explain what it does. 
Ollama only. No external API keys. All models must run locally. 
One repo per exercise or one organized monorepo with clearly separated folders. 
README is mandatory in every deliverable. If it's not documented, it doesn't exist. 
 
