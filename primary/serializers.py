from rest_framework import serializers
from .models import Post,PostImage,Review,Reply


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id','image']  

    def create(self, validated_data):
        if validated_data['image'] is None:
            raise serializers.ValidationError("Image can't be empty")
        post_id=self.context['post_id']
        return PostImage.objects.create(post_id=post_id,**validated_data)
    


class PostSerializer(serializers.ModelSerializer):
    # image=serializers.ListField(child=serializers.ImageField())
    image=PostImageSerializer(many=True,required=False)
    class Meta:
        model=Post
        fields=['id','title','description','created_at','image']

    def create(self, validated_data):
        user_id=self.context['user_id']
        return Post.objects.create(user_id=user_id,**validated_data)
    # def create(self, validated_data):
    #     user_id = self.context['user_id']
    #     images_data = validated_data.pop('image', [])

    #     post = Post.objects.create(user_id=user_id, **validated_data)

    #     for image_data in images_data:
    #         PostImage.objects.create(post=post, **image_data)

    #     return post
    


class ReviewSerializer(serializers.ModelSerializer):
    fullname=serializers.SerializerMethodField(method_name='get_fullname')
    class Meta:
        model=Review
        fields=['id','fullname','description','date']

    def get_fullname(self,review):
        return f"{review.user.first_name} {review.user.last_name}"


    def create(self, validated_data):
        post_id=self.context['post_id']
        user_id=self.context['user_id']
        return Review.objects.create(post_id=post_id,user_id=user_id,**validated_data)
        
class ReplySerializer(serializers.ModelSerializer):
    fullname=serializers.SerializerMethodField(method_name='get_fullname')
    class Meta:
        model=Reply
        fields=['id','fullname','reply','date']

    def get_fullname(self,reply):
        return f"{reply.user.first_name} {reply.user.last_name}"

    def create(self, validated_data):
        user_id=self.context['user_id']
        review_id=self.context['review_id']
        return Reply.objects.create(user_id=user_id,review_id=review_id,**validated_data)

    