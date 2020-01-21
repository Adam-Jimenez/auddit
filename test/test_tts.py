# Python code to demonstrate working of unittest 
import unittest 
from src.tasks.text_to_speech.task import save_tts, save_gtts
  
class TestTTS(unittest.TestCase): 
      
    def setUp(self): 
        pass
  
    def test_normal(self): 
        save_tts("I am a potato")
        save_gtts("I am a potato")
  
if __name__ == '__main__': 
    unittest.main() 
