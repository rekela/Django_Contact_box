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
							<td> <a href = http://127.0.0.1:8000/modify/{}><input type='submit' name='save' value='MODIFY'> </a> </td>
							<td> <a href = http://127.0.0.1:8000/delete/{}><input type='submit' name='save' value='DELETE'> </a> </td>
						</tr>""".format(person.id, person.name, person.surname, person.description, person.id, person.id)
	html = html.format(list_of_contacts)
	return HttpResponse(html)



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
					Name <input type="text" name="name" placeholder="{}">
					Surname <input type="text" name="surname" placeholder="{}">
					Description <input type="text" name="description" placeholder="{}">
				</fieldset>
				</form>
				<form>
				<fieldset>
					<legend> <h4> E-mail </h4> </legend>
					Private <input type="text" name="private" placeholder="{}">
					Business <input type="text" name="business" placeholder="{}">
				</fieldset>
				</form>
				<form>
				<fieldset>
					<legend> <h4> Phone </h4> </legend>
					Home <input type="text" name="home" placeholder="{}">
					Mobile <input type="text" name="mobile" placeholder="{}">
					Business <input type="text" name="business" placeholder="{}">
				</fieldset>
				</form>
				<form>
				<fieldset>
					<legend> <h4> Address </h4> </legend>
						<fieldset>
							<legend> Permanent </legend>
							City <input type="text" name="city" placeholder="{}">
							Street <input type="text" name="street" placeholder="{}">
							Number <input type="text" name="number" placeholder="{}">
							Local number <input type="text" name="local_num" placeholder="{}">
						</fieldset>
						<br/>
						<fieldset>
							<legend> Of residence </legend>
							City <input type="text" name="city" placeholder="{}">
							Street <input type="text" name="street" placeholder="{}">
							Number <input type="text" name="number" placeholder="{}">
							Local number <input type="text" name="local_num" placeholder="{}">
						</fieldset>
						<br/>
						<fieldset>
							<legend> For correspondence </legend>
							City <input type="text" name="city" placeholder="{}">
							Street <input type="text" name="street" placeholder="{}">
							Number <input type="text" name="number" placeholder="{}">
							Local number <input type="text" name="local_num" placeholder="{}">
						</fieldset>
				</fieldset>
				</form>
				<p> <a href = http://127.0.0.1:8000/modify/{}> Modify </a> </p>
				<p> <a href = http://127.0.0.1:8000/delete/{}> Delete </a> </p>
				""".format(persons.name, persons.surname, persons.name, persons.surname, persons.description,
				email_private.email, email_business.email,
				phone_home.phone_number, phone_mobile.phone_number, phone_business.phone_number,
				add_perm.city, add_perm.street, add_perm.number, add_perm.local_num,
				add_res.city, add_res.street, add_res.number, add_res.local_num,
				add_cor.city, add_cor.street, add_cor.number, add_cor.local_num, persons.id, persons.id)

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
					<input type='submit' name='save' value='SAVE'>
				</form>
				"""
		return HttpResponse(html)

	if request.method == "POST":
		new_person = Person()
		new_email = Email()
		new_phone = Phone()
		new_address = Address()
		
		name_from_form = request.POST.get("name")
		surname_from_form = request.POST.get("surname")
		description_from_form = request.POST.get("description")

		if name_from_form == "":
			empty_name = """<a href = http://127.0.0.1:8000/new> You should give a name </a>"""
			return HttpResponse(empty_name)

		new_person = Person.objects.create(name=name_from_form, surname=surname_from_form, description=description_from_form) 

		person = Person.objects.get(id=new_person.id)
		new_email = Email.objects.create(email_type=0, person=person)
		new_email = Email.objects.create(email_type=1, person=person)
		new_phone = Phone.objects.create(phone_type=0, person=person)
		new_phone = Phone.objects.create(phone_type=1, person=person)
		new_phone = Phone.objects.create(phone_type=2, person=person)
		new_address = Address.objects.create(address_type=0, person=person)
		new_address = Address.objects.create(address_type=1, person=person)
		new_address = Address.objects.create(address_type=2, person=person)

		result = """<a href = http://127.0.0.1:8000/show/{}> 
					New person added <a/>""".format(person.id)
					
		return HttpResponse(result)
		


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
		


