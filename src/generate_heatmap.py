import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

def generate_heatmap(csv_path, output_path):
    # Read data
    df = pd.read_csv(csv_path)
    
    # Create a 5x5 matrix of counts (Likelihood vs Impact)
    matrix = pd.crosstab(df['likelihood'], df['impact'], 
                         dropna=False).reindex(index=range(1,6), 
                                               columns=range(1,6), 
                                               fill_value=0)
    
    # Convert to numpy for heatmap
    data = matrix.values
    
    # Plot
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(data, annot=True, fmt='d', cmap='Reds', 
                     cbar_kws={'label': 'Number of Risks'},
                     xticklabels=range(1,6), yticklabels=range(1,6),
                     linewidths=0.5, linecolor='white')
    
    ax.set_xlabel('Impact', fontsize=12)
    ax.set_ylabel('Likelihood', fontsize=12)
    ax.set_title('5×5 Risk Heatmap', fontsize=16, fontweight='bold')
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Heatmap saved to {output_path}")

if __name__ == "__main__":
    # Default paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_path = os.path.join(project_root, 'data', 'sample_risks.csv')
    out_path = os.path.join(project_root, 'outputs', 'risk_heatmap.png')
    
    # Allow custom paths via command line arguments
    if len(sys.argv) >= 2:
        data_path = sys.argv[1]
    if len(sys.argv) >= 3:
        out_path = sys.argv[2]
    
    if not os.path.exists(data_path):
        print(f"Error: Data file not found at {data_path}")
        sys.exit(1)
    
    generate_heatmap(data_path, out_path)