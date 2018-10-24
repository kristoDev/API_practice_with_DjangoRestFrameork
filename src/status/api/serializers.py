from rest_framework import serializers
from status.models import Status



class StatusSerializer(serializers.ModelSerializer):

	class Meta:

		model = Status

		fields = [

			'user',
			'content',
			'image'

		]


		def valudate(self,data):

			content = data.get('content', None)

			if content == "":
				content = None

			image = data.get('image', None)

			if content is None or image is None:

				raise serializers.ValidationError(
					"either the image or content is missing"
					)

				return data