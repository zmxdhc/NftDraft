# test_nftdraft.py
"""
Tests for NftDraft module.
"""

import unittest
from nftdraft import NftDraft

class TestNftDraft(unittest.TestCase):
    """Test cases for NftDraft class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = NftDraft()
        self.assertIsInstance(instance, NftDraft)

    def test_run_method(self):
        """Test the run method."""
        instance = NftDraft()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
