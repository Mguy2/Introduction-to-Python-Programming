"""
XB_0082: The Youtube Trending Analyzer
Author: Leon Willems

Copyright (c) 2021-2022 - Eindhoven University of Technology - VU Amsterdam, The Netherlands
This software is made available under the terms of the MIT License.
"""

import csv
from typing import List, Dict, Tuple
from pathlib import Path


def test(entries: List[List], views: int = None) -> int:
    for entry in entries[1:]: 
        if entry[12]:
            print ("found one")

def find_more_than_x_views(entries: List[List], views: int = None) -> int:
    """
    Runs through the dataset and calculates the number of trending
    videos with more than a certain number of views, given by user
    :param entries: the dataset, list of videos
    :param views: threshold number of views
    :return: number of videos with more than the threshold views
    """
    if views is None:
        views = input('Views: ')
    more_than_x_views = []
    for entry in entries[1:]:  # We skip the first entry, because they are column names
        if int(entry[7]) > int(views):
            more_than_x_views.append(entry)

    print(len(more_than_x_views))

    return len(more_than_x_views)


def total_views_per_day(entries: List[List], output_file_name: str = None) -> int:
    """
    Calculates, for each day, the sum of views for all videos on
    that day, and outputs this to a CSV file.
    :param entries: the dataset, list of videos
    :param output_file_name: name of the output file (including .csv)
    :return: returns the number of days included in the file
    """
    view_counter = {}

    #// BEGIN_TODO [task_1] Total views per day

    # Lovely two lines of code :)
    for lists in entries[1:]:
            view_counter[lists[1]] = view_counter.get(str(lists[1]), 0) + int(lists[7])

    # // END_TODO [task_1]

    if output_file_name is None:
        output_file_name = input('What will be the name of your output file? ')

    path = Path(__file__).parent / f'../data/{output_file_name}'
    with open(path, 'w', newline='') as csvfile:
        views_writer = csv.writer(csvfile, delimiter=',')
        for date, views in view_counter.items():
            views_writer.writerow([date, views])

    return len(view_counter)

#// BEGIN_TODO [task_2] popular videos


def most_popular(entries :List[List[any]]) -> None:
    """Prints the most popular video by user-given parameters.

    Args:
        entries (List[List[any]]): List of lists where the former represents a video and the latter an index filled with information.
    """
    option = ""
    while type(option) != int or option < 1 or option > 3:
        option = int(input("Please choose an option between 1 and 3:\n"))
    target_video :Tuple = ("video", 0, "message")
    for entry in entries[1:]:
            if int(entry[7]) > target_video[1] and option == 1:
                target_video = (entry[2], int(entry[7]), "highest views")
            if int(entry[8]) - int(entry[9]) > target_video[1] and option == 2:
                target_video = (entry[2], (int(entry[8]) - int(entry[9])), "most likes minus dislikes")
            if int(entry[8]) <= 0:
                continue
            elif int(entry[8])/(int(entry[8])+int(entry[9])) > target_video[1] and option == 3:
                target_video = (entry[2], int(entry[8])/(int(entry[8])+int(entry[9])), "best like to dislike ratio")
    print(f"Video: {target_video[0]}, has the {target_video[2]}: {target_video[1]}")


#// END_TODO [task_2]

#// BEGIN_TODO [task_3] controversial videos


def controversial_videos(entries :List[List[any]]) -> None:
    """Prints a table with average, maximum and minumum ratios for comments enabled and disabled.

    Args:
        entries (List[List[any]]): List of lists where the former represents a video and the latter an index filled with information.
    """
    data_true = [] # declare lists in which to store all ratios
    data_false = []
    for entry in entries[1:]: # for loop where we append all ratios to the lists
        if int(entry[8]) > 0 and entry[12] == "True":
            data_true.append(int(entry[8]) / (int(entry[8]) + int(entry[9])))
        if int(entry[8]) > 0 and entry[12] == "False":
            data_false.append(int(entry[8]) / (int(entry[8]) + int(entry[9])))
    # Print Average, maximum, minimum in a table with nice lines
    # Average = sum(list) / len(list) and is calculated in the print
    print("-"*62,"\n","Comments Enabled", " "*10, "false", ' '*17, \
        "true\n","-"*62,"\n","Average:", ' '*12, (sum(data_true) / len(data_true)), \
        ' '*3, (sum(data_false) / len(data_false)), "\n", "-"*62, "\n", "Maximum:", \
        ' '*19, max(data_true), ' '*18, max(data_false), "\n", "-"*62, "\n", \
        "Minimum:", ' '*12, min(data_true), ' '*3, min(data_false), "\n", "-"*62, \
         "\n", sep='')
 

#// END_TODO [task_3]






