import argparse     
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def read(input):
  in_file = open(input, "r")

  content = in_file.read()
  engine.say(content)

  engine.runAndWait()

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument(help="Enter filename for input", dest="input_dest", type=str)
  args = parser.parse_args()

  read(args.input_dest)

if __name__=="__main__" :
  main()
