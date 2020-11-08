Notes on Udacity Nanodregree Program: [Full Stack Web Developer](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044)

# Full Stack Web Developer - Udacity Nanodegree

## Relationships & Joins

Relational databases map relationships between tables and between rows across tables:

Ex:

- Between tables:  A driver has many vehicles.

- Between rows across tables: Driver Amy has 2 vehicles: a 2018 Nissan Altima and a 2007 Ninja 250.


<div align="center">
<img src=src/parent_child_relationship.png>
<p>Relationship between parent and child table.</p>
</div>

In example above, we have a parent table (drivers) and a child table (vehicles). To create a relationship between these two tables, a foreign key is included into the child table. In this case, the foreign key is the driver id, which relates the vehicle to its driver. With this mapping, we can use JOIN statment to get info combining child and parent tables.

Ex: What is the make, model, and year of vehicles that driver Sarah have?

<div align="center">
<img src=src/query_child_parent.png>
<p>Query example using foreign key.</p>
</div>

In this example, we get information (make, model and year) from a child table (vehicles) joined with a parent table (drivers) to use the driver's name as a filter.