# Library Project

### 🛡️ Permission System Setup

This project uses Django's built-in permission and group system to control access to views related to the `Document` model.

#### 🔐 Custom Permissions (in Document model):

- `can_view`: View the list of documents.
- `can_create`: Create new documents.
- `can_edit`: Edit existing documents.
- `can_delete`: Delete documents.

#### 👥 Groups:

- `Viewers`: Has `can_view` permission.
- `Editors`: Has `can_view`, `can_create`, `can_edit` permissions.
- `Admins`: Has all permissions.

#### 🔍 How to Test:

1. Create users via Django admin.
2. Assign them to the appropriate group.
3. Try accessing different views:
   - `/documents/` → Requires `can_view`
   - `/documents/create/` → Requires `can_create`
   - `/documents/edit/<id>/` → Requires `can_edit`
   - `/documents/delete/<id>/` → Requires `can_delete`

## 🔐 Django Security Enhancements

### 1. Secure Settings

- DEBUG = False
- Secure headers: SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, etc.
- Cookies are sent only over HTTPS

### 2. CSRF Protection

- All forms include `{% csrf_token %}` for CSRF defense

### 3. Safe Querying

- All user input is validated using Django Forms
- Views use Django ORM, no raw SQL used

### 4. CSP

- Django-CSP installed and configured to restrict JS and CSS sources

### 5. Testing

- Forms tested for CSRF token presence
- Inputs tested against XSS and SQL injection
