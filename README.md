
# nlw_python

This repository contains a project developed during Next Level Week (NLW), a programming immersion event. The focus of this project is the use of the Python language to create a practical application. 

The main objective of this project is to create events where we can register people for these events. We also have a ranking of registrations based on links that users will have to attract more people.


# Installation
Follow the steps below to configure the project locally:

1️⃣ **Clone the repository**

First, clone the repository to your local machine using the command:

```bash
 git clone https://github.com/Quin-shi-huan/nlw_python.git
```

2️⃣ **Navigate to the project folder**  

After cloning the repository, enter the project folder:


```bash
 cd nlw_python
```

3️⃣ **Install the dependencies**  

Now install the required dependencies for the project with pip:

```bash
 pip install -r requirements.txt
```


## Routes

### Create a new event

```http
  POST /event
```

**Request example**:
```json
{
    "data": {
        "name": "Rocketseat NLW 2024"
    }
}
```

**Success Response**:
```json
{
    "data": {
        "Type": "Event",
        "attributes": {
            "event_name": "Rocketseat NLW 2024"
        },
        "count": 1
    }
}
```
***
### Returning the number of subscribers per link

```http
  GET /subscriber/link/<link>/event/<event_id>

```
| Parameter   | Type      | Description                          |
| :---------- | :--------- | :---------------------------------- |
| `<link>` | `string` | The event invitation url|
| `<event_id>` | `number` | The ID of the registered event|




**Request example**:

```json
{
    "data": {
        "name": "Rocketseat NLW 2025"
    }
}
```

**Success Response**:

```json
{
    "data": {
        "Type": "Subscriber",
        "count": 1,
        "subscribers": [
            {
                "email": "email@email.com",
                "nome": "meuNome"
            }
        ]
    }
}
```
***

### Ranking of subscribers per link

```http
  GET /subscriber/ranking/event/<event_id>
```

| Parameter  | Type       | Description                         |
| :---------- | :--------- | :---------------------------------- |
| `<event_id>` | `number` | The ID of the registered event|


**Success Response**:
```json
{
    "data": {
        "Type": "Ranking",
        "count": 3,
        "ranking": [
            {
                "link": "event_link_generic-1",
                "total_subscribers": 2
            },
            {
                "link": "event_link_generic-2",
                "total_subscribers": 2
            },
            {
                "link": "event_link_generic-3",
                "total_subscribers": 1
            }
        ]
    }
```
***
### Create a new link for the user to share
```http
  POST /events_link

```

**Request example**:

```json
{
    "data": {
        "event_id": 1,
        "subscriber_id": 1
    }
}
```
**Success Response**:

```json
{
    "data": {
        "Type": "Event Link",
        "attributes": {
            "event_id": 1,
            "link": "evento-5-11-8084393",
            "subscriber_id": 1
        },
        "count": 1
    }
}
```
