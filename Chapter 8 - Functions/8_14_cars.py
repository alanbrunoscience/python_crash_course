def make_car(manufacturer, model_name, **features):
    features['Manufacturer'] = manufacturer.title()
    features['Model_name'] = model_name.title()
    
    return features
        
car = make_car('subaru', 'outback', Color='Blue', Tow_package=True)
print(car)