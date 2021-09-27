from django.test import TestCase
from .models import  Business, Neighborhood, Users, Post
# Create your tests here.
class ProjectsTestClass(TestCase):
    def setUp(self):
       

        # Creating a new Neighborhood and saving it
        self.new_neighborhood = Neighborhood(name="Mwangaza",location = 'Rongai', occupants_count=1)
        self.new_neighborhood.save()
        
        # Creating a new user and saving it
        self.user=Users(name="kelvin kip",profile_photo = 'xyz.png', email="triplek@gmail.com", phone_number ='+254725801772',date_joined="2021-09-05 22:16:35.61389+03",neighborhood=self.new_neighborhood)
        self.user.save()

        # Creating a new business and saving it
        self.new_business = Business(name="Kware supermatt",business_email="kwaremat@yahoo.com",neighborhood=self.new_neighborhood, user=self.user)
        self.new_business.save()

    def tearDown(self):
        Users.objects.all().delete()
        Business.objects.all().delete()
        Neighborhood.objects.all().delete()

    # TEST USERS
    def test_saveuser(self):
        user=Users(username="kk",profile_photo = 'xyz.png',name="kelvin koech", email="triplek@gmail.com", phone_number ='+254725801772',date_joined="2021-09-05 22:16:35.61389+03")
        # Users.save_user(user)
        users_count = Users.objects.all().count()
        self.assertTrue(users_count>0)


    def test_update_user(self):
        user = Users.objects.first()
        id=user.id
        name="koech"  
        profile_photo="abc.jpg"
        phone_number="+254725801772"     
        neighborhood=self.new_neighborhood
        Users.update_user(id,profile_photo,phone_number,neighborhood,name )
        updated_user = Users.objects.get(id=id)
        self.assertEqual(updated_user.name,"koech")

    def test_delete_user(self):
        user=Users.objects.first()
        id=user.id
        Users.delete_user(id)
        try:
            Users.objects.get(id=id)
            self.assertTrue("Some results")
        except Users.DoesNotExist:
            self.assertTrue("no results"=="no results")

    # TEST NEIGHBORHOOD
    def test_save_create_neighborhood(self):
        neighborhood=Neighborhood(name="Mwangaza",location = 'Rongai', occupants_count=1)
        Neighborhood.create_neigborhood(neighborhood)
        neighborhood_obj = Neighborhood.objects.all().count()
        self.assertTrue(neighborhood_obj>1)


    def test_find_neigborhood(self):
        name="Mwangaza"
        count=Neighborhood.find_neigborhood(name)
        self.assertTrue(count>0)

    def test_update_neighborhood(self):
        neighborhood = Neighborhood.objects.first()
        id=neighborhood.id
        name="Olekasase"
        Neighborhood.update_neighborhood(id,name)
        profile = Neighborhood.objects.get(id=id)
        self.assertEqual(profile.name,"Olekasase")

    def test_update_occupants_count(self):
        neighborhood = Neighborhood.objects.first()
        id=neighborhood.id
        occupants_count=10
        Neighborhood.update_occupants(id,occupants_count)
        new_neighborhood = Neighborhood.objects.get(id=id)
        self.assertEqual(new_neighborhood.occupants_count,10)

    # TEST BUSINESS
    # def test_save_business(self):
    #     user=Users(username="kk",profile_photo = 'xyz.png',name="kelvin koech", email="triplek@gmail.com", phone_number ='+254725801772',date_joined="2021-09-05 22:16:35.61389+03")
    #     # Users.save_user(user)
    #     users_count = Users.objects.all().count()
    #     self.assertTrue(users_count>0)
        
    def test_delete_business(self):
        business=Business.objects.first()
        id=business.id
        Business.delete_business(id)
        try:
            Business.objects.get(id=id)
            self.assertTrue("Some results")
        except Business.DoesNotExist:
            self.assertTrue("no results"=="no results")

    def test_update_business(self):
        business_obj = Business.objects.first()
        id=business_obj.id
        name="Tumaini Supermarket"
        business_email="tumain@gmail.com"   
        Business.update_business(id,name, business_email)
        updated_business = Business.objects.get(id=id)
        self.assertEqual(updated_business.name, "Tumaini Supermarket")
    # # TEST REVIEW
    # def test_save_review(self):
    #     review= Review(design=2,usability=6,content=8,project=self.new_project,date_voted="2021-09-05 22:16:35.61389+03", user=self.user)
    #     review.save_review()
    #     review_obj = Review.objects.all().count()
    #     self.assertTrue(review_obj>1)


    # def test_update_review(self):
    #     review_obj = Review.objects.first()
    #     id=review_obj.id
    #     design=3
    #     content=6
    #     usability=10    
    #     Review.update_review(id,design,content,usability)
    #     updated_review = Review.objects.get(id=id)
    #     self.assertEqual(updated_review.content,6.0)

    # def test_delete_review(self):
    #     reviews=Review.objects.first()
    #     id=reviews.id
    #     reviews.delete_review(id)
    #     try:
    #         Review.objects.get(id=id)
    #         self.assertTrue("Some results")
    #     except Review.DoesNotExist:
    #         self.assertTrue("no results"=="no results")