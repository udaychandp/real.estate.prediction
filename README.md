# real.estate.prediction
This is a project where you can sort undervalued properties with their per_sq_mtr value basically you can assign the threshold and classify the value based on the your own Budget

> Overview of this Project

I leverage data sourced from Magicbricks, a renowned platform for property listings. Through systematic data extraction and analysis, I gather essential information such as plot prices, sizes, and the number of bedrooms (BHK). Employing predictive modeling techniques, I aim to identify undervalued plots within the dataset. The criteria for determining undervalued properties involve intricate considerations, with one significant factor being the price per square foot. By establishing a threshold based on comprehensive market insights, the algorithm assesses each plot's pricing against its size, enabling it to pinpoint those properties that exhibit potential undervaluation. This predictive approach allows for a nuanced understanding of the real estate market, providing valuable insights to investors, developers, and homebuyers seeking lucrative opportunities in the ever-evolving property landscape.

> Installing the Libraries through requirements.txt

```
pip install requireents.txt
```

> how to use the scraper file to get data from web to csv

basically you should get to the magic bricks website where you weanna filter the prediction and copy the link as shown in below image

![readme_1](https://github.com/udaychandp/image.conversion.with.python/assets/114306402/36b608f7-05f6-430d-9b04-7919518f47be)

now use the below commad to create your new csv file 

```
py scraper.py [link_thet_you_copied_form_web] [file_name.csv]
```
> For example

```
py scraper.py 'https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Hyderabad' file1.csv
```

> Now or the Prediction file execution

```
py pred.py [filename.csv] [threshold_value]
```

> For example

```
py pred.py file1.csv 1100
```

Thus you can generate the output as shown in the below image

![output](https://github.com/udaychandp/image.conversion.with.python/assets/114306402/7d3b16db-70d3-4ba4-962e-9a641582e02c)

