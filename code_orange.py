# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 07:18:05 2020

@author: krish
Primary goal:
This program was created as an ABM model of the disease spread during the COVID-19 outbreak of 2019-20

Secondary goal:
To extend this model to a general frame for simulation spreads
"""

#Imported Libraries
import networkx as nx
import matplotlib.pyplot as plt

#Step 1:
# Making a fully connected graph
class Country(object):
    def __init__(self, name, population):
        self.name = name
        self.population = population
        
    def __str__(self):
        return "%s has a population of %d people" % (self.name, self.population)
        
        
if __name__=="__main__":
    #input
    print("This is a simulation of 4 countries\n")
    n_countries = 4
    names_countries = ["India", "Netherlands", "UAE", "China"]
    population_countries = [100, 30, 43, 150]
    #computing
    countries = []
    for i in range(n_countries):  
        country = Country(names_countries[i], population_countries[i])
        countries.append(country)
    
    frame = nx.complete_graph(n_countries)
    country_dict = {i:names_countries[i] for i in range(n_countries)}
    world = nx.relabel_nodes(frame,country_dict)
    
    #output
    for country in countries:
        print(country)
    plt.figure()    
    nx.draw(world)
    plt.show()
        

