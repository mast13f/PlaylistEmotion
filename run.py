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

happy_percent = len([x for x in y_pred if x == 1])/len(y_pred)
sad_percent = len([x for x in y_pred if x == 0])/len(y_pred)
angry_percent = len([x for x in y_pred if x == 2])/len(y_pred)


print('This playlist is',round(100*sad_percent,3),'% sad.')
print('This playlist is',round(100*happy_percent,3),'% happy.')
print('This playlist is',round(100*angry_percent,3),'% angry.')





