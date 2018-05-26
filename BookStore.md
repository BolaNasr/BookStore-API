# Book Store ApI

<a name="overview"></a>
## Overview

### Version information
*Version* : 1.0

### URI scheme
*BasePath* : http://localhost:5000

<a name="paths"></a>
## Paths

<a name=""></a>
### /books

```
GET /books
```
#### Description


#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|  | |
<a name=""></a>
### /books

```
POST /books
```
#### Description


#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**201**| Book has been successfully created. | |
|**409**| Book already exists. | |

<a name=""></a>
### Retrieve book-related information.

```
GET /books/{bookId}
```
#### Description
Retrieve book-related information.

#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
|****|**bookId**   <br>*required* | Book Identifier
| <no value>|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|  | |
<a name=""></a>
### Update book information.

```
PUT /books/{bookId}
```
#### Description
Update book information.

#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
|****|**bookId**   <br>*required* | Book Identifier
| <no value>|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**| The book has been successfully updated.
 | |
|**404**| Unable to find book ... check Book ID.
 | |
<a name=""></a>
### Remove book from the Store.

```
DELETE /books/{bookId}
```
#### Description
Remove book from the Store.

#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
|****|**bookId**   <br>*required* | Book Identifier
| <no value>|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**| The book has been successfully removed.
 | |
|**404**| Unable to find book ... check Book ID.
 | |



<a name="types"></a>
## Types
