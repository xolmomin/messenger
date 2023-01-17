mig:
	./manage.py makemigrations
	./manage.py migrate

#user:
#	python3 manage.py shell -c "from apps.models import User; User.objects.create_superuser('admin1', '1')"
