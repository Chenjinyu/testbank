from django.db import models
from django.core.validators import RegexValidator


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    birthday = models.DateField(null=False)
    ssn = models.CharField(null=False, validators=[RegexValidator(regex='^[0-9]{9}$')])
    create_dt = models.DateTimeField(auto_now=True)
    update_dt = models.DateTimeField(null=True)

    class Meta:
        db_table = 'customer'


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, null=False)
    street_address_1 = models.CharField(max_length=100, null=False)
    street_address_2 = models.CharField(max_length=100, null=True)
    state = models.ForeignKey('states', null=False)
    zip_code = models.IntegerField(max_length=5)
    country = models.ForeignKey(null=False, default='US')


class States(models.Model):
    state_id = models.SmallIntegerField(primary_key=True)
    state_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'states'


class DebitAccount(models.Model):
    debit_account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, null=False)
    address_id = models.ForeignKey(Address, null=False)
    card_number = models.CharField(max_length=16, null=False)
    route_number = models.CharField(max_length=9, null=False)
    account_number = models.CharField(max_length=9, null=False)
    current_balance = models.MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='USD')
    create_date = models.DateTimeField(auto_now=True)
    expired_date = models.DateTimeField(null=False)

    class Meta:
        db_table = 'debit_account'


class CreditAccount(models.Model):
    credit_account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, null=False)
    address_id = models.ForeignKey(Address, null=False)
    card_number = models.CharField(max_length=16, null=False)
    current_balance = models.MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='USD')
    available_credit = models.MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='USD')
    next_payment_date = models.DateTimeField(null=False)
    next_payment_amount = models.MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='USD')
    create_date = models.DateTimeField(auto_now=True)
    expired_date = models.DateTimeField(null=False)

    class Meta:
        db_table = 'credit_account'


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, null=False)
    account_type = models.PositiveIntegerField(choices=((1, 'debit'), (2, 'credit')), null=False)
    account_id = models.IntegerField(null=False)
    tran_info = models.TextField(max_length=500, null=False)
    tran_note = models.TextField(max_length=100, null=True)
    tran_amount = models.MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='USD')
    tran_status = models.PositiveIntegerField(choices=((0, 'initial'), (1, 'pending'), (2, 'credit')), default=0)
    tran_create_date = models.DateTimeField(auto_now=True)
    tran_update_date = models.DateTimeField(null=False)

    class Meta:
        db_table = 'transaction'


# class Countries(models.Model):
#     country_id = models.SmallIntegerField(primary_key=True)
#     country_name = models.CharField(max_length=50, null=False)
#
#     class Meta:
#         db_table = 'countries'
