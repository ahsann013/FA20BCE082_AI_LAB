# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:40:33 2023

@author: Ahsan
"""

print("CGPA Calculator")


cur_gpa = float(input("What is your current CGPA: "))
req_gpa = float(input("What is your required CGPA: "))
cur_cdh = int(input("What are your credit hours in total: "))
new_cdh = int(input("What are your credit hours in this semester: "))

cur_pts = cur_gpa*cur_cdh

total_cdh = cur_cdh+new_cdh

points = req_gpa*total_cdh
 
t_points = (points-cur_pts)/new_cdh

print("You should get ",round(t_points,2), "cgpa") 

