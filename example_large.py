from scheduler import solve_scheduling
from visualize import show_plots

machines = [
    [0, 5, 9, 10, 10, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14],
    [0, 4, 7, 11, 13, 16, 18, 19, 20, 20, 21, 21, 22, 22, 23],
    [0, 3, 6, 8, 9, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13],
    [0, 6, 10, 13, 15, 17, 18, 19, 19, 20, 20, 21, 21, 21, 22],
    [0, 8, 14, 18, 21, 23, 24, 25, 25, 26, 26, 27, 27, 27, 28],
    [0, 10, 18, 24, 28, 31, 33, 35, 36, 37, 38, 38, 39, 39, 40],
    [0, 7, 13, 17, 20, 22, 24, 25, 26, 27, 27, 28, 28, 29, 29]
]

machine_names = [
    "3D Printer",
    "CNC Machine",
    "Testing Rig",
    "Laser Cutter",
    "GPU Cluster",
    "Distillation Col.",
    "Network An."
]

total_time = 14

allocations, max_benefit = solve_scheduling(machines, total_time)

print(f"Maximum Benefit: {max_benefit}")
print(f"Total Time Used: {sum(allocations)}/{total_time}\n")

for i, alloc in enumerate(allocations):
    benefit = machines[i][alloc]
    print(f"{machine_names[i]:<20} {alloc} units -> benefit {benefit}")

show_plots(machines, allocations, max_benefit, machine_names)

