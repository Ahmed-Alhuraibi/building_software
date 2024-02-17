# ### Plot
# 1. Plot two or more columns in your data using `matplotlib`, `seaborn`, or `plotly`. Make sure that your plot has labels, a title, a grid, and a legend.


# matplotlib chart


import pandas as pd

import matplotlib.pyplot as plt

import argparse

import logging


parser = argparse.ArgumentParser(description='Bed Occupancy Analysis')
parser.add_argument('--title', '-t', type=str, help='Plot title')
parser.add_argument('--output_file', '-o', type=str, help='Output plot filename')
parser.add_argument('config', type=str, help='Path to the configuration file')
parser.add_argument('--std_font_size', '-s', type=int, help='Standard font size')
parser.add_argument('--hd_font_size', '-hs', type=int, help='Header font size')

args = parser.parse_args()
try:
    df_Col_Rename = pd.read_csv(args.config)
    logging.info(f'Successfully loaded {args.config}')
except Exception as e:
    logging.error('Error loading dataset', exc_info=e)
    raise e

# defining variables
plot_figsize = (25, 10)
std_font_size = args.std_font_size
header_font_size=args.hd_font_size
group_by_column = ['CITY','PROGRAM_AREA','PROGRAM_MODEL','SECTOR','CAPACITY_TYPE']

Program_summary = (df_Col_Rename.groupby(group_by_column)
                 .agg(CAP_ACT_BED_TOTAL=('CAPACITY_ACTUAL_BED', 'sum'),
                      OCCUPIED_BED_TOTAL=('OCCUPIED_BEDS', 'sum'),
                      DAY_CNT=('DAY', 'count'),
                      OCCUPANCY_RATE_BED_MEAN=('OCCUPANCY_RATE_BEDS', 'mean')))



# To Create a figure and axis objects
fig, ax = plt.subplots(figsize=plot_figsize) 

# Plot for unoccupied beds
unoccupied = ax.scatter(df_Col_Rename['OCCUPANCY_RATE_BEDS'], df_Col_Rename['UNOCCUPIED_BEDS'], label='Unoccupied Beds')

# Plot for occupied beds
occupied = ax.scatter(df_Col_Rename['OCCUPANCY_RATE_BEDS'], df_Col_Rename['OCCUPIED_BEDS'], label='Occupied Beds')


# Adding labels and title
ax.set_xlabel('Rate',fontsize=std_font_size)
ax.set_ylabel('Number of Beds',fontsize=std_font_size)
ax.set_title('Bed Occupancy Analysis',fontsize=header_font_size)
ax.set_axisbelow(True)


# legend and position it out of the plot area
ax.legend(loc='upper left',fontsize=std_font_size)

# Displaying the plot
plt.grid()
plt.show()

plt.savefig(f'{args.output_file}.png')

# To run this file from terminal 
# python Py_Assign2_Panda_Visualization_ArgParse.py -o config_output --std_font_size 14 Alhuraibi_alamoudi_ahmed_python_assignment2_proc.csv
