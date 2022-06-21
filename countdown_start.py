# Use the recursion to implement a countdown counter

def countdown(x):
    if x == 0: # When the countdown hits 0 break recursion
        print("Done!")
        return
    else: # If countdown is not 0 continue
        print(x, "...")
        countdown(x-1)

countdown(5) # First count down value
