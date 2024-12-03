# ----------------------------------------------------------------------------------------------------
# run.py 
# takes in file input, with amazon listing urls line by line, then also the names of each product
# run command: python run.py input_url.txt -l iphone12 iphone14 iphoneXP iphone11
# ----------------------------------------------------------------------------------------------------

from web import Selenium
from model import Phi3
from rating import ProcessRating
from graph import Graph

import threading
import argparse
import queue

model_path = "C:\\Users\\yapiz\\Documents\\CS325\\models\\Phi-3-mini-4k-instruct-q4.gguf"

# For the purpose of using multi-threading, to speed up process, uses ProcessRating class
# with Selenium and Phi3 to gather amount of positive, neutral, and negative reviews in
# the format of [0,0,0], then adds them to queue
def get_vals(webscrapper, model, model_path, url, name, q, i):
  pr = ProcessRating(webscrapper, model, model_path, url, name)
  pr.process()
  vals = pr.parse_txt()
  q.put((i, vals))


# Multithreads the previous definition, then sorts the queue and returns values 
# format : [[0,0,0], [0,0,0], ...]
def get_values(input_dest):
  url_file = open(input_dest, "r")
  q = queue.Queue()
  threads = []
  values = []
  results = []

  #threads previous definition
  i=0
  for url in url_file:
    t = threading.Thread(target=get_vals, args=(Selenium(), Phi3(), model_path, url, str(i), q, i))
    threads.append(t)
    t.start()
    i+=1
  for t in threads:
    t.join()

  # gathers queue values and sorts
  while not q.empty():
    results.append(q.get())
  results.sort(key=lambda x: x[0])

  # takes only important part of queue (not order num)
  for val in results:
    values.append(val[1])

  # close and return values
  url_file.close()
  return values
  

# ----------------------------------------------------------------------------------------------------
# Main Function: takes url_path, calls get values, then makes a graph --------------------------------
# ----------------------------------------------------------------------------------------------------
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument(help="Enter filename for input", dest="input_dest", type=str)
  parser.add_argument('-l', '--list', nargs='+', help="List of Product Names", dest="input_list", required=True)
  args = parser.parse_args()

  
  values = get_values(args.input_dest)
  graph = Graph(values, args.input_list)
  graph.display()

# ------------------------------------------------------------------------------------
# Run main ---------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
if __name__=="__main__" :
  main()