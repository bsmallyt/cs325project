from llama_cpp import Llama
import argparse
import os

model_path = "C:\\Users\\yapiz\\Documents\\CS325\\models\\Phi-3-mini-4k-instruct-q4.gguf"
llm = Llama(model_path=model_path)


def contact(str):
  prompt = "Q: " + str + "A:"
  response = llm(
    prompt, 
    max_tokens=None, # generate a response without length restrictions
    stop=["Q:", "\n"], # stop after one respone
    echo=False # repeat prompt in response
  )
  return response["choices"][0]['text'].strip()



def readwrite(input, output):
  in_file = open(input, "r")
  out_file = open(output, "w")

  for x in in_file :
    out_file.write("Q: " + x.strip() + "\n")
    print(contact(x.strip()))
    out_file.write("A: " + contact(x.strip()) + "\n")



def main():
  parser = argparse.ArgumentParser()

  parser.add_argument(help="Enter filename for input", dest="input_dest", type=str)
  parser.add_argument(help="Enter filename for output", dest="output_dest", type=str)

  args = parser.parse_args()

  readwrite(args.input_dest, args.output_dest)



if __name__=="__main__" :
  main()



#os.system('cls')

