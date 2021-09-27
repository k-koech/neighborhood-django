from django.test import TestCase
from .models import  Business, Health, Neighborhood, Police, Users, Post
# Create your tests here.
class ProjectsTestClass(TestCase):
    def setUp(self):
       

        # Creating a new Neighborhood and saving it
        self.new_neighborhood = Neighborhood(name="Mwangaza",location = 'Rongai', occupants_count=1)
        self.new_neighborhood.save()
        
        # Creating a new user and saving it
        self.user=Users(name="kelvin kip",profile_photo = 'xyz.png', email="triplek@gmail.com", phone_number ='+254725801772',neighborhood=self.new_neighborhood)
        self.user.save()

        # Creating a new business and saving it
        self.new_business = Business(name="Kware supermatt",business_email="kwaremat@yahoo.com",neighborhood=self.new_neighborhood, user=self.user)
        self.new_business.save()

        # Creating a new health and saving it
        self.new_health = Health(contact="mtcr@gmail.com" , neighborhood=self.new_neighborhood)
        self.new_health.save()
        
        # Creating a new police and saving it
        self.new_police = Police(contact="rongaipolice@gmail.com", neighborhood=self.new_neighborhood)
        self.new_police.save()


    def tearDown(self):
        Users.objects.all().delete()
        Business.objects.all().delete()
        Neighborhood.objects.all().delete()


    """TEST USERS"""
    def test_saveuser(self):
        user=Users(username="kk",profile_photo = 'xyz.png',name="kelvin koech", email="triplek@gmail.com", phone_number ='+254725801772')
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


    """TEST NEIGHBORHOOD"""
    def test_save_create_neighborhood(self):
        neighborhood=Neighborhood(name="Mwangaza",location = 'Rongai', occupants_count=1)
        Neighborhood.create_neigborhood(neighborhood)
        neighborhood_obj = Neighborhood.objects.all().count()
        self.assertTrue(neighborhood_obj>1)


    def test_find_neigborhood(self):
        neighborhood = Neighborhood.objects.first()
        id=neighborhood.id
        count=Neighborhood.find_neigborhood(id)
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


    """TEST BUSINESS"""
    def test_save_business(self):
        business=Business(name="Kware supermatt",business_email="kwaremat@yahoo.com",neighborhood=self.new_neighborhood, user=self.user)
        Business.create_business(business)
        business_count = Business.objects.all().count()
        self.assertTrue(business_count>0)
        
    def test_delete_business(self):
        business=Business.objects.first()
        id=business.id
        Business.delete_business(id)
        try:
            Business.objects.get(id=id)
            self.assertTrue("Some results")
        except Business.DoesNotExist:
            self.assertTrue("no results"=="no results")

    def test_find_business(self):
        business = Business.objects.first()
        id=business.id
        count=Business.find_business(id)
        self.assertTrue(count>0)


    def test_update_business(self):
        business_obj = Business.objects.first()
        id=business_obj.id
        name="Tumaini Supermarket"
        business_email="tumain@gmail.com"   
        Business.update_business(id,name, business_email)
        updated_business = Business.objects.get(id=id)
        self.assertEqual(updated_business.name, "Tumaini Supermarket")


    """TEST POST"""
    def test_save_post(self):
        post=Post(title="Lets have fun tommorow",content="We will have a ride to Ngong and back",neighborhood=self.new_neighborhood, user=self.user)
        Post.save_post(post)
        post_obj = Post.objects.all().count()
        self.assertTrue(post_obj==1)


    def test_update_post(self):
        post=Post(title="Lets have fun tommorow",content="We will have a ride to Ngong and back",neighborhood=self.new_neighborhood, user=self.user)
        Post.save_post(post)
        post_obj = Post.objects.first()
        id=post_obj.id
        title="Yesterday robbery"
        content="We will have a ride to Ngong and back tommorow"
        image="ysc.png"  
        Post.update_post(id,title, content,image)
        updated_post = Post.objects.get(id=id)
        self.assertEqual(updated_post.title,"Yesterday robbery")

    def test_delete_post(self):
        post=Post(title="Lets have fun tommorow",content="We will have a ride to Ngong and back",neighborhood=self.new_neighborhood, user=self.user)
        Post.save_post(post)
        posts=Post.objects.all().first()
        id=posts.id
        Post.delete_post(id)
        try:
            Post.objects.get(id=id)
            self.assertTrue("Some results")
        except Post.DoesNotExist:
            self.assertTrue("no results"=="no results")

    """TEST HEALTH"""
    def test_save_health(self):
        health=Health(contact="mtcr@gmail.com", neighborhood=self.new_neighborhood)
        Health.create_health(health)
        health_obj = Health.objects.all().count()
        self.assertTrue(health_obj>1)
   
    def test_update_health(self):
        health_obj = Health.objects.first()
        id=health_obj.id
        contact="kmtc@yahoo.com"  
        Health.update_health(id,contact)
        updated_health = Health.objects.get(id=id)
        self.assertEqual(updated_health.contact,"kmtc@yahoo.com")

    def test_delete_health(self):
        health=Health.objects.first()
        id=health.id
        Health.delete_health(id)
        try:
            Health.objects.get(id=id)
            self.assertTrue("Some results")
        except Health.DoesNotExist:
            self.assertTrue("no results"=="no results")
    
    """TEST POLICE"""
    def test_save_police(self):
        police=Police(contact="rongaipolice@gmail.com", neighborhood=self.new_neighborhood)
        Police.create_police(police)
        police_obj = Police.objects.all().count()
        self.assertTrue(police_obj>1)
   
    def test_update_police(self):
        police_obj = Police.objects.first()
        id=police_obj.id
        contact="rongaipolice@yahoo.com"  
        Police.update_police(id,contact)
        updated_police = Police.objects.get(id=id)
        self.assertEqual(updated_police.contact,"rongaipolice@yahoo.com")

    def test_delete_police(self):
        police=Police.objects.first()
        id=police.id
        police.delete_police(id)
        try:
            Police.objects.get(id=id)
            self.assertTrue("Some results")
        except Police.DoesNotExist:
            self.assertTrue("no results"=="no results")
