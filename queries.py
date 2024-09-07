drop_table='''DROP TABLE IF EXISTS employee'''
create_table='''CREATE TABLE IF NOT EXISTS employee(
    id int PRIMARY KEY,
    name varchar(40) NOT NULL,
    salary int,
    dept_id varchar(30))'''
insert_data = '''INSERT INTO employee(id,name,salary,dept_id) VALUES (%s,%s,%s,%s)'''
insert_value = [(1,'James',12000,'D1'),(2,'Barney',12000,'D1'),(3,'Tedd',12000,'D1'),(4,'Marshal',12000,'D1')]
update_data='''UPDATE employee SET salary=salary+(salary*0.5)'''
fetch_data='''SELECT * FROM employee'''