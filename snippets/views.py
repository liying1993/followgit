# _*_ coding:utf-8 _*_
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet,Product
# from django_url_filter import
from snippets.serializers import *
from django.db import models
from django.core.exceptions import *
from rest_framework.views import exception_handler
from rest_framework.permissions import IsAdminUser
from rest_framework.exceptions import APIException
from django import forms
from django.shortcuts import render,get_object_or_404
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import detail_route
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework import views
from rest_framework import status
import pdb
import time
from django.http import Http404
from rest_framework import mixins
import django_filters
from account.models import *

# from django_filters import rest_framework
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
class SnippetList(APIView):
    def get(self, request,format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return Response(serializer.data)
    def post(self, request,format=None):
        serializer = SnippetSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser,)

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser,)
#
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         # pdb.set_trace()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000
    # page_query_param = 'title'

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A viewset that provides the standard actions
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     @detail_route(methods=['post'])
#     def set_password(self, request, pk=None):
#         user = self.get_object()
#         serializer = PasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             user.set_password(serializer.data['password'])
#             user.save()
#             return Response({'status': 'password set'})
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)
#
#     @list_route()
#     def recent_users(self, request):
#         recent_users = User.objects.all().order('-last_login')
#
#         page = self.paginate_queryset(recent_users)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(recent_users, many=True)
#         return Response(serializer.data)
# class ProcurementFilter(filters.FilterSet):
#     class Meta:
#         model = Snippet
#         fields = ['code','id','title']
class ProcurementFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr=['contains','dictinct'])
    class Meta:
        model = Snippet
        fields = ['title','code']
    # class Meta:
    #     model = Snippet
    #     fields = {
    #         'title':['contains'],
    #     }
class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    # search_fields = ('$title', 'code')
    filter_class = ProcurementFilter
    pagination_class = LargeResultsSetPagination
    # def get_queryset(self):
    #     queryset = Snippet.objects.all()
    #     return queryset
    # def list(self, request, *args, **kwargs):
    #     pdb.set_trace()
    #     baseQueryset = self.get_queryset()
    #     subQueryset = ProcurementFilter(request.query_params, baseQueryset)
    #     serializer = SnippetSerializer(subQueryset, many=True)
        # return Response(serializer.data)
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)
    lookup_field = ('title',)

    def get_queryset(self):
        user = self.request.user
        return user.accounts.all()
    # def get(self, request, *args, **kwargs):
    #     snippet = self.get_object()
    #     # 会调用父类的get_objects()，直接在这个方法里面根据查询条件过滤得到对应的对象
    #     return Response(snippet.highlighted)
    #     #在页面上输入并保存的时候，已经转换成了html了

