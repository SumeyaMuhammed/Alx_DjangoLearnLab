# Permissions & Groups Setup

This module uses Django custom permissions and groups to control access.

Custom permissions (defined in Article model):
- can_view
- can_create
- can_edit
- can_delete

Groups:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

Views enforce permissions via @permission_required.

To update permissions:
1. Edit Meta.permissions in models.py
2. Run migrations
3. Assign permissions via Django Admin
