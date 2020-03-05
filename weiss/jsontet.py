class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return 'student name: %s, score: %s' % (self.name, self.score)

    __repr__ = __str__

    def printscore(self):
        print(self.score)

    def __call__(self, *args, **kwargs):
        print('my name is %s.' % self.name)


import json

s = Student('siwei', 100)
print(json.dumps(s, default=lambda obj: obj.__dict__))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
jsonresult = json.loads(json_str)
print(type(jsonresult))
print('name: %s' % jsonresult['name'])
for (key, value) in jsonresult.items():
    print('%s,%s' % (key, value))

exit()
