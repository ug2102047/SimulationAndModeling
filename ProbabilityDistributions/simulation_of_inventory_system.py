 
import random
import numpy as np
 
# ----------------------------
# Parameters
# ----------------------------
SIM_TIME = 120  # months

s = 20
S = 60

K = 32      # setup cost
i = 3       # per item cost
h = 1       # holding cost
p = 5       # backlog cost

inventory = 60          # I(0)
outstanding_order = 0
order_arrival_time = None

time = 0
last_event_time = 0

area_holding = 0
area_backlog = 0
total_order_cost = 0

# demand size distribution
def demand_size():
    return random.choices(
        [1, 2, 3, 4],
        weights=[1/6, 1/3, 1/3, 1/6]
    )[0]

# ----------------------------
# Simulation loop
# ----------------------------
while time < SIM_TIME:

    # next demand time
    time_to_demand = np.random.exponential(0.1)
    next_demand_time = time + time_to_demand

    # next order arrival time
    if order_arrival_time is not None:
        next_event_time = min(next_demand_time, order_arrival_time)
    else:
        next_event_time = next_demand_time

    # update holding & backlog area
    holding = max(inventory, 0)
    backlog = max(-inventory, 0)

    area_holding += holding * (next_event_time - time)
    area_backlog += backlog * (next_event_time - time)

    time = next_event_time

    # ----------------------------
    # Order arrives
    # ----------------------------
    if order_arrival_time == time:
        inventory += outstanding_order
        outstanding_order = 0
        order_arrival_time = None

    # ----------------------------
    # Demand occurs
    # ----------------------------
    else:
        d = demand_size()
        inventory -= d

    # ----------------------------
    # Monthly review (order decision)
    # ----------------------------
    if outstanding_order == 0 and inventory < s:
        Z = S - inventory
        total_order_cost += K + i * Z

        lead_time = random.uniform(0.5, 1)
        order_arrival_time = time + lead_time
        outstanding_order = Z

# ----------------------------
# Results
# ----------------------------
avg_holding_cost = h * area_holding / SIM_TIME
avg_backlog_cost = p * area_backlog / SIM_TIME
avg_order_cost = total_order_cost / SIM_TIME

total_cost = avg_holding_cost + avg_backlog_cost + avg_order_cost

print("Average monthly holding cost:", avg_holding_cost)
print("Average monthly backlog cost:", avg_backlog_cost)
print("Average monthly ordering cost:", avg_order_cost)
print("Total average monthly cost:", total_cost)
