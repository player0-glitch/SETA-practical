# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Products(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=2)  
    productname = models.TextField(db_column='ProductName', db_collation='SQL_Latin1_General_CP1_CI_AS')  
    description = models.CharField(db_column='Description', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  
    imageurl = models.TextField(db_column='ImageUrl', db_collation='SQL_Latin1_General_CP1_CI_AS')  
    quantity = models.IntegerField(db_column='Quantity')  
    isavailable = models.BooleanField(db_column='IsAvailable')   
    suppliername = models.CharField(db_column='SupplierName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')  
    supplierid = models.IntegerField(db_column='SupplierId')  
    categoryname = models.TextField(db_column='CategoryName', db_collation='SQL_Latin1_General_CP1_CI_AS')  
    categoryid = models.ForeignKey('Categories', models.DO_NOTHING, db_column='CategoryId')  

    class Meta:
        managed = False
        db_table = 'Products'


class Users(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    name = models.CharField(db_column='Name', unique=True, max_length=450, db_collation='SQL_Latin1_General_CP1_CI_AS')  
    passwordhashed = models.TextField(db_column='PasswordHashed', db_collation='SQL_Latin1_General_CP1_CI_AS')  
    email = models.TextField(db_column='Email', db_collation='SQL_Latin1_General_CP1_CI_AS')  
    roleid = models.IntegerField(db_column='RoleId')  
    rolename = models.TextField(db_column='RoleName', db_collation='SQL_Latin1_General_CP1_CI_AS')  
    rolesid = models.ForeignKey('Roles', models.DO_NOTHING, db_column='RolesId', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Users'


class Wallets(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  
    transactionid = models.IntegerField(db_column='TransactionId')  
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  
    balance = models.DecimalField(db_column='Balance', max_digits=18, decimal_places=2)  
    timestamp = models.DateTimeField(db_column='TimeStamp')  
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  
    type = models.TextField(db_column='Type', db_collation='SQL_Latin1_General_CP1_CI_AS')  

    class Meta:
        managed = False
        db_table = 'Wallets'
