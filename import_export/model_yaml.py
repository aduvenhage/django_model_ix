

from django.contrib.postgres.fields.jsonb import JSONField
from django.db import models
from django.db.models import fields

import tablib
import os




# return DB style formatted field value
def __exportField(f, instance):
    return f.value_to_string(instance)


# copy model fields to dictionary
def __exportDict(instance):
    data = {}

    for f in instance._meta.get_fields():
        # ignore all 'ForeignObjectRel' field types
        if isinstance(f, fields.related.ForeignObjectRel):
            pass

        # export 'ForeignKey' field types
        elif isinstance(f, fields.related.ForeignKey):
            data[f.name] = __exportField(f, instance)

        # ignore all 'ForeignObjectRel' field types (besides ForeignKey)
        elif isinstance(f, fields.related.RelatedField):
            pass

        else:
            data[f.name] = __exportField(f, instance)

    return data


# write model content to file in YAML format
def __writeYamlFile(modelType, path):
    objects = list(modelType.objects.all())
    if objects:
        headers = __exportDict(objects[0]).keys()
        dataset = tablib.Dataset(headers=headers)

        for obj in objects:
            attr = __exportDict(obj)
            dataset.append(attr.values())

        # create file and write dataset (text/yaml)
        filePath = os.path.join(path, modelType.__name__ + ".yaml")
        with open(filePath, "w+") as fout:
            fout.write(dataset.yaml)


# write resource to file in YAML format (with error handling)
def exportYaml(modelType, path):
    try:
        __writeYamlFile(modelType, path)
        print("Exported '%s' to '%s'." % (modelType.__name__, path))

    except Exception as e:
        print("Failed to export '%s' to '%s'. %s" % (modelType.__name__, path, str(e)))



# import formatted value
def __importField(instance, f, data):
    try:
        # NOTE: sets the model column attribute value for related fields
        if isinstance(f, fields.related.RelatedField):
            setattr(instance, f.column, data[f.name])
        else:
            setattr(instance, f.name, data[f.name])

    except:
        pass


# update model fields with dictionary
def __importDict(instance, data):
    for f in instance._meta.get_fields():
        # ignore all 'ForeignObjectRel' field types
        if not isinstance(f, fields.related.ForeignObjectRel):
            __importField(instance, f, data)


# read model content from YAML file
def __readYamlFile(modelType, path):
    # open data set file
    filePath = os.path.join(path, modelType.__name__ + ".yaml")

    with open(filePath, "r") as fin:
        # read yaml/text
        yaml = fin.read()

        # import data set from yaml
        dataset = tablib.Dataset().load(yaml)

        for row in dataset:
            obj = modelType()
            __importDict(obj, dict(zip(dataset.headers, row)))

            obj.save()


# read model content from YAML file (with error handling)
def importYaml(modelType, path):
    try:
        __readYamlFile(modelType, path)
        print("Imported to '%s' from '%s'." % (modelType.__name__, path))

    except Exception as e:
        print("Failed to import to '%s' from '%s'. %s" % (modelType.__name__, path, str(e)))

