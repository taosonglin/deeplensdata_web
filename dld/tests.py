import os
import django
os.environ.setdefault('DJANGO_SETTING_MODULE', 'deeplens.settings')
django.setup()
from dld.models import Users

def main():
    print(Users.objects.all())

if __name__ == '__main__':
    main()