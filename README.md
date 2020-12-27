# Dog Sitters Business Owner

This is a request from an owner of a small business. 

- [About](#about)
- [Using this Project](#installation)
  - [Development](#development)
  - [Production](#production)
  - [Commands](#commands)
- [License](#license)

## About

She is in strong need of having a web app to manage her employees and to connect them with potential clients. The idea is simple: she needs a system, where either client, employee, or an admin can log in. 

### Client
The Client can view available dog sitters in her area, their experience, rating, and reviews from other Clients. He can choose a sitter, choose a time and a date where the sitter can come in to take a dog for a walk, add an address, and a payment option. 

### Sitter
The Sitter can add info for her experience and any information about her. The Sitter can leave a comment about the Client and accept or decline an offer. 

### Admin
The Admin can view everything and manage both Sitters and Clients. On the log in you can create an account as a client or register as a Sitter. 

There may be other features, Development Team can add anything they think will help an Owner to reach their business goal.

## Using this Project

Clone this project:

```bash
git clone https://github.com/ShviXXL/business-doggies.git
```

Then move to the project's folder.

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

- **Migrate.** To create tables in database:
  
  ```bash
  # Development
  docker-compose -f docker-compose.dev.yml exec web python manage.py migrate

  # Production
  docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
  ```

- **Make migrations.** To apply changes to the database:
  
  ```bash
  # Development
  docker-compose -f docker-compose.dev.yml exec web python manage.py makemigrations

  # Production
  docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations
  ```

- **Create groups.** To create required groups with permissions for users (Sitters and Clients):
  
  ```bash
  # Development
  docker-compose -f docker-compose.dev.yml exec web python manage.py create_groups

  # Production
  docker-compose -f docker-compose.prod.yml exec web python manage.py create_groups
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