import re
import random

class TemplateGen:
	def __init__(self):
		pass

	def get_ckeys(self, template):
		return re.findall(r"_C_\w+", template)

	def generate_sentences(self, template, data_dict):
		# If there is one rule template, process the rule template. 
		if '(' in template or '|' in template or '[' in template:

			def interior_sign(string):										# A function to determin which '_C_' will be kept if '|' exists. 
				a_list = string.split(' | ')
				a = len(data_dict[a_list[0]])
				b = len(data_dict[a_list[1]])
				maxi = max(a, b)
				res = []
				if a == maxi:
					res.append(a_list[0])
				if b == maxi:
					res.append(a_list[1])
				determined = random.choice(res)
				return determined

			if '[' in template:												# Process the situation including '[]'
				p = re.compile(r'[\[](.*?)[\]]', re.S)
				item_0 = re.findall(p, template)
				for i in item_0:
					if '|' in i:
						item = interior_sign(i)
					else:
						item = i
					determined = random.choice([0, 1])
					if determined == 1:
						template = template.replace('[' + i + ']', item)
					else:
						template = template.replace('[' + i + '] ', '')

			if '(' in template:												# Process the situation including '()'
				p = re.compile(r'[(](.*?)[)]', re.S)
				item_0 = re.findall(p, template)
				for i in item_0:
					if '|' in i:
						item = interior_sign(i)
					else:
						item = i
					template = template.replace('(' + i + ')', item)

		# Process template without rule or formatted template. 
		a_list = self.get_ckeys(template)
		string = a_list[0]
		result = []
		for value in (data_dict[string]):
			new_string = template.replace(string, value)
			result.append(new_string)
		index = 1
		while(index < len(a_list)):
			temp = []
			string = a_list[index]
			for value in (data_dict[string]):
				for res in result:
					new_string = res.replace(string, value)
					temp.append(new_string)
			result = temp
			index += 1
		return result

templates=[
        "_C_PLEASE _C_BRIEF_ME",
        "_C_PLEASE _C_BRIEF_ME _C_TIME_LY",
        "_C_PLEASE _C_BRIEF_ME about _C_TIME_REL",
        "_C_PLEASE _C_BRIEF_ME about _C_TIME_REL's headlines"
]

data_dict={
    "_C_PLEASE": [
        "please",
        "can you",
        "will you",
        "could you",
        "would you",
        "can you please",
        "will you please",
        "could you please",
        "would you please" #9
    ],
    "_C_BRIEF_ME": [
        "brief me",
        "start briefing me" #2
    ],
    "_C_TIME_REL": [
        "today",
        "yesterday",
        "this week",
        "last week",
        "this month",
        "last month" #6
    ],
    "_C_TIME_LY": [
        "daily",
        "weekly",
        "monthly" #3
    ]
}

templates2 = [
    "[_C_PLEASE] _C_BRIEF_ME about _C_TIME_REL headlines",
    "(_C_PLEASE | _C_BRIEF_ME) about _C_TIME_REL headlines",
]

output = [
    "please brief me",
    "can you brief me",
    "will you brief me",
    "could you brief me",
    "would you brief me",
    "can you please brief me",
    "will you please brief me",
    "could you please brief me",
    "would you please brief me",
    "please start briefing me",
    "can you start briefing me",
    "will you start briefing me",
    "could you start briefing me",
    "would you start briefing me",
    "can you please start briefing me",
    "will you please start briefing me",
    "could you please start briefing me",
    "would you please start briefing me"
]

template = TemplateGen()
result = template.generate_sentences(templates[0], data_dict)
print(result)
# print(result == output)
