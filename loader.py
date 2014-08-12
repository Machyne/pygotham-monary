from os import path

import cElementTree as ElementTree
import pymongo


def parse_file(fname):
    collection = path.split(fname)[-1][:-4].lower()
    docs = []
    with pymongo.MongoClient() as client:
        for event, elem in ElementTree.iterparse(fname):
            if elem.tag == "row":
                doc = elem.attrib
                doc["_id"] = doc["Id"]
                doc.pop("Id", None)
                for key in doc:
                    if 'Name' not in key and doc[key].isdigit():
                        doc[key] = int(doc[key])
                docs.append(doc)
            if len(docs) >= 2000:
                client.superuser.__getattr__(collection).insert(docs)
                docs = []
            elem.clear()

file_list = ['Badges.xml', 'Comments.xml', 'PostHistory.xml', 'PostLinks.xml',
             'Posts.xml', 'Tags.xml', 'Users.xml', 'Votes.xml']


if __name__ == '__main__':
    with pymongo.MongoClient() as client:
        print('Removing old database.')
        client.drop_database('superuser')
    print('Inserting new documents...')
    for fname in file_list:
        print('\tParsing %s' % fname)
        parse_file(path.join('superuser.com', fname))
    print('Done.')
