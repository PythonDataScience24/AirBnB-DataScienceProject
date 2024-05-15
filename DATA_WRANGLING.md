# Data Wrangling of AirBnB data set
## Findings and results
While wrangling with the [AirBnB data set provided by Kaggle](https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata/discussion/368099), we found that the descriptions in the 'name'-variable hold a lot of duplicate values. This is surprising in a couple of ways:
- it's a 'free text field'. While it is possible that hosts describe their listings in the same way, it does not explain the amount of ~40k exact same strings
- Even complex strings are listed up to 4 times in the data set.
- items with the same 'name' usually only differ slightly in one or two data points, e.g. they have different cancellation_policy or house_rules
- items however, display new id's and host_id's.
- items are located at the same latitude and longitude

**Example listing that differs in id, host_id, cancellation_policy and house_rules**

![item-listing.PNG](imgs%2Fitem-listing.PNG)

### Finding 1: Every time a host updates a listing, a new listing is created
**How many listings in the same place (long/lat) and with the same name exist in the data set?**
Of the 102k items in the data set, as many as 35k - 40k of the listings could stem from hosts updating their listings.
Looking at the 'name' variable, we found that 40k listings are present with the exact same 'name'. We could argue, that of the 102k listings, 40k have been updated 2x, 23k 3x and 4k more than 4x and more.

**What do the names of the groups 'name/lat/long' look like?**
![sameName-sameLocation.PNG](imgs%2FsameName-sameLocation.PNG)

We can see that there's a listing with "Loft Suite" that exists > 8 times at the same location. The 'name' DOUBLE SHARE BATHROOM exists 7 times at the exact same location
A listing carrying a very elaborate name 'Sunny Spacious Friendly....' is listed 4x in the exact same location.

**What are the chances, that 4 listings in the same location are meant to be the exact same differing in only one or two data points?**

![listing-description-names.PNG](imgs%2Flisting-description-names.PNG)

### Finding 2: No unique identifier exists for a listing
When we wanted to clean the data and remove the 'old listings' and only use the latest, updated listings, we realized that there was no way we could identify which listing was the one updated. The only date we have is the one from the last_review. It turns out, this cannot be used, since it is copied as well and is not unique.

### Finding 3: Since New York has a lot of skyscrapers, there probably are many listings at the same long/lat
Taking New York's unique geographic in to account, removing those items with the same name/long/lat almost gets impossible. We found a case where a hotel was advertising its many hotel rooms. How could we know, which one's are updates and which one's are actual listings?

|![king-bed.PNG](imgs%2Fking-bed.PNG)|![water-view.PNG](imgs%2Fwater-view.PNG)|
|---|---|

## Results: Consequences for travellers using our dashboard are dire
Overall, the consequences for the travellers trying to find accomodation in New York using our data set are grave: if more than 30% of the listings are not real listings but outdated listing, the dashboard vastly exaggerates the actual number of available listings.
Also, basing their decision for accommodation on outdated listings might cause confusion and a lot of bad surprises. Exactly the things that we wanted to avoid in the first place, when offering such a service. Hopefully, future AirBnB data sets will provide better ways of dealing with listing updates.


