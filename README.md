
# Backend Assignment | FamPay

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Requirements
- Server should call async task to fetch data from Youtube API and store it in the database - Solved ✅
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime - Solved ✅
- A basic search API to search the stored videos using their title and description - Solved ✅
- Dockerize the project - Solved ✅
- It should be scalable and optimised - Solved ✅
- Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key - Solved ✅
- Make a dashboard to view the stored videos with filters and sorting options - Unsolved ❌
- Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description - Unsolved ❌
    - Ex 1: A video with title *`How to make tea?`* should match for the search query `tea how`

## Installation

Install app with docker

```bash
  docker-compose -f docker-compose.yml up -d --build 
```
## API Reference

### Get videos - Paginated API to fetch video info stored in DB


  #### GET /videos/

| Parameter | Type     | Description                           |
| :-------- | :------- | :---------------------------------    |
|  `page_no`   |`integer` |    Page number (> 0)  (optional)      |
|`limit`| `integer`|    Page number (> 0)  (optional)      |



#### cURL
```bash
curl --location --request GET 'localhost:8000/videos/?page_no=1&limit=5'
```

### Search - Basic search API to search for video where title or description contains given string query

 #### GET /search/


| Parameter   | Type      |     Description                          |
| :--------   | :-------  | :-------------------------------------   |
|  `page_no`   |`integer` |    Page number (> 0)  (optional)      |
|`limit`| `integer`|    Page number (> 0)  (optional)      |
|`description`| `string`  |    description to search for  (optional) |


#### cURL

```bash
curl --location --request GET 'localhost:8000/search/?page_no=1&limit=20&query=india'
```

