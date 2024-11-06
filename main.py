from user import User

'''
mau tambah user dengan nama Disa
'''

user1 = User()
user1.register(username='Disa', monthly_expense=10, monthly_income=20)


'''
misalnya Disa belanja sepatu = 10 juta dan tas = 10 juta, dengan diskon dari membershipnya,
berapa total belanja yang harus disa bayar?
'''

total_harga = user1.calculate_total_price('disa', [10,10])