The following project was made to communicate with the Phi-3 language model.

Installing language Model (Phi-3):
  1. Navigate to the Phi-3-mini-4k-instruct-q4.gguf page on the huggingface website. https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/blob/main/Phi-3-mini-4k-instruct-q4.gguf
  2. Download the model. The download selection can be found near the center of the page.
  3. Move the model file to the file path of your choice. Save this path as it will be used later.

Installing Conda:
  1. You can install the miniconda software using the installer links on the following page: https://docs.anaconda.com/miniconda/

Setting Up Phi-3 Communication:
  1. Download or Copy the entire project on home computer.
  2. Move the folder to your preferred destination.
  3. Open up the com.py file using something like microsofts visual studio code. 
  4. Change the model path to the destination where you placed the Phi-3 model in a previous step.
  5. Open a terminal and navigate to the folder from step 2. 
  6. Run the following command to make the conda environment, then open it: 
  ```powershell
  conda env create -f requirement.yaml
  conda activate phi3env
  ```

Communicating with Phi-3:
  1. You must provide an input file with questions separated by line, and a file for output, when running the program. 
  2. An example is as followed:
  ```powershell
  python com.py input.txt output.txt
  ```

