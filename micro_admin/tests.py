from django.test import TestCase
from micro_admin.forms import *
from micro_admin.models import *
from django.test import Client as TestClient
from tempfile import NamedTemporaryFile
from micro_admin.templatetags import ledgertemplatetags

# Create your tests here.
class Modelform_test(TestCase):
    def setUp(self):
        self.b=Branch.objects.create(name='sbh', opening_date='2014-10-10', country='ind', state='AP', district='Nellore', city='Nellore', area='circle', phone_number=944454651165, pincode=502286)
        self.u = User.objects.create_superuser('jag123','jagadeesh123@gmail.com')
        self.f = NamedTemporaryFile(delete=False, suffix='.jpg',)

    def test_BranchForm(self):
        form = BranchForm(data = {'name':'andhra', 'opening_date':'12/10/2014', 'country':'ind', 'state':'AP', 'district':'Nellore', 'city':'Nellore', 'area':'circle', 'phone_number':944454651165, 'pincode':502286})
        self.assertTrue(form.is_valid())

    # BRANCH FORM INVALID
    def test_BranchForm_invalid(self):
        form = BranchForm(data = {'name':'', 'opening_date':'', 'country':'', 'state':'', 'district':'', 'city':'', 'area':'', 'phone_number': '', 'pincode': ''})
        self.assertFalse(form.is_valid())

    def test_UserForm(self):
        form = UserForm(data={'email':'jag@gmail.com', 'first_name':'jagadeesh', 'gender':'M', 'branch':self.b.id, 'user_roles':'BranchManager', 'username':'jagadeesh', 'password':'jag123'})
        self.assertTrue(form.is_valid())

    # USER FORM INVALID
    def test_UserForm_invalid(self):
        form = UserForm(data={'email': '', 'first_name': '', 'gender': '', 'branch': self.b.id, 'user_roles': '', 'username': '', 'password': ''})
        self.assertFalse(form.is_valid())

    def test_GroupForm(self):
        form = GroupForm(data={"name":'Star', "account_number":123456, "activation_date":'10/10/2014', "branch":self.b.id})
        self.assertTrue(form.is_valid())

    # GROUP FORM INVALID
    def test_GroupForm(self):
        form = GroupForm(data={"name": "", "account_number": "", "activation_date": "", "branch": self.b.id})
        self.assertFalse(form.is_valid())

    def test_ClientForm(self):
        form = ClientForm(data={"first_name":"Micro", "last_name":"Pyramid", "date_of_birth":'10/10/2014', "joined_date":"10/10/2014", "branch":self.b.id, "account_number":123, "gender":"M", "client_role":"FirstLeader", "occupation":"Teacher", "annual_income":2000, "country":'Ind', "state":'AP',"district":'Nellore', "city":'Nellore', "area":'rfc'})
        form = ClientForm(data={"first_name":"Micro", "last_name":"Pyramid", "date_of_birth":'10/10/2014', "joined_date":"10/10/2014", "branch":self.b.id, "account_number":123, "gender":"M", "client_role":"FirstLeader", "occupation":"Teacher", "annual_income":2000, "country":'Ind', "state":'AP',"district":'Nellore', "city":'Nellore', "area":'rfc', "mobile":944454651165, "pincode":502286})
        self.assertTrue(form.is_valid())

    # CLIENT FORM INVALID
    def test_ClientForm_invalid(self):
        form = ClientForm(data={"first_name": "", "last_name": "", "date_of_birth": '', "joined_date": "", "branch": self.b.id, "account_number": "", "gender": "", "client_role": "", "occupation": "", "annual_income": '', "country": '', "state": '', "district": '', "city": '', "area": '', "mobile": '', "pincode": ''})
        self.assertFalse(form.is_valid())

    def test_SavingsAccountForm(self):
        form = SavingsAccountForm(data={"account_no":12345, "opening_date":'10/10/2014', "min_required_balance":0, "annual_interest_rate":0})
        self.assertTrue(form.is_valid())

    def test_LoanAccountForm(self):
        form = LoanAccountForm(data={"account_no":12,'created_by':self.u.id, "loan_amount":10000, "interest_type":'Flat', "loan_repayment_period":123, "loan_repayment_every":12, "annual_interest_rate":12, "loanpurpose_description":'Hospitality'})
        self.assertTrue(form.is_valid())

    # Loan ACCOUNT FORM INVALID
    def test_LoanAccountForm(self):
        form = LoanAccountForm(data={"account_no": '', 'created_by': self.u.id, "loan_amount": '', "interest_type": '', "loan_repayment_period": '', "loan_repayment_every": '', "annual_interest_rate": '', "loanpurpose_description": ''})
        self.assertFalse(form.is_valid())

    def test_SavingsAccountForm(self):
        form = SavingsAccountForm(data={"account_no":123, "opening_date":'10/10/2014', "min_required_balance":0, "annual_interest_rate":3})
        self.assertTrue(form.is_valid())

    def test_LoanAccountForm(self):
        form = LoanAccountForm(data={"account_no":123, "interest_type":'Flat', "loan_amount":1000, "loan_repayment_period":10, "loan_repayment_every":10, "annual_interest_rate":3, "loanpurpose_description":'self finance'})
        self.assertTrue(form.is_valid())

    def test_ReceiptForm(self):
        form = ReceiptForm(data={"date":'10/10/2014', "branch":self.b.id, "receipt_number":12345})
        self.assertTrue(form.is_valid())

    def test_PaymentForm(self):
        form = PaymentForm(data={"date":'10/10/2014', "branch":self.b.id, "voucher_number":1231, "payment_type":'Loans', "amount":500, "interest":3, "total_amount":5000, "totalamount_in_words":'1 rupee'})
        self.assertTrue(form.is_valid())

    # PAYMENT FORM INVALID
    def test_PaymentForm(self):
        form = PaymentForm(data={"date": "", "branch": "", "voucher_number": "", "payment_type": "", "amount": "", "interest": "", "total_amount": "", "totalamount_in_words": ""})
        self.assertFalse(form.is_valid())

    def test_FixedDepositForm(self):
        form = FixedDepositForm(data={"nominee_firstname":'john', "nominee_lastname":'kumar', "nominee_occupation":'Big data analyst', "fixed_deposit_number":12, "deposited_date":'10/10/2014', "fixed_deposit_amount":12, "fixed_deposit_period":10, "fixed_deposit_interest_rate":3, "relationship_with_nominee":'friend', "nominee_photo":self.f, "nominee_signature":self.f})
        #self.assertTrue(form.is_valid())

    def test_ReccuringDepositForm(self):
        form = ReccuringDepositForm(data={"nominee_firstname":'john', "nominee_lastname":'johny', "nominee_occupation":'devoloper', "reccuring_deposit_number":123, "deposited_date":'10/10/2014', "recurring_deposit_amount":500, "recurring_deposit_period":20, "recurring_deposit_interest_rate":20, "relationship_with_nominee":'friend', "nominee_photo":self.f, "nominee_signature":self.f})
        #self.assertTrue(form.is_valid())



class template_tags(TestCase):

    def test_demand_collections_difference(self):
        res = ledgertemplatetags.demand_collections_difference(20, 10)
        self.assertEqual(res,10)


