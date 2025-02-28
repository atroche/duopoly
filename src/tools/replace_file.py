from gpt import gpt_query
from utilities.prompts import load_prompt

SYSTEM_REPLACE_THINK = load_prompt("replace_think")

SYSTEM_REPLACE = load_prompt("replace")


def modify_file(original_file, instructions, context="", file_name=None):
    thinking_text = (
        f"### THINKING FOR {file_name} ###" if file_name else "### THINKING ###"
    )
    new_file_text = f"### NEW FILE {file_name} ###" if file_name else "### NEW FILE ###"

    instructions = f"### CONTEXT ###\n{context}\n### INSTRUCTIONS ###\n{instructions}\n### ORIGINAL FILE ###\n(see context)\n{thinking_text}"
    thinking = gpt_query(instructions, SYSTEM_REPLACE_THINK)
    instructions = f"{instructions}\n{thinking}\n{new_file_text}"
    new_file = gpt_query(instructions, SYSTEM_REPLACE)

    return new_file
