
def roll_call_dwarves(dwarves):
    num = 1
    for dwarf in dwarves:
        print(str(num) + '.', dwarf)
        # print(f"{num}. {dwarf}")
        num += 1

def summon_captain_planet(planeteer_calls):
    result = []
    for calls in planeteer_calls:
        new_call = calls.capitalize() + "!"
        result.append(new_call)
    return result

def long_planeteer_calls():
    pass

def find_the_cheese():
    pass

roll_call_dwarves(["Dopey", "Grumpy", "Bashful"])
print(summon_captain_planet(["carrot", "cucumber", "pepper"]))