class Admin_Views_test(TestCase):
    # def setUp(self):
    #   self.client=TestClient()
    #   self.user = User.objects.create_superuser('jagadeesh', 'jag123')
    #   self.b = Branch.objects.create(name='sbh', opening_date='2014-10-10', country='ind', state='AP', district='Nellore', city='Nellore', area='circle', phone_number=944454651165, pincode=502286)
    #   self.u = User.objects.create_user('jag','jagadeesh@gmail.com')
    #   self.c = Client.objects.create(first_name="Micro", last_name="Pyramid",created_by=self.u , date_of_birth='2014-10-10', joined_date="2014-10-10", branch = self.b, account_number=123, gender="M", client_role="FirstLeader", occupation="Teacher", annual_income=2000, country='Ind', state='AP',district='Nellore', city='Nellore', area='rfc')
    #   self.s = SavingsAccount.objects.create(account_no=123456,client=self.c, opening_date='2014-10-10', min_required_balance=0, annual_interest_rate=0)

    def setUp(self):
        self.user = User.objects.create_superuser('jagadeesh', 'jag123')
        self.b = Branch.objects.create(name='sbh', opening_date='2014-10-10', country='ind', state='AP', district='Nellore', city='Nellore', area='circle', phone_number=944454651165, pincode=502286)
        self.u = User.objects.create_user(username = 'jag',email='jagadeesh@gmail.com',branch=self.b,password='jag')
        self.c = Client.objects.create(first_name="Micro", last_name="Pyramid",created_by=self.u , date_of_birth='2014-10-10', joined_date="2014-10-10", branch = self.b, account_number=123, gender="M", client_role="FirstLeader", occupation="Teacher", annual_income=2000, country='Ind', state='AP',district='Nellore', city='Nellore', area='rfc')
        self.c1 = Client.objects.create(first_name="Micro1", last_name="Pyramid",created_by=self.u , date_of_birth='2014-10-10', joined_date="2014-10-10", branch = self.b, account_number=1234, gender="M", client_role="FirstLeader", occupation="Teacher", annual_income=2000, country='Ind', state='AP',district='Nellore', city='Nellore', area='rfc')
        
        self.cs = SavingsAccount.objects.create(account_no='CS1',client=self.c, opening_date='2014-1-1', min_required_balance=0, savings_balance=100, annual_interest_rate=1,created_by=self.u,status='Approved')
        self.cs1 = SavingsAccount.objects.create(account_no='CS2',client=self.c1, opening_date='2014-1-1', min_required_balance=0, savings_balance=100, annual_interest_rate=1,created_by=self.u,status='Approved')

        self.g = Group.objects.create(name='group1', created_by=self.u, account_number='1', activation_date='2014-1-1', branch=self.b)
        self.g.clients.add(self.c)
        self.g.save()
        self.c.status = 'Assigned'
        self.c.save()

        self.group_client = Client.objects.create(first_name="Micro2", last_name="Pyramid",created_by=self.u , date_of_birth='2014-10-10', joined_date="2014-10-10", branch = self.b, account_number=1, gender="M", client_role="FirstLeader", occupation="Teacher", annual_income=2000, country='Ind', state='AP',district='Nellore', city='Nellore', area='rfc')
        self.g1 = Group.objects.create(name='group2', created_by=self.u, account_number='2', activation_date='2014-1-1', branch=self.b)
        self.g1.clients.add(self.group_client)
        self.g1.clients.add(self.c1)
        self.g1.save()
        self.group_client.status = 'Assigned'
        self.group_client.save()

        self.u2 = User.objects.create_user(username = 'ravi',email='ravi@gmail.com',branch=self.b,password='ravi')
        self.gs = SavingsAccount.objects.create(account_no='GS1',group=self.g, opening_date='2014-1-1', min_required_balance=0,  savings_balance=100, annual_interest_rate=1,created_by=self.u2,status='Approved')
        self.gs1 = SavingsAccount.objects.create(account_no='GS2',group=self.g1, opening_date='2014-1-1', min_required_balance=0, savings_balance=100, annual_interest_rate=1,created_by=self.u,status='Approved')
        
        self.grouploan = LoanAccount.objects.create(account_no='GL1', interest_type='Flat', group=self.g, created_by=self.u,status="Approved", loan_amount=12000, loan_repayment_period=12,loan_repayment_every=1,annual_interest_rate=2, loanpurpose_description='Home Loan',interest_charged=20,total_loan_balance=12000,principle_repayment=1000)
        self.clientloan = LoanAccount.objects.create(account_no='CL1', interest_type='Flat', client=self.c, created_by=self.u,status="Approved", loan_amount=12000,          loan_repayment_period=12,loan_repayment_every=1,annual_interest_rate=2, loanpurpose_description='Home Loan',interest_charged=20,total_loan_balance=12000,principle_repayment=1000)

        self.loanaccount_group2 = LoanAccount.objects.create(account_no='GL2', interest_type='Flat', group=self.g1, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=20, total_loan_balance=12000, principle_repayment=1000)
        fxd = FixedDeposits.objects.create(client=self.c, deposited_date='2014-1-1', status='Opened', fixed_deposit_number='f1', fixed_deposit_amount=1200, fixed_deposit_period=12, fixed_deposit_interest_rate=3, nominee_firstname='r', nominee_lastname='k',nominee_gender='M',relationship_with_nominee='friend',nominee_date_of_birth='2014-10-10', nominee_occupation='teacher', )
        rcd = RecurringDeposits.objects.create(client=self.c, deposited_date='2014-1-1', reccuring_deposit_number='r1', status='Opened', recurring_deposit_amount=1200, recurring_deposit_period=200, recurring_deposit_interest_rate=3, nominee_firstname='ra', nominee_lastname='ku', nominee_gender='M', relationship_with_nominee='friend', nominee_date_of_birth='2014-1-1', nominee_occupation='Teacher')
        self.f = NamedTemporaryFile(delete=False, suffix='.jpg',)
        self.receipt = Receipts.objects.create(receipt_number=1, date="2015-2-20", staff=self.u, branch=self.b, client=self.c, entrancefee_amount="100")
        self.payments = Payments.objects.create(date="2015-2-20", staff=self.u, branch=self.b, client=self.c, payment_type="OtherCharges", voucher_number=1, amount=100, total_amount=101, interest=1, totalamount_in_words="hundred")

    def test_views(self):
        client = Client()
        user_login=self.client.login(username='jagadeesh',password='jag123')
        self.assertTrue(user_login)

        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')


        response = self.client.get('/createbranch/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'createbranch.html')


        response = self.client.get('/createclient/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'createclient.html')

        response = self.client.get('/createuser/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'createuser.html')

        response = self.client.get('/creategroup/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'creategroup.html')

        response = self.client.get('/editbranch/1/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'editbranchdetails.html')


        response = self.client.get('/edituser/1/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'edituser.html')


        response = self.client.get('/branchprofile/1/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'branchprofile.html')


        response = self.client.get('/userprofile/1/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'userprofile.html')


        response = self.client.get('/userslist/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'listofusers.html')


        response = self.client.get('/viewbranch/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'viewbranch.html')


        response = self.client.get('/groupslist/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'listofgroups.html')


        response = self.client.get('/viewclient/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'viewclient.html')


        response = self.client.get('/deletebranch/1/')
        self.assertEqual(response.status_code,302)


        response = self.client.get('/userchangepassword/1/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'user_change_password.html')


        response = self.client.get('/daybookpdfdownload/2014-10-10/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pdf_daybook.html')


        response = self.client.get('/generalledgerpdfdownload/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pdfgeneral_ledger.html')


        response = self.client.get('/paymentslist/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'list_of_payments.html')


        response = self.client.get('/recurringdeposits/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'recurring_deposit_application.html')

    def test_views_post_data(self):
        user_login=self.client.login(username='jag',password='jag')
        self.assertTrue(user_login)

        response = self.client.post('/createbranch/',{'name':'andhra', 'opening_date':'12/10/2014', 'country':'ind', 'state':'AP', 'district':'Nellore', 'city':'Nellore', 'area':'circle', 'phone_number':944454651165, 'pincode':502286})
        self.assertEqual(response.status_code,200)
        self.assertTrue('"error": false' in response.content )

        response = self.client.post('/editbranch/2/',{'name':'andhra', 'opening_date':'12/10/2014', 'country':'ind', 'state':'AP', 'district':'Nellore', 'city':'Nellore', 'area':'circle', 'phone_number':944454651165, 'pincode':502286})
        self.assertEqual(response.status_code,200)
        self.assertTrue('"error": false' in response.content )

        response = self.client.post('/createclient/',{"first_name":"Micro", "last_name":"Pyramid","created_by":self.u.username, "date_of_birth":'10/10/2014', "joined_date":"10/10/2014", "branch":self.b.id, "account_number":561, "gender":"M", "client_role":"FirstLeader", "occupation":"Teacher", "annual_income":2000, "country":'Ind', "state":'AP',"district":'Nellore', "city":'Nellore', "area":'rfc', "mobile":944454651165, "pincode":502286})
        self.assertTrue('"error": false' in response.content)
        self.assertEqual(response.status_code,200)

        response = self.client.post('/createuser/',{'email':'jag1221@gmail.com', 'first_name':'jag123223', 'gender':'M', 'branch':self.b.id, 'user_roles':'BranchManager', 'username':'jagadeesh121', 'password':'jag123'})
        self.assertTrue('"error": false}' in response.content)
        self.assertEqual(response.status_code,200)

        response = self.client.post('/creategroup/',{"name":'Star', "account_number":123456,"created_by":self.u.username, "activation_date":'10/10/2014', "branch":self.b.id})
        self.assertTrue('"error": false}' in response.content)
        self.assertEqual(response.status_code,200)

        response = self.client.post('/editbranch/1/',{'name':'andhra', 'opening_date':'12/10/2014', 'country':'ind', 'state':'AP', 'district':'Nellore', 'city':'Nellore', 'area':'circle', 'phone_number':944454651165, 'pincode':502286})
        self.assertEqual(response.status_code,200)

        response = self.client.post('/edituser/1/',{'email':'jag@gmail.com', 'first_name':'jagadeesh', 'gender':'M', 'branch':self.b.id, 'user_roles':'BranchManager', 'username':'jagadeesh', 'password':'jag123'})
        self.assertEqual(response.status_code,200)

        response = self.client.post('/editclient/1/', {"first_name":"Micro", "last_name":"Pyramid", "date_of_birth":'10/10/2014', "joined_date":"10/10/2014", "branch":self.b.id, "account_number":123, "gender":"M", "client_role":"FirstLeader", "occupation":"Teacher", "annual_income":2000, "country":'Ind', "state":'AP',"district":'Nellore', "city":'Nellore', "area":'rfc',"mobile":944454651165, "pincode":502286})
        self.assertTrue('"error": false}' in response.content)
        self.assertEqual(response.status_code,200)

        # response = self.client.post('/groupsavingsapplication/1/',{"account_no":123, "opening_date":'10/10/2014', "min_required_balance":0, "annual_interest_rate":3})
        # self.assertEqual(response.status_code,200)

        response = self.client.post('/grouploanapplication/1/',{"account_no":123, "interest_type":'Flat', "created_by":self.u.username, "loan_amount":1000, "loan_repayment_period":10, "loan_repayment_every":10, "annual_interest_rate":3, "loanpurpose_description":'self finance'})
        self.assertEqual(response.status_code,200)

        # response = self.client.post('/receiptsdeposit/',{"date":'10/10/2014', 'name':self.c.first_name,'account_number':123, "branch":self.b.id, "receipt_number":12345, 'loan_account_no':123,'sharecapital_amount':200, 'savingsdeposit_thrift_amount':200})
        # self.assertEqual(response.status_code,200)

        response = self.client.get('/daybookpdfdownload/2014-10-10/')
        self.assertEqual(response.status_code,200)

        response = self.client.post('/clientloanapplication/1/',{"account_no":12, "created_by":self.u.username, "loan_amount":10000, "interest_type":'Flat', "loan_repayment_period":123, "loan_repayment_every":12, "annual_interest_rate":12, "loanpurpose_description":'Hospitality'})
        self.assertEqual(response.status_code,200)

        response = self.client.get('/updateclientprofile/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/clientprofile/1/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('clientprofile.html')

        response = self.client.get('/groupprofile/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/userslist/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/viewbranch/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/groupslist/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/viewclient/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/assignstaff/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.post('/assignstaff/1/',{'staff':1})
        self.assertTrue('"error": false}' in response.content)
        self.assertEqual(response.status_code,200)

        response = self.client.get('/addmember/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/viewmembers/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/groupmeetings/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/addgroupmeeting/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/addgroupmeeting/1/',{'meeting_date':'2014/10/10:10-10-10'})
        self.assertEqual(response.status_code,200)

        response = self.client.get('/clientsavingsapplication/1/')
        self.assertEqual(response.status_code,302)

        # response = self.client.post('/clientsavingsapplication/1/',{"account_no":12345,"created_by" : self.u.username, "opening_date":'10/10/2014', "min_required_balance":0, "annual_interest_rate":0, })
        # self.assertEqual(response.status_code,200)
        # self.assertTrue(' "error": false' in response.content )

        response = self.client.get('/clientsavingsaccount/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/groupsavingsapplication/1/')
        self.assertEqual(response.status_code,302)


        # response = self.client.post('/groupsavingsapplication/1/',{"account_no":123, "created_by" : self.u.username, "opening_date":'10/10/2014','created_by':self.u.id,'status':"Applied", "min_required_balance":0, "annual_interest_rate":3})
        # print response.content
        # self.assertEqual(response.status_code,200)

        # response = self.client.post('/groupsavingsapplication/1/',{"account_no":123, "opening_date":'10/10/2014', "created_by" : self.u.username, "min_required_balance":0, "annual_interest_rate":3})
        # self.assertTrue('"error": false', response.content)
        # self.assertEqual(response.status_code,200)

        # response = self.client.get('/groupsavingsaccount/1/')
        # self.assertEqual(response.status_code,200)

        response = self.client.post('/approvesavings/1/', {'savingsaccount_id':1})
        self.assertEqual(response.status_code,200)

        response = self.client.post('/rejectsavings/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.post('/rejectsavings/1/', {'savingsaccount_id':1})
        self.assertEqual(response.status_code,200)


        response = self.client.post('/withdrawsavings/1/',{'savingsaccount_id':1})
        self.assertEqual(response.status_code,200)

        response = self.client.get('/viewgroupsavingsdeposits/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/issueloan/1/')
        self.assertEqual(response.status_code,302)

        response = self.client.get('/viewgroupsavingswithdrawals/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.post('/grouploanapplication/1/',{"account_no":1239, "interest_type":'Flat', "loan_amount":1000, "loan_repayment_period":10, "loan_repayment_every":10, "annual_interest_rate":3, "loanpurpose_description":'self finance'})
        self.assertTrue('"error": false}' in response.content)
        self.assertEqual(response.status_code,200)

        response = self.client.get('/grouploanaccount/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/clientloanaccount/2/')
        self.assertEqual(response.status_code,200)

        response = self.client.post('/approveloan/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.post('/rejectloan/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.post('/closeloan/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.post('/listofclientloandeposits/1/2/')
        self.assertEqual(response.status_code,200)


        response = self.client.post('/listofclientsavingsdeposits/1/')
        self.assertEqual(response.status_code,200)


        response = self.client.post('/viewgrouploandeposits/1/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.post('/issueloan/1/')
        self.assertEqual(response.status_code,302)

        response = self.client.post('/receiptslist/')
        self.assertEqual(response.status_code,200)

        # response = self.client.post('/ledgeraccount/2/1/')
        # self.assertEqual(response.status_code,200)

        response = self.client.get('/generalledger/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/fixeddeposits/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/clientfixeddepositsprofile/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/viewclientfixeddeposits/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/viewdaybook/')
        self.assertEqual(response.status_code,200)

        # response = self.client.post('/viewdaybook/',{'data':'2014-10-10'})
        # self.assertEqual(response.status_code,200)

        response = self.client.get('/viewparticularclientfixeddeposits/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/payslip/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/grouploanaccountslist/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/clientloanaccountslist/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/paymentslist/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/recurringdeposits/')
        self.assertEqual(response.status_code,200)

        response = self.client.post('/recurringdeposits/',{'client_name': 'Micro', 'client_account_no': '123', "nominee_firstname":'john', "nominee_lastname":'johny', "nominee_occupation":'devoloper', "reccuring_deposit_number":123, "deposited_date":'10/10/2014', "recurring_deposit_amount":500, "recurring_deposit_period":20, "recurring_deposit_interest_rate":20, "relationship_with_nominee":'friend'}) #"nominee_photo":self.f, "nominee_signature":self.f})
        #print response.content
        self.assertEqual(response.status_code,200)

        response = self.client.get('/clientrecurringdepositsprofile/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/viewclientrecurringdeposits/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/viewparticularclientrecurringdeposits/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/clientledgercsvdownload/1/')
        self.assertTrue('Date,Recepit No,Demand Principal' in response.content)
        self.assertEqual(response.status_code,200)

        response = self.client.get('/clientledgerexceldownload/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/clientledgerpdfdownload/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/daybookpdfdownload/2014-10-10/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/generalledgerpdfdownload/')
        self.assertEqual(response.status_code,200)

        response = self.client.get('/userchangepassword/1/')
        self.assertEqual(response.status_code,200)

        response = self.client.post('/userchangepassword/1/',{'current_password':'jag123', 'new_password': '123123', 'confirm_new_password': '123123'})
        self.assertTrue('{"error": false}' in response.content)
        self.assertEqual(response.status_code,200)

        response = self.client.post('/getmemberloanaccounts/',{'account_number':123})
        self.assertEqual(response.status_code,200)
        self.assertTrue(' "error": false}' in response.content)

        response = self.client.post('/getloandemands/',{'loan_account_no':'GL1'})
        self.assertEqual(response.status_code,200)

    def test_user_logout(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.get("/logout/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/', status_code=302, target_status_code=200)

    def test_user_logout_without_login(self):
        response = self.client.get("/logout/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, '')

    def test_user_login_view(self):
        response = self.client.post("/login/", {'username': 'jagadeesh', 'password': 'jag123'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Loggedin Successfully' in response.content)

    def test_user_login_wrong_input(self):
        response = self.client.post("/login/", {'username': 'jagadeesh', 'password': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Username and Password were incorrect.' in response.content)

    def test_create_branch_invalid_post_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/createbranch/', {'name': '', 'opening_date': '', 'country': '', 'state': '', 'district': '', 'city': '', 'area': '', 'phone_number': '', 'pincode': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_create_client_invalid_post_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/createclient/', {"first_name": "", "last_name": "", "date_of_birth": '', "joined_date": "", "branch": self.b.id, "account_number": '', "gender": "", "client_role": "", "occupation": "", "annual_income": '', "country": '', "state": '', "district": '', "city": '', "area": '', "mobile": '', "pincode": ''})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_removemembers_from_group_view(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.get('/removemember/'+str(self.g.id)+'/'+str(self.c.id)+'/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/groupprofile/'+str(self.g.id)+"/", status_code=302, target_status_code=200)

    def test_create_client_invalid_post_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/createuser/', {'email': '', 'first_name': '', 'gender': '', 'branch': self.b.id, 'user_roles': '', 'username': '', 'password': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_create_group_invalid_post_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/creategroup/', {"name": '', "account_number": '', "activation_date": '', "branch": self.b.id})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_addmembers_to_group_post_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/addmember/'+str(self.g.id)+'/', {"clients": [self.c.id]})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_addmembers_to_group_post_invalid_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/addmember/'+str(self.g.id)+'/', {"clients": ""})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    # def test_group_delete(self):
    #     group_count = Group.objects.count()
    #     response = self.client.get("/deletegroup/"+str(self.g.id)+"/")
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(Group.objects.count(), group_count-1)
    #     self.assertRedirects(response, "/groupslist/", status_code=302, target_status_code=200)
    def test_add_group_meeting_post_invalid_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/addgroupmeeting/'+str(self.g.id)+'/', {"meeting_date": "2/20/2015", "meeting_time": "10-10-10", "group": self.g.id})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/groupprofile/'+str(self.g.id)+"/", status_code=302, target_status_code=200)

    def test_client_savings_application_post_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/clientsavingsapplication/'+str(self.c.id)+'/', {"account_no": 123, "opening_date": '10/10/2014', "min_required_balance": 0, "annual_interest_rate": 3})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_client_savings_application_post_invalid_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/clientsavingsapplication/'+str(self.c.id)+'/', {"account_no": '', "opening_date": '', "min_required_balance": '', "annual_interest_rate": ''})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_group_savings_application_post_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/groupsavingsapplication/'+str(self.g.id)+'/', {"account_no": 123, "opening_date": '10/10/2014', "min_required_balance": 0, "annual_interest_rate": 3})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_group_savings_application_post_invalid_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/groupsavingsapplication/'+str(self.g.id)+'/', {"account_no": '', "opening_date": '', "min_required_balance": '', "annual_interest_rate": ''})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_group_savings_account(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.get('/groupsavingsaccount/'+str(self.g.id)+'/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "group_savings_account.html")

    def test_group_loan_application(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.get('/grouploanapplication/'+str(self.g.id)+'/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "group_loan_application.html")

    def test_group_loan_application_post_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/grouploanapplication/'+str(self.g.id)+'/', {"account_no": 12, 'created_by': self.u.id, "loan_amount": 10000, "interest_type": 'Flat', "loan_repayment_period": 123, "loan_repayment_every": 12, "annual_interest_rate": 12, "loanpurpose_description": 'Hospitality'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_group_loan_application_post_invalid_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/grouploanapplication/'+str(self.g.id)+'/', {"account_no": '', 'created_by': self.u.id, "loan_amount": '', "interest_type": '', "loan_repayment_period": '', "loan_repayment_every": '', "annual_interest_rate": '', "loanpurpose_description": ''})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_client_loan_application(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.get('/clientloanapplication/'+str(self.c.id)+'/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "client_loan_application.html")

    def test_client_loan_application_post_invalid_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/clientloanapplication/'+str(self.c.id)+'/', {"account_no": '', 'created_by': self.u.id, "loan_amount": '', "interest_type": '', "loan_repayment_period": '', "loan_repayment_every": '', "annual_interest_rate": '', "loanpurpose_description": ''})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_listofclient_savings_withdrawals(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.get('/listofclientsavingswithdrawals/'+str(self.c.id)+'/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listof_clientsavingswithdrawals.html")

    def test_issue_loan_client(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.get("/issueloan/"+str(self.clientloan.id)+"/")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/clientloanaccount/'+str(self.clientloan.id)+'/', status_code=302, target_status_code=200)

    def test_withdraw_loan_post_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post("/withdrawloan/"+str(self.clientloan.id)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_withdraw_loan_post_data_group(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post("/withdrawloan/"+str(self.grouploan.id)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    # def test_withdraw_loan_post_data_admin(self):
    #     user_login = self.client.login(username='jagadeesh', password='jag123')
    #     print self.u.is_admin
    #     response = self.client.post("/withdrawloan/"+str(self.grouploan.id)+"/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('"error": false' in response.content)

    def test_withdraw_loan_post_data_exception(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post("/withdrawloan/"+'23'+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.get('/receiptsdeposit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "receiptsform.html")

    # def test_receipts_deposit_post_data_membershipfee(self):
    #     user_login = self.client.login(username='jagadeesh', password='jag123')
    #     Client.objects.get(first_name__iexact=self.c.first_name, account_number=self.c.account_number)
    #     response = self.client.post('/receiptsdeposit/', {"date": '10/10/2015', 'client': self.c.first_name, 'member_loan_account': 123, "branch": self.b.id, "receipt_number": 2, "membershipfee_amount": 100})
    #     self.assertEqual(response.status_code, 200)

    # def test_receipts_deposit_post_data_loan_acct_num(self):
    #     user_login = self.client.login(username='jagadeesh', password='jag123')
    #     Client.objects.get(first_name__iexact=self.c.first_name, account_number=self.c.account_number)
    #     response = self.client.post('/receiptsdeposit/', {"loan_account_no": 12, "date": '10/10/2015', 'client': self.c.first_name, 'member_loan_account': 123, "branch": self.b.id, "receipt_number": 3, "loanprocessingfee_amount": 700})
    #     self.assertEqual(response.status_code, 200)

    def test_ledger_account(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.get('/ledgeraccount/'+str(self.c.id)+'/'+str(self.clientloan.id)+'/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "client_ledger_account.html")

    def test_general_ledger(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.get('/generalledger/', {"date": '2015-2-20'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "generalledger.html")

    def test_day_book(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/viewdaybook/', {"date": '2/20/2015'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "day_book.html")

    def test_payslip_post_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"date": '2/20/2015', "branch": self.b.id, "voucher_number": 25, "payment_type": 'OtherCharges', "amount": 0, "interest": '', "total_amount": 0, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_invalid_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"date": "", "branch": "", "voucher_number": "", "payment_type": "", "amount": "", "interest": "", "total_amount": "", "totalamount_in_words": ""})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data1(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"date": '2/20/2015', "branch": self.b.id, "voucher_number": 36, "payment_type": 'TravellingAllowance', "amount": 500, "interest": '', "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data2(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"date": '2/20/2015', "branch": self.b.id, "voucher_number": 2, "payment_type": 'TravellingAllowance', "amount": 500, "interest": '', "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        # Please enter Employee Username
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data3(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"staff_username": 'user', "date": '2/20/2015', "branch": self.b.id, "voucher_number": 3, "payment_type": 'TravellingAllowance', "amount": 500, "interest": '', "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        # Entered Employee Username is incorrect
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data4(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        User.objects.create_user(username='user1', password='user1', email="user1@mp.com", branch=self.b,)
        response = self.client.post('/payslip/', {"staff_username": 'user1', "date": '2/20/2015', "branch": self.b.id, "voucher_number": 4, "payment_type": 'TravellingAllowance', "amount": 500, "interest": '', "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        # False
        self.assertTrue('"error": false' in response.content)

    def test_payslip_post_data5(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        User.objects.create(username='user1', password='user1', email="user1@mp.com", branch=self.b,)
        response = self.client.post('/payslip/', {"staff_username": 'user1', "date": '2/20/2015', "branch": self.b.id, "voucher_number": 5, "payment_type": 'TravellingAllowance', "amount": 500, "interest": '2', "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        # "Interest must be empty for TA and Payment of salary Voucher."
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data6(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        User.objects.create(username='user1', password='user1', email="user1@mp.com", branch=self.b,)
        response = self.client.post('/payslip/', {"staff_username": 'user1', "date": '2/20/2015', "branch": self.b.id, "voucher_number": 6, "payment_type": 'TravellingAllowance', "amount": 50, "interest": '', "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        # Entered total amount is not equal to amount.
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data7(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"date": '2/20/2015', "branch": self.b.id, "voucher_number": 7, "payment_type": 'PrintingCharges', "amount": 500, "interest": '', "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_payslip_post_data8(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"date": '2/20/2015', "branch": self.b.id, "voucher_number": 8, "payment_type": 'PrintingCharges', "amount": 50, "interest": '', "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data9(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"date": '2/20/2015', "branch": self.b.id, "voucher_number": 9, "payment_type": 'PrintingCharges', "amount": 50, "interest": 1, "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_10(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"client_name": "", "date": '2/20/2015', "branch": self.b.id, "voucher_number": 10, "payment_type": 'SavingsWithdrawal', "amount": 50, "interest": 1, "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        # Please enter the Member First Name
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_11(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"client_name": "Micro1", "client_account_number": '', "date": '2/20/2015', "branch": self.b.id, "voucher_number": 11, "payment_type": 'SavingsWithdrawal', "amount": 50, "interest": 1, "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        # Please enter the Member Account number
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_12(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"client_name": "Micro1", "client_account_number": '1234', "date": '2/20/2015', "branch": self.b.id, "voucher_number": 12, "payment_type": 'SavingsWithdrawal', "amount": 50, "interest": 1, "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        # Please enter the Group name of the Member.
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_13(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"client_name": "Micro12", "client_account_number": '12345', "date": '2/20/2015', "branch": self.b.id, "voucher_number": 13, "payment_type": 'SavingsWithdrawal', "amount": 50, "interest": 1, "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        # Member does not exists with this First Name and A/C Number. Please enter correct details.
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_14(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        Client.objects.create(first_name="Micro12", last_name="Pyramid", created_by=self.u, date_of_birth='2014-10-10', joined_date="2014-10-10", branch=self.b, account_number=12345, gender="F", client_role="FirstLeader", occupation="Teacher", annual_income=2000, country='Ind', state='AP',district='Nellore', city='Nellore', area='rfc')
        response = self.client.post('/payslip/', {"client_name": "Micro12", "client_account_number": '12345', "date": '2/20/2015', "branch": self.b.id, "voucher_number": 14, "payment_type": 'SavingsWithdrawal', "amount": 50, "interest": 1, "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        # Member does not have Savings Account to withdraw amount.
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_15(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"client_name": "Micro1", "client_account_number": '1234', "date": '2/20/2015', "branch": self.b.id, "voucher_number": 15, "payment_type": 'SavingsWithdrawal', "amount": 500, "interest": 1, "total_amount": 500, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        # Member Savings Account does not have sufficient balance.
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_16(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "", "client_name": "Micro1", "client_account_number": 1234, "date": '2/20/2015', "branch": self.b.id, "voucher_number": 16, "payment_type": 'SavingsWithdrawal', "amount": 50, "interest": '', "total_amount": 50, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        # Please enter the Group name of the Member.
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_17(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "group2", "client_name": "Micro", "client_account_number": 123, "date": '2/20/2015', "branch": self.b.id, "voucher_number": 17, "payment_type": 'SavingsWithdrawal', "amount": 50, "interest": '', "total_amount": 50, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        # Member does not belong to the entered Group Name.
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_18(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "group2", "group_account_number": 3, "client_name": "Micro1", "client_account_number": 1234, "date": '2/20/2015', "branch": self.b.id, "voucher_number": 18, "payment_type": 'SavingsWithdrawal', "amount": 50, "interest": '', "total_amount": 50, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        # Entered Group A/C Number is incorrect.
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_19(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "group2", "group_account_number": 2, "client_name": "Micro1", "client_account_number": 1234, "date": '2/20/2015', "branch": self.b.id, "voucher_number": 19, "payment_type": 'SavingsWithdrawal', "amount": 50, "interest": '', "total_amount": 50, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_payslip_post_data_20(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "group2", "group_account_number": 2, "client_name": "Micro1", "client_account_number": 1234, "date": '2/20/2015', "branch": self.b.id, "voucher_number": 20, "payment_type": 'SavingsWithdrawal', "amount": 50, "interest": '', "total_amount": 51, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_21(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "group2", "group_account_number": 2, "client_name": "Micro1", "client_account_number": 1234, "date": '2/20/2015', "branch": self.b.id, "voucher_number": 21, "payment_type": 'SavingsWithdrawal', "amount": 50, "interest": 1, "total_amount": 51, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_payslip_post_data_22(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "group2", "group_account_number": 2, "client_name": "Micro1", "client_account_number": 1234, "date": '2/20/2015', "branch": self.b.id, "voucher_number": 22, "payment_type": 'SavingsWithdrawal', "amount": 50, "interest": 1, "total_amount": 52, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_23(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"client_name": "Micro1", "client_account_number": 1234, "date": '2/20/2015', "branch": self.b.id, "voucher_number": 23, "payment_type": 'Loans', "amount": 50, "interest": 1, "total_amount": 52, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_24(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "group2", "group_account_number": 2, "client_name": "Micro1", "client_account_number": 1234, "date": '2/20/2015', "branch": self.b.id, "voucher_number": 23, "payment_type": 'Loans', "amount": 50, "interest": "", "total_amount": 52, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_25(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "", "date": '2/20/2015', "branch": self.b.id, "voucher_number": 24, "payment_type": 'Loans', "amount": 50, "total_amount": 52, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_26(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "group2", "group_account_number": "",  "date": '2/20/2015', "branch": self.b.id, "voucher_number": 25, "payment_type": 'Loans', "amount": 50, "total_amount": 52, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_27(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "group3", "group_account_number": "3", "date": '2/20/2015', "branch": self.b.id, "voucher_number": 26, "payment_type": 'Loans', "amount": 50, "total_amount": 52, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_28(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "group2", "group_account_number": "2", "date": '2/20/2015', "branch": self.b.id, "voucher_number": 26, "payment_type": 'Loans', "amount": 50, "total_amount": 52, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_29(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "group2", "group_account_number": "2", "group_loan_account_no": "GL2", "date": '2/20/2015', "branch": self.b.id, "voucher_number": 27, "payment_type": 'Loans', "amount": 50, "total_amount": 52, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_30(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "group2", "group_account_number": "2", "group_loan_account_no": "GL2", "date": '2/20/2015', "branch": self.b.id, "voucher_number": 27, "payment_type": 'Loans', "amount": 50, "total_amount": 50, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_31(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "group2", "group_account_number": "2", "group_loan_account_no": "GL2", "date": '2/20/2015', "branch": self.b.id, "voucher_number": 27, "payment_type": 'Loans', "amount": 12000, "total_amount": 12000, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_payslip_post_data_32(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        g2 = Group.objects.create(name='group4', created_by=self.u, account_number='4', activation_date='2014-1-1', branch=self.b)
        loanaccount_group4 = LoanAccount.objects.create(account_no='GL4', interest_type='Flat', group=g2, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=20, total_loan_balance=12000, principle_repayment=1000)
        response = self.client.post('/payslip/', {"group_name": "group4", "group_account_number": "4", "group_loan_account_no": "GL4", "date": '2/20/2015', "branch": self.b.id, "voucher_number": 27, "payment_type": 'Loans', "amount": 12000, "total_amount": 12000, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_payslip_post_data_33(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/payslip/', {"group_name": "group2", "group_account_number": "", "client_name": "Micro1", "client_account_number": 1234, "date": '2/20/2015', "branch": self.b.id, "voucher_number": 18, "payment_type": 'SavingsWithdrawal', "amount": 50, "interest": '', "total_amount": 50, "totalamount_in_words": '1 rupee'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_invalid_data(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"date": "", "name": "", "account_number": "", "branch": self.b.id, "receipt_number": ""})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data1(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"loaninterest_amount": 0, "sharecapital_amount": 100, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": "2"})
        self.assertEqual(response.status_code, 200)
        # False
        self.assertTrue('"error": false' in response.content)

    def test_receipts_deposit_post_data2(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"loaninterest_amount": 0, "entrancefee_amount": 1000, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 3})
        self.assertEqual(response.status_code, 200)
        # False
        self.assertTrue('"error": false' in response.content)

    def test_receipts_deposit_post_data3(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"loaninterest_amount": 0, "membershipfee_amount": 110, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 4})
        self.assertEqual(response.status_code, 200)
        # False
        self.assertTrue('"error": false' in response.content)

    def test_receipts_deposit_post_data4(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"loaninterest_amount": 0, "bookfee_amount": 10, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 5})
        self.assertEqual(response.status_code, 200)
        # False
        self.assertTrue('"error": false' in response.content)

    def test_receipts_deposit_post_data5(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"loaninterest_amount": 0, "date": "2/2/2015", "name": "Micro", "account_number": "1235", "branch": self.b.id, "receipt_number": "2"})
        self.assertEqual(response.status_code, 200)
        # No Client exists with this First Name and Account number.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data6(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"loaninterest_amount": 0, "loanprocessingfee_amount": 10, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 5})
        self.assertEqual(response.status_code, 200)
        # Please enter the Member Loan Account Number to pay the Loan processing fee.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data7(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loan_account_no": "CL1", "loaninterest_amount": 0, "loanprocessingfee_amount": 1000, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 5})
        self.assertEqual(response.status_code, 200)
        # False
        self.assertTrue('"error": false' in response.content)

    def test_receipts_deposit_post_data8(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": "", "group_loan_account_no": "GL1", "loan_account_no": "CL1", "loaninterest_amount": 0, "loanprocessingfee_amount": 1000, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 5})
        self.assertEqual(response.status_code, 200)
        # Please enter the Group Name and Account Number.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data9(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"group_name": "group2", "group_account_number": "2", "group_loan_account_no": "GL1", "loan_account_no": "CL1", "loaninterest_amount": 0, "loanprocessingfee_amount": 1000, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 5})
        self.assertEqual(response.status_code, 200)
        # Member does not belong to this group.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data10(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 3, "group_loan_account_no": "GL1", "loan_account_no": "CL1", "loaninterest_amount": 0, "loanprocessingfee_amount": 1000, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 5})
        self.assertEqual(response.status_code, 200)
        # No Group exists with this name.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data11(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL3", "loan_account_no": "CL1", "loaninterest_amount": 0, "loanprocessingfee_amount": 1000, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 5})
        self.assertEqual(response.status_code, 200)
        # Loan does not exists with this Loan Account Number for this Group.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data12(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"loan_account_no": "CL3", "loaninterest_amount": 0, "loanprocessingfee_amount": 1000, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 5})
        self.assertEqual(response.status_code, 200)
        # Loan does not exists with this Loan Account Number for this Member.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data13(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "", "loan_account_no": "CL1", "loaninterest_amount": 0, "loanprocessingfee_amount": 1000, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 5})
        self.assertEqual(response.status_code, 200)
        # Please enter the group loan account number.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data14(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.c4 = Client.objects.create(first_name="Micro4", last_name="Pyramid", created_by=self.u, date_of_birth='2014-10-10', joined_date="2014-10-10", branch=self.b, account_number=4, gender="F", client_role="FirstLeader", occupation="Teacher", annual_income=2000, country='Ind', state='AP', district='Nellore', city='Nellore', area='rfc')
        LoanAccount.objects.create(account_no='CL4', interest_type='Flat', client=self.c4, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=20, total_loan_balance=12000, principle_repayment=1000)
        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "", "loaninterest_amount": 0, "loanprocessingfee_amount": 1000, "date": "2/2/2015", "name": "Micro4", "account_number": "4", "branch": self.b.id, "receipt_number": 5, "loan_account_no": "CL4"})
        self.assertEqual(response.status_code, 200)
        # Member has not been assigned to any group.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data15(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"savingsdeposit_thrift_amount": 100, "group_name": "group1", "group_account_number": 1, "group_loan_account_no": "", "loan_account_no": "CL1", "loaninterest_amount": 0, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 5})
        self.assertEqual(response.status_code, 200)
        # False
        self.assertTrue('"error": false' in response.content)

    def test_receipts_deposit_post_data16(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.group_client1 = Client.objects.create(first_name="Micro4", last_name="Pyramid", created_by=self.u, date_of_birth='2014-10-10', joined_date="2014-10-10", branch=self.b, account_number=4, gender="F", client_role="FirstLeader", occupation="Teacher", annual_income=2000, country='Ind', state='AP', district='Nellore', city='Nellore', area='rfc')
        self.group_client1_SA = SavingsAccount.objects.create(account_no='CS4', client=self.group_client1, opening_date='2014-1-1', min_required_balance=0, savings_balance=100, annual_interest_rate=1, created_by=self.u, status='Approved')

        self.g3 = Group.objects.create(name='group3', created_by=self.u, account_number='3', activation_date='2014-1-1', branch=self.b)
        self.g3.clients.add(self.group_client1)
        self.g3.save()
        response = self.client.post("/receiptsdeposit/", {"savingsdeposit_thrift_amount": 100, "group_name": "group3", "group_account_number": 3, "loaninterest_amount": 0, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 6})
        self.assertEqual(response.status_code, 200)
        # "Member does not belong to this Group.Please check Group Name and Account Number.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data17(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.group_client2 = Client.objects.create(first_name="Micro5", last_name="Pyramid", created_by=self.u, date_of_birth='2014-10-10', joined_date="2014-10-10", branch=self.b, account_number=5, gender="F", client_role="FirstLeader", occupation="Teacher", annual_income=2000, country='Ind', state='AP', district='Nellore', city='Nellore', area='rfc')
        self.group_client2_SA = SavingsAccount.objects.create(account_no='CS5', client=self.group_client2, opening_date='2014-1-1', min_required_balance=0, savings_balance=100, annual_interest_rate=1, created_by=self.u, status='Approved')

        self.g4 = Group.objects.create(name='group4', created_by=self.u, account_number='4', activation_date='2014-1-1', branch=self.b)
        self.g4.clients.add(self.group_client2)
        self.g4.save()
        response = self.client.post("/receiptsdeposit/", {"savingsdeposit_thrift_amount": 100, "group_name": "group4", "group_account_number": 4, "group_loan_account_no": "", "loan_account_no": "CL1", "loaninterest_amount": 0, "date": "2/2/2015", "name": "Micro5", "account_number": 5, "branch": self.b.id, "receipt_number": 7})
        self.assertEqual(response.status_code, 200)
        # Group does not have savings account to make thrift deposit.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data18(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.group_client3 = Client.objects.create(first_name="Micro6", last_name="Pyramid", created_by=self.u, date_of_birth='2014-10-10', joined_date="2014-10-10", branch=self.b, account_number=6, gender="F", client_role="FirstLeader", occupation="Teacher", annual_income=2000, country='Ind', state='AP', district='Nellore', city='Nellore', area='rfc')
        self.g.clients.add(self.group_client3)
        response = self.client.post("/receiptsdeposit/", {"savingsdeposit_thrift_amount": 100, "group_name": "group1", "group_account_number": 1, "loaninterest_amount": 0, "date": "2/2/2015", "name": "Micro6", "account_number": "6", "branch": self.b.id, "receipt_number": 11})
        self.assertEqual(response.status_code, 200)
        # Member does not have savings account to make thrift deposit.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data19(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"savingsdeposit_thrift_amount": 100, "group_name": "group5", "group_account_number": 5, "group_loan_account_no": "", "loan_account_no": "CL1", "loaninterest_amount": 0, "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 8})
        self.assertEqual(response.status_code, 200)
        # No Group exists with this Name and Account Number.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data20(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"savingsdeposit_thrift_amount": 100, "group_name": "", "group_account_number": "", "group_loan_account_no": "", "loan_account_no": "CL1", "loaninterest_amount": 0, "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 9})
        self.assertEqual(response.status_code, 200)
        # Please enter Group Name and Account Number.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data21(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"recurringdeposit_amount": 100, "loan_account_no": "CL1", "loaninterest_amount": 0, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 12})
        self.assertEqual(response.status_code, 200)
        # False
        self.assertTrue('"error": false' in response.content)

    def test_receipts_deposit_post_data22(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        client = Client.objects.create(first_name="Micro7", last_name="Pyramid", created_by=self.u, date_of_birth='2014-10-10', joined_date="2014-10-10", branch=self.b, account_number=7, gender="F", client_role="FirstLeader", occupation="Teacher", annual_income=2000, country='Ind', state='AP', district='Nellore', city='Nellore', area='rfc')

        response = self.client.post("/receiptsdeposit/", {"recurringdeposit_amount": 100, "loan_account_no": "CL1", "loaninterest_amount": 0, "date": "2/2/2015", "name": "Micro7", "account_number": "7", "branch": self.b.id, "receipt_number": 13})
        self.assertEqual(response.status_code, 200)
        # Member does not have savings account.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data23(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"loaninterest_amount": 0, "insurance_amount": 10, "date": "2/2/2015", "name": "Micro1", "account_number": "1234", "branch": self.b.id, "receipt_number": 14})
        self.assertEqual(response.status_code, 200)
        # False
        self.assertTrue('"error": false' in response.content)

    def test_receipts_deposit_post_data24(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"loaninterest_amount": 100, "loan_account_no": "", "insurance_amount": 10, "date": "2/2/2015", "name": "Micro1", "account_number": "1234", "branch": self.b.id, "receipt_number": 15})
        self.assertEqual(response.status_code, 200)
        # Please enter the the Member Loan A/C Number.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data25(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"loaninterest_amount": 100, "loan_account_no": "CL1", "insurance_amount": 10, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 16})
        self.assertEqual(response.status_code, 200)
        # Please enter the the Group Loan A/C Number.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data26(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"loaninterest_amount": 100, "loan_account_no": "CL2", "insurance_amount": 10, "date": "2/2/2015", "name": "Micro1", "account_number": "1234", "branch": self.b.id, "receipt_number": 17})
        self.assertEqual(response.status_code, 200)
        # "Member does not have any Loan to pay the Loan interest amount.
        self.assertTrue('"error": true' in response.content)

    # def test_receipts_deposit_post_data27(self):
    #     user_login = self.client.login(username="jagadeesh", password="jag123")
    #     response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loaninterest_amount": 100, "loan_account_no": "CL1", "insurance_amount": 10, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 18})
    #     self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": false' in response.content)

    def test_receipts_deposit_post_data28(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.group_client2 = Client.objects.create(first_name="Micro5", last_name="Pyramid", created_by=self.u, date_of_birth='2014-10-10', joined_date="2014-10-10", branch=self.b, account_number=5, gender="F", client_role="FirstLeader", occupation="Teacher", annual_income=2000, country='Ind', state='AP', district='Nellore', city='Nellore', area='rfc')
        self.clientloan = LoanAccount.objects.create(account_no='CL5', interest_type='Flat', client=self.group_client2, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=20, total_loan_balance=12000, principle_repayment=1000)
        self.g4 = Group.objects.create(name='group5', created_by=self.u, account_number='4', activation_date='2014-1-1', branch=self.b)
        self.g4.clients.add(self.group_client2)
        self.g4.save()
        response = self.client.post("/receiptsdeposit/", {"group_name": "group5", "group_account_number": 4, "group_loan_account_no": "GL1", "loaninterest_amount": 100, "loan_account_no": "CL5", "insurance_amount": 10, "date": "2/2/2015", "name": "Micro5", "account_number": "5", "branch": self.b.id, "receipt_number": 19})
        self.assertEqual(response.status_code, 200)
        # Group does not have any Loan to pay the Loan interest amount.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data29(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.g4 = Group.objects.create(name='group5', created_by=self.u, account_number='4', activation_date='2014-1-1', branch=self.b)
        response = self.client.post("/receiptsdeposit/", {"group_name": "group5", "group_account_number": 4, "group_loan_account_no": "GL1", "loaninterest_amount": 100, "loan_account_no": "CL1", "insurance_amount": 10, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 20})
        self.assertEqual(response.status_code, 200)
        # Member does not belong to this Group.Please check Group Name and Account Number.__loaninterest_amount
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data30(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.g4 = Group.objects.create(name='group5', created_by=self.u, account_number='4', activation_date='2014-1-1', branch=self.b)
        response = self.client.post("/receiptsdeposit/", {"group_name": "group5", "group_account_number": 11, "group_loan_account_no": "GL1", "loaninterest_amount": 100, "loan_account_no": "CL1", "insurance_amount": 10, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 21})
        self.assertEqual(response.status_code, 200)
        # No Group exists with this Name and Account Number.__loaninterest_amount
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data31(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.g4 = Group.objects.create(name='group5', created_by=self.u, account_number='4', activation_date='2014-1-1', branch=self.b)
        response = self.client.post("/receiptsdeposit/", {"group_name": "", "group_account_number": "", "group_loan_account_no": "GL1", "loaninterest_amount": 100, "loan_account_no": "CL1", "insurance_amount": 10, "date": "2/2/2015", "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 22})
        self.assertEqual(response.status_code, 200)
        # Please enter Group Name and Account Number.__loaninterest_amount
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data32(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        group_client2 = Client.objects.create(first_name="Micro5", last_name="Pyramid", created_by=self.u, date_of_birth='2014-10-10', joined_date="2014-10-10", branch=self.b, account_number=5, gender="F", client_role="FirstLeader", occupation="Teacher", annual_income=2000, country='Ind', state='AP', district='Nellore', city='Nellore', area='rfc')
        clientloan = LoanAccount.objects.create(account_no='CL5', interest_type='Flat', client=group_client2, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=20, total_loan_balance=12000, principle_repayment=1000)
        g5 = Group.objects.create(name='group5', created_by=self.u, account_number='4', activation_date='2014-1-1', branch=self.b)
        response = self.client.post("/receiptsdeposit/", {"group_name": "group5", "group_account_number": 4, "group_loan_account_no": "GL1", "loaninterest_amount": 100, "loan_account_no": "CL5", "insurance_amount": 10, "date": "2/2/2015", "name": "Micro5", "account_number": "5", "branch": self.b.id, "receipt_number": 23})
        self.assertEqual(response.status_code, 200)
        # Member has not been assigned to any group._loaninterest_amount
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data33(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"loanprinciple_amount": 100, "loan_account_no": "CL1", "date": "2/2/2015", "loaninterest_amount": 0, "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 24})
        self.assertEqual(response.status_code, 200)
        # Please enter the Member Loan A/C Number.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data34(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"loanprinciple_amount": 100, "loan_account_no": "CL5", "date": "2/2/2015", "loaninterest_amount": 0, "name": "Micro", "account_number": "123", "branch": self.b.id, "receipt_number": 25})
        self.assertEqual(response.status_code, 200)
        # Member does not have any Loan with this Loan A/C Number.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data35(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        group_client2 = Client.objects.create(first_name="Micro5", last_name="Pyramid", created_by=self.u, date_of_birth='2014-10-10', joined_date="2014-10-10", branch=self.b, account_number=5, gender="F", client_role="FirstLeader", occupation="Teacher", annual_income=2000, country='Ind', state='AP', district='Nellore', city='Nellore', area='rfc')
        clientloan = LoanAccount.objects.create(account_no='CL5', interest_type='Flat', client=group_client2, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=20, total_loan_balance=12000, principle_repayment=1000)
        g5 = Group.objects.create(name='group5', created_by=self.u, account_number='4', activation_date='2014-1-1', branch=self.b)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group5", "group_account_number": 4, "loanprinciple_amount": 100, "loan_account_no": "CL5", "date": "2/2/2015", "loaninterest_amount": 0, "name": "Micro5", "account_number": 5, "branch": self.b.id, "receipt_number": 26})
        self.assertEqual(response.status_code, 200)
        # Member has not been assigned to any group.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data36(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"group_name": "", "group_account_number": "", "loanprinciple_amount": 100, "loan_account_no": "CL1", "date": "2/2/2015", "loaninterest_amount": 0, "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 27})
        self.assertEqual(response.status_code, 200)
        # Please enter the Group Name and Account Number.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data37(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"group_name": "g1", "group_account_number": "1", "loanprinciple_amount": 100, "loan_account_no": "CL1", "date": "2/2/2015", "loaninterest_amount": 0, "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 28})
        self.assertEqual(response.status_code, 200)
        # Group does not exists with this Name and Account Number.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data38(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "loanprinciple_amount": 100, "loan_account_no": "CL1", "date": "2/2/2015", "loaninterest_amount": 0, "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 29})
        self.assertEqual(response.status_code, 200)
        # Please enter the group loan account number.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data39(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 100, "loan_account_no": "CL1", "date": "2/2/2015", "loaninterest_amount": 0, "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 30})
        self.assertEqual(response.status_code, 200)
        # Loan Payment has not yet done.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data40(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 13000, "loan_account_no": "CL1", "date": "2/2/2015", "loaninterest_amount": 0, "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 31})
        self.assertEqual(response.status_code, 200)
        # Amount is greater than loan balance.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data41(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        group_client6 = Client.objects.create(first_name="Micro6", last_name="Pyramid", created_by=self.u, date_of_birth='2014-10-10', joined_date="2014-10-10", branch=self.b, account_number=6, gender="F", client_role="FirstLeader", occupation="Teacher", annual_income=2000, country='Ind', state='AP', district='Nellore', city='Nellore', area='rfc')
        clientloan = LoanAccount.objects.create(account_no='CL6', interest_type='Flat', client=group_client6, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=20, total_loan_balance=0, principle_repayment=1000)

        g6 = Group.objects.create(name='group6', created_by=self.u, account_number='6', activation_date='2014-1-1', branch=self.b)
        g6.clients.add(group_client6)
        g6.save()
        # LoanAccount.objects.create(account_no='GL6', interest_type='Flat', group=g6, loan_repayment_amount=0, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=0, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=0, total_loan_balance=0, principle_repayment=0, loan_issued_date="2015-2-2")

        response = self.client.post("/receiptsdeposit/", {"group_name": "group6", "group_account_number": 6, "group_loan_account_no": "GL6", "loanprinciple_amount": 100, "loan_account_no": "CL6", "date": "2/2/2015", "loaninterest_amount": 0, "name": "Micro6", "account_number": 6, "branch": self.b.id, "receipt_number": 32})
        self.assertEqual(response.status_code, 200)
        # Group does not have any Loan with this Loan A/C Number.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data42(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(loan_repayment_amount=0, account_no='CL5', interest_type='Flat', client=self.c, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=0, total_loan_balance=0, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 13000, "loan_account_no": "CL5", "date": "2/2/2015", "loaninterest_amount": 0, "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 33})
        self.assertEqual(response.status_code, 200)
        # Loan has been cleared sucessfully.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data43(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(loan_repayment_amount=0, account_no='CL5', interest_type='Flat', client=self.c, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=10, total_loan_balance=1000, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 100, "loan_account_no": "CL5", "date": "2/2/2015", "loaninterest_amount": 100, "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 34})
        self.assertEqual(response.status_code, 200)
        # Entered interest amount is greater than interest charged.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data44(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(loan_repayment_amount=0, account_no='CL5', interest_type='Flat', client=self.c, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=14, total_loan_balance=14000, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 13000, "loaninterest_amount": 12, "loan_account_no": "CL5", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 35})
        self.assertEqual(response.status_code, 200)
        # Amount is greater than issued loan amount. Transaction can't be done.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data45(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(loan_repayment_amount=0, account_no='CL5', interest_type='Flat', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=14, total_loan_balance=14000, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 1000, "loaninterest_amount": 12, "loan_account_no": "CL5", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 36})
        self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data46(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL5', total_loan_balance=0, interest_type='Flat', client=self.c, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 12, "loan_account_no": "CL5", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 37})
        self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data47(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL5', total_loan_balance=0, interest_type='Flat', client=self.c, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=100)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 12, "loan_account_no": "CL5", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 38})
        self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data48(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL5', total_loan_balance=0, interest_type='Flat', client=self.c, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=14, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 12, "loan_account_no": "CL5", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 39})
        self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data49(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL5', total_loan_balance=0, interest_type='Flat', client=self.c, created_by=self.u, status="Approved", loan_amount=12000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=14, principle_repayment=100)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 12, "loan_account_no": "CL5", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 40})
        self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data50(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=24, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL5', total_loan_balance=1000, interest_type='Flat', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 12, "loan_account_no": "CL5", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 41})
        self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data51(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=24, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL5', total_loan_balance=1000, interest_type='Declining', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 12, "loan_account_no": "CL5", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 42})
        self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data52(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=24, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL5', total_loan_balance=1000, interest_type='Flat', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 10, "loan_account_no": "CL5", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 41})
        self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data53(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=24, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL5', total_loan_balance=1000, interest_type='Declining', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 10, "loan_account_no": "CL5", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 42})
        self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data53(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=24, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL5', total_loan_balance=1000, interest_type='Flat', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 10, "loan_account_no": "CL5", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 43})
        self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data54(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=24, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL5', total_loan_balance=1000, interest_type='Declining', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=100)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 10, "loaninterest_amount": 10, "loan_account_no": "CL5", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 44})
        self.assertEqual(response.status_code, 200)

    def test_receipts_deposit_post_data55(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=1, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL5', total_loan_balance=1000, interest_type='Flat', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=14, principle_repayment=0)
        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 14, "loan_account_no": "CL5", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 45})
        self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data56(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=11, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL5', total_loan_balance=1000, interest_type='Flat', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 10, "loan_account_no": "CL5", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 46})
        self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data64(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=1, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL6', total_loan_balance=1000, interest_type='Declining', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 12, "loan_account_no": "CL6", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 54})
        self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data65(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.loan_issued_date = '2015-2-2'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=1, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL6', total_loan_balance=1000, interest_type='Declining', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 10, "loan_account_no": "CL6", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 55})
        self.assertEqual(response.status_code, 200)

    # def test_receipts_deposit_post_data66(self):
    #     user_login = self.client.login(username="jagadeesh", password="jag123")
    #     self.grouploan.loan_issued_date = '2015-2-2'
    #     self.grouploan.save()
    #     self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=2, total_loan_amount_repaid=100, loan_repayment_amount=0, account_no='CL7', total_loan_balance=10, interest_type='Declining', client=self.c, created_by=self.u, status="Approved", loan_amount=24000, loan_repayment_period=2, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

    #     response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 12000, "loaninterest_amount": 10, "loan_account_no": "CL7", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 56})
    #     self.assertEqual(response.status_code, 200)
        #
        # self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data57(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=11, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL6', total_loan_balance=1000, interest_type='Declining', client=self.c, created_by=self.u, status="Applied", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 12, "loan_account_no": "CL6", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 47})
        self.assertEqual(response.status_code, 200)
        # Member Loan / Group Loan is under pending for approval.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data58(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=11, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL7', total_loan_balance=1000, interest_type='Declining', client=self.c, created_by=self.u, status="Rejected", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 12, "loan_account_no": "CL7", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 48})
        self.assertEqual(response.status_code, 200)
        # Member Loan has been Rejected.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data59(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=11, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL8', total_loan_balance=1000, interest_type='Declining', client=self.c, created_by=self.u, status="Closed", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 12, "loan_account_no": "CL8", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 49})
        self.assertEqual(response.status_code, 200)
        # Member Loan has been Closed.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data60(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.status = 'Applied'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=11, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL9', total_loan_balance=1000, interest_type='Declining', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 12, "loan_account_no": "CL9", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 50})
        self.assertEqual(response.status_code, 200)
        # Group Loan is under pending for approval.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data61(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.status = 'Applied'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=11, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL10', total_loan_balance=1000, interest_type='Declining', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 12, "loan_account_no": "CL10", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 51})
        self.assertEqual(response.status_code, 200)
        # Group Loan is under pending for approval.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data62(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.status = 'Rejected'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=11, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL11', total_loan_balance=1000, interest_type='Declining', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 12, "loan_account_no": "CL11", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 52})
        self.assertEqual(response.status_code, 200)
        # Group Loan has been Rejected.
        self.assertTrue('"error": true' in response.content)

    def test_receipts_deposit_post_data63(self):
        user_login = self.client.login(username="jagadeesh", password="jag123")
        self.grouploan.status = 'Closed'
        self.grouploan.save()
        self.clientloan = LoanAccount.objects.create(no_of_repayments_completed=11, total_loan_amount_repaid=12000, loan_repayment_amount=0, account_no='CL12', total_loan_balance=1000, interest_type='Declining', client=self.c, created_by=self.u, status="Approved", loan_amount=13000, loan_repayment_period=12, loan_repayment_every=1, annual_interest_rate=2, loanpurpose_description='Home Loan', interest_charged=12, principle_repayment=0)

        response = self.client.post("/receiptsdeposit/", {"group_name": "group1", "group_account_number": 1, "group_loan_account_no": "GL1", "loanprinciple_amount": 0, "loaninterest_amount": 12, "loan_account_no": "CL12", "date": "2/2/2015", "name": "Micro", "account_number": 123, "branch": self.b.id, "receipt_number": 53})
        self.assertEqual(response.status_code, 200)
        # Group Loan has been Closed.
        self.assertTrue('"error": true' in response.content)

    def test_close_loan_post_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post("/closeloan/"+str(self.clientloan.id)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_close_loan_post_data_group(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post("/closeloan/"+str(self.grouploan.id)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_close_loan_post_data_exception(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post("/closeloan/"+'23'+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_approve_loan_post_data(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post("/approveloan/"+str(self.clientloan.id)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_approve_loan_post_data_group(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post("/approveloan/"+str(self.grouploan.id)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_approve_loan_post_data_exception(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post("/approveloan/"+'23'+"/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": true' in response.content)

    def test_withdraw_savings_post_data_group(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/withdrawsavings/'+str(self.gs.id)+'/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_close_savings_post_data_group(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/closesavings/'+str(self.gs.id)+'/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_close_savings_post_data_client(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/closesavings/'+str(self.cs.id)+'/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_reject_savings_post_data_group(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/rejectsavings/'+str(self.gs.id)+'/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_reject_savings_post_data_client(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/rejectsavings/'+str(self.cs.id)+'/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_apporve_savings_post_data_client(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/approvesavings/'+str(self.cs.id)+'/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)

    def test_apporve_savings_post_data_group(self):
        user_login = self.client.login(username='jagadeesh', password='jag123')
        response = self.client.post('/approvesavings/'+str(self.gs.id)+'/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('"error": false' in response.content)
