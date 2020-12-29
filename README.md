# Dog Sitters Business Owner

 Web Application that works like freelance platform but for Dog Sitters. This project is built with Django, Django Rest Framework, Vue.js, Bootstrap. Nginx and Gunicorn are used as a server. We also used Docker and docker-compose for deploying.

- [About](#about)
- [Using this Project](#installation)
  - [Development](#development)
  - [Production](#production)
  - [Commands](#commands)
- [License](#license)

## About

This is a request from an owner of a small business.

Customer is in strong need of having a web app to manage his employees and to connect them with potential clients. The idea is simple: he needs a system, where either client, employee, or an admin can log in. On the log in User can create an account as a *Client* or register as a *Sitter*. 

There may be other features, Development Team can add anything they think will help an Owner to reach their business goal.

### Client
The *Client* can view available dog sitters in his area, their experience, rating, and reviews from other *Clients*. He can choose a sitter, choose a time and a date where the sitter can come in to take a dog for a walk, add an address, and a payment option. 

### Sitter
The *Sitter* can add information about his experience and about himself. The *Sitter* can leave a review about the *Client* and accept or decline an offer. 

### Admin
The *Admin* can view everything and manage both *Sitters* and *Clients*.

## Using this Project

Clone this project:

```bash
git clone https://github.com/ShviXXL/business-doggies.git
```

Then move to the project's folder.
```bash
cd business-doggies
```

### Development

To bring containers up:

```bash
docker-compose -f docker-compose.dev.yml up --build
```

To view logs:

```bash
docker-compose -f docker-compose.dev.yml logs
```

To bring the containers down:
```bash
docker-compose -f docker-compose.dev.yml down
```

### Production

To bring containers up:

```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

To bring the containers down:
```bash
docker-compose -f docker-compose.prod.yml down
```

### Commands

- **Migrate.** Run this command if you want to apply migrations or create a database if not already created:
  
  ```bash
  # Development
  docker-compose -f docker-compose.dev.yml exec web python manage.py migrate

  # Production
  docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
  ```

- **Make migrations.** To apply changes to the database. Run this command if you made any changes to the models in ```models.py``` file:
  
  ```bash
  # Development
  docker-compose -f docker-compose.dev.yml exec web python manage.py makemigrations

  # Production
  docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations
  ```

- **Create groups.** To create required groups with permissions for users (Sitters and Clients). You should run this command after creating containers because these groups are necessary for the application:
  
  ```bash
  # Development
  docker-compose -f docker-compose.dev.yml exec web python manage.py creategroups

  # Production
  docker-compose -f docker-compose.prod.yml exec web python manage.py creategroups
  ```

- **Create superuser.** To create an administrator account to access the admin dashboard:

  ```bash
  # Development
  docker-compose -f docker-compose.dev.yml exec web python manage.py createsuperuser

  # Production
  docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
  ```

- **Flush.** To remove all data from database:
  
  ```bash
  # Development
  docker-compose -f docker-compose.dev.yml exec web python manage.py flush

  # Production
  docker-compose -f docker-compose.prod.yml exec web python manage.py flush
  ```

## License
[MIT](https://github.com/ShviXXL/business-doggies/blob/main/LICENSE)