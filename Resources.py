from Organization import Staff
from Bio import bio

class organization:
    def __init__(self):
        self.workers = []
        self.bio_worker = []

# the following line adds workers to the class object self.workers by appending workers.

    def add_workers(self, new_workers ):
        self.workers.append(new_workers)

# this line of codes execute similar actions as the above code appending self.bio which is adding worker's biography.
    def add_bio(self, staff_bio):
        self.bio_worker.append(staff_bio)

# in the line below we are displaying workers information and salary.

    def display_workers(self):     # we are displaying workers
        print('                        ')
        print(' Meet our staff:')
        print('-----------------')

        for i in self.workers:
            print(i.fname, i.lname, i.position)
            print(f'weekly Salary : ${i.weekly_pay():.2f}')



            print('                         ')

        print ('Staff Biography')
        print('----------------')


# displaying worker' s biography.

        for o in self.bio_worker:
            print(o.ffname)
            print('AGE :',o.age)
            print('RACE :',o.race)
            print('GENDER :',o.gender)
            print('ETHNICITY :',o.ethnicity)
            print('                   ')
            print('<<<<<>>>>>')


# here is the main code below.
def main():
    main_office = organization()

    Owner = Staff('Meti', 'Bedada', '/ Owner', 90)
    Owner_bio = bio('Metasebia Bedada',45, 'Black','Female','Ethiopian')
    main_office.add_workers(Owner)
    main_office.add_bio(Owner_bio)
    manager = Staff('Henri', 'Nguema', '/ Manager', 60)
    manager_bio = bio('Nguema Henri',42, 'Black', 'male', 'Earthian')
    main_office.add_workers(manager)
    main_office.add_bio(manager_bio)
    CFO = Staff('Mickael', 'Solomon', '/ Chief Finance Officer',100)
    CFO_bio = bio('Mickael Solomon',13, 'Black', 'male', 'Ethiopian')
    main_office.add_workers(CFO)
    main_office.add_bio(CFO_bio)
    Operation_dir = Staff( 'Emaye', 'Lishan','  / Operation Director', 80)
    Operation_bio = bio('Emaye Lishan',67, 'Black', 'Female', 'Ethiopian')

# this will execute the commands.

    main_office.add_workers(Operation_dir)
    main_office.add_bio(Operation_bio)
    print(main_office.display_workers())



main()

