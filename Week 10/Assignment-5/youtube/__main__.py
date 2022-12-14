"""
XB_0082: The Youtube Trending Analyzer
Author: Leon Willems

Copyright (c) 2021-2022 - Eindhoven University of Technology - VU Amsterdam, The Netherlands
This software is made available under the terms of the MIT License.
"""

import youtube.tools as tools

# Don't execute this if file is imported
if __name__ == '__main__':
    entries = tools.read_file('videos.csv')
    tools.dataset_viewer(entries)
    tools.analyzer(entries)
