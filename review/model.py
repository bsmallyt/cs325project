from llama_cpp import Llama 
from abc import ABC, abstractmethod
import argparse 

model_path = "C:\\Users\\yapiz\\Documents\\CS325\\models\\Phi-3-mini-4k-instruct-q4.gguf"

# ----------------------------------------------------------------------------------------------------
# Basic Class for any llm to have, incase change to new model besides Phi3 ---------------------------
# ----------------------------------------------------------------------------------------------------
class LanguageModel :
  @abstractmethod
  def set_model(self) :
    pass
  def chat(self, str_input) -> str : 
    pass
  def files(self, input_path, output_path) :
    pass

# ----------------------------------------------------------------------------------------------------
# Phi3 Class: set_model, files -----------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
class Phi3(LanguageModel) :
  # Pass whatever necessary for the model to be created, aka model_path, then initilize model
  def set_model(self, model_path):
    self.llm = Llama(model_path=model_path, chat_format="chatml", n_ctx=8192)

  # Takes string input, passes to model, gathers and returns response
  def chat(self, str_input) -> str :
    response = self.llm.create_chat_completion(
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
    return response["choices"][0]["message"]["content"].split("\"")[3].strip()
  
  # takes an input file and output file, reads line by line into chat feature, outputs to file
  def files(self, input_path, output_path) :
    in_file = open(input_path, "r")
    out_file = open(output_path, "w")

    for x in in_file :
      out_file.write("Q: " + x.strip() + "\n")
      out_file.write("A: " + self.chat(x.strip()) + "\n")

    in_file.close()
    out_file.close()




# ----------------------------------------------------------------------------------------------------
# Main Function: takes file path as input and reads to model line by line and outputs response to 
# second file path -----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument(help="Enter filename for input", dest="input_dest", type=str)
  parser.add_argument(help="Enter filename for output", dest="output_dest", type=str)
  args = parser.parse_args()

  phi = Phi3()
  phi.set_model(model_path)
  phi.files(args.input_dest, args.output_dest)

# ------------------------------------------------------------------------------------
# Run main ---------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
if __name__=="__main__" :
  main()