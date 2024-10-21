from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Test case for positive sentiment
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1[1], 'SENT_POSITIVE')  # Accessing label from tuple
        
        # Test case for negative sentiment
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2[1], 'SENT_NEGATIVE')  # Accessing label from tuple
        
        # Test case for neutral sentiment
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3[1], 'SENT_NEUTRAL')  # Accessing label from tuple

# This will run the tests when this script is executed
if __name__ == '__main__':
    unittest.main()
