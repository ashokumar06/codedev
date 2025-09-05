#!/usr/bin/env python3
"""
Sample Python project for testing CodeAS
"""

def hello_world():
    """Print hello world message"""
    print("Hello from CodeAS sample project!")

def calculate_fibonacci(n):
    """Calculate fibonacci number"""
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

if __name__ == "__main__":
    hello_world()
    print(f"Fibonacci(10) = {calculate_fibonacci(10)}")
