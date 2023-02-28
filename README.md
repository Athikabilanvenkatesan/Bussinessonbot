# Bussinessonbot

Backend

You need to create a REST service that can fetch bank details, using the data given in the API’s query parameters. You can use the data available in this Link in your backend DB

Case 1

 Search API to return possible matches across all columns and all rows, ordered by IFSC code (ascending order) with limit and offset.

Request URL  - /api/search?q=Mumbai&limit=2&offset=1 

Case 2

 Branch API to return possible matches based on the branch name ordered by IFSC code (descending order) with limit and offset

Request URL  - /api/branch?q=LONI&limit=1&offset=1 


