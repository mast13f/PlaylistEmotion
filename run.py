from getdata import *
import gui
import lightgbm as lgb

def func(a):
    #userplaylist = [input('Playlist link: ')]
    userplaylist = a
    userplaylist = get_attributes(userplaylist,features)


    # lightGBM
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

# # radar chart
# import plotly.express as px
# df = pd.DataFrame(dict(
#     r=[happy_percent, sad_percent, angry_percent],
#     theta=['happy','sad','angry']))



# fig = px.line_polar(df, r='r', theta='theta', line_close=True)
# fig.update_traces(fill='toself')
# fig.show()




