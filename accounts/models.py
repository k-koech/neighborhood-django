from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import datetime as dt

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError(" User must have an email address")
        if not username:
            raise ValueError(" User must have an username!")    
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password = password,
            username=username,
        )
        user.email = email
        user.is_admin = True 
        user.is_staff = True 
        user.is_superuser = True 
        user.save(using=self._db)
        return user
        
class Users(AbstractBaseUser):
    name = models.CharField( max_length=200)  
    username = models.CharField( max_length=200, blank=True)  
    email = models.CharField( max_length=100, unique=True)
    id_number = models.IntegerField(null=True)
    phone_number = models.CharField(max_length = 15,blank =True)
    neighborhood=models.ForeignKey("Neighborhood",on_delete=models.CASCADE, null=True)
    profile_photo = CloudinaryField('image', default='image/upload/v1631717620/default_uomrne.jpg') 
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(default=dt.datetime.now)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password_reset = models.CharField( max_length=50, default="e5viu3snjorndvd")    
    password = models.CharField(max_length=100)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username']
    
    objects=MyAccountManager()
     
    def _str_(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name_plural='Users'


    def save_user(self):
        self.save()

    @classmethod
    def delete_user(cls,id):
        delete_user = cls.objects.get(id=id)
        delete_user.delete()
        return delete_user
    
    @classmethod
    def update_user(cls,id,profile_photo, phone_number,neighborhood, name):
        user=cls.objects.get(id=id)

        user.profile_photo=profile_photo
        user.phone_number=phone_number
        user.neighborhood=neighborhood
        user.name=name
        return user.save()



class Post(models.Model):
    '''
     Post class to define post Objects
    '''
    title = models.CharField(max_length =200)
    date_posted = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    content= models.TextField()
    image = CloudinaryField('image') 
    user=models.ForeignKey("Users",on_delete=models.CASCADE)
    neighborhood=models.ForeignKey("Neighborhood",on_delete=models.CASCADE)

    # @classmethod
    def save_post(self):
        self.save()
        
    @classmethod
    def delete_post(cls,id):
        delete_post = cls.objects.get(id=id)
        delete_post.delete()
        return delete_post
    
    @classmethod
    def update_post(cls,id,title, content,image):
        post=cls.objects.get(id=id)
        post.title=title
        post.content=content
        post.image=image
        return post.save()
    

class Neighborhood(models.Model):
    """NEIGHBORHOOD MODEL"""
    name = models.CharField(max_length =200)
    location = models.CharField(max_length =200)
    occupants_count = models.IntegerField()
    # admin=models.ForeignKey("Admin",on_delete=models.CASCADE)


    def create_neigborhood(self):
        self.save()
    
    @classmethod
    def delete_neigborhood(cls):
        delete_post = cls.objects.get(id=id)
        delete_post.delete()
        return delete_post

    @classmethod
    def find_neigborhood(cls,neigborhood_id):
        neighborhood=cls.objects.filter(id=neigborhood_id).count()
        return neighborhood

    @classmethod
    def update_neighborhood(cls,id, name):
        neighborhood=cls.objects.get(id=id)
        neighborhood.name=name
        return neighborhood.save()

    @classmethod
    def update_occupants(cls, id, occupants_count):
        neighborhood=cls.objects.get(id=id)
        neighborhood.occupants_count=occupants_count
        return neighborhood.save()

class Business(models.Model):
    """BUSINESS MODEL"""
    name = models.CharField(max_length =200)
    business_email=models.CharField(max_length =200)
    neighborhood=models.ForeignKey("Neighborhood",on_delete=models.CASCADE)
    user=models.ForeignKey("Users",on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural='Businesses'
    
    def create_business(self):
        self.save()
        
    @classmethod
    def find_business(cls,business_id):
        neighborhood=cls.objects.filter(id=business_id).count()
        return neighborhood

    @classmethod
    def delete_business(cls,id):
        delete_business = cls.objects.get(id=id)
        delete_business.delete()
        return delete_business
    
    @classmethod
    def update_business(cls,id,name, business_email):
        business=cls.objects.get(id=id)
        business.name=name
        business.business_email=business_email
        return business.save()
    

class Health(models.Model):
    """HEALTH MODEL"""
    contact = models.CharField(max_length =200)
    neighborhood=models.ForeignKey("Neighborhood",on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Health'
        
    def create_health(self):
        self.save()

    @classmethod
    def delete_health(cls,id):
        delete_health = cls.objects.get(id=id)
        delete_health.delete()
        return delete_health
    
    @classmethod
    def update_health(cls,id,contact):
        health=cls.objects.get(id=id)
        health.contact=contact
        return health.save()
    
 
class Police(models.Model):
    contact = models.CharField(max_length =200)
    neighborhood=models.ForeignKey("Neighborhood",on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Police'

    def create_police(self):
        self.save()

    @classmethod
    def delete_police(cls,id):
        delete_police = cls.objects.get(id=id)
        delete_police.delete()
        return delete_police
    
    @classmethod
    def update_police(cls,id,contact):
        police=cls.objects.get(id=id)
        police.contact=contact
        return police.save()