@csrf_exempt 
def modify_contact(request, my_id):
	persons = Person.objects.get(id = my_id)

	email_private = Email.objects.get(person = persons, email_type=0)
	email_business = Email.objects.get(person = persons, email_type=1)

	phone_home = Phone.objects.get(person = persons, phone_type=0)
	phone_mobile = Phone.objects.get(person = persons, phone_type=1)
	phone_business = Phone.objects.get(person = persons, phone_type=2)
	
	add_perm = Address.objects.get(person = persons, address_type=0)
	add_res = Address.objects.get(person = persons, address_type=1)
	add_cor = Address.objects.get(person = persons, address_type=2)

	if request.method == "GET":
		modify_data = """
				<h2>{} {} - Modify data </h2>
				<form method='POST'>
					
					<fieldset>
						<legend> <h4> Basic data </h4> </legend>
						Name <input type="text" name="name" value="{}">
						Surname <input type="text" name="surname" value="{}">
						Description <input type="text" name="description" value="{}">
					</fieldset>
				
					<fieldset>
						<legend> <h4> E-mail </h4> </legend>
						Private <input type="text" name="private_email" value="{}">
						Business <input type="text" name="business_email" value="{}">
					</fieldset>
					
					<fieldset>
						<legend> <h4> Phone </h4> </legend>
						Home <input type="text" name="home_phone" value="{}">
						Mobile <input type="text" name="mobile_phone" value="{}">
						Business <input type="text" name="business_phone" value="{}">
					</fieldset>
				
					<fieldset>
						<legend> <h4> Address </h4> </legend>
							<fieldset>
								<legend> Permanent </legend>
								City <input type="text" name="city_p" value="{}">
								Street <input type="text" name="street_p" value="{}">
								Number <input type="text" name="number_p" value="{}">
								Local number <input type="text" name="local_num_p" value="{}">
							</fieldset>
							<br/>
							<fieldset>
								<legend> Of residence </legend>
								City <input type="text" name="city_r" value="{}">
								Street <input type="text" name="street_r" value="{}">
								Number <input type="text" name="number_r" value="{}">
								Local number <input type="text" name="local_num_r" value="{}">
							</fieldset>
							<br/>
							<fieldset>
								<legend> For correspondence </legend>
								City <input type="text" name="city_c" value="{}">
								Street <input type="text" name="street_c" value="{}">
								Number <input type="text" name="number_c" value="{}">
								Local number <input type="text" name="local_num_c" value="{}">
							</fieldset>
					</fieldset>
					<br/>
				<input type='submit' name='option' value='MODIFY'>
				<input type='submit' name='option' value='CANCEL'> """.format(persons.name, persons.surname, 
					persons.name, persons.surname, persons.description, email_private.email, email_business.email,
					phone_home.phone_number, phone_mobile.phone_number, phone_business.phone_number,
					add_perm.city, add_perm.street, add_perm.number, add_perm.local_num,
					add_res.city, add_res.street, add_res.number, add_res.local_num,
					add_cor.city, add_cor.street, add_cor.number, add_cor.local_num)	

		return HttpResponse(modify_data)
	
	if request.method == "POST":
		option = request.POST.get("option")

		name_change = request.POST.get("name")
		surname_change = request.POST.get("surname")
		description_change = request.POST.get("description")

		private_email = request.POST.get("private_email")
		business_email = request.POST.get("business_email")

		home_phone = request.POST.get("home_phone")
		mobile_phone = request.POST.get("mobile_phone")
		business_phone = request.POST.get("business_phone")

		city_p = request.POST.get("city_p")
		street_p = request.POST.get("street_p")
		number_p = request.POST.get("number_p")
		local_num_p = request.POST.get("local_num_p")

		city_r = request.POST.get("city_r")
		street_r = request.POST.get("street_r")
		number_r = request.POST.get("number_r")
		local_num_r = request.POST.get("local_num_r")

		city_c = request.POST.get("city_c")
		street_c = request.POST.get("street_c")
		number_c = request.POST.get("number_c")
		local_num_c = request.POST.get("local_num_c")

		if option == "MODIFY":
			if name_change != persons.name:
				persons.name = name_change
				persons.save()
			if surname_change != persons.surname:
				persons.surname = surname_change
				persons.save()
			if description_change != persons.description:
				persons.description = description_change
				persons.save()

			if private_email != email_private.email:
				email_private.email = private_email
				email_private.save()
			if business_email != email_business.email:
				email_business.email = business_email
				email_business.save()

			if home_phone != phone_home.phone_number:
				phone_home.phone_number = home_phone
				phone_home.save()
			if mobile_phone != phone_mobile.phone_number:
				phone_mobile.phone_number = mobile_phone
				phone_mobile.save()
			if business_phone != phone_business.phone_number:
				phone_business.phone_number = business_phone
				phone_business.save()

			if city_p != add_perm.city:
				add_perm.city = city_p
				add_perm.save()
			if street_p != add_perm.street:
				add_perm.street = street_p
				add_perm.save()
			if number_p != add_perm.number:
				add_perm.number = number_p
				add_perm.save()
			if local_num_p != add_perm.local_num:
				add_perm.local_num = local_num_p
				add_perm.save()

			if city_r != add_res.city:
				add_res.city = city_r
				add_res.save()
			if street_r != add_res.street:
				add_res.street = street_r
				add_res.save()
			if number_r != add_res.number:
				add_res.number = number_r
				add_res.save()
			if local_num_r != add_res.local_num:
				add_res.local_num = local_num_r
				add_res.save()

			if city_c != add_cor.city:
				add_cor.city = city_c
				add_cor.save()
			if street_c != add_cor.street:
				add_cor.street = street_c
				add_cor.save()
			if number_c != add_cor.number:
				add_cor.number = number_c
				add_cor.save()
			if local_num_c != add_cor.local_num:
				add_cor.local_num = local_num_c
				add_cor.save()

			return HttpResponse("<a href=http://127.0.0.1:8000> Modified </a>")

		return HttpResponse("<a href=http://127.0.0.1:8000> Return to contact list </a>")



def add_group(request):
	new_group = Group()
	new_group = Group.objects.create(name="colleagues",description="colleagues from work")
	
	return HttpResponse("Dodano wpisy")



def add_group_person(request,my_id):
	p = Person.objects.get(id = my_id)
	g = Group.objects.get(id=2) # 1:friends 2:family 3:colleagues
	g.person.add(p)
	return HttpResponse("Dodano wpisy")

