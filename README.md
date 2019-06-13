# Django Model Import-Export
As part of my efforts to learn python and django I decided to create a little module that can export model fields to YAML and then import it again to restore your DB.  It works for your own models and users, groups, etc.  Have not tested it with user permissions and group membership, but it might work. Sharing this code on GitHub so that peers can review it and also to keep it safe.

Key features of Python/Django I had to learn:
- Django model fields (spent some time on docs and even django code on git to figure out which way was up)
- Django model options and `_meta API`
- Python `tablib`

The import and export features are very simple and might not work for all models yet.

Before I decided to create this module I looked at django-import-export (https://django-import-export.readthedocs.io).  It was super easy to export models to YAML, but I just could not figure out the importing.  It did however learn quite a lot about django's models, fields and `_meta` API while trying to debug the importing.  

## Python Usage Examples

