# Summary of "Flat Datacenter Storage"
Xiangfeng Zhu(zxfeng)

## Problem and Motivation
Oversubscription
Switch ports and cabling have both monetary cost and an operational cost in data centers. Imagine you have to wire 1000s machines together. How would you do it? The following figure shows the dominant design pattern for data-center architecture today(2012). 

As shown in the above figure, the network is a tree-like hierarchy reaching from a layer of servers in racks at the bottom to a layer of core routers at the top. Orange rectangles represent switches. Unfortunately, this conventional design suffers from a fundamental limitation: Limited server-to-server capacity(i.e., oversubscription).
As we go up the hierarchy, we are confronted with steep technical and financial barriers in sustaining high bandwidth. Thus, as traffic moves up through the layers of switches and routers, the over-subscription ratio increases rapidly. Top-level switches can be oversubscribed by greater than 1000x, meaning that only one in 1000 machines can send data across the top level to the other side at a time. 

This paper provides more detailed explanation. 

## Hypothesis


## Solution Overview


## Limitations and Possible Improvements


## Summary of Class Discussion