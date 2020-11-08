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

## SQLAlchemy ORM - db.relationship

- SQLAlchemy configures the settings between model relationship once, and generates JOIN statements for us whenever we need them.
- `db.relationship` is an interface offered in SQLAlchemy to provide and configure a mapped relationship between two models.
- `db.relationship` is defined on the parent model, and it sets:
    - the name of its children (e.g. `children`), for example `parent_1.children`.
    - the name of a parent on a child using the backref, for example `child_1.my_amazing_parent`.

<div align="center">
<img src=src/db_relationship_example.png>
<p>Example of db.relationship.</p>
</div>

## Configuring Relationships

`db.relationship` allows configure when joined should be loaded. This mechanism is important because joins are very expansive. To make joins using the parent-child relationship, we have two options, described below.

### Lazy loading

Load needed joined data only as needed. __Default__ in SQLAlchemy.

- PRO: no initial wait time. Load only what you need.
- CON: produces a join SQL call every time there is a request for a joined asset. Bad if done often.

### Eager loading

Load all needed joined data objects, all ta once.

- PRO: reduces further queries to the database. Subsequent SQL calls read existing data.
- CON: loading the joined table has a long upfront initial load time.

Considering lazy loading, `lazy=True`, is the default option in `db.relationship`.
