# HSN_VALIDATOR_AGENT-using-Google-Agent-Development-Kit


# HSN Code Validation Agent

An AI agent built with Google’s Agent Developer Kit (ADK) that validates Harmonized System Nomenclature (HSN) codes against a static Excel dataset. Accepts one or more HSN codes and returns each code’s description or an “invalid hsn code” message.

## Features

- **Format Validation**: Ensures each code is numeric and 2–8 digits long.  
- **Existence Validation**: Checks for exact matches in the provided Excel master list.  
- **Batch Processing**: Supports comma‑ or space‑separated lists of codes in a single request.  
- **Built‑in Web UI**: Launch via `adk web`—no external deployment required.

## Prerequisites

- Python 3.8 or later  
- Google ADK  
- `pandas`  
- `openpyxl`

## Installation

1. Clone the repository.  
2. Install dependencies:
   ```bash
   pip install google-adk pandas openpyxl

## Repository Structure
.
├── README.md
├── agent.py                # Agent and tool configuration (not shown here)
├── HSN_Master_Data.xlsx    # Master list of HSN codes and descriptions
├── requirements.txt        # (optional) pinned dependencies
└── ...


## Configuration

Agent Name: hsn_validator_agent

Model: gemini-2.0-flash

Tool: HSNValidator (a custom Tool subclass that loads the Excel file on startup, parses input, and performs both format and existence checks)


## How It Works

On startup, the agent loads the Excel file into a pandas DataFrame, trimming whitespace and storing codes as strings.

A custom tool (“HSNValidator”) splits user input into individual codes (comma‑ or space‑separated), checks that each code consists solely of digits and is 2–8 characters long, and then looks up each in the DataFrame.

For every code, the agent returns a line of text: either “<code>: <description>” if found or “<code>: invalid hsn code” otherwise.

##  Running the Agent

Place HSN_Master_Data.xlsx in the project root.

Install required packages.

Launch ADK’s built‑in web interface with the command adk web.

In the browser UI, enter one or more HSN codes (for example, 0101, 01012100, 9999, abc) and submit.

The agent responds immediately with descriptions or invalid‑code messages.

## Example Interaction

Input: 0101, 01012100, 9999, abc

Output:

0101: LIVE HORSES, ASSES, MULES AND HINNIES.

01012100: PURE‑BRED BREEDING ANIMALS

9999: invalid hsn code

abc: invalid hsn code
