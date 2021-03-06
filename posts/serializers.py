from rest_framework import serializers
from common import models


class PostSerializer(serializers.ModelSerializer):
	post_title_img_url = serializers.ReadOnlyField()
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	# user = serializers.CharField(source='user.username')


	class Meta:
		model = models.Posts
		fields = '__all__'