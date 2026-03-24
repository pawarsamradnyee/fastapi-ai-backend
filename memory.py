# prompt/message construction file and Memory Builder
MAX_MESSAGES = 10                                                               # sets a limit on how many past messages to keep.

# function that creates the system prompt and System prompt tells the AI how to behave.
def build_system_prompt(mode="detailed"):
    if mode == "short":
        return (
            "You are a helpful AI assistant. "
            "Reply briefly and clearly in 2 to 4 lines."
        )
    return (
        "You are an intelligent and helpful AI assistant. "
        "Give clear, structured answers. "
        "Use bullet points when useful. "
        "For technical questions, include simple examples."
    )

''' Creates the full messages list that will be sent to the OpenAI API.
        prompt = current user question
        history = earlier conversation
        mode = short/detailed behavior
'''
def build_messages(prompt, history=None, mode="detailed"):
    messages = [
        {"role": "system", "content": build_system_prompt(mode)}
    ]

    if history:
        for msg in history[-MAX_MESSAGES:]:                                 # Loop through only the last MAX_MESSAGES messages.
            messages.append({"role": msg.role, "content": msg.content})     # Add each old message to the new messages list.

    messages.append({"role": "user", "content": prompt})                    # Add each old message to the new messages list.   
    return messages