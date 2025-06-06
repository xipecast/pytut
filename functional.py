states = ["Kansas", "Nebraska", "North Dakota", "South Dakota"]
numbers = range(1, 101) # 1 up to 100

#singles: Imperative version
def imperative_singles(states):
    singles = []
    for state in states:

        if len(state.split()) == 1:
            singles.append(state)
    return singles

print(imperative_singles(states))

#Functional Version.
def functional_singles(states):
    return [state for state in states if len(state.split()) == 1]

def urlify(string):
    """Return a URL-friendly version of a string.

    Example: "North Dakota" -> "north-dakota"

    """
    return "-".join(string.lower.split())

#urls: Imperative version
def imperative_urls(states):
    urls = []
    for state in states:
        urls.append("-".join(state.lower().split()))
    return urls

print(imperative_urls(states))

# urls: myFunctional version
def functional_urls(states):
    return ["-".join(state.lower().split()) for state in states]

print(functional_urls(states))

# lengths: Imperative Version
def imperative_lengths(states):
    lengths = {}
    for state in states:
        lengths[state] = len(state)
    return lengths

print(imperative_lengths(states))

#lengths: Functional Version
def functional_lengths(states):
    return {state: len(state) for state in states}

print(functional_lengths(states))

# sum: Imperative soln
def imperative_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(imperative_sum(numbers))
print(sum(numbers))
