# langgraph

`langgraph` is a Python project for building, visualizing, and experimenting with agent-based computation graphs, especially for language model workflows. It features several example agents and graph-based applications, including games, calculators, and document assistants, using the `langgraph` and `langchain` libraries.

## Features

- **Agent Graphs**: Compose agents as nodes in a directed graph, with support for conditional routing and state management.
- **Examples Included**:
  - Multi-step agent flows (e.g., personalized compliments, skill listing)
  - Conditional operation graphs (addition, subtraction, etc.)
  - Higher-lower guessing game with stateful logic
  - Document drafting and saving assistant
  - ReAct-style agent with tool use (add, subtract, multiply)
  - Simple conversational bots

## Requirements

- Python 3.8+
- `langgraph`
- `langchain`
- `langchain_huggingface`
- `langchain_openai`
- `python-dotenv`
- `huggingface_hub`
- (Other dependencies as required by your environment)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/EquineNaveen/langgraph.git
   cd langgraph
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   Or manually install the required packages:
   ```
   pip install langgraph langchain langchain_huggingface langchain_openai python-dotenv huggingface_hub
   ```

3. Set up your `.env` file with any required API keys (e.g., HuggingFace, OpenAI).

## Usage

Each Python file demonstrates a different agent or graph pattern. For example:

- Run the higher-lower game:
  ```
  python higher_lower_game_graph.py
  ```
- Try the document drafter agent:
  ```
  python Agent/drafter.py
  ```
- Experiment with the ReAct agent:
  ```
  python Agent/ReAct.py
  ```

Some scripts will generate a `graph.png` file visualizing the computation graph.

## Examples

- **multiple_nodes.py**: Welcomes a user, states their age, and lists their skills.
- **personalised_complement_agent.py**: Generates a personalized compliment.
- **graph_operations.py**: Performs addition or multiplication on a list of values.
- **conditional_graph.py**: Demonstrates conditional routing in a computation graph.
- **Agent/bot.py**: Simple conversational agent using HuggingFace models.
- **Agent/drafter.py**: Interactive document editing and saving agent.
- **Agent/ReAct.py**: Agent with tool use and reasoning.

## Project Structure

```
.
├── Agent/
│   ├── bot.py
│   ├── drafter.py
│   ├── ReAct.py
│   └── smartbot.py
├── conditional_graph.py
├── graph_operations.py
├── higher_lower_game_graph.py
├── multiple_nodes.py
├── personalised_complement_agent.py
├── README.md
└── graph.png
```

