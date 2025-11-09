def is_admin(user):
  return user.userprofile.role == 'Admin'
