"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


class StandardData:
    """
       Родительский класс для указания переменных и их инкапсуляции
       """
    conn = psycopg2.connect(
        host='localhost',
        database='north_data',
        user='postgres',
        password='57365')

    def __init__(self):
        pass

    @classmethod
    def csv_loader(cls, file):
        pass


class Customers_Data(StandardData):
    all = []

    def __init__(self, customer_id, company_name, contact_name):
        super().__init__()
        self.company_name = company_name
        self.customer_id = customer_id
        self.contact_name = contact_name

    @classmethod
    def csv_loader(cls, file='north_data/customers_data.csv'):
        with open(file, 'r', encoding='cp1251') as f:
            reader = csv.DictReader(f)
            for item in reader:
                cls.all.append(cls(item['customer_id'],
                                   item['company_name'],
                                   item['contact_name']))
            return cls.all

    @classmethod
    def add_data_sql(cls):
        Customers_Data.csv_loader()
        try:
            with Customers_Data.conn:
                with Customers_Data.conn.cursor() as cur:
                    for customer in Customers_Data.all:
                        cur.execute('insert into customers_data values(%s, %s, %s)', (customer.customer_id,
                                                                                      customer.company_name,
                                                                                      customer.contact_name))
                    cur.execute('select * from public.customers_data')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        finally:
            Customers_Data.conn.close


class Employees_Data(StandardData):
    all = []

    def __init__(self, employee_id, first_name, last_name, title, birth_date, notes):
        super().__init__()
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.birth_date = birth_date
        self.notes = notes

    @classmethod
    def csv_loader(cls, file='north_data/employees_data.csv'):
        with open(file, 'r', encoding='cp1251') as f:
            reader = csv.DictReader(f)
            for item in reader:
                cls.all.append(cls(item['employee_id'],
                                   item['first_name'],
                                   item['last_name'],
                                   item['title'],
                                   item['birth_date'],
                                   item['notes']))
            return cls.all

    @classmethod
    def add_data_sql(cls):
        Employees_Data.csv_loader()
        try:
            with Employees_Data.conn:
                with Employees_Data.conn.cursor() as cur:
                    for employee in Employees_Data.all:
                        cur.execute('insert into employees_data values(%s, %s, %s, %s, %s, %s)', (employee.employee_id,
                                                                                                  employee.first_name,
                                                                                                  employee.last_name,
                                                                                                  employee.title,
                                                                                                  employee.birth_date,
                                                                                                  employee.notes,))
                    cur.execute('select * from public.customers_data')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        finally:
            Employees_Data.conn.close


class Orders_Data(StandardData):
    all = []

    def __init__(self, order_id, customer_id, employee_id, order_date, ship_city):
        super().__init__()
        self.order_id = order_id
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.order_date = order_date
        self.ship_city = ship_city

    def __repr__(self):
        return self.order_id

    @classmethod
    def csv_loader(cls, file='north_data/orders_data.csv'):
        with open(file, 'r', encoding='cp1251') as f:
            reader = csv.DictReader(f)
            for item in reader:
                cls.all.append(cls(item['order_id'],
                                   item['customer_id'],
                                   item['employee_id'],
                                   item['order_date'],
                                   item['ship_city']))
            return cls.all

    @classmethod
    def add_data_sql(cls):
        Orders_Data.csv_loader()
        try:
            with Orders_Data.conn:
                with Orders_Data.conn.cursor() as cur:
                    for order in Orders_Data.all:
                        cur.execute('insert into orders_data values(%s, %s, %s, %s, %s)', (order.order_id,
                                                                                              order.customer_id,
                                                                                              order.employee_id,
                                                                                              order.order_date,
                                                                                              order.ship_city,))
                    cur.execute('select * from public.customers_data')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        finally:
            Orders_Data.conn.close


##################################################

Customers_Data.add_data_sql()
Employees_Data.add_data_sql()
Orders_Data.add_data_sql()
