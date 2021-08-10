#for balencing an equation it is a lot like 
#foil in math
#for this reason I need to create something that retruns something


from tkinter import *

import sys, os


try:
	from sympy import Matrix, lcm
except:
	if sys.platform == "linux":
		os.system("pip3 install sympy")
	elif sys.platform == 'win32':
		os.system("pip install sympy")


from string import ascii_uppercase as UPPERCASE

from string import ascii_lowercase as LOWERCASE

from string import digits as DIGITS

from backend import SYMBOLS


def get_elements(x):

	elements = []

	for each_term in x:

		for each_element in SYMBOLS:

			if each_term.__contains__(each_element):

				for each_letter in range(len(each_term)):

					if each_term[each_letter:each_letter+len(each_element)] == each_element:

						each_term = each_term[:each_letter] + each_term[each_letter+len(each_element)+1:]

						break



				elements.append(each_element)

	return elements

def reformat(x, e):

	elements = []

	for each_term in x:

		each_term += "  "

		for each_element in e:

			if each_term.__contains__(each_element):

				for each_letter in range(len(each_term)):

					if each_term[each_letter:each_letter+len(each_element)] == each_element:

						if each_term[each_letter+len(each_element)] not in DIGITS:

							each_term = each_term[:each_letter+len(each_element)]+ "1" + each_term[each_letter+len(each_element):]



						

						break

		each_term = each_term[:len(each_term)-2]

		elements.append(each_term)

	return elements

def create_matrices(r, p, e):
	total = len(r) + len(p)
	m = dict()
	for i in range(len(e)):
		m[e[i]]=[0 for e in range(total)]
	num_r, num_p = len(r), len(p)
	r = reformat(r, e)
	p = reformat(p, e)

	for each_term in range(len(r)):

		for each_element in SYMBOLS:

			if r[each_term].__contains__(each_element):

				for each_letter in range(len(r[each_term])):

					if r[each_term][each_letter:each_letter+len(each_element)] == each_element:
	
						m[each_element][each_term] = int(r[each_term][each_letter+len(each_element)])

	for each_term in range(len(p)):

		for each_element in SYMBOLS:

			if p[each_term].__contains__(each_element):

				for each_letter in range(len(p[each_term])):

					if p[each_term][each_letter:each_letter+len(each_element)] == each_element:
	
						m[each_element][each_term+len(r)] = int(p[each_term][each_letter+len(each_element)])*-1

	matr = []

	for i in m:
		matr.append(m[i])

	return matr



def balence(equation):

	reactants, products = equation.replace(" ", "").split("=")[0].split("+"), equation.replace(" ", "").split("=")[1].split("+")





	m = create_matrices(reactants, products, get_elements(reactants))


	m = Matrix(m)


	solution=m.nullspace()[0]


	multiple = lcm([val.q for val in solution])

	solution = multiple*solution

	coEffi=solution.tolist()

	output=""

	for i in range(len(reactants)):
		if coEffi[i][0] != 1:
			output+=str(coEffi[i][0])+"("+reactants[i]+")"
		else:
			output+=reactants[i]
		if i<len(reactants)-1:
		   output+=" + "
	output+=" -> "
	for i in range(len(products)):
		if coEffi[i][0] != 1:
			output+=str(coEffi[i+len(reactants)][0])+"("+products[i]+")"
		else:
			output += products[i]
		if i<len(products)-1:
		   output+=" + "
	return output



def create_window(eq):
	global _Balence_Entry
	_Balence_Entry.delete(0, END)
	_Balence_Entry.insert(0, balence(eq))



def clear_entry(event):
	global _Balence_Entry
	_Balence_Entry.delete(0, 'end')
	return None




def create_balencer(t):

	global _Balence_Frame, _Balence_Entry, _Balence_Enter

	_Balence_Frame = LabelFrame(t, text = 'Equation Balencer', width = 400, height = 80, font = ("Montserrat", 10), bg = "#373e40", fg = "#ffffff")

	_Balence_Frame.place(x = 10, y = 100)

	_Balence_Entry = Entry(_Balence_Frame,bg = '#ffffff', fg = '#121212', font = ("Montserrat", 10), width = 42)

	_Balence_Entry.insert(0, "Enter Equation")

	_Balence_Entry.bind("<Button-1>", clear_entry)

	_Balence_Enter = Button(_Balence_Frame, text = 'Get Balence', command = lambda:create_window(_Balence_Entry.get()), font = ('Montserrat', 10), width = 40)

	_Balence_Enter.place(x = 5, y = 25)

	_Balence_Entry.place(x = 7, y = 0)



