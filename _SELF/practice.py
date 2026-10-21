# . Fuel Tank Drain

# A fuel tank is completely full at the start.
# An engine uses the same amount of fuel every hour. 
# Read two positive integers, one per line: capacity (litres in the full tank) and usage (litres burned every hour).

# Every hour, subtract the usage from the fuel level. 
# If subtracting the full amount would take the level below 0, 
# just set it to 0, so the fuel level never goes below 0.

# Print one line for every hour in the form:
# Hour <h>: Fuel left = <f>

# When the tank is empty (the fuel level is 0), 
# print how many hours it took, in the form:
# Tank empty in <n> hour(s).

# Input
# Two lines. Line 1: the integer capacity. Line 2: the integer usage.

# Output
# One line for every hour, followed by the final line.

# Example 1
# Input:

# 1000
# 300

# Output:

# Hour 1: Fuel left = 700
# Hour 2: Fuel left = 400
# Hour 3: Fuel left = 100
# Hour 4: Fuel left = 0
# Tank empty in 4 hour(s).

# capacity = int(input().strip())
# usage = int(input().strip())

# fuel = capacity
# hour = 0
# while fuel > 0:
#     hour += 1
#     fuel = max(fuel - usage, 0)
#     print(f"Hour {hour}: Fuel left = {fuel}")
# print(f"Tank empty in {hour} hour(s).")

# 2. Step Goal Tracker

# A person wants to reach a total step goal. 
# Read two positive integers,
#  one per line: goal (total steps to reach) and daily (steps walked every day).

# Every day, add the daily steps to the running total. 
# Unlike a tank, the total is not capped, so it may go above the goal.

# Print one line for every day in the form:
# Day <d>: Total steps = <s>

# When the total is greater than or equal to the goal, print:
# Goal reached in <n> day(s).

# Input
# Two lines. Line 1: the integer goal. Line 2: the integer daily.

# Output
# One line for every day, followed by the final line.

# Example 1
# Input:

# 10000
# 4000

# Output:

# Day 1: Total steps = 4000
# Day 2: Total steps = 8000
# Day 3: Total steps = 12000
# Goal reached in 3 day(s)

# goal = int(input().strip())
# daily = int(input().strip())

# total = 0
# day = 0
# while total < goal:
#     day += 1
#     total += daily
#     print(f"Day {day}: Total steps = {total}")

# print(f"Goal reached in {day} day(s).")