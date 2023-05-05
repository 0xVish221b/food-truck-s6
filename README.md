# Food truck app

This is a sample solution for the food truck app built as part of Unit 2 (starting at https://git.generalassemb.ly/seifxr11anz/course-materials-for-students/blob/master/U2/W9/W9D3.md#food-truck-multi-lesson-mini-project-stage-1).

## Setup

### Pre-requisites

- Python3 with `flask` and `psycopg2` modules
- PostgreSQL

### Instructions

1. Create a PostgreSQL database `food_truck`
2. Run the [seed_food_table.sql](./seed_food_table.sql) file to create and seed a table in the database (`psql -f seed_food_table.sql food_truck`)
3. Run the app (`python app.py`)