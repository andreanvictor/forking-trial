# thse are some random code


```python
from django.utils import timezone
from datetime import date, time, datetime

# create a list of dictionaries, where each dictionary represents a FeatureValue instance
feature_values = [
    {
        'feature': feature_object,
        'sources': [source_object_1, source_object_2],
        'value_bool': True,
        'value_char': 'Some text',
        'value_text': 'Some long text',
        'value_int': 123,
        'value_float': 3.14,
        'value_date': date.today(),
        'value_time': time(hour=12, minute=30),
        'value_datetime': datetime.now(tz=timezone.utc),
        'created': timezone.now(),
        'modified': timezone.now(),
    },
    # add more FeatureValue instances here...
]

# perform bulk create
FeatureValue.objects.bulk_create([
    FeatureValue(**kwargs) for kwargs in feature_values
])


# create a new source object
source = Source(name='My source')
source.save()

# create a new feature object
feature = Feature(name='My feature')
feature.save()

# create a new FeatureValue instance with the source object
feature_value = FeatureValue.objects.create(
    feature=feature,
    value_text='some value',
)
feature_value.sources.add(source)


feature_value_moving_averages = []

for fx_spot in FxSpot.objects.all():
    feature_value_moving_averages.append(
        {
            'feature': self.feature,
            'value_float': fx_spot.rate,
            'created': datetime.datetime.now(),
            'modified': datetime.datetime.now(),
        }
    )

# perform bulk create
FeatureValue.objects.bulk_create([
    FeatureValue(**kwargs).save() for kwargs in feature_value_moving_averages for source in kwargs.pop('sources', [fx_spot])
    kwargs['sources'].add(source)
])
```