class TestGenerics(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    lookup_field = ('title',)
    def get_queryset(self):
        queryset = Snippet.objects.all()
        return queryset
    def list(self, request, *args, **kwargs):
        subQueryset = self.get_queryset()
        serializer = SnippetSerializer(subQueryset, many=True)
        return Response(serializer.data)
class ProductFilter(filters.FilterSet):
    # price = django_filters.NumberFilter()
    # price__gt = django_filters.NumberFilter(name='price',lookup_expr='gt')
    # price__lt = django_filters.NumberFilter(name='price',lookup_expr='lt')
    #
    # release_year = django_filters.NumberFilter(name='release_date',lookup_expr='year')
    # release_year__gt = django_filters.NumberFilter(name='release_date',lookup_expr='year__gt')
    # release_year__lt = django_filters.NumberFilter(name='release_date',lookup_expr='year__lt')
    # manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Product
        # fields = ['price','price__gt','release_year','release_year__lt','manufacturer__name']
        fields = ['price','release_date']
        # fields = {
        #     'price':['lt','gt'],
        #     'release_date':['exact','year__gt'],
        # }
        # fields = {
        #     'name':['exact'],
        #     'release_date':['isnull'],
        # }
        # filter_overrides = {
        #     models.CharField:{
        #         'filter_class':django_filters.CharFilter,
        #         'extra':lambda f:{
        #             'lookup_expr':'icontains',
        #         },
        #     },
        #     models.BooleanField:{
        #         'filter_class':django_filters.BooleanFilter,
        #         'extra':lambda f:{
        #             'widget':forms.CheckboxInput,
        #         },
        #     },
        # }
        # @property
        # def qs(self):
        #     parent = super(ProductFilter,self).qs
        #     return parent.filter(name='aa')
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductFilter

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name','release_date')

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class AccountFilter(filters.FilterSet):
    class Meta:
        model = Profile
        fields = ['id','username']

class AcountResultsSetPagination(LimitOffsetPagination):
    # default_limit
    # limit_query_param
    # offset_query_param
    max_limit = 100

class IsOwnerFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        searchparam = request.GET['id']
        afterlist = []
        # pdb.set_trace()
        listquery = searchparam.split(',')
        for i in listquery:
            # i = int(i)-1
            queryid = int(i)
            # pdb.set_trace()
            try:
                afterquery = Profile.objects.get(id=queryid)
            except  ObjectDoesNotExist as exc:
                context = {"ss":"ss"}
                # pdb.set_trace()
                custom_exception_handler(exc,context)
                if len(afterlist):
                    return afterlist
                else:

                    # pdb.set_trace()
                    # content = {'533':'there are not what you query'}
                    # return Response({'status': 'password set'})
                    # custom_exception_handler(ObjectDoesNotExist,content)
                    # error = NotFound()

                    raise NotFound()
                # raise Http404

            afterlist.append(afterquery)
        return afterlist

    def custom_exception_handler(self,exc, context):
        # Call REST framework's default exception handler first,
        # to get the standard error response.
        response = exception_handler(exc, context)

        # Now add the HTTP status code to the response.
        if response is not None:
            response.data['status_code'] = response.status_code
        return response
class NotFound(APIException):
    # status_code = status.HTTP_404_NOT_FOUND
    # default_detail = 'The resource was not found.'
    status_code = 404
    default_detail = {'error_code':3333,'mess':'ssssssssssss'}
    # default_code = 'service_unavailable'
    # error_code = '3333333333'
    def __init__(self,detail=None):
        if detail is not None:
            self.detail = force_text(detail)
        else:
            self.detail = force_text(self.default_detail)
            # self.error_code = force_text(self.error_code)

    def empty_view(self):
        content = {'please move along': 'nothing to see here'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    def __init__(self, detail=None):
        self.detail = detail or self.default_detail
    # def empty_view(self):
    #     content = {'please move along': 'nothing to see here'}
    #     return Response(content, status=status.HTTP_404_NOT_FOUND)

class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = AccountSerializer
    # filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    # filter_backends = (filters.OrderingFilter,)
    # filter_class =
    # filter_backends = (IsOwnerFilterBackend,filters.SearchFilter,)

    # search_fields = ('id',)
    # ordering_fields = ('username',)
    # filter_class = AccountFilter
    # pagination_class = AcountResultsSetPagination

class AccountTeamViewSet(viewsets.ModelViewSet):
    queryset = Profile_Team.objects.all()
    serializer_class = AccountTeamSerializer
    # def get_queryset(self):
    #     queryset = Profile_Team.objects.all()
    #     profile = Profile.objects.all()
    #     total = []
    #     turnaround = []
    #     teamdict = {}
    #     Profile.objects.filter(profile_team=1)
    #     for team in queryset:
    #         list1 = Profile.objects.filter(profile_team=team.id)
    #         key = team.name
    #         teamdict[key] = list1
    #         total.append(teamdict)
    #         teamdict = {}
    #     for item in total:
    #         itemobject = DictObj(item);
    #         turnaround.append(itemobject)
    #     return turnaround

class DictObj(object):
    def __init__(self,map):
        self.map = map

    def __setattr__(self, name, value):
        if name == 'map':
             object.__setattr__(self, name, value)
             return;
        print 'set attr called ',name,value
        self.map[name] = value

    def __getattr__(self,name):
        v = self.map[name]
        if isinstance(v,(dict)):
            return DictObj(v)
        if isinstance(v, (list)):
            r = []
            for i in v:
                r.append(DictObj(i))
            return r
        else:
            return self.map[name];

    def __getitem__(self,name):
        return self.map[name]
def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response






