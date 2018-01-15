#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)


import os
import unittest



case_path = os.path.join(os.getcwd(),'test_case')
print(case_path)
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(all_case())