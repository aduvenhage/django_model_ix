# Django Model Import-Export
As part of my efforts to learn python and django I decided to create a little module that can export model fields to YAML and then import it again to restore your DB.  It works for your own models and users, groups, etc.  Have not tested it with user permissions and group membership, but it might work. Sharing this code on GitHub so that peers can review it and also to keep it safe.

Key features of Python/Django I had to learn:
- Django model fields (spent some time on docs and even django code on git to figure out which way was up)
- Django model options and `_meta API`
- Python `tablib`

The import and export features are very simple and might not work for all models yet.

## Python Usage Examples

