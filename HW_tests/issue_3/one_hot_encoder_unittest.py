import unittest
from one_hot_encoder import fit_transform

class TestTF(unittest.TestCase):
   def test_tf_equal(self):
       actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
       expected = [('Moscow', [0, 0, 1]), ('New York', [0, 1, 0]), ('Moscow', [0, 0, 1]), ('London', [1, 0, 0])]

       self.assertEqual(actual, expected)
       
   def test_tf_notequal(self):
       actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
       expected = [('Moscow', [0, 0, 1]), ('New York', [0, 1, 0]), ('London', [1, 0, 0])]

       self.assertNotEqual(actual, expected)

   def test_empty(self):
       actual = list(fit_transform(''))
       expected = [('', [1])]

       self.assertEqual(actual, expected)

   def test_NotIn(self):
        actual = fit_transform(['a', 'b'])
        
        self.assertNotIn('jgj', actual)
        
   def exception(self):
       with self.assertRaises(TypeError):
           fit_transform()
        
if __name__ == '__main__':
   unittest.main()
