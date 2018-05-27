# Congo API For Drone Deliveries

<a name="overview"></a>
## Overview

### Version information
*Version* : 

### URI scheme
*BasePath* : http://localhost:8080

<a name="paths"></a>
## Paths

<a name=""></a>
### Get a list of deliveries

```
GET /deliveries
```
#### Description
Get a list of deliveries

#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
|**date**|**sinceDate** | | <no value>|
|**date**|**throughDate** | | <no value>|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|  | |
<a name=""></a>
### Create/request a new delivery

```
POST /deliveries
```
#### Description
Create/request a new delivery

#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**201**|  | |

<a name=""></a>
### Get information on a specific delivery

```
GET /deliveries/{deliveryId}
```
#### Description
Get information on a specific delivery

#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|  | |
<a name=""></a>
### Update the information on a specific delivery

```
PATCH /deliveries/{deliveryId}
```
#### Description
Update the information on a specific delivery

#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|  | |
<a name=""></a>
### Cancel a specific delivery

```
DELETE /deliveries/{deliveryId}
```
#### Description
Cancel a specific delivery

#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|  | |

<a name=""></a>
### Get a list of drones

```
GET /drones
```
#### Description
Get a list of drones

#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
|**number**|**atAltitude** | Altitude in meters above the [ellipsoid](http://www.w3.org/TR/geolocation-API/#ref-wgs)| <no value>|
|**number**|**atLatitude** | Latitude in decimal degrees| <no value>|
|**number**|**atLongitude** | Longitude in decimal degrees| <no value>|
|**number**|**atRange** | Maximum distance from location, in meters| 100|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|  | |
<a name=""></a>
### Add a new drone to the fleet

```
POST /drones
```
#### Description
Add a new drone to the fleet

#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|

<a name=""></a>
### Get information on a specific drone

```
GET /drones/{droneId}
```
#### Description
Get information on a specific drone

#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|  | |
<a name=""></a>
### Update the information on a specific drone

```
PATCH /drones/{droneId}
```
#### Description
Update the information on a specific drone

#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|  | |
<a name=""></a>
### Remove a drone from the fleet

```
DELETE /drones/{droneId}
```
#### Description
Remove a drone from the fleet

#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**204**|  | |

<a name=""></a>
### The deliveries scheduled for the current drone

```
GET /drones/{droneId}/deliveries
```
#### Description
The deliveries scheduled for the current drone

#### Parameters
|Type|Name|Description|Default|
|---|---|---|---|
#### Responses

|HTTP Code|Description|Schema|
|---|---|---|
|**200**|  | |



<a name="types"></a>
## Types


<a name="EnumAddress"></a>
### EnumAddress


|Name|Description|Type|
|---|---|---|


<a name="User"></a>
### User


|Name|Description|Type|
|---|---|---|
|**age**| |integer|
|**assets**| |string|
|**dob**| |date|
|**firstName**| |string|
|**height**| |number|
|**iscrazy**| |boolean|
|**lastName**| |<no value>|
