from rest_framework import serializers
from .models import Album, Track

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'track_name', 'track_number', 'duration']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)
    class Meta:
        model = Album
        fields = ['id', 'album_name', 'artist', 'tracks']
        
    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album

    def update(self, instance, validated_data):
        tracks_data = validated_data.pop('tracks')
        tracks = (instance.tracks).all()
        tracks = list(tracks)

        instance.album_name = validated_data.get('album_name', instance.album_name)
        instance.artists = validated_data.get('artist', instance.artist)
        instance.save()
        for track_data in tracks_data:
            track = tracks.pop(0)
            track.track_name = track_data.get('track_name', track.track_name)
            track.track_number = track_data.get('track_number', track.track_number)
            track.duration = track_data.get('duration', track.duration)

            track.save()

        return instance