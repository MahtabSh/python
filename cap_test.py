import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'mahtab'
        res = cap.cap_text(text)
        self.assertEqual(res,'Mahtab')
    
    def test_multiple_word(self):
        text = 'i should learn more'
        res = cap.cap_text(text)
        self.assertEqual(res,'I Should Learn More')

if __name__=='__main__':
   unittest.main()
