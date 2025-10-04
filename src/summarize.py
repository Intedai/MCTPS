# FOR NOW I AM NOT USING THIS, WILL PROBS USE FOR TITLE OR SOMETHING

from ollama import chat
from ollama import ChatResponse

def get_response(model: str, initial_string: str, description: str) -> str:
    """
    Gets a response from an Ollama ai model, with injected string
    :param model: model name
    :param initial_string: injected message at the top
    :param description: description of the texturepack, aka the message
    :returns: response
    """

    response: ChatResponse = chat(model=model, messages=[
    {
        'role': 'user',
        'content': f'{initial_string}\n{description}',
    },
    ])

    return response.message.content

def find_good_response(model: str, initial_string: str, description: str)  -> str:
    """
    Gets a response from an Ollama ai model, with injected string.
    loops until user types Y to ensure the response is good
    :param model: model name
    :param initial_string: injected message at the top
    :param description: description of the texturepack, aka the message
    :returns: response
    """
    
    while True:
        current = get_response(model, initial_string, description)
        print(current, end="\n\n\n")
        inp = input("Type 'Y' if response is good (press ENTER or type anything else if it's not): ")

        if inp.lower() == 'y':
            break
    
    return current
