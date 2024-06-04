
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

def long_planeteer_calls(calls):
    for call in calls:
        if (len(call) > 4):
            return True
    return False

def find_the_cheese(items):
    cheeses = ["cheddar", "gouda", "camembert"]
    for item in items:
        if item in cheeses:
            return item
    return None
    
roll_call_dwarves(["Dopey", "Grumpy", "Bashful"])
print(summon_captain_planet(["carrot", "cucumber", "pepper"]))