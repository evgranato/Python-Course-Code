from random import choice

def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("is healthy must be a bool")
    ending = "because YOLO"
    if is_healthy:
        ending = "because my body is a temple"
    return f"I'm eating {food}, {ending}"

def nap(num_hours):
    if num_hours <= 1:
        return f"I'm feeling refreshed after my {num_hours} hour nap"
    return f"Ugh I overslept. I didn't mean to nap for {num_hours} hours"

def is_funny(person):
    if person is "tim":
        return False
    return True

def laugh():
    return choice(('lol', 'haha', 'tehehe'))