from ..utils import get_mongodb
from django import template

register = template.Library()


def get_author(id_):

    db = get_mongodb()

    author = db.authors_collection.find_one({'_id':id_})

    return author['fullname']


register.filter('author', get_author)
