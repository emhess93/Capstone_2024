import os;
import pandas;

#import meteosource data
curl "https://bulk.meteostat.net/v2/hourly/10637.csv.gz" --output "10637.csv.gz";
