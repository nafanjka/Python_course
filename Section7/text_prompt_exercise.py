full_text = []
while True:
    text_prompt = input("Say something: ")
    if text_prompt == "\end":
        break
    elif text_prompt.startswith(("how", "why", "what", "where", "who", "which", "when")):
        full_text.append(text_prompt.capitalize() + "?")
    else:
        full_text.append(text_prompt.capitalize() + ".")
print(str.join(" ", full_text))

# better solution

def sentence_maker(phrase):
    interrogatives = ("how", "why", "what", "where", "who", "which", "when")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))               
