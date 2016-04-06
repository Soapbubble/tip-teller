#!/bin/python3

import os
import logging

lookup_ext = "*"
recursive_lookup = True # look in children directories inside the lookup paths
tip_declarator = "^\[tip\]\s*$" # everything that follows after a line matching this regex is considered a new tip

def get_lookup_paths(fname):
  with open(fname, 'r') as f:
    lines = f.read().splitlines()
    return lines

def get_all_files(paths):
  all_files = []
  for path in paths:
    all_files += get_files_in(path)
  return all_files

def get_files_in(top_path):
  all_files = []
  # logging.debug("Searching files in: '{dir}'...".format(dir=top_path))
  for root, dirs, files in os.walk(top_path, topdown=False):
    for file in files:
      abs_file_path = os.path.join(root, file)
      all_files.append(abs_file_path)
  return all_files

def count_tips_in_file(file):
  import re
  pattern = re.compile(tip_declarator)
  nb_tips = 0
  with open(file, 'r') as f:
    for line in f:
      if (pattern.match(line)):
        nb_tips += 1
  return nb_tips

def count_tips_in(files):
  nb_tips = 0
  for file in files:
    nb_tips += count_tips_in_file(file)
  return nb_tips

def main():
  import argparse
  parser = argparse.ArgumentParser()
  parser.parse_args()

  input_lookup_paths = get_lookup_paths("lookup_paths.txt")
  logging.debug('Will search for tips in the following directories: {}'.format(input_lookup_paths))

  all_files = get_all_files(input_lookup_paths)
  logging.debug("Discovered the following files:")
  logging.debug(all_files)

  nb_tips = count_tips_in(all_files)
  logging.debug("Found a total of {} tips".format(nb_tips))
  

if __name__ == "__main__":
  # configure the logging system
  logging.basicConfig(level=logging.DEBUG)

  # launch the app
  main()
