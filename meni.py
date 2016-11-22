#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open('meni.txt', 'w') as file:
    file.write('{:30}'.format('Jed') + "Cena (€) \n\n")


while True:
    jed = raw_input("Vnesi jed: ")
    cena = raw_input("Vnesi ceno: ")

    with open('meni.txt', 'a') as file:
        file.write('{:30}'.format(jed) + cena + "\n")

file.close()
