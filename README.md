# Dog Sitters Business Owner

This is a request from an owner of a small business. She is in strong need of having a web app to manage her employees and to connect them with potential clients. The idea is simple: she needs a system, where either client, employee, or an admin can log in. 

## About request

### Client
The Client can view available dog sitters in her area, their experience, rating, and reviews from other Clients. He can choose a sitter, choose a time and a date where the sitter can come in to take a dog for a walk, add an address, and a payment option. 

### Sitter
The Sitter can add info for her experience and any information about her. The Sitter can leave a comment about the Client and accept or decline an offer. 

### Admin
The Admin can view everything and manage both Sitters and Clients. On the log in you can create an account as a client or register as a Sitter. 

There may be other features, Development Team can add anything they think will help an Owner to reach their business goal.

## Using our Project

To clone our project:

```bash
git clone https://github.com/ShviXXL/business-doggies.git
```

### Development

```bash
# Run containers
docker-compose -f docker-compose.dev.yml up --build

# Run migrations
docker-compose -f docker-compose.dev.yml exec web python manage.py migrate
```

If you need to make migrations:
```bash
docker-compose -f docker-compose.dev.yml exec web python manage.py makemigrations
```

Also you may want to clear out the database:
```bash
docker-compose -f docker-compose.dev.yml exec web python manage.py flush
```

To bring the containers down:
```bash
docker-compose -f docker-compose.dev.yml down -v
```

### Production

```bash
# Run containers
docker-compose -f docker-compose.prod.yml up -d --build

# Run migrations
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```

To bring the containers down:
```bash
docker-compose -f docker-compose.prod.yml down -v
```