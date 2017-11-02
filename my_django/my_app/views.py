from django.shortcuts import render
from my_app.models import Person, Address, Phone, Email, Group
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def contacts_list(request):
	persons = Person.objects.all().order_by("name")
	html = """
			<html>
			<body>
				<h1> List of contacts </h1>
				<table>
				{}
				</table>
				<p> <a href = http://127.0.0.1:8000/new> Add new person </a> </p>
				<p> <a href = http://127.0.0.1:8000/> List of groups </a> </p>
			</body>
			</html>
			"""

	list_of_contacts = ""
	for person in persons:
		list_of_contacts += """
						<tr>
							<td><a href = http://127.0.0.1:8000/show/{}> {} </a></td>
							<td> {} </td>
							<td> {} </td>
							<td><button type='submit'> MODIFY </button></td>
							<td><button type='submit'> DELETE </button></td>
						</tr>""".format(person.id,person.name, person.surname, person.description)
	html = html.format(list_of_contacts)
	return HttpResponse(html)



def add_group(request):
	new_group = Group()
	new_group = Group.objects.create(name="colleagues",description="colleagues from work")
	
	return HttpResponse("Dodano wpisy")



def add_group_person(request,my_id):
	p = Person.objects.get(id = my_id)
	g = Group.objects.get(id=2) # 1:friends 2:family 3:colleagues
	g.person.add(p)
	return HttpResponse("Dodano wpisy")



def show_contact(request, my_id):
	persons = Person.objects.get(id = my_id)
	
	email_private = Email.objects.get(person = persons, email_type=0)
	email_business = Email.objects.get(person = persons, email_type=1)

	phone_home = Phone.objects.get(person = persons, phone_type=0)
	phone_mobile = Phone.objects.get(person = persons, phone_type=1)
	phone_business = Phone.objects.get(person = persons, phone_type=2)
	
	add_perm = Address.objects.get(person = persons, address_type=0)
	add_res = Address.objects.get(person = persons, address_type=1)
	add_cor = Address.objects.get(person = persons, address_type=2)

	show_data = """
			<h2>{} {}</h2>
			<form>
				<fieldset>
					<legend> <h4> Basic data </h4> </legend>
					<label for="name"> Name </label>
					<input type="text" name="name" id="name" placeholder="{}">
					<label for="surname"> Surname </label>
					<input type="text" name="surname" id="surname" placeholder="{}">
					<label for="description"> Description </label>
					<input type="text" name="description" id="description" placeholder="{}">
				</fieldset>
			</form>
			<form>
				<fieldset>
					<legend> <h4> E-mail </h4> </legend>
					<label for="private"> Private </label>
					<input type="text" name="private" id="private" placeholder="{}">
					<label for="business"> Business </label>
					<input type="text" name="business" id="business" placeholder="{}">
				</fieldset>
			</form>
			<form>
				<fieldset>
					<legend> <h4> Phone </h4> </legend>
					<label for="home"> Home </label>
					<input type="text" name="home" id="home" placeholder="{}">
					<label for="mobile"> Mobile </label>
					<input type="text" name="mobile" id="mobile" placeholder="{}">
					<label for="business"> Business </label>
					<input type="text" name="business" id="business" placeholder="{}">
				</fieldset>
			</form>
			<form>
				<fieldset>
					<legend> <h4> Address </h4> </legend>
						<fieldset>
							<legend> Permanent </legend>
							<label for="city"> City </label>
							<input type="text" name="city" id="city" placeholder="{}">
							<label for="street"> Street </label>
							<input type="text" name="street" id="street" placeholder="{}">
							<label for="number"> Number </label>
							<input type="text" name="number" id="number" placeholder="{}">
							<label for="local_num"> Local number </label>
							<input type="text" name="local_num" id="local_num" placeholder="{}">
						</fieldset>
						<br/>
						<fieldset>
							<legend> Of residence </legend>
							<label for="city"> City </label>
							<input type="text" name="city" id="city" placeholder="{}">
							<label for="street"> Street </label>
							<input type="text" name="street" id="street" placeholder="{}">
							<label for="number"> Number </label>
							<input type="text" name="number" id="number" placeholder="{}">
							<label for="local_num"> Local number </label>
							<input type="text" name="local_num" id="local_num" placeholder="{}">
						</fieldset>
						<br/>
						<fieldset>
							<legend> For correspondence </legend>
							<label for="city"> City </label>
							<input type="text" name="city" id="city" placeholder="{}">
							<label for="street"> Street </label>
							<input type="text" name="street" id="street" placeholder="{}">
							<label for="number"> Number </label>
							<input type="text" name="number" id="number" placeholder="{}">
							<label for="local_num"> Local number </label>
							<input type="text" name="local_num" id="local_num" placeholder="{}">
						</fieldset>
				</fieldset>
			</form>
			<form>
				<fieldset>
					<legend> <h4> Groups </h4> </legend>
					
				</fieldset>
			</form>
			<p> <a href = http://127.0.0.1:8000/> Modify </a> </p>
			<p> <a href = http://127.0.0.1:8000/delete/{}> Delete </a> </p>
			""".format(persons.name, persons.surname, persons.name, persons.surname, persons.description,
				email_private.email, email_business.email,
				phone_home.phone_number, phone_mobile.phone_number, phone_business.phone_number,
				add_perm.city, add_perm.street, add_perm.number, add_perm.local_num,
				add_res.city, add_res.street, add_res.number, add_res.local_num,
				add_cor.city, add_cor.street, add_cor.number, add_cor.local_num, persons.id)

	return HttpResponse(show_data)



@csrf_exempt 
def add_new_person(request):
	if request.method == "GET":
		html = """<h2> Add new person </h2>
				<form method='POST'>
					<fieldset>
						<legend> <h4> Basic data </h4> </legend>
						Name: <input type="text" name="name">
						Surname: <input type="text" name="surname">
						Description: <input type="text" name="description">
					</fieldset>
					<br/>
					<button type='submit'> SAVE </button>
				</form>
				"""
		return HttpResponse(html)

	if request.method == "POST":
		new_person = Person()
		name_from_form = request.POST.get("name")
		surname_from_form = request.POST.get("surname")
		description_from_form = request.POST.get("description")
		if name_from_form == "":
			empty_name = """<a href = http://127.0.0.1:8000/new> You should give a name </a>"""
			return HttpResponse(empty_name)
		new_person = Person.objects.create(name=name_from_form, surname=surname_from_form, description=description_from_form) 
		return HttpResponse("New person added")
		

@csrf_exempt 
def delete_contact(request, my_id):
	persons = Person.objects.get(id = my_id)
	if request.method == "GET":
		contact_to_delete = """
						<h3>Are you sure you want to delete contact?</h3>
						<form method='POST'>
						<table>	
							<tr>
								<td> {} </td>
								<td> {} </td>
								<td> {} </td>
							</tr>
						</table>
						<br/>
						<input type='submit' name='option' value='DELETE'>
						<input type='submit' name='option' value='CANCEL'>
							""".format(persons.name, persons.surname, persons.description, persons.id)
		return HttpResponse(contact_to_delete)

	if request.method == "POST":
		option = request.POST.get('option')
		
		if option == "DELETE":
			persons.delete()
			return HttpResponse("<a href=http://127.0.0.1:8000> Contact deleted </a>")
		return HttpResponse("<a href=http://127.0.0.1:8000> Return to contact list </a>")
		
