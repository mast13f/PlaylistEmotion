from getdata import *

userplaylist = [input('Playlist link: ')]
userplaylist = get_attributes(userplaylist,features)


# lightGBM
import lightgbm as lgb
X = merged.drop('label', axis=1)
Y = merged['label']
clf0 = lgb.LGBMClassifier()
clf0.fit(X,Y)

y_pred=clf0.predict(userplaylist)
y_pred = [eval(i) for i in y_pred]
percent = (sum(y_pred)/len(y_pred))*100

print('This playlist is',round(100-percent,3),'% sad.')




