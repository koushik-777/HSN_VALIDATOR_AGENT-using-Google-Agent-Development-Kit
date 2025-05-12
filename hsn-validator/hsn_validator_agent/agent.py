import pandas as pd
import re
from google.adk.agents import Agent

# Data Loading (executed once)
hsn_df = pd.read_excel("D:\hsn-validator\hsn_validator_agent\HSN_SAC.xlsx")               # Read Excel into DataFrame:contentReference[oaicite:12]{index=12}
hsn_dict = {str(c): d for c, d in zip(hsn_df['\nHSNCode'], hsn_df['Description'])}

def validate_hsn_codes(codes_input: str) -> dict:
    """
    Validate one or more HSN codes provided as input.
    Checks that each code is 2-8 digits and exists in the dataset.
    Args:
        codes_input (str): HSN codes separated by commas or spaces.
    Returns:
        dict: {
            "status": "success" or "error",
            "report": "HSN Code X: Desc. ...",
            "error_message": "...if error"
        }
    """
    parts = re.split(r'[\s,;]+', codes_input.strip())
    codes = [p for p in parts if p]
    if not codes:
        return {"status": "error", "error_message": "No valid HSN code provided."}

    results = []
    any_success = False
    for code in codes:
        if not code.isdigit() or len(code) < 2 or len(code) > 8:
            results.append(f"HSN Code {code}: invalid hsn code")
        else:
            desc = hsn_dict.get(code)
            if desc:
                results.append(f"HSN Code {code}: {desc}")
                any_success = True
            else:
                results.append(f"HSN Code {code}: invalid hsn code")

    report = ". ".join(results)
    if not report.endswith("."):
        report += "."
    status = "success" if any_success else "error"
    return {"status": status, "report": report}

# Agent Setup
root_agent = Agent(
    name="hsn_validator_agent",
    model="gemini-2.0-flash",
    description="Agent for validating HSN code(s) from a provided dataset.",
    instruction=(
        "Validate the given HSN code(s) using the provided dataset. "
        "For each code, return its description if valid, or 'invalid hsn code'."
    ),
    tools=[validate_hsn_codes]
)
