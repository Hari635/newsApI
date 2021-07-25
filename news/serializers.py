from datetime import datetime
from django.utils.timesince import timesince
from django.db.models import fields
from django.utils.translation import activate
from rest_framework import serializers
from .models import Article, Journalist

class ArticleSerilizer(serializers.ModelSerializer):
    # there is advantage in this serializers.ModelSerializer class which can't define readonly property to our fields
    time_since_publication=serializers.SerializerMethodField()
    # we can add additional fields to serializers which is not present in the model class
    # to get value for particular fields we have to define the method get_feildname
    # author=serializers.StringRelatedField()
    # def __str__(self) -> str:
    #     return f"{self.first_name} {self.last_name}"
    #the above function is called it will dispay the firstname and last name



    class Meta:
        model=Article
        exclude=("id",)
        # fields="__all__" #we want all the fields of our model
        # fields=("title","description","body") # we want to choose a couple of fields
    def get_time_since_publication(self,object):
        publication_date=object.publication_date
        now=datetime.now()
        time_delta=timesince(publication_date,now)
        return time_delta
    #above mehtod is the get_fieldsname method

    def validate(self, attrs):
        if( attrs["title"]==attrs["description"]):
            raise serializers.ValidationError("Title and Description must be different")
        return attrs
        #this is field level validator
    def validate_title(self, attrs):
        if(len(attrs)<60):
            raise serializers.ValidationError("title is less than 60")
        return attrs
        #   to create validate for particular fields we want to add validate_fieldsname


class JournalistSerializer(serializers.ModelSerializer):
    articles=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name="article-detail")
    #the above field is used to create the link
    # articles=ArticleSerilizer(many=True,read_only=True)
    class Meta:
        model=Journalist
        fields="__all__"

# class ArticleSerilizer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     author=serializers.CharField()
#     title=serializers.CharField()
#     description=serializers.CharField()
#     body=serializers.CharField()
#     location=serializers.CharField()
#     publication_date=serializers.DateField()
#     active=serializers.BooleanField()
#     created_at=serializers.DateTimeField(read_only=True)
#     updated_at=serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.author=validated_data.get('author',instance.author)
#         instance.title=validated_data.get('title',instance.title)
#         instance.description=validated_data.get('description',instance.description)
#         instance.body=validated_data.get('body',instance.body)
#         instance.location=validated_data.get('location',instance.location)
#         instance.publication_date=validated_data.get('publication_date',instance.publication_date)
#         instance.active=validated_data.get('active',instance.active)
#         # validated_data.get() this method takes two value one is new value another one is old value
#         instance.save()
#         return instance
    
#     def validate(self, attrs):
#         if( attrs["title"]==attrs["description"]):
#             raise serializers.ValidationError("Title and Description must be different")
#         return attrs
#         #this is field level validator
    
#     def validate_title(self, attrs):
#         if(len(attrs)<60):
#             raise serializers.ValidationError("title is less than 60")
#         return attrs
          #to create validate for particular fields we want to add validate_fieldsname










        