import os

# ----------------------------------------------------------------------------------------------------
# Process Rating Class, takes a webscrapper, language model, url and computes whether ratings are ----
# positive, nuetral, or negative, returns list with three digits -------------------------------------
# ----------------------------------------------------------------------------------------------------
class ProcessRating:
  def __init__(self, webscrapper, model, model_path, url, name):
    self.web = webscrapper
    self.model = model
    self.model_path = model_path
    self.url = url 
    self.review_file_name = ("review_out" + name + ".txt")
    self.inquery_file_name = ("inquery_file" + name + ".txt")
    self.model_file_name = ("model_out" + name + ".txt")

    self.vals = [0,0,0]

  # grabs reviews from url, puts them into a file, appends the rating question to each review, 
  # submits new file to llm and outputs results to file
  def process(self):
    #grab web reviews 
    self.web.grab_contents(self.url)
    self.web.write_to_file(self.review_file_name)

    #open files
    review_file = open(self.review_file_name, "r")
    inquery_file = open(self.inquery_file_name, "w")

    #create the inquery file for the model
    for review in review_file:
      inquery_file.write(review.strip() + " If you think the previous review is postive reply with positive, if neutral: neutral, and negative: negative. \n")
    
    #close files 
    review_file.close()
    inquery_file.close()

    #have the model process the inqueries 
    self.model.set_model(self.model_path)
    self.model.files(self.inquery_file_name, self.model_file_name)

    #delete the no longer needed files
    os.remove(self.review_file_name)
    os.remove(self.inquery_file_name)

  # takes llm output file and adds up positive, neutral, and negative values, returns them as list
  def parse_txt(self):
    file = open(self.model_file_name, "r")
    i = 1

    for line in file:
      if (i%2 == 0):
        val = line.split("A:")[1].strip()
        if val == "positive":
          self.vals[0]+=1
        elif val == "neutral":
          self.vals[1]+=1
        elif val == "negative":
          self.vals[2]+=1
      i+=1

    file.close()
    os.remove(self.model_file_name)
    return self.vals
  
  # returns vals
  def get_vals(self):
    return self.vals
