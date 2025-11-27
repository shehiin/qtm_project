import matplotlib.pyplot as plt

def show_plots(machines, allocations, max_benefit, machine_names=None):
    if machine_names is None:
        machine_names = [f"Machine {i+1}" for i in range(len(machines))]
    
    benefits = [machines[i][allocations[i]] for i in range(len(machines))]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax1.bar(machine_names, allocations, color='steelblue', edgecolor='black')
    ax1.set_ylabel('Time Units')
    ax1.set_title('Time Allocation')
    ax1.grid(axis='y', alpha=0.3)
    
    ax2.bar(machine_names, benefits, color='coral', edgecolor='black')
    ax2.set_ylabel('Benefit')
    ax2.set_title('Benefit per Machine')
    ax2.grid(axis='y', alpha=0.3)
    
    fig.suptitle(f'Maximum Total Benefit: {max_benefit}', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.show()

