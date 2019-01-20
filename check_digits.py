class Check_Digits:
    def __init__(self):
        self.sum = 0
        self.digits_list = []

    def get_digits(self):
        digits = input('Enter eleven digits: ')

        # store numbers in list and make them ints
        for nums in digits:
            self.digits_list.append(int(nums))

    def sum_odd_digits(self):
        return sum(self.digits_list[0::2])

    def product_result(self):
        return self.sum_odd_digits() * 3

    def sum_even_digits(self):
        return self.product_result() + sum(self.digits_list[1::2])

    def find_remainder(self):
        remainder = self.sum_even_digits() % 10
        if remainder != 0:
            return 10 - remainder
        return 0 
       
# main program
# note: cd == checked digits
cd = Check_Digits()
cd.get_digits()
cd.sum_odd_digits()
cd.product_result()
cd.sum_even_digits()
print(cd.find_remainder())