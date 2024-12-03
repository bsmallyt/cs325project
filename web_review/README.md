The following project was created using python and selenium, its purpose to grab the reviews for any amazon listing. Installation and usage requires the miniconda software, all dependencies are listed in the requirement.yaml file.

Installing Conda:
  1. You can install the miniconda software using the installer links on the following page: https://docs.anaconda.com/miniconda/

Setting Up Webscrapper:
  1. Download or Copy the entire project on home computer. One way you can do this is by selecting the code button in top right of project and choosing the download zip file option.
  2. Unzip and move the folder to your preferred destination. 
  3. Navigate to file explorer and open the CS325PROJECT folder, then open the web_review folder using the code editor of your choice, or your terminal
  6. Run the following command to make the conda environment, then open it: 
  ```powershell
  conda env create -f requirement.yaml
  conda activate webReview
  ```

Using the Webscrapper:
  1. You must provide an input file with the amazon listing url seperated by line. Outputs will be created in seperate files based on the line number of the url; output<# of line>.txt
  2. Simply by using the the input_url.txt file already in the project, you can change or append urls in that text file then run the following code to execute the program.
  ```powershell
  python grab_review.py input_url.txt
  ```

