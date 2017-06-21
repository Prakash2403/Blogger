from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
import models

connections.create_connection()


def bulk_indexing():
    PostIndex.init("post")
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Post.objects.all().iterator()))


class PostIndex(DocType):
    title = Text()
    author = Text()
    content = Text()
    categories = Text()

    class Meta:
        index = 'blog'
