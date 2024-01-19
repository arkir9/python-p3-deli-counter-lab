def line(deli_counter):
    if not deli_counter:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently: " + " ".join([f"{i + 1}. {person}" for i, person in enumerate(deli_counter)])
        print(line_str)
        
def take_a_number(deli_counter, person):
    deli_counter.append(person)
    print(f"Welcome, {person}. You are number {len(deli_counter)} in line.")
def now_serving(deli_counter):
    if deli_counter:
        print(f"Currently serving {deli_counter[0]}.")
        deli_counter.pop(0)
    else:
        print("There is nobody waiting to be served!")