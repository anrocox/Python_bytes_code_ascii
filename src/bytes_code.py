#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

How to know the numeric code representing a character of a bytes
object in Python?

¿Cómo saber el código numérico que representa un carácter de un
objeto bytes en Python?
'''

#return an integer representing the Unicode code point of that character.
c = ord(b'w')
print(c)

#create a bytes object
b = b'hello world'

#generates a list of codes from the characters of bytes
l = list(b)
print(l)
