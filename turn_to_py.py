#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[2]:


def tabusearch(stop_time,initial_route,candidate_t,tabu_length):
    # Stop time: stop running when we reach this iteration limit.
    # Initial_route: route in a sequence: 1-2-3..-29. 
    # The start city won't change
    # Candidate t: determine the length of candidate
    # Tabu_length: the length of tabu list
    # Return: the minumum travel distance; the best route.
    def calcu_cost(route):
        # input the route(ex:1-2-3...29), output the total distance
        distance=0
        for i in range(0,28):
            distance+=np.linalg.norm(np.array([float(route[i][1][0]),
                                               float(route[i][1][1])])
                                     -np.array([float(route[i+1][1][0]),
                                                float(route[i+1][1][1])]))
        distance+=np.linalg.norm(np.array([float(route[0][1][0]),
                                           float(route[0][1][1])])
                                 -np.array([float(route[28][1][0]),
                                            float(route[28][1][1])]))
        return distance
    def move(route,t):
        # Input the route
        # Output t different solutions in the neighbour space. 
        # Random swap two cities in the route.
        # Return t new routes, t swaped paired cities,t travel distances.
        min_distance=100000
        best_route=0
        best_change=0
        routes=[]
        changes=[]
        distances=[]
        for i in range(t):
            route_new=route.copy()
            change=random.sample(route_new[1:],2)
            change.sort()
            route_new[route_new.index(change[1])]=change[0]
            route_new[route_new.index(change[0])]=change[1]
            routes.append(route_new)
            changes.append(change)
            distances.append(calcu_cost(route_new))
        return(routes,changes,distances)
    def add_or_not(move_tabu,distance_tabu,new_move,new_distance):
        # Determine whether the best solution should be add in the tabu list?
        # Add, if it's not included in tabu list
        # Add, if it's in tabu list but is better than the old solution
        # Else, ignore it.
        if new_move not in move_tabu:
            return(True)
        elif new_distance < distance_tabu[move_tabe.index(new_move)]:
            return(True)
        else:
            return(False)    
    def add_tabulist(move_tabu,distance_tabu,new_move,new_distance,tabu_length):
        move_tabu.append(new_move)
        distance_tabu.append(new_distance)
        if len(move_tabu)>tabu_length:
            del move_tabu[0]
            del distance_tabu[0]
        return(move_tabu,distance_tabu)
    all_routes=[]
    all_distances=[]
    move_tabe=[]
    distance_tabu=[]
    route=initial_route.copy()
    for i in range(stop_time):
        routes,changes,distances=move(route,candidate_t)
        a=0
        while a==0:
            if add_or_not(move_tabe,distance_tabu,
                          changes[distances.index(min(distances))],
                          min(distances)):
                move_tabe,distance_tabu= add_tabulist(
                    move_tabe,distance_tabu,
                    changes[distances.index(min(distances))],
                    min(distances),tabu_length)
                all_routes.append(routes[distances.index(min(distances))])
                all_distances.append(min(distances))
                a=1
                route=routes[distances.index(min(distances))]
            else:
                routes.remove(routes[distances.index(min(distances))])
                changes.remove(changes[distances.index(min(distances))])
                distances.remove(min(distances))
                if len(routes)==0:
                    a=1        
    return(min(all_distances),all_routes[all_distances.index(min(all_distances))])


# In[3]:


def parallelfunc(city):
    # This function is defined for parallel. 
    # Input a route, and output the best solution.
    # the parameter are fixed before we run parallel.
    return(tabusearch(stop_time=100,initial_route=city,
                      candidate_t=100,tabu_length=30))


# In[1]:


try:   
    get_ipython().system('jupyter nbconvert --to python turn_to_py.ipynb')

except:
    pass

