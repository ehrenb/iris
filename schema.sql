CREATE TABLE apps(
id serial PRIMARY KEY,
package TEXT,
item_name TEXT,
updated TEXT,
author TEXT,
filesize TEXT,
downloads TEXT,
version TEXT,
version_code INTEGER,
compatibility TEXT,
content_rating TEXT,
author_link TEXT,
genre TEXT,
price TEXT,
rating_value TEXT,
review_number TEXT,
description TEXT,
iap TEXT,
developer_badge TEXT,
physical_address TEXT,
video_url TEXT,
developer_id TEXT,
time_scraped timestamp default current_timestamp,
downloaded boolean default FALSE, 
filepath TEXT default null);

CREATE TABLE orphaned(
id INTEGER PRIMARY KEY,
app_id TEXT,
version TEXT,
filepath TEXT,
time_inserted timestamp default current_timestamp);