class SimpleSalary:

    def solution(self, number, hours, salary):
        print('NUMBER = ' + str(number))
        salary = hours * salary;
        return 'SALARY = U$ ' + '%.2f' % salary

