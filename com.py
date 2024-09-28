'''
Name: com.py
Description: Accepts an input and output file, then answers the input questions using the Phi-3 Model
Author: Benjamin Small
Date: 9/24/24
'''
from llama_cpp import Llama           #for dealing with gguf file
import argparse                       #for input and output destination

#Change the following line to the installed models path
model_path = "C:\\Users\\yapiz\\Documents\\CS325\\models\\Phi-3-mini-4k-instruct-q4.gguf"

#creates an instance of llama for chating with phi 3 model
llm = Llama(model_path=model_path, chat_format="chatml")


# ------------------------------------------------------------------------------------
# Deals with contacting the model and outputing a response ---------------------------
# ------------------------------------------------------------------------------------
def chat(str_input) -> str :
  response = llm.create_chat_completion(
    messages = [
      #Makes sure the model understands it's role
      {"role": "system", "content": "You are an assistant who answers questions."}, 
      #Sets up the users question and sends to the model
      {
        "role": "user",
        "content": str_input
      }
    ],
    response_format = {
      #Makes sure the responses will be valid characters for a text file
      "type": "json_object",
      #Makes sure that the response is of string type and will always output
      "schema": {
        "type": "object",
        "properties": {"response": {"type": "string"}},
        "required": ["response"],
      },
    }
  )
  #Outputs information
  return response["choices"][0]["message"]["content"].split("\"")[3]


# ------------------------------------------------------------------------------------
# Opens input and output files, reads from input, asks model for answers, then outputs
# answers to output file -------------------------------------------------------------
# ------------------------------------------------------------------------------------
def readwrite(input, output):
  in_file = open(input, "r")
  out_file = open(output, "w")

  for x in in_file :
    out_file.write("Q: " + x.strip() + "\n")
    out_file.write("A: " + chat(x.strip()) + "\n")


# ------------------------------------------------------------------------------------
# Main function: uses argparser for input and output, calls readwrite ----------------
# ------------------------------------------------------------------------------------
def main():
  parser = argparse.ArgumentParser()

  parser.add_argument(help="Enter filename for input", dest="input_dest", type=str)
  parser.add_argument(help="Enter filename for output", dest="output_dest", type=str)

  args = parser.parse_args()

  readwrite(args.input_dest, args.output_dest)


# ------------------------------------------------------------------------------------
# Run the program --------------------------------------------------------------------
# ------------------------------------------------------------------------------------
if __name__=="__main__" :
  main()

