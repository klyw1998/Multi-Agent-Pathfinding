# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 19:58:26 2021

@author: kris

MIT License

Copyright (c) [2021] [Liangyawei Kuang @HKUST]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import math

class Vector2(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.thresh = 0.000001
    
    # Arithmetic Methods
    
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __div__(self, scalar):
        if scalar != 0 :
            return Vector2(self.x / float(scalar), self.y / float(scalar))
        return None
    
    def __truediv__(self, scalar):
        return self.__div__(scalar)
    
    # Equality Methods
    
    def __eq__(self, other):
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True
        return False
    
    def magnitudeSquared(self):
        return self.x**2 + self.y**2
    
    def magnitude(self):
        return math.sqrt(self.magnitudeSquared())
    
    def copy(self):
        return Vector2(self.x, self.y)
    
    def asTuple(self):
        return self.x, self.y
    
    def asInt(self):
        return int(self.x), int(self.y)
    
    # String Method: this method doesn't affect the functionality of the game or anything, it's really a convenience function so that we can easily print out the vector
    
    def __str__(self):
        return "<" + str (self.x) + ", " + str(self.y) + ">"