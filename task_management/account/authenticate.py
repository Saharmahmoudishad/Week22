# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model 

# class EmailBackend:
#     # def authenticate(self,request,email=None,password=None):
#     #     try:
#     #         user=User.objects.get(email=email)
#     #         if user.check_password(password):
#     #             return user
#     #         return None
#     #         # else:
#     #         #     user=User.objects.get(nationalcode=username)
#     #         #     return user
#     #     except User.DoesNotExist:
#     #         return None
#     USERNAME_FIELD= 'email'  
#     UserModel = get_user_model()
#     def authenticate(self, request, username=None, password=None, email=None,**kwargs):
#         if '@' in username:
#             kwargs =
#             email = kwargs.get(self.UserModel.USERNAME_FIELD)
#         if username is None or password is None:
#             return
#         try:
#             user = UserModel._default_manager.get_by_natural_key(username)
#         except UserModel.DoesNotExist:
#             # Run the default password hasher once to reduce the timing
#             # difference between an existing and a nonexistent user (#20760).
#             UserModel().set_password(password)
#         else:
#             if user.check_password(password) and self.user_can_authenticate(user):
#                 return user
    
#     def get_user(self,user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
        



             
         