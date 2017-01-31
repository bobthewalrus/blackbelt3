from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re
from datetime import *

emailregex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
nameregex = re.compile(r'^[a-zA-Z]+$')

class UserManager(models.Manager):
    def registervalidation(self,post):
        errors = self.validate_inputs(post)

        if len(errors) >0:
            return (False, errors)
        password = post['password'].encode()
        pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())
        print pw_hash

        user = self.create(name=post['name'], alias = post['alias'], email=post['email'], pw_hash=pw_hash, dob=post['dob'], pokecount=0)
        print user.pw_hash
        return (True, user)

    def validate_inputs(self,post):
        email = post['email'].lower()
        name = post['name'].lower()
        alias = post['alias'].lower()
        password = post['password']
        passwordconf = post['passwordconf']

        errors=[]
        if len(name) <3 or len(alias) <3:
            errors.append("Names must be longer than 2 characters.")
        if not nameregex.match(name):
            errors.append('Names must contain  only letters.')

        if not nameregex.match(alias):

            errors.append('Alias must contain only letters.')
        if not emailregex.match(email):
            errors.append('Email is invalid.')

        if password != passwordconf:
            errors.append('Passwords do not match!')
        elif len(password) < 8:
            errors.append('Password is too short!')

        users_list = User.objects.filter(email=email)
        if users_list:
            errors.append('Email is invalid.')

        return errors

    def loginvalidation(self,post):
        print '**********validating login******'
        try:
            users_list = User.objects.filter(email=post['email'])
            if users_list:
                user = users_list[0]
            else:
                return (False, ["email or password didn't exist"])
            password = post['password'].encode()
            passwordhashed = bcrypt.hashpw(password, bcrypt.gensalt())
            print passwordhashed
            print "user's pw_hash is ",user.pw_hash
            print password
            if bcrypt.hashpw(password, user.pw_hash.encode()) == user.pw_hash.encode():
                print bcrypt.hashpw(password, user.pw_hash.encode())
                print user.pw_hash
                return (True, user)
        except ObjectDoesNotExist:
            print "POOOOP"
            pass
        return (False, ["Email and password don't match."])

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    dob = models.DateField(default=datetime.now())
    pokecount = models.IntegerField()
    objects = UserManager()

class Poke(models.Model):
    user = models.ForeignKey(User)
    pokeid = models.CharField(max_length=45, null=True)
