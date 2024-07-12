from rest_framework.permissions import BasePermission, SAFE_METHODS
import json

# attendant
class Attendant_FullAccess(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.account_type == 'at':
                return True
        except Exception as e:
            return False
class Attendant_ReadOnly(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.account_type == 'at':
                return request.method in SAFE_METHODS
        except:
            return False
        
# support
class Support_FullAccess(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.account_type == 'sp':
                return True
        except:
            return False
        
# consumer
class Consumer_FullAccess(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.account_type == 'cn':   
                return True
        except:
            return False
class Consumer_ReadOnly(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.account_type == 'cn':
                return request.method in SAFE_METHODS
        except:
            return False
        
# manager
class Manager_FullAccess(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.account_type == 'mn':
                return True
        except:
            return False
class Manager_ReadOnly(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.account_type == 'mn':
                return request.method in SAFE_METHODS
        except:
            return False
        
        
# readonly
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    
class IsOwnAccount(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.method not in SAFE_METHODS:
                print(1)
                data = request.body
                data_dict = json.loads(data.decode("utf-8")) 
                print(data_dict['pk'] == request.user.pk) 
                print(data_dict['pk']) 
                print(request.user.pk) 
                print('shooo')
                return data_dict['pk'] == request.user.pk
            else:
                print(request.user.pk)
                print(request.get_full_path_info().split("/")[-2])
                return int(request.get_full_path_info().split("/")[-2]) == request.user.pk
        
        except:
            return False
    def has_object_permission(self, request, view, obj):
        print(obj.pk == request.user.pk)
        print(213)

        return obj.pk == request.user.pk