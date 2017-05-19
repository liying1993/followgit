from rest_framework import serializers
from snippets.models import Snippet,Product,Album,Track, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from account.models import Profile,Profile_Team
import time
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('url','id', 'owner','title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = '__all__'
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('order','title','duration')

class TrackListingField(serializers.RelatedField):
    def to_representation(self, value):
        duration = time.strftime('%M:%S', time.gmtime(value.duration))
        return 'Track %d:%s(%s)' % (value.order, value.name, duration)


class AlbumSerializer(serializers.ModelSerializer):
    # tracks = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='track-detail')
    # tracks = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
    # track_listing = serializers.HyperlinkedIdentityField(view_name='track-detail')
    tracks = TrackSerializer(many=True,read_only=True)
    # tracks = TrackListingField(many=True)
    class Meta:

        model = Album
        fields = ('album_name','artist','tracks')
    def create(self, validated_data):
        '''
        >>> data = {
        'album_name': 'The Grey Album',
        'artist': 'Danger Mouse',
        'tracks': [
        {'order': 1, 'title': 'Public Service Announcement', 'duration': 245},
        {'order': 2, 'title': 'What More Can I Say', 'duration': 264},
        {'order': 3, 'title': 'Encore', 'duration': 159},
        ],
        }
        >>> serializer = AlbumSerializer(data=data)
        >>> serializer.is_valid()
        True
        >>> serializer.save()
        <Album: Album object>
        :param validated_data: 
        :return: 
        '''
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album,**track_data)
        return album
class AccountSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    login_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    logout_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    profile_team = serializers.StringRelatedField(many=True)
    class Meta:
        model = Profile
        fields = '__all__'
        # fields = ('created_at','login_at','logout_at','updated_at','username','profile_team')
class AccountTeamSerializer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField(many=True)
    class Meta:
        model = Profile_Team
        # fields = '__all__'
        fields = ('profile','name',)




