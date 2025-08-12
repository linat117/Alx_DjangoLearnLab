## Blog Post Management

### Features

- View all blog posts
- View individual posts
- Create posts (login required)
- Edit & delete posts (author only)

### URLs

- `/` → List all posts
- `/posts/<id>/` → View post details
- `/posts/new/` → Create a new post
- `/posts/<id>/edit/` → Edit post (author only)
- `/posts/<id>/delete/` → Delete post (author only)

### Permissions

- Only authenticated users can create posts.
- Only the post’s author can edit or delete it.
- All posts are visible to everyone.
