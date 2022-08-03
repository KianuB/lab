import unittest
from classes import *  # import statement needed to gain access to Television class


class TestCase(unittest.TestCase):
    def setUp(self):
        self.t1 = Television()

    def tearDown(self):
        del self.t1

    def test_init(self):
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = False, Channel = 0, Volume = 0')

    def test_power(self):
        self.t1.power()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = True, Channel = 0, Volume = 0')
        self.t1.power()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = False, Channel = 0, Volume = 0')

    def test_channel_up(self):
        self.t1.power()
        self.t1.channel_up()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = True, Channel = 1, Volume = 0')
        self.t1.channel_up()
        self.t1.channel_up()
        self.t1.channel_up()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = True, Channel = 0, Volume = 0')

    def test_channel_down(self):
        self.t1.power()
        self.t1.channel_down()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = True, Channel = 3, Volume = 0')
        self.t1.channel_down()
        self.t1.channel_down()
        self.t1.channel_down()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = True, Channel = 0, Volume = 0')

    def test_volume_up(self):
        self.t1.power()
        self.t1.volume_up()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = True, Channel = 0, Volume = 1')
        self.t1.power()
        self.t1.volume_up()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = True, Channel = 0, Volume = 1')
        self.t1.power()
        self.t1.volume_up()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = True, Channel = 0, Volume = 2')
        self.t1.volume_up()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = True, Channel = 0, Volume = 2')
        
    def test_volume_down(self):
        self.t1.power()
        self.t1.volume_up()
        self.t1.volume_up()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = True, Channel = 0, Volume = 2')
        self.t1.volume_down()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = True, Channel = 0, Volume = 1')
        self.t1.power()
        self.t1.volume_down()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = True, Channel = 0, Volume = 1')
        self.t1.power()
        self.t1.volume_down()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = True, Channel = 0, Volume = 0')
        self.t1.volume_down()
        self.assertEqual(self.t1.__str__(), 'TV status: Is on = True, Channel = 0, Volume = 0')


if __name__ == '__main__':
    unittest.main()
