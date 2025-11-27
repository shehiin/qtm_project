from scheduler import solve_scheduling
from visualize import show_plots

machines = [
    [0, 5, 9, 10, 10],
    [0, 4, 7, 11, 13],
    [0, 3, 6, 8, 9]
]

machine_names = [
    "3D Printer",
    "CNC Machine",
    "Testing Rig"
]

total_time = 4

allocations, max_benefit = solve_scheduling(machines, total_time)

print(f"Maximum Benefit: {max_benefit}")

for i, alloc in enumerate(allocations):
    benefit = machines[i][alloc]
    print(f"{machine_names[i]}: {alloc} units -> benefit {benefit}")

show_plots(machines, allocations, max_benefit, machine_names)

