#!/usr/bin/env python3
"""
Example file for testing @ references
"""

def hello_world():
    print("Hello, World!")
    
def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    hello_world()
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
