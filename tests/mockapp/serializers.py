# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from rest_framework.serializers import HyperlinkedIdentityField

from drf_haystack.serializers import HaystackSerializer, HighlighterMixin
from .search_indexes import MockPersonIndex, MockLocationIndex


class SearchSerializer(HaystackSerializer):

    class Meta:
        index_classes = [MockPersonIndex, MockLocationIndex]
        fields = [
            "firstname", "lastname", "full_name",
            "address", "city", "zip_code",
        ]


class HighlighterSerializer(HighlighterMixin, HaystackSerializer):

    highlighter_css_class = "my-highlighter-class"
    highlighter_html_tag = "em"

    class Meta:
        index_classes = [MockPersonIndex, MockLocationIndex]
        fields = [
            "firstname", "lastname", "full_name",
            "address", "city", "zip_code",
        ]


class MoreLikeThisSerializer(HaystackSerializer):

    more_like_this = HyperlinkedIdentityField(view_name="search3-more-like-this", read_only=True)

    class Meta:
        index_classes = [MockPersonIndex]
        fields = [
            "firstname", "lastname", "full_name",
        ]
