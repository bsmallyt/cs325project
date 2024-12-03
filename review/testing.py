# ----------------------------------------------------------------------------------------------------
# testing.py 
# used to test the Selenium, Phi3, ProcessRating, and Graph class
# run command: pytest testing.py
# ----------------------------------------------------------------------------------------------------

from web import Selenium
from model import Phi3
from rating import ProcessRating
from graph import Graph

import os
import pytest

import matplotlib.pyplot as plt
from unittest.mock import patch

model_path = "C:\\Users\\yapiz\\Documents\\CS325\\models\\Phi-3-mini-4k-instruct-q4.gguf"
url = "https://www.amazon.com/Pack-Athletic-Gym-Mens-Shorts/dp/B0CRHF41F7/ref=sr_1_6?crid=1HDX81GCI00UY&dib=eyJ2IjoiMSJ9.Qfk_OlpuOMOTgkBKkL01zBHJ6PsDBo_z4Jr8NQ4R-ot8Ch6xvlGwFT-UU0T8263l0eDMT3K_0WSw9EEw1HuDMHF496y3qZCCbmkEhgLiJZdH3-m0D9ZuEi2QDNGg2ZzIUmkrw7wMuhPT0Cn68m-0HdKqMY0HwmKd6CIu2R4bn_8MApTndwbMbvZZOeq7QAB5sbAgqAXtsb29Wuyewkak9dOp_IIW5VK2QHCIY8qkTx150_AjZt1CRBmBX8zVCVVoKFn4Igb0Gxfcfm670KQULLFUlUAJWJ8BLooEoLgTAdI.v4F9h023ACS4A09oXbtJp3DqHjh_SSTaWf_MSgnESos&dib_tag=se&keywords=shorts+men&qid=1733169195&sprefix=%2Caps%2C132&sr=8-6"


# ----------------------------------------------------------------------------------------------------
# Webscrapper Tests ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
sel_file = "sel_test_out.txt"
sel = Selenium()


def test_selenium_return_reviews():  
  content = sel.grab_contents(url) 
  assert len(content) > 0

def test_selenium_write_contents():
  sel.write_to_file(sel_file) 
  assert os.path.exists(sel_file)

  with open(sel_file, "r") as f:
    file_content = f.read()
  assert len(file_content) > 0



# ----------------------------------------------------------------------------------------------------
# LLM Tests ------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
phi_in = "phi_test_in.txt"
phi_out = "phi_test_out.txt"

phi = Phi3()
phi.set_model(model_path)


def test_llm_chat():
  response = phi.chat("Hey, how are you")
  print(response)
  assert len(response) > 0

def test_llm_files():
  f = open(phi_in, "w")
  f.write("hello \n")
  f.write("hey \n")
  f.close()

  phi.files(phi_in, phi_out)
  assert os.path.exists(phi_out)

  with open(phi_out, "r") as f:
    file_content = f.read()
  assert len(file_content) > 0



# ----------------------------------------------------------------------------------------------------
# Rating Tests ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
pr = ProcessRating(Selenium(), Phi3(), model_path, url, "test")
pr_path = "model_outtest.txt"

def test_pr_process():
  pr.process()
  assert os.path.exists(pr_path)

  with open(pr_path, "r") as f:
    file_content = f.read()
  assert len(file_content) > 0

def test_pr_parse():
  vals = pr.parse_txt()
  assert len(vals) > 0



# ----------------------------------------------------------------------------------------------------
# Graph Tests ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
values = [[1,2,3],[3,2,1],[3,1,2]]

def test_graph():
  graph = Graph(values, ['hello', 'hello', 'hello'])

  with patch("matplotlib.pyplot.show") as mock_show:
    graph.display()
    mock_show.assert_called_once()


# ----------------------------------------------------------------------------------------------------
# Clean up -------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
@pytest.fixture(scope="session", autouse=True)
def cleanup_after_tests():
  yield
  os.remove(sel_file)
  os.remove(phi_in)
  os.remove(phi_out)
