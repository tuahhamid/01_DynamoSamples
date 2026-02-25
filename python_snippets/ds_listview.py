#Copyright (c) mostafa el ayoubi ,  2016
#Data-Shapes www.data-shapes.net , elayoubi.mostafa@gmail.com

class listview():

    def __init__(self,inputname,height,highlight,display_mode,element_count,default_values,sorted,showId):
        self.inputname = inputname
        self.height = height
        self.highlight = highlight
        self.display_mode = display_mode
        self.element_count = element_count
        self.default_values = default_values
        self.sorted = sorted
        self.showId = showId

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def values(self):
        return self.__dict__.values()

    def keys(self):
        return self.__dict__.keys()

    def __repr__(self):
        return 'UI.ListView input'

if isinstance(IN[1],list):
	in1 = IN[1]
else:
	in1 = [IN[1]]

if isinstance(IN[2],list):
	in2 = IN[2]
else:
	in2 = [IN[2]]

if IN[6]:
	element_count = len(in1)
else:
	element_count = 0

x = listview(IN[0],IN[3],IN[4],IN[5],element_count,IN[7],IN[8],IN[9])

for k,v in zip(in1,in2):
	if x.showId :
		try:
			try:
				x[str(k)+ '  -  id: ' + str(v.Id)] = v
			except:
				x[k.encode('utf-8').decode('utf-8') + '  -  id: ' + str(v.Id)] = v
		except:
			try:
				x[str(k)] = v
			except:
				x[k.encode('utf-8').decode('utf-8')] = v
	else:
		try:
			try:
				x[str(k)] = v
			except:
				x[k.encode('utf-8').decode('utf-8')] = v
		except:
			try:
				x[str(k)] = v
			except:
				x[k.encode('utf-8').decode('utf-8')] = v
OUT = x