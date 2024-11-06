from tabulate import tabulate

class User:
    membership_req = [
        {
            'Membership':'Platinum',
            'Expense':8,
            'Income':15
        },
        {
            'Membership':'Gold',
            'Expense':6,
            'Income':10
        },
        {
            'Membership':'Silver',
            'Expense':5,
            'Income':7
        },
    ]

    membership_benefit = [
        {
            "Membership": "Platinum",
            "Discount": '15%',
            "Another Benefit": "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"
        },
        {
            "Membership": "Gold",
            "Discount": '10%',
            "Another Benefit": "Benefit Silver + Voucher Ojek Online"
        },
        {
            "Membership": "Silver",
            "Discount": '8%',
            "Another Benefit": "Voucher Makanan"
        }
    ]

    user_data = {
        # 'disa':[6, 10, 'Gold'],     #contoh data
        # 'rara':[5, 7, 'Silver'],    #dummy
    }

    def __init__(self):
        self.username = None
        self.monthly_expense = None
        self.monthly_income = None
        self.membership = None

    def register(self, username, monthly_expense, monthly_income):
        '''
        register user baru, masukin username, expense, income. untuk membershipnya bakal pake
        method predict_membership
        '''
        username = str(username.lower())
        if username not in self.user_data.keys(): # kalo gaada usernamenya, bikin user baru
            self.username = username
            self.monthly_expense = monthly_expense
            self.monthly_income = monthly_income
            self.membership = self.predict_membership(expense=monthly_expense, income=monthly_income)
        
            self.user_data[username] = [self.monthly_expense, self.monthly_income, self.membership]
        else:
            print(f'username {username} sudah terdaftar')
        

    def predict_membership(self, expense, income):
        '''
        untuk predict membership based on expense and income, outputnya jenis membershipnya
        '''

        distances = {}

        for req in self.membership_req:
            type = req['Membership']
            distance = ((expense-req['Expense'])**2 + (income-req['Income'])**2 )**0.5

            distances[type] = distance  # mengumpulkan semua jarak kedalam dict distances
        
        min_dist_list = min([value for value in distances.values()])    # menentukan jarak terkecil untuk menentukan membership
        member = None
        for key, value in distances.items():
            if value == min_dist_list:
                member = key
                break

        return member
    
    def show_benefit(self):
        benefit_header = list(self.membership_benefit[0].keys())
        benefit_content = [list(x.values()) for x in self.membership_benefit]

        print('Benefit dari PacCommerce:')
        print('')
        print(tabulate(benefit_content, headers=benefit_header, tablefmt='pretty'))

    def show_requirement(self):
        req_header = list(self.membership_req[0].keys())
        req_content = [list(req.values()) for req in self.membership_req]

        print('Requirement dari PacCommerce (dalam juta)')
        print('')
        print(tabulate(req_content, headers=req_header, tablefmt='pretty'))

    def calculate_total_price(self, username, price_list):
        '''
        menghitung total price dari seluruh belanjaan user setelah diskon berdasarkan membership dari user
        '''
        username = str(username.lower())
        tier_member = self.user_data[username][-1]
        # disc = None

        for tier in self.membership_benefit:
            if tier_member == tier['Membership']:
                disc = float(tier['Discount'].replace('%',''))/100
                break

        # total = sum(price_list) - (sum(price_list)*disc)
        total = sum(price_list)*(1-disc)

        print(f'total yang harus dibayar adalah: {total} juta')
    
    def show_user(self):
        user_header = ['Username', 'Membership']
        user_content = []

        for user, data in self.user_data.items():
            membership = data[-1]
            username = str(user).capitalize()

            user_content.append([username, membership])
        
        print(tabulate(user_content, headers=user_header, tablefmt='pretty'